from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
import streamlit as st
from lib.utils import *

# load env variables
load_dotenv()
    
def main():

    # config page
    st.set_page_config(page_title="Tell a story about an image", page_icon="🎶")
    st.header("Story for image.")

    # uploaded for image
    uploaded_file = st.file_uploader("Choose an image.", type = ["jpeg", "png"])

    if uploaded_file is not None:

        print("File uploaded.")

        # write image locally
        bytes_image = uploaded_file.getvalue()
        with open(os.path.join("out", uploaded_file.name), "wb") as f:
            f.write(bytes_image)

        # show image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        # transfer image 2 text
        scenario = img2text(r"in\image.jpg", False)
        print(f"EXTRACTED TEXT FROM IMAGE: {scenario}")

        # tell story to image
        story = tellAStory("azure", scenario, False)
        print(f"Story told: {story}")

        # convert story 2 audio
        audio = query({"inputs": story})
        fp_audio = os.path.join("out","audio.flac")
        with open(fp_audio, "wb") as f:
            f.write(audio)

        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)

        st.audio(fp_audio)

# python -m streamlit run .\app.py
if __name__ == "__main__":
    print(os.getcwd())
    main()