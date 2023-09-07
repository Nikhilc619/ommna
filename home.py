import streamlit as st
from streamlit_option_menu import option_menu
from chat import Chat
from convo import convo

def homepage():
    st.title("Home")   
    # st.header("Home Page")
    st.subheader("Welcome to the Home Page")

def dashboard():
    # st.title("Dashboard")
    # st.header("Dashboard")

    with st.sidebar:
        selected = option_menu("Menu", ["Home", "Dashboard","Chat","Conversation","Logout"], icons=['house', 'activity'], menu_icon="cast", default_index=0)
    if selected == "Home":
        homepage()
        
    elif selected == "Dashboard":
        "gfjfvjhvjhv"
    elif selected == "Chat":
        Chat()
    elif selected == "Conversation":
        convo()
    elif selected == "Logout":
        st.session_state["user"] = "visitor"
        st.experimental_rerun()


       
        

        




