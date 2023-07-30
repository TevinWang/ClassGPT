
import streamlit as st
from components.sidebar import sidebar
from s3 import S3
from utils import query_gpt, query_gpt_memory, show_pdf

st.set_page_config(
    page_title="ClassGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://twitter.com/benthecoder1",
        "Report a bug": "https://github.com/benthecoder/ClassGPT/issues",
        "About": "ClassGPT is a chatbot that answers questions about your pdf files",
    },
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    # Set menu items to provide helpful links for users
    menu_items={
        "Get Help": "https://twitter.com/benthecoder1",
        "Report a bug": "https://github.com/benthecoder/ClassGPT/issues",

if "chosen_pdf" not in st.session_state:
    st.session_state.chosen_pdf = "--"

if "memory" not in st.session_state:
    st.session_state.memory = ""


if "chosen_pdf" not in st.session_state:
    st.session_state.chosen_pdf = "--"
    # Initialize chosen PDF to default "--" value
if "memory" not in st.session_state:
    st.session_state.memory = ""

all_classes = s3.list_files()

st.header("ClassGPT: ChatGPT for your lectures slides")
# Initialize S3 client
bucket_name = "classgpt"
s3 = S3(bucket_name)
if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]
    list(all_classes.keys()) + ["--"],
    index=len(all_classes),
)
# Store selected class in session state
st.session_state.chosen_class = chosen_class
# Check if a class is selected
if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]
    # Dropdown to select PDF file
    chosen_pdf = st.selectbox(
        "Select a PDF file",
        all_pdfs + ["--"],
            st.markdown(
    )
    st.session_state.chosen_pdf = chosen_pdf
    # Check if a PDF is selected
    if st.session_state.chosen_pdf != "--":
        col1, col2 = st.columns(2)
            )
            query = st.text_area("Enter your question", max_chars=200)

            if st.button("Ask"):
                if query == "":
                    st.error("Please enter a question")
                with st.spinner("Generating answer..."):
                    # res = query_gpt_memory(chosen_class, chosen_pdf, query)
                    res = query_gpt(chosen_class, chosen_pdf, query)
                    st.markdown(res)

                    # with st.expander("Memory"):
                    #      st.write(st.session_state.memory.replace("\n", "\n\n"))

        with col2:
                )
                query = st.text_area("Enter your question", max_chars=200)
                # Button to trigger answer generation
                if st.button("Ask"):
                    if query == "":
                        st.error("Please enter a question")
                        st.markdown(res)
                        # Uncomment to show chat history
                        # with st.expander("Memory"):
                        #      st.write(st.session_state.memory.replace("\n", "\n\n"))
        with col2:
            # Display selected PDF
            show_pdf(chosen_class, chosen_pdf)


