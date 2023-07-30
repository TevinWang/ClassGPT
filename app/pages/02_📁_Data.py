import streamlit as st
from components.sidebar import sidebar
from s3 import S3
import os

sidebar()
bucket_name = "classgpt"
bucket_name = "classgpt"
s3 = S3(bucket_name)
all_classes = s3.list_files()

tab1, tab2, tab3 = st.tabs(["Upload data", "Add Class", "Delete"])

with tab1:
    st.subheader("Upload new lectures")

    chosen_class = st.selectbox(
        "Select a class",
        list(all_classes.keys()) + ["--"],
        index=len(all_classes),
    )

    if chosen_class != "--":
        with st.form("upload_pdf"):
            uploaded_files = st.file_uploader(
                "Upload a PDF file", type="pdf", accept_multiple_files=True
            )

            submit_button = st.form_submit_button("Upload")

            if submit_button:
                if len(uploaded_files) == 0:
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
        )

        if chosen_pdf != "--":
            submit_button = st.button("Remove")

            if submit_button:
                if chosen_pdf == "all":
                    s3.remove_folder(chosen_class)
                    st.success(f"{chosen_class} removed")
                else:
                    s3.remove_file(chosen_class, chosen_pdf)
                    st.success(f"{chosen_pdf} removed")

        st.success(f"{chosen_class} removed")
    else:
        s3.remove_file(chosen_class, chosen_pdf)
        os.remove(f"temp/{chosen_class}/{chosen_pdf}")
        st.success(f"{chosen_pdf} removed")

    s3 resource to manage files in an S3 bucket.
"""
import boto3
import os
import botocore


    def upload_files(self, file_obj, file_path):
        """Upload a file object to S3"""
        self.bucket.upload_fileobj(file_obj, file_path)
        os.makedirs(os.path.dirname(f"temp/{file_path}"), exist_ok=True)

    def remove_folder(self, folder_name):
        """Remove a folder from S3"""
                Delete={"Objects": [{"Key": f"{folder_name}/{file_name}"}]}
            )

        os.remove(f"temp/{folder_name}/{file_name}")

    def download_file(self, from_file_path, to_file_path):
        """Download a file from S3 to a local path"""
        self.bucket.download_file(from_file_path, to_file_path)
