from fastapi import APIRouter, HTTPException,Depends
from schema.chat_schema import ChatRequest,ChatResponse
from services.langchain_gemini import generate_response
from models.chat_model import Message
from core.config import get_db
from  sqlalchemy.orm import Session
from langchain_core.messages import HumanMessage,AIMessage
from schema.conversation_schema import ConversationRequest,ConversationResponse


router = APIRouter()


@router.get('/')
def home():
    return {"msg":"hello"}


@router.post("/chat",response_model=ChatResponse)
def chat(data:ChatRequest,db:Session = Depends(get_db)):
    conversation_id=data.conversation_id
    msg = data.content

    user_message = Message(
        role="USER",
        conversation_id=conversation_id,
        content=msg
    )
    db.add(user_message)
    db.commit()
    db.refresh(user_message)


    messages=db.query(Message).filter(Message.conversation_id==data.conversation_id).order_by(Message.id.desc()).limit(10).all()
    messages=list(reversed(messages))
    lc=[]
    for msg in messages:
        if msg.role == 'USER':
            lc.append(HumanMessage(content=msg.content))
        if msg.role == 'AI':
            lc.append(AIMessage(content=msg.content))
    
    try:
        output=generate_response(lc)
        # output={"content":"hello"}
        print(output)
        
        
        ai_message = Message(
            role='AI',
            conversation_id=conversation_id,
            content=output.content
        )
        db.add(ai_message)
        db.commit()
        db.refresh(ai_message)
        return {'content':output.content}
    except Exception as e:
        
        raise HTTPException(status_code=400,detail=f"{e}")



@router.post('/chat_content',response_model=ConversationResponse)
def get_chats(data:ConversationRequest,db:Session=Depends(get_db)):
    chats=db.query(Message).filter(Message.conversation_id==data.conversation_id).all()
    chats=list((chats))
    lc=[]
    for chat in chats:
        if chat.role == 'USER':
            lc.append({'role':chat.role,'msg':chat.content})
        if chat.role == "AI":
            lc.append({'role':chat.role,'msg':chat.content})
    return {"conversation_id":data.conversation_id,"content":lc}