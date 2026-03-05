import streamlit as st
import requests
import json

url="http://127.0.0.1:8000/chat"

user_input=st.chat_input('write something')

payload={'content':user_input}



user_message=st.chat_message('user')
ai_message=st.chat_message('ai')

if user_input:
    user_message.write(user_input)

    response=requests.post(url,json=payload)
    data=response.json()
    print(data)
    ai_message.write(data['content'])

