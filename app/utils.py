
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
import base64
import logging
import os
import tempfile
from io import BytesIO

from s3 import S3

# set to DEBUG for more verbose logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# langchain
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

# llama_index
from llama_index import Document, GPTSimpleVectorIndex, LLMPredictor
# from pypdf import PdfReader
from s3 import S3

# set to DEBUG for more verbose logging
logging.basicConfig(level=logging.INFO)


s3 = S3("classgpt")


# ------------------- index creation ------------------- #
import pdfplumber


def parse_pdf(file: BytesIO):


    return [Document(text)]


def create_index(pdf_obj, folder_name, file_name):
    """
    Create an index for a given PDF file and upload it to S3.
    """
    index_name = file_name.replace(".pdf", ".json")

    logging.info("Generating new index...")
    documents = parse_pdf(pdf_obj)

    logging.info("Creating index...")
    index = GPTSimpleVectorIndex(documents)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = f"{tmp_dir}/{index_name}"
        logging.info("Saving index...")
        index.save_to_disk(tmp_path)

        with open(tmp_path, "rb") as f:
            logging.info("Uploading index to s3...")
            s3.upload_files(f, f"{folder_name}/{index_name}")

    return index
        index = GPTSimpleVectorIndex(documents)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = f"{tmp_dir}/index.json"
        logging.info("Saving index...")
        index.save_to_disk(tmp_path)

        with open(tmp_path, "rb") as f_index:
            logging.info("Uploading index to s3...")
            s3.upload_files(f, f"{folder_name}/{index_name}")

        logging.info("Index found, loading index...")
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = f"{tmp_dir}/{index_name}"
            s3.download_file(f"{folder_name}/{index_name}", tmp_path)
            index = GPTSimpleVectorIndex.load_from_disk(tmp_path)

    else:
        logging.info("Index not found, generating index...")
        with tempfile.NamedTemporaryFile("wb") as f_src:
            logging.info(f"{file_name} downloaded")

    if s3.file_exists(folder_name, index_name):
        logging.info("Index found, loading index...")
        with tempfile.TemporaryDirectory() as tmp_dir_load:
            tmp_path = f"{tmp_dir}/{index_name}"
            s3.download_file(f"{folder_name}/{index_name}", tmp_path)
            index = GPTSimpleVectorIndex.load_from_disk(tmp_path)

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
    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(
            temperature=0,
            model_name="gpt-3.5-turbo-0301",
        )
    )

    index = get_index(chosen_class, chosen_pdf)
    response = index.query(query, llm_predictor=llm_predictor)

    return response


# ------------------- Render PDF ------------------- #


@st.cache_data
def get_pdf_html(folder_name, file_name):
    pass

def query_gpt_memory(chosen_class, chosen_pdf, query):


    with tempfile.NamedTemporaryFile("wb") as f_src:
        logging.info(f"Downloading {file_name}...")
        s3.download_file(f"{folder_name}/{file_name}", f_src.name)

        with open(f_src.name, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        pdf_display = f"""

    return res


