import streamlit as st
from home import dashboard
from streamlit_option_menu import option_menu
import json
import uuid


st.set_page_config(page_title="Authentication", page_icon=":guardsman:", layout="wide")

# st.title("Authentication")


def load_json():
   with open("database/data.json") as file:
        data = json.load(file)
        return data
        


    

def save_json():
 with open("database/data.json", "w") as file:
        json.dump(data, file, indent=4)



def login():
    st.title("Login")
    data = json.load(open("database/data.json"))
    usrname = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login", key="loginkey"):
        for user in data["users"]:
            if usrname == user["username"] and password == user["password"]:
                st.success("Logged in as {}".format(usrname))
                st.session_state["user"] = "logged"
                flag = True
                st.experimental_rerun()
            else:
                flag = False
        if flag == False:
            st.error("Invalid username or password")
            st.stop()
    st.balloons()


def signup():

    st.title("Signup")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Signup", key="signupkey"):
        if password == confirm_password:
            data = json.load(open("database/data.json"))
            newuser = {
                "username": username,
                "password": password,
                "id": str(uuid.uuid4())
            }
            data["users"].append(newuser)
            json.dump(data, open("database/data.json", "w"), indent=4)
            st.success("Account created! You can now login.")  
            st.snow() 
            st.cache_data.clear()
        else:
            st.error("Passwords do not match")
        
def main():
    # st.title("Authentication")
    if "user" not in st.session_state:
        st.session_state["user"] = "visitor"



    if st.session_state["user"] == "logged":
        dashboard()

    elif st.session_state["user"] == "visitor":
   
        option = option_menu(
            menu_title="Authentication",
            options=["Login", "Signup"],
            icons=["house", "activity"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",

        )
        if option == "Login":
            login()
        elif option == "Signup":
            signup()
            


main()

