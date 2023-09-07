from transformers import pipeline, Conversation
import streamlit as st
from streamlit_option_menu import option_menu


def convo():
    convo = st.text_input("Enter your message")
    chatbot = pipeline(task= "conversational" ,model="microsoft/DialoGPT-medium")
    # usrinput = Conversation(convo)
    # chitchat = chatbot(usrinput)
    
    ans = chatbot(
        convo,candidate_labels=["HELP","PROBLEM SOLVE","GENERAL TALK"])
    conversation.generated_responses[-1] 

    if ans["scores"][0] > 0.85:
        st.session_state["user"] = "visitor"
        with st.chat_message("assistant"):
            "You are now sleeping in dream"
        st.experimental_rerun()
    else:
        with st.chat_message("assistant"):
            chitchat

    
convo()    
    
