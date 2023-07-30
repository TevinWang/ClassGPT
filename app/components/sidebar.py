
import os

import streamlit as st

import os

import streamlit as st
from dotenv import load_dotenv
load_dotenv()


def sidebar():
            "2. Ask a question on the ❓ Ask page\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-xxx...",
            help="Get an API key here 👉 https://platform.openai.com/account/api-keys.",
            value="",
        )

        if api_key_input:
            os.environ["OPENAI_API_KEY"] = api_key_input
            st.success("API key set")

        st.markdown(
            """
            ---
            API key set

        st.markdown(
            """

            ---
            ## About


            Contributions are welcomed on [GitHub](https://github.com/benthecoder/ClassGPT)

            Made with ♥️ by [Benedict Neo](https://benneo.super.site/)
            """
        )
            Made with ♥️ by [Benedict Neo](https://benneo.super.site/)
            """
        )

