import streamlit as st
# Import sidebar component
from components.sidebar import sidebar
# Import S3 and GPT utils
from s3 import S3
from utils import query_gpt, query_gpt_memory, show_pdf

st.set_page_config(
    page_title="ClassGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    },
)
# Session states to store user selections
# Session states
# --------------

# Session states
# --------------
if "chosen_class" not in st.session_state:
    st.session_state.chosen_class = "--"
    st.session_state.chosen_pdf = "--"
if "memory" not in st.session_state:
    # Initialize memory for conversation
    st.session_state.memory = ""


st.header("ClassGPT: ChatGPT for your lectures slides")
# Initialize S3 client
bucket_name = "classgpt"
s3 = S3(bucket_name)
# Get list of classes
all_classes = s3.list_files()
chosen_class = st.selectbox(
    "Select a class", list(all_classes.keys()) + ["--"], index=len(all_classes)
)
# Store selected class in session state
st.session_state.chosen_class = chosen_class
if st.session_state.chosen_class != "--":
if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]
        chosen_pdf = st.selectbox(
            "Select a PDF file", all_pdfs + ["--"], index=len(all_pdfs)
        )
        # Store selected PDF in session state
        st.session_state.chosen_pdf = chosen_pdf
        if st.session_state.chosen_pdf != "--":

    if st.session_state.chosen_pdf != "--":
        col1, col2 = st.columns(2)
                st.subheader("Ask a question")
                st.markdown(
                    """
                    # Some example prompts
                    Here are some prompts:
                    - `What is the main idea of this lecture in simple terms?`
                    - `Summarize the main points of slide 5`
                - `What is the main idea of this lecture in simple terms?`
                - `Summarize the main points of slide 5`
                - `Provide 5 practice questions on this lecture with answers`
                """
                if st.button("Ask"):
                    if query == "":
                        st.error("Please enter a question")
                    # Show spinner while generating answer
                    with st.spinner("Generating answer..."):
                        # Query GPT model
                        res = query_gpt(chosen_class, chosen_pdf, query)
                        st.markdown(res)
                        # Uncomment to show conversation memory
                        # with st.expander("Memory"):
                        #     st.write(st.session_state.memory.replace("\n", "\n\n"))
            with col2:
                # Display PDF
                show_pdf(chosen_class, chosen_pdf)
            show_pdf(chosen_class, chosen_pdf)

