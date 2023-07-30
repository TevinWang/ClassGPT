import streamlit as st
# Import sidebar component 
from s3 import S3

# Import utility functions
from utils import query_gpt, show_pdf  

# Set page config
st.set_page_config(
  page_title="ClassGPT",
  page_icon="🤖",  
  layout="wide",
  initial_sidebar_state="expanded",
  menu_items={
    "Get Help": "https://twitter.com/benthecoder1",
    "Report a bug": "https://github.com/benthecoder/ClassGPT/issues",
    "About": "ClassGPT is a chatbot that answers questions about your pdf files"
  }
)

# Session states
# Store selected class and PDF  
# Default to '--' initially
if "chosen_class" not in st.session_state:
  st.session_state.chosen_class = "--"

if "chosen_pdf" not in st.session_state:
  st.session_state.chosen_pdf = "--"


# Call sidebar component
sidebar()

# Page header
st.header("ClassGPT: ChatGPT for your lectures slides")

# Initialize S3 client
bucket_name = "classgpt"
s3 = S3(bucket_name)

# Get list of classes
all_classes = s3.list_files()

# Selectbox for class 
chosen_class = st.selectbox(
  "Select a class", 
  list(all_classes.keys()) + ["--"], 
  index=len(all_classes)
)

# Update session state
st.session_state.chosen_class = chosen_class

# If a class is selected
if st.session_state.chosen_class != "--":
  
  # Get PDFs for that class
  all_pdfs = all_classes[chosen_class]

  # Selectbox for PDF
  chosen_pdf = st.selectbox(
    "Select a PDF file", 
    all_pdfs + ["--"],
    index=len(all_pdfs)
  )
  
  # Update session state
  st.session_state.chosen_pdf = chosen_pdf

  # If a PDF is selected
  if st.session_state.chosen_pdf != "--":
      
    # Create two columns 
    col1, col2 = st.columns(2)

    # Column 1 
    with col1:
      
      st.subheader("Ask a question")
      
      st.markdown("""
        Here are some prompts:  
        - What is the main idea of this lecture in simple terms?
        - Summarize the main points of slide 5  
        - Provide 5 practice questions on this lecture with answers
      """)
      
      # Text area for question  
      query = st.text_area("Enter your question", max_chars=200)

      # Button to trigger query
      if st.button("Ask"):
        
        # Basic validation
        if query == "":
          st.error("Please enter a question")
        
        else:
          
          # Spinner during query  
          with st.spinner("Generating answer..."):
            
            # Query GPT model 
            res = query_gpt(chosen_class, chosen_pdf, query)
            
            # Display response
            st.markdown(res)

    # Column 2             
    with col2:
      show_pdf(chosen_class, chosen_pdf)

@@ -209,14 +258,35 @@ def sidebar():

bucket_name = "classgpt"
s3 = S3(bucket_name)

# Get list of classes
all_classes = s3.list_files()

# Tabs for different operations  
tab1, tab2, tab3 = st.tabs(["Upload data", "Add Class", "Delete"])

with tab1:
  
  # Header
  st.subheader("Upload new lectures")

  # Class selectbox
  chosen_class = st.selectbox(
    "Select a class",
    list(all_classes.keys()) + ["--"],  
    index=len(all_classes)
  )

  # If a class is chosen
  if chosen_class != "--":
    
    # File uploader widget
    with st.form("upload_pdf"):
      
      uploaded_files = st.file_uploader(
          "Upload a PDF file", type="pdf", accept_multiple_files=True
      )
      submit_button = st.form_submit_button("Upload")

      if submit_button:
        
        if len(uploaded_files) == 0:
          st.error("Please upload at least one file")
        else:
              s3.upload_files(
                  uploaded_file, f"{chosen_class}/{uploaded_file.name}"
              )
              
              # Confirmation message
              st.success(f"{len(uploaded_files)} files uploaded")


with tab2:
  
  st.subheader("Add a new class")

  with st.form("add_class"):

    submit_button = st.form_submit_button("Add")

    # Form submission
    if submit_button:
      if add_class == "":
        st.error("Please enter a class name")
        st.success(f"Class {add_class} added")

with tab3:
  
  st.subheader("Delete a class or a PDF file")

  chosen_class = st.selectbox(
        index=len(all_pdfs),
      )

      # Submit button to confirm
      if chosen_pdf != "--":
        submit_button = st.button("Remove")
        
        # On click 
        
        if submit_button:
          if chosen_pdf == "all":
            s3.remove_folder(chosen_class)
