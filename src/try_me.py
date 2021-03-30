import streamlit as st
from src.utils import select_model, process_file


def create_try_page():

    task = st.selectbox(
        'Select the task',
        options=['Source separation', 'Speech enhancement'])

    if task == 'Source separation':
        st.write(
            "This model is trained with files with 16kHz data and 2 speakers. "
            "Upload data accordingly.")
        model = st.selectbox(
            'Select the model',
            options=['ConvTasNet'])

    elif task == 'Speech enhancement':
        st.write("This model is trained with files with 16kHz data. "
                 "Upload data accordingly.")
        model = st.selectbox(
            'Select the model',
            options=['DPTNet'])

    selected_model = select_model(model, task)
    wav_file = st.file_uploader("Upload your file", type=['wav'])
    if wav_file is not None:
        process_file(wav_file, selected_model, task)
