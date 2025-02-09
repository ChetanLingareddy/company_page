import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
context = """
The best growing company to be found any where in the world.cgfjkdhk FHJABCDHJCB jbdvbdsbv bhjscvhsabv a vhjzc hj hav
a scgdcjdbc vcjcv bdjhbc bcdjcb cbvdjcvjb fbdbCB BVCJHDVCH.
"""
st.write(context)

st.header("Our Team")

col1, col2, col3 = st.columns([1,1,1])
df = pandas.read_csv("data.csv" ,sep=",")


with col1:
    for index , row in df[:4].iterrows():
        name = row['first name'].title() + " " +  row['last name'].title()
        st.subheader(name)
        st.text(row["role"])
        st.image("images/" + row["image"])
with col2:
    for index , row in df[4:8].iterrows():
        name = row['first name'].title() + " " +  row['last name'].title()
        st.subheader(name)
        st.text( row["role"] )
        st.image ("images/" + row["image"])
with col3:
    for index , row in df[8:].iterrows():
        name = row['first name'].title() + " " +  row['last name'].title()
        st.subheader(name)
        st.text( row["role"] )
        st.image ("images/"+ row["image"])