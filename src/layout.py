import streamlit as st


def create_layout():
    st.image(image="img/img.png")
    menu = ["Home", "Source separation", "Speech enhancement", "Try me"]
    option = st.sidebar.selectbox("Menu", menu)
    return option
