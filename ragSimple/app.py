import streamlit as st
from lib.utils import *

def main():

    # initialize llm and vector store
    if 'qa' not in st.session_state:
        print("INITIALIZE QA")
        st.session_state.fp_pdfs = fr"C:\Users\{os.getlogin()}\Documents\gitProjects\dataAndAiExamples\ragSimple\in\pdfs"
        st.session_state.qa = get_qa(st.session_state.fp_pdfs, openai_source)

    # Button for reloading
    if st.button('Reload PDFs'):
        print(f"RELOAD QA")
        st.session_state.qa = get_qa(st.session_state.fp_pdfs, openai_source)

    st.title("Echo Bot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input(""):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = st.session_state.qa.run(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

openai_source = "openai"
# python -m streamlit run .\app.py
if __name__ == "__main__":
    main()