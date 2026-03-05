from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

MESSAGE_DATABASE_URL= "sqlite:///./test.db"





engine = create_engine(MESSAGE_DATABASE_URL,connect_args={'check_same_thread':False})


session_local =sessionmaker(bind=engine,autoflush=False,autocommit=False)



Base = declarative_base()


def get_db():
    db= session_local()
    try:
        yield db
    finally:
        db.close()
