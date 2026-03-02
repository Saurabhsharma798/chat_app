from pydantic import BaseModel

class ChatRequest(BaseModel):
    # conversation_id:str
    content:str 

class ChatResponse(BaseModel):
    content:str




