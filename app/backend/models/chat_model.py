from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.sql import func
from models.conversation_model import Conversation
from core.config import Base







class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, index=True,primary_key=True)
    conversation_id = Column(Integer,ForeignKey(Conversation.id),nullable=False)
    role=Column(String,nullable=False)
    content = Column(String,nullable=False)

    created_at=Column(DateTime(timezone=True),server_default=func.now())

    model_config = {"from_attributes":True}




