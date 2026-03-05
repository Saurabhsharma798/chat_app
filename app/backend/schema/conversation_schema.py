from pydantic import BaseModel


class ConversationRequest(BaseModel):
    conversation_id:int


class ConversationResponse(BaseModel):
    conversation_id:int
    content:list