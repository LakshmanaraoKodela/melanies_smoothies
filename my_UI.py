import streamlit as st

st.title("Login Page")

# Get username and password from user
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Check if username and password are correct
if st.button("Login"):
    if username == "example_user" and password == "example_password":
        st.success("Login Successful!")
    else:
        st.error("Invalid Username or Password")
