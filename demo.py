import streamlit as st
import os
from asteroid.models import *
import soundfile as sf
import torch
import numpy as np

source_sep_folder = "source_separation/"
speech_enh_folder = "speech_enhancement/"

st.image(image="img/img.png")

menu = ["Home", "Source separation", "Speech enhancement", "Try me"]

option = st.sidebar.selectbox("Menu", menu)

if option == 'Home':
    with open("README.md") as f:
        readme = f.read()
    st.markdown(readme)

if option == 'Source separation':

    examples_dir = os.path.join(source_sep_folder, 'examples')
    with open(os.path.join(source_sep_folder, "README.md")) as f:
        readme = f.read()
    st.markdown(readme)
    for i, example in enumerate(os.listdir(examples_dir)):

        # And within an expander
        my_expander = st.beta_expander(f"Example {i + 1}", expanded=False)
        with my_expander:
            current_path = os.path.join(examples_dir, example)
            # with open(os.path.join(current_path, "metrics.json")) as m:
            #     metrics = json.load(m)
            # metrics.pop("mix_path")

            mixture = open(os.path.join(current_path, "mixture.wav"), 'rb')
            mix_bytes = mixture.read()

            s1 = open(os.path.join(current_path, "s1.wav"), 'rb')
            s1_bytes = s1.read()

            s2 = open(os.path.join(current_path, "s2.wav"), 'rb')
            s2_bytes = s2.read()

            est_s2 = open(os.path.join(current_path, "s2_estimate.wav"), 'rb')
            est_s2_bytes = est_s2.read()

            est_s1 = open(os.path.join(current_path, "s1_estimate.wav"), 'rb')
            est_s1_bytes = est_s1.read()

            st.write("The mixture")
            st.audio(mix_bytes)
            st.write("The sources")
            st.audio(s1_bytes)
            st.audio(s2_bytes)
            st.write("The estimates")
            st.audio(est_s1_bytes)
            st.audio(est_s2_bytes)
            # st.json(metrics)

if option == 'Speech enhancement':

    examples_dir = os.path.join(speech_enh_folder, 'examples')
    with open(os.path.join(speech_enh_folder, "README.md")) as f:
        readme = f.read()
    st.markdown(readme)

    for i, example in enumerate(os.listdir(examples_dir)[0:10]):
        # And within an expander
        my_expander = st.beta_expander(f"Example {i + 1}", expanded=False)
        with my_expander:
            current_path = os.path.join(examples_dir, example)

            mixture = open(os.path.join(current_path, "mixture.wav"), 'rb')
            mix_bytes = mixture.read()

            est_s1 = open(os.path.join(current_path, "s0_estimate.wav"), 'rb')
            est_s1_bytes = est_s1.read()

            st.write("The mixture")
            st.audio(mix_bytes)

            st.write("The estimate")
            st.audio(est_s1_bytes)

if option == 'Try me':

    def read_array(array,sr):
        sf.write('temp.wav', array, sr)
        st.audio('temp.wav', format='audio/wav')
        os.remove('temp.wav')
        return


    def normalize_estimates(est_np, mix_np):
        """Normalizes estimates according to the mixture maximum amplitude

        Args:
            est_np (np.array): Estimates with shape (n_src, time).
            mix_np (np.array): One mixture with shape (time, ).

        """
        mix_max = np.max(np.abs(mix_np))
        return np.stack(
            [est * mix_max / np.max(np.abs(est)) for est in est_np])

    def select_model(model_name,task):
        from asteroid.models.base_models import BaseModel
        if task == "Speech enhancement":
            # if model_name == "ConvTasNet":
            #     path = "JorisCos/ConvTasNet_Libri1Mix_enhsingle_16k"
            if model_name == "DPTNet":
                path = "JorisCos/DPTNet_Libri1Mix_enhsingle_16k"
            # elif model_name == "DPRNNTasNet":
            #     path = "JorisCos/DPRNNTasNet-ks2_Libri1Mix_enhsingle_16k"
            # elif model_name == "DCCRNet":
            #     path = "JorisCos/DCCRNet_Libri1Mix_enhsingle_16k"
            # elif model_name == "DCUNet":
            #     path = "JorisCos/DCUNet_Libri1Mix_enhsingle_16k"
        elif task == "Source separation":
            if model_name == "ConvTasNet":
                path = "JorisCos/ConvTasNet_Libri2Mix_sepclean_16k"
            if model_name == "DPRNNTasNet":
                path = "mpariente/DPRNNTasNet-ks2_WHAM_sepclean"
        return BaseModel.from_pretrained(path)

    task = st.selectbox(
    'Select the task',
    options = ['Source separation', 'Speech enhancement'])

    if task == 'Source separation':
        st.write("This model is trained with files with 16kHz data and 2 speakers. "
                 "Upload data accordingly.")
        model = st.selectbox(
            'Select the model',
            options=['ConvTasNet'])

        selected_model = select_model(model, task)
        wav_file = st.file_uploader("Upload your file", type=['wav'])
        if wav_file is not None:
            mix, sr = sf.read(wav_file,dtype='float32')
            st.write("Your mixture")
            read_array(mix, sr)
            torch_mix = torch.from_numpy(mix)
            output = selected_model(torch_mix)
            output = output.squeeze(0).cpu().data.numpy()
            output_normalize = normalize_estimates(output,mix)
            st.write("Our estimates")
            read_array(output_normalize[0], sr)
            read_array(output_normalize[1], sr)

    elif task == 'Speech enhancement':
        st.write("This model is trained with files with 16kHz data. "
                 "Upload data accordingly.")
        model = st.selectbox(
            'Select the model',
            options=['DPTNet'])

        selected_model = select_model(model, task)
        wav_file = st.file_uploader("Upload your file", type=['wav'])
        if wav_file is not None:
            mix, sr = sf.read(wav_file, dtype='float32')
            st.write("Your mixture")
            read_array(mix, sr)
            torch_mix = torch.from_numpy(mix)
            output = selected_model(torch_mix)
            output = output.squeeze().data.numpy()
            st.write("Our estimate")
            read_array(output, sr)
