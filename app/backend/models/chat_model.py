from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,DateTime
from datetime import datetime,timezone
from sqlalchemy.sql import func

DATABASE_URL= "sqlite:///./test.db"

engine = create_engine(DATABASE_URL,connect_args={'check_same_thread':False})


session_local =sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()






class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, index=True,primary_key=True)
    # conversation_id = Column(Integer,ForeignKey('conversations.id'),nullable=False)
    role=Column(String,nullable=False)
    content = Column(String,nullable=False)

    created_at=Column(DateTime(timezone=True),server_default=func.now())

    model_config = {"from_attributes":True}




