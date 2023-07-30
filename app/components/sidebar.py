import os
import streamlit as st


def sidebar():

  # Expandable sidebar
  with st.sidebar:
    
    # How to use
    st.markdown("""
      ## How to use  
      
      1. Add your files in 📁 Data page
      2. Ask a question on the ❓ Ask page
    """)
    
    # API key input
    api_key = st.text_input(
      "OpenAI API Key",
      type="password",
      placeholder="sk-xxx...",
      help="Get an API key here 👉 https://platform.openai.com/account/api-keys."
    )
    
    # Set API key if entered
    if api_key:
      os.environ["OPENAI_API_KEY"] = api_key
      st.success("API key set")
      
    # About section  
    st.markdown("""  
      ---  
      ## About
      
      ClassGPT lets you ask questions about your class lectures and get accurate answers
      
      This tool is a work in progress. 
      
      Contributions are welcomed on [GitHub](https://github.com/benthecoder/ClassGPT)
      
      Made with ♥️ by [Benedict Neo](https://benneo.super.site/)
    """)

            """
        )

