from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from models.chat_model import Message
load_dotenv()



model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=1.0,
    max_tokens=250,
    
)

def generate_response(messages:str):
    response=model.invoke(messages)
    return response


