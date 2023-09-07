from transformers import pipeline, Conversation
# import streamlit_option_menu
import streamlit as st

def Chat():

    query = st.chat_input("Enter your query")
    convo = pipeline("conversational")
    oracle = pipeline(task="zero-shot-classification", model="facebook/bart-large-mnli")
    usrinput = Conversation(query)
    chitchat = convo(usrinput)
    ans = oracle(
        query,
        candidate_labels=["logout"])

    if ans["scores"][0] > 0.85:
        st.session_state["user"] = "visitor"
        with st.chat_message("assistant"):
            "You are now sleeping in dream"
        st.experimental_rerun()
    else:
        with st.chat_message("assistant"):
            chitchat
        

Chat()


