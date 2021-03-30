import streamlit as st
import os

speech_enh_folder = "speech_enhancement/"


def create_enh_page():
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