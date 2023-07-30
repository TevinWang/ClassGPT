
import streamlit as st
from components.sidebar import sidebar
from s3 import S3
from utils import query_gpt, query_gpt_memory, show_pdf

st.set_page_config(
    page_title="ClassGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://twitter.com/benthecoder1",
        "Report a bug": "https://github.com/benthecoder/ClassGPT/issues",
        "About": "ClassGPT is a chatbot that answers questions about your pdf files",
    },
)

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

            "Provide 5 practice questions on this lecture with answers"
            """
        )

        # with st.expander("Memory"):
        #      st.write(st.session_state.memory.replace("\n", "\n\n"))
        "Select a PDF file", all_pdfs + ["--"], index=len(all_pdfs)
    )

            show_pdf(chosen_class, chosen_pdf)

+        query = st.text_area("Enter your question", max_chars=200)
+
+        if st.button("Ask"):
+            if query == "":
+                st.error("Please enter a question")
+            else:
+                with st.spinner("Generating answer..."):
+                    res = query_gpt(chosen_class, chosen_pdf, query)
+                    st.markdown(res)

                - `Summarize the main points of slide 5`
                - `Provide 5 practice questions on this lecture with answers`
                """
            )
            query = st.text_area("Enter your question", max_chars=200)

            if st.button("Ask"):
                if query == "":
                    st.error("Please enter a question")
                with st.spinner("Generating answer..."):
                    # res = query_gpt_memory(chosen_class, chosen_pdf, query)
                    res = query_gpt(chosen_class, chosen_pdf, query)
                    st.markdown(res)

                    # with st.expander("Memory"):
                    #      st.write(st.session_state.memory.replace("\n", "\n\n"))

        with col2:
            show_pdf(chosen_class, chosen_pdf)

