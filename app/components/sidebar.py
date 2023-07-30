from streamlit import st


def sidebar():
def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Add your files in 📁 Data page\n"
            "2. Ask a question on the ❓ Ask page\n"
        )
            type="password",
            placeholder="sk-xxx...",
            help="Get an API key here 👉 https://platform.openai.com/account/api-keys.",
            value=st.secrets["OPENAI_API_KEY"],
        )

        if api_key_input:

        if api_key_input:
            os.environ["OPENAI_API_KEY"] = api_key_input
            st.success("API key set")

        st.markdown(
            """
            ---
            ## About

            ClassGPT lets you ask questions about your class \
                lectures and get accurate answers

            This tool is a work in progress.

            Contributions are welcomed on [GitHub](https://github.com/benthecoder/ClassGPT)

            Made with ♥️ by [Benedict Neo](https://benneo.super.site/)
            """
        )

st.experimental_singleton()
