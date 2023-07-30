
import streamlit as st
from components.sidebar import sidebar
from s3 import S3
from utils import query_gpt, query_gpt_memory, show_pdf

st.set_page_config(
    page_title="ClassGPT",
    page_icon="🤖",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    # Add menu items for help, reporting bugs, and about page
    # This improves discoverability and usability
    menu_items={
        "Get Help": "https://twitter.com/benthecoder1",
        "Report a bug": "https://github.com/benthecoder/ClassGPT/issues",
    },
    },
)

# Use session state to persist values across reruns
# Session states
# --------------
if "chosen_class" not in st.session_state:

if "chosen_pdf" not in st.session_state:
    st.session_state.chosen_pdf = "--"

if "memory" not in st.session_state:
    st.session_state.memory = ""

    st.session_state.memory = ""


# Call sidebar component to load sidebar content
sidebar()

st.header("ClassGPT: ChatGPT for your lectures slides")

bucket_name = "classgpt"
# Initialize S3 client
s3 = S3(bucket_name)

all_classes = s3.list_files()
    "Select a class", list(all_classes.keys()) + ["--"], index=len(all_classes)
)

st.session_state.chosen_class = chosen_class

if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]

    chosen_pdf = st.selectbox(
        "Select a PDF file", all_pdfs + ["--"], index=len(all_pdfs)
    )

    st.session_state.chosen_pdf = chosen_pdf

    if st.session_state.chosen_pdf != "--":
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Ask a question")
            st.markdown(
                """
                Here are some prompts:
                - `What is the main idea of this lecture in simple terms?`
                - `Summarize the main points of slide 5`
                - `Provide 5 practice questions on this lecture with answers`
                """
            )
            query = st.text_area("Enter your question", max_chars=200)
            st.markdown(
                """
                Here are some prompts:
                # Example prompts to guide the user
                - `What is the main idea of this lecture in simple terms?` 
                - `Summarize the main points of slide 5`
                - `Provide 5 practice questions on this lecture with answers`
                    res = query_gpt(chosen_class, chosen_pdf, query)
                    st.markdown(res)

                    # with st.expander("Memory"):

            if st.button("Ask"):
                if query == "":
                    st.error("Please enter a question!")
                with st.spinner("Generating answer..."):
                    res = query_gpt(chosen_class, chosen_pdf, query)

                    # with st.expander("Memory"):
                    #      st.write(st.session_state.memory.replace("\n", "\n\n"))
