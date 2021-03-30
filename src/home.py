import streamlit as st
import os


def create_home_page():
    with open("README.md") as f:
        readme = f.read()
    st.markdown(readme)