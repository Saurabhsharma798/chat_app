from fastapi import FastAPI
from api.routes.chat_route import router
from fastapi.middleware.cors import CORSMiddleware
from models.chat_model import Base,engine



app = FastAPI()


Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=['*'],
    allow_headers=['*'],
)

app.include_router(router)