# Streamlit framework for building web apps in Python
import streamlit as st
# Custom sidebar component
from components.sidebar import sidebar
# S3 utility functions
from s3 import S3
# Utility functions for OpenAI queries
from utils import query_gpt, query_gpt_memory, show_pdf

# Set page config
st.set_page_config(
    page_title="ClassGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={ # Create menu
        "Get Help": "https://twitter.com/benthecoder1", # Links for help
        "Report a bug": "https://github.com/benthecoder/ClassGPT/issues", # Link to report issues
        "About": "ClassGPT is a chatbot that answers questions about your pdf files", # Description
    } 
)

# Session states
# Session states
# --------------
if "chosen_class" not in st.session_state:
    st.session_state.chosen_class = "--"

if "chosen_pdf" not in st.session_state:
    st.session_state.chosen_pdf = "--"

if "memory" not in st.session_state:
    st.session_state.memory = ""


sidebar()

st.header("ClassGPT: ChatGPT for your lectures slides")

# S3 bucket name
bucket_name = "classgpt"
# Initialize S3 client
s3 = S3(bucket_name)

# Get list of classes and files from S3
all_classes = s3.list_files()

# Dropdown to select class
chosen_class = st.selectbox(
    "Select a class", list(all_classes.keys()) + ["--"], index=len(all_classes)
)

st.session_state.chosen_class = chosen_class

# If a class is chosen, show files dropdown
if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]

    # Dropdown to select PDF file
    chosen_pdf = st.selectbox(
        "Select a PDF file", all_pdfs + ["--"], index=len(all_pdfs)
    )

    # Store chosen PDF in session state
    st.session_state.chosen_pdf = chosen_pdf

    if st.session_state.chosen_pdf != "--":
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Ask a question")
            st.subheader("Ask a question")
            st.markdown(
                """
                Here are some example prompts:
                
                - `What is the main idea of this lecture in simple terms?`
                
                - `Summarize the main points of slide 5`
                
                - `Provide 5 practice questions on this lecture with answers`
                """
            )
            
            query = st.text_area("Enter your question", max_chars=200)

            if st.button("Ask"):
                if query == "":
                    st.error("Please enter a question")
                
                with st.spinner("Generating answer..."):
                    
                    # Query GPT model with PDF content index
                    res = query_gpt(chosen_class, chosen_pdf, query)
                    st.markdown(res)

                    # Show chat history 
                    with st.expander("Chat History"):
                         st.write(st.session_state.memory.replace("\n", "\n\n"))

        with col2:
            show_pdf(chosen_class, chosen_pdf)

