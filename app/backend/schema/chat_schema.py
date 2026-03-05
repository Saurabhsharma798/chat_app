from pydantic import BaseModel

class ChatRequest(BaseModel):
    conversation_id:int
    content:str 

class ChatResponse(BaseModel):
    content:str




