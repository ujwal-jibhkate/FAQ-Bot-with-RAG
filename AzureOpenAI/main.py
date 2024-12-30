#Importing necessary dependencies
import streamlit as st
from utils import *

st.title("FAQ Bot")

#Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

def get_response(prompt):
    return chain.run(prompt)

#React to user input
if prompt := st.chat_input("What is UP?") :
    #Display user message in chat message container
    with st.chat_message('user'):
        st.markdown(prompt)
    #Add user message to chat history
    st.session_state.messages.append({'role':"user","content":prompt})

    response = get_response(f"ElectricUK's FAQ chatbot aims to provide helpful and informative responses in a professional yet friendly tone. Below you have given a query. Use formal tone for the response. Use specific formatting preferences, such as bullet points or paragraph structure. Your goal is to ensure that customer receives an accurate and tailored assistance for their inquiries based on the content on the document. Query : {prompt}")
    #Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    #Add assistant response to chat history
    st.session_state.messages.append({"role":"assistant" , "content": response})