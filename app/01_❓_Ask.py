import streamlit as st
from components.sidebar import sidebar
# S3 wrapper for interacting with AWS S3
from s3 import S3
# GPT querying functions
from utils import query_gpt, query_gpt_memory, show_pdf

# Set page title and other configurations
st.set_page_config(
    page_title="ClassGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    # Add menu links
    menu_items={
        "Get Help": "https://twitter.com/benthecoder1",
        "Report a bug": "https://github.com/benthecoder/ClassGPT/issues",
        "About": "ClassGPT is a chatbot that answers questions about your pdf files",
    },
)

# Initialize session states
# --------------
# Keep track of chosen class and pdf
if "chosen_class" not in st.session_state:
    st.session_state.chosen_class = "--"
if "chosen_pdf" not in st.session_state:
    st.session_state.chosen_pdf = "--"

    st.session_state.memory = ""


# Render sidebar component 
sidebar()

st.header("ClassGPT: ChatGPT for your lectures slides")

st.header("ClassGPT: ChatGPT for your lectures slides")
s3 = S3(bucket_name)

all_classes = s3.list_files()
# Selectbox to pick class
chosen_class = st.selectbox(
    "Select a class", list(all_classes.keys()) + ["--"], index=len(all_classes)
)

st.session_state.chosen_class = chosen_class

# If a class is chosen, show pdfs for that class
if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]

if st.session_state.chosen_class != "--":
        "Select a PDF file", all_pdfs + ["--"], index=len(all_pdfs)
    )

    # Update session state with chosen pdf
    st.session_state.chosen_pdf = chosen_pdf

    # If a pdf is chosen, show the query column
    if st.session_state.chosen_pdf != "--":
        col1, col2 = st.columns(2)
        # Column for asking questions

        with col1:
            st.subheader("Ask a question")

                Here are some prompts:
                - `What is the main idea of this lecture in simple terms?`
                - `Summarize the main points of slide 5`
                - `Provide 3 practice questions on this lecture with answers`
                """
            )
            query = st.text_area("Enter your question", max_chars=200)
                - `Provide 5 practice questions on this lecture with answers`
                """
                if query == "":
                    st.error("Please enter a question")
                with st.spinner("Generating answer..."):
                    # Query GPT model with question
                    res = query_gpt(chosen_class, chosen_pdf, query)
                    st.markdown(res)
                    
        # Column to show PDF
        with col2:
            show_pdf(chosen_class, chosen_pdf)
            

@@ -83,7 +84,7 @@ def sidebar():
        st.text_input(
            "OpenAI API Key",
            type="password",
            help="Get an API key here 👉 https://platform.openai.com/account/api-keys.",
            value="",
        )
        # Set OPENAI_API_KEY env variable if key is entered
        if api_key_input:
            os.environ["OPENAI_API_KEY"] = api_key_input
            st.success("API key set")

        st.markdown(
            """
            ---
            ## About

            ClassGPT lets you ask questions about your class \
            """
        )


@@ -126,12 +127,15 @@ def create_index(pdf_obj, folder_name, file_name):
    text = "\n".join(text_list)

    return [Document(text)]

# Create index for PDF and upload to S3
def create_index(pdf_obj, folder_name, file_name):
    """Create index for given PDF and upload to S3"""
    
    index_name = file_name.replace(".pdf", ".json")

    logging.info("Generating new index...")
            logging.info("Uploading index to s3...")
            s3.upload_files(f, f"{folder_name}/{index_name}")

    # Return index object
    return index


@st.cache_resource(show_spinner=False)
def get_index(folder_name, file_name):
    """Get index for given PDF, download from S3 if exists, else generate"""
    index_name = file_name.replace(".pdf", ".json")
    index = None

    return index


# Query GPT-3.5 Turbo with given question
def query_gpt(chosen_class, chosen_pdf, query):

    if not os.getenv("OPENAI_API_KEY"):

    agent = create_agent(chosen_class, chosen_pdf)
    res = ""
    # Run agent and handle errors
    try:
        res = agent.run(input=query)
    except Exception as e:

    st.session_state.memory = agent.memory.buffer

    # Return agent response
    return res
@@ -209,6 +216,7 @@ def create_tool(_index, chosen_pdf):
            description="Useful to answering questions about the given file",
            return_direct=True,
        ),
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Get index and tools for given PDF
    index = get_index(chosen_class, chosen_pdf)
    tools = create_tool(index, chosen_pdf)


    return agent


@@ -229,6 +237,7 @@ def show_pdf(folder_name, file_name):
        logging.info(f"Downloading {file_name}...")
        s3.download_file(f"{folder_name}/{file_name}", f_src.name)

