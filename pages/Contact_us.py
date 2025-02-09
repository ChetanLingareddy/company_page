import streamlit as st
import pandas
from User_email import email

df = pandas.read_csv("topics.csv")

st.header("Contact Me")

with st.form(key = "User_email"):
    user_email = st.text_input("Enter your email")
    topic = st.selectbox("What topic do you want to discuss?",
                         df["topic"])
    raw_message = st.text_area("Enter your message")
    message=f"""\
Subject: New Mail Received
Form:
topic  '{topic}'
{raw_message}
{user_email}
"""
    button = st.form_submit_button("submit")
    if button:
        email(message)
        st.info("Email sent Successfully.")