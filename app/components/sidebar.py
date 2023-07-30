
import os

import streamlit as st
    at the top of the file to load the API key from the environment.

    Also remove the hardcoded API key input box, as we want to enforce
    storing the key safely in the environment rather than in the code.

    Lastly, fix the path of the logo image to point to a real location.
-->

            "1. Add your files in 📁 Data page\n"
            "2. Ask a question on the ❓ Ask page\n"
        import os
        
        os.environ["OPENAI_API_KEY"] = api_key_input
        st.success("Successfully set environment variable OPENAI_API_KEY")

        st.markdown(
            ClassGPT lets you ask questions about your class \
                lectures and get accurate answers

            This tool is a work in progress.

            Contributions are welcomed on [GitHub](https://github.com/benthecoder/ClassGPT)

            Made with ♥️ by [Benedict Neo](https://benneo.super.site/)
            """
        )

                Made with ♥️ by [Benedict Neo](https://benneo.super.site/)
                """
        )
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def sidebar():
    st.markdown(
        2. Ask a question on the ❓ Ask page
        """
    )

        ClassGPT lets you ask questions about your class \
            lectures and get accurate answers
