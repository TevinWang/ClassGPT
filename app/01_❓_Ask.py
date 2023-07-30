
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
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://twitter.com/benthecoder1",
        "Report an issue": "https://github.com/benthecoder/ClassGPT/issues",
        "About": "ClassGPT is a chatbot that answers questions about your pdf files",
    },
)
# --------------
if "chosen_class" not in st.session_state:
    st.session_state.chosen_class = "--"

if "chosen_pdf" not in st.session_state:
    st.session_state.chosen_pdf = "--"

if "memory" not in st.session_state:
    st.session_state.memory = ""


sidebar()

st.header("ClassGPT: ChatGPT for your lectures slides")

bucket_name = "classgpt"
s3 = S3(bucket_name)

all_classes = s3.list_files()

chosen_class = st.selectbox(
    "Select a class", list(all_classes.keys()) + ["--"], index=len(all_classes)
)

st.session_state.chosen_class = chosen_class

if st.session_state.chosen_class != "--":
    all_pdfs = all_classes[chosen_class]

    chosen_pdf = st.selectbox(
        "Select a PDF file", all_pdfs + ["--"], index=len(all_pdfs)
    )

    st.session_state.chosen_pdf = chosen_pdf

    if st.session_state.chosen_pdf != "--":
                    st.spinner("Generating answer..."):
                if query == "":
                    st.error("Please enter a question")
                else:
                with st.spinner("Generating answer..."):
                    # res = query_gpt_memory(chosen_class, chosen_pdf, query)
                    res = query_gpt(chosen_class, chosen_pdf, query)
                    st.markdown(res)

                    st.session_state.queries.append(query)
                    # with st.expander("Memory"):
                    #      st.write(st.session_state.memory.replace("\n", "\n\n"))

            )
            with col2:
                show_pdf(chosen_class, chosen_pdf)

st.subheader("Recent Questions")
for query in st.session_state.queries[-5:]:
    st.markdown(f"- {query}")

                    st.error("Please enter a question")
                with st.spinner("Generating answer..."):
                    # res = query_gpt_memory(chosen_class, chosen_pdf, query)
                    res = query_gpt(chosen_class, chosen_pdf, query)
                    st.markdown(res)

                    # with st.expander("Memory"):
                    #      st.write(st.session_state.memory.replace("\n", "\n\n"))

        with col2:
            show_pdf(chosen_class, chosen_pdf)

