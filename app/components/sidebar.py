
import os

import streamlit as st


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Add your files in 📁 Data page\n"
# Load environment variables
load_dotenv()

@@ -15,6 +18,4 @@
    help="Get an API key here 👉 https://platform.openai.com/account/api-keys.",
    value="",
            "OpenAI API Key",
            type="password",
    if api_key_input:
        os.environ["OPENAI_API_KEY"] = api_key_input
        st.success("API key set")
    else:
        st.error("No API key provided")
        )

        if api_key_input:
            os.environ["OPENAI_API_KEY"] = api_key_input
            st.success("API key set")

        st.markdown(

st.markdown(
            ---
            ## About

            ClassGPT lets you ask questions about your class \
                lectures and get accurate answers

    Contributions are welcomed on [GitHub](https://github.com/benthecoder/ClassGPT)
    Made with ♥️ by [Benedict Neo](https://benneo.super.site/)

    Powered by OpenAI's GPT-3
""")
            Made with ♥️ by [Benedict Neo](https://benneo.super.site/)
            """
        )

