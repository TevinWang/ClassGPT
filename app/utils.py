
import base64
import logging
import os
import sys
import tempfile
from io import BytesIO

import openai
import streamlit as st
from dotenv import load_dotenv
from langchain import OpenAI

# langchain
from langchain.agents import Tool, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

# llama_index
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

import tempfile
# llama_index
from llama_index import Document, GPTSimpleVectorIndex, LLMPredictor
from pypdf import PdfReader


load_dotenv()
if os.getenv("OPENAI_API_KEY") is None:
    st.error("OpenAI API key not set")
else:
    openai.api_key = os.getenv("OPENAI_API_KEY")


s3 = S3("classgpt")


# ------------------- index creation ------------------- #


def parse_pdf(file: BytesIO):

    pdf = PdfReader(file)
    text_list = []

    # Get the number of pages in the PDF document
    num_pages = len(pdf.pages)

    # Iterate over every page
    for page in range(num_pages):
        # Extract the text from the page
        page_text = pdf.pages[page].extract_text()
        text_list.append(page_text)

    text = "\n".join(text_list)

    return [Document(text)]


def create_index(pdf_obj, folder_name, file_name):
    """
    Create an index for a given PDF file and upload it to S3.
    """
        documents = parse_pdf(pdf_obj)

        logging.info("Creating index...")
        os.makedirs(f"temp/{folder_name}", exist_ok=True) 
        index = GPTSimpleVectorIndex(documents)

        with tempfile.TemporaryDirectory() as tmp_dir:
    index = GPTSimpleVectorIndex(documents)
            logging.info("Saving index...")
            index.save_to_disk(tmp_path)

            with open(f"temp/{folder_name}/{index_name}", "rb") as f:
                logging.info("Uploading index to s3...")
                s3.upload_files(f, f"{folder_name}/{index_name}")

            logging.info("Uploading index to s3...")
            s3.upload_files(f, f"{folder_name}/{index_name}")

    return index


@st.cache_resource(show_spinner=False)
def get_index(folder_name, file_name):
    """
    if s3.file_exists(folder_name, index_name):
        logging.info("Index found, loading index...")
        with tempfile.TemporaryDirectory() as tmp_dir:
            index = GPTSimpleVectorIndex.load_from_disk(f"temp/{folder_name}/{index_name}")

    else:
        logging.info("Index not found, generating index...")
        with open(f"temp/{folder_name}/{file_name}", "wb") as f_src:
            logging.info(f"{file_name} downloaded")
            s3.download_file(f"{folder_name}/{file_name}", f_src.name)

        logging.info("Index not found, generating index...")
        with tempfile.NamedTemporaryFile("wb") as f_src:
            logging.info(f"{file_name} downloaded")
            s3.download_file(f"{folder_name}/{file_name}", f_src.name)

            with open(f_src.name, "rb") as f:
                index = create_index(f, folder_name, file_name)

    return index


def query_gpt(chosen_class, chosen_pdf, query):

    if not os.getenv("OPENAI_API_KEY"):
        st.error("Enter your OpenAI API key in the sidebar.")
        st.stop()

    # LLM Predictor (gpt-3.5-turbo)
    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(
            temperature=0,
            model_name="gpt-3.5-turbo",
        )
    )

    index = get_index(chosen_class, chosen_pdf)
    response = index.query(query, llm_predictor=llm_predictor)

    # logging.info(response.get_formatted_sources())

    return response


@st.cache_resource
def create_tool(_index, chosen_pdf):
    tools = [
        Tool(
            name=f"{chosen_pdf} index",
            func=lambda q: str(_index.query(q)),
            description="Useful to answering questions about the given file",
            return_direct=True,
        ),
    ]

    return tools


        memory = ConversationBufferMemory(memory_key="chat_history")
        llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")

        index = get_index(chosen_class, chosen_pdf)        
        tools = create_tool(index, chosen_pdf)

        agent = initialize_agent(

    agent = initialize_agent(
        tools, llm, agent="conversational-react-description", memory=memory
    )

    return agent


def query_gpt_memory(chosen_class, chosen_pdf, query):

    agent = create_agent(chosen_class, chosen_pdf)
    res = ""

    try:

@st.cache_data
def show_pdf(folder_name, file_name):
    
    with open(f"temp/{folder_name}/{file_name}", "wb") as f_src:
        logging.info(f"Downloading {file_name}...")
        s3.download_file(f"{folder_name}/{file_name}", f_src.name)


        pdf_display = f"""
        <iframe
def show_pdf(folder_name, file_name):

    with tempfile.NamedTemporaryFile("wb") as f_src:
        logging.info(f"Downloading {file_name}...")
        s3.download_file(f"{folder_name}/{file_name}", f_src.name)

        with open(f_src.name, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        pdf_display = f"""
        