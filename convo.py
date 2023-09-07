from transformers import pipeline, Conversation
import streamlit as st
from streamlit_option_menu import option_menu


def convo():
    convo = st.text_input("Enter your message")
    chatbot = pipeline(task="conversational", model="microsoft/DialoGPT-medium")
    conversation = Conversation(convo)



    # candidate_labels = ["HELP", "PROBLEM SOLVE", "GENERAL TALK"]


    ans = chatbot(conversation)
    # add_user_input = st.button("Add User Input")

    # conversation.add_user_input("{}".format(convo))
    # conversation = chatbot(conversation)
    # conversation.generated_responses[-1]
    st.write(ans)


convo()
