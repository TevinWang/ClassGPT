# Import modules

import streamlit as st
from components.sidebar import sidebar
from s3 import S3
from s3 import S3

sidebar()
bucket_name = "classgpt"
s3 = S3(bucket_name)
all_classes = s3.list_files()

tab1, tab2, tab3 = st.tabs(["Upload data", "Add Class", "Delete"])

with tab1:

    chosen_class = st.selectbox(
        "Select a class",
        # Class list from S3
        list(all_classes.keys()) + ["--"],
        index=len(all_classes),
    )
    )
    if chosen_class != "--":
        with st.form("upload_pdf"):
            uploaded_files = st.file_uploader(
                # Allow multiple file upload
                "Upload a PDF file", type="pdf", accept_multiple_files=True
            )

            submit_button = st.form_submit_button("Upload")

            # Upload files to S3 on submit
            if submit_button:
                if len(uploaded_files) == 0:
                    st.error("Please upload at least one file")
                    st.error("Please upload at least one file")
                else:
                    with st.spinner(f"Uploading {len(uploaded_files)} files..."):
                        for uploaded_file in uploaded_files:
                            s3.upload_files(
                                uploaded_file, f"{chosen_class}/{uploaded_file.name}"
                            )

                        st.success(f"{len(uploaded_files)} files uploaded")


with tab2:
    st.subheader("Add a new class")

    with st.form("add_class"):
        add_class = st.text_input("Enter a new class name")

        submit_button = st.form_submit_button("Add")
        
        # Create new folder on S3
        if submit_button:
            if add_class == "":
                st.error("Please enter a class name")
            
            else:
                s3.create_folder(add_class)
                st.success(f"Class {add_class} added")

with tab3:
    st.subheader("Delete a class or a PDF file")

    chosen_class = st.selectbox(
        "Select a class to delete",
        list(all_classes.keys()) + ["--"],
        index=len(all_classes),
    )

    if chosen_class != "--":
        all_pdfs = all_classes[chosen_class] + ["all"]

        # Remove empty values
        all_pdfs = [x for x in all_pdfs if x]

        chosen_pdf = st.selectbox(
            "Select a PDF file or choose 'all' to delete the whole class",
            all_pdfs + ["--"],
            index=len(all_pdfs),

        chosen_pdf = st.selectbox(
            "Select a PDF file or choose 'all' to delete the whole class",
            # PDF list from S3 
            all_pdfs + ["--"],
            index=len(all_pdfs),
        )

        if chosen_pdf != "--":
            submit_button = st.button("Remove")
            
            # Delete file or folder on submit
            if submit_button:
                if chosen_pdf == "all":
                    # Delete entire folder
                    s3.remove_folder(chosen_class)
                    st.success(f"{chosen_class} removed")
                else:
