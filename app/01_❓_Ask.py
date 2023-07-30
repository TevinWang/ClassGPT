import logging
import streamlit as st
from components.sidebar import sidebar
from s3 import S3
from s3 import S3
from utils import query_gpt, query_gpt_memory, show_pdf

st.set_page_config(
    page_title="ClassGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Home": "/",
        "Data": "/data",
        "Settings": "/settings",
        "Get Help": "https://twitter.com/benthecoder1",
        "Report a bug": "https://github.com/benthecoder/ClassGPT/issues",
        "About": "ClassGPT is a chatbot that answers questions about your pdf files",
    },
)

# Session states
# --------------
if "chosen_class" not in st.session_state:
    st.session_state.chosen_class = "--"
    st.session_state.chosen_pdf = "--"

if "memory" not in st.session_state:
    st.session_state.memory = ""

# Logging
logging.basicConfig(level=logging.INFO)

# Layout
    st.session_state.memory = ""




sidebar()

st.header("ClassGPT: ChatGPT for your lectures slides")

bucket_name = "classgpt"
s3 = S3(bucket_name)

all_classes = s3.list_files()


chosen_class = st.selectbox(
    "Select a class", list(all_classes.keys()) + ["--"], index=len(all_classes)
)

if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]

    chosen_pdf = st.selectbox(
        "Select a PDF file", all_pdfs + ["--"], index=len(all_pdfs)
)

    st.session_state.chosen_pdf = chosen_pdf

    if st.session_state.chosen_pdf != "--":
        col1, col2 = st.columns(2)

        with col2:
            st.subheader("Ask a question")
            st.markdown(
                """
                """
                Here are some prompts:
                - `What is the main idea of this lecture in simple terms?`
                - `Summarize the main points of slide 5`
                - `Provide 5 practice questions on this lecture with answers`

            if st.button("Ask"):
                if query == "":
                    st.warning("Please enter a question")
                with st.spinner("Generating answer..."):
                    res = query_gpt_memory(chosen_class, chosen_pdf, query)
                    st.markdown(res)


        with col1:
            show_pdf(chosen_class, chosen_pdf)



