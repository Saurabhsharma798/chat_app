from core.config import Base
# from datetime import datetime,timezone
from sqlalchemy import Integer,Column,DateTime,func


class Conversation(Base):
    __tablename__ = "conversations"

    id=Column(Integer,primary_key=True,index=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    model_config={"from_attributes":True}

    