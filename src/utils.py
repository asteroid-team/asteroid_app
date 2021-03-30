import streamlit as st
import soundfile as sf
import os
import numpy as np
from asteroid.models.base_models import BaseModel
import torch


def read_array(array, sr):
    """ A trick to read numpy array with streamlit audio reader

    """
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


def select_model(model_name, task):
    """ Select a model from Hugging face

    """
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


def process_file(wav_file, selected_model, task):
    """ Process the file with the corresponding model

    """
    with st.spinner(text='In progress...'):
        mix, sr = sf.read(wav_file, dtype='float32')
        st.write("Your mixture")
        read_array(mix, sr)
        torch_mix = torch.from_numpy(mix)
        output = selected_model(torch_mix)

        if task == 'Source separation':
            output = output.squeeze(0).cpu().data.numpy()
            output_normalize = normalize_estimates(output, mix)
            st.write("Our estimates")
            read_array(output_normalize[0], sr)
            read_array(output_normalize[1], sr)

        elif task == 'Speech enhancement':
            torch_mix = torch.from_numpy(mix)
            output = selected_model(torch_mix)
            output = output.squeeze().data.numpy()
            output_normalize = normalize_estimates(output, mix)
            st.write("Our estimate")
            read_array(output_normalize, sr)