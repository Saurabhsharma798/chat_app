from fastapi import APIRouter, HTTPException,Depends
from schema.chat_schema import ChatRequest,ChatResponse
from services.langchain_gemini import generate_response
from models.chat_model import Message
from core.config import get_db
from  sqlalchemy.orm import Session


router = APIRouter()

# messages=[]

@router.get('/')
def home():
    return {"msg":"hello"}


@router.post("/chat",response_model=ChatResponse)
def chat(data:ChatRequest,db:Session = Depends(get_db)):
    msg = data.content
    user_message = Message(
        role="USER",
        content=msg
    )
    db.add(user_message)
    db.commit()
    db.refresh(user_message)

    output=generate_response(msg)
    ai_message = Message(
        role='AI',
        content=output
    )
    db.add(ai_message)
    db.commit()
    db.refresh(ai_message)
    return {'content':output}
