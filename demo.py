import streamlit as st
import os
import json

st.image(image="img/img.png")

menu = ["Home", "Source separation", "Speech enhancement"]

option = st.sidebar.selectbox("Menu", menu)

if option == 'Home':
    with open("README.md") as f:
        readme = f.read()
    st.markdown(readme)

source_sep_folder = "source_separation/"
speech_enh_folder = "speech_enhancement/"

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
            st.write("The metrics")

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

            st.write("The estimates")
            st.audio(est_s1_bytes)
