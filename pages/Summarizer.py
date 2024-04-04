import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader

# Load the pipeline for summarization
pipe = pipeline("summarization", model="asadcr/autotrain-intelligize-edgar-analysis-2-1722460190")

# Function to extract text from a PDF file
def extract_text_from_pdf(uploaded_file):
    pdf_file = PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(pdf_file.pages)):
        text += pdf_file.pages[page_num].extract_text()
    return text

# Streamlit app
def main():
    st.title("PDF Summarizer App")

    option = st.radio("Choose an option:", ("Upload a PDF Document", "Enter Text"))

    if option == "Upload a PDF Document":
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

        if uploaded_file is not None:
            st.subheader("Original Text")
            pdf_text = extract_text_from_pdf(uploaded_file)
            st.text_area("Original Text", pdf_text, height=400)

            if st.button("Summarize"):
                st.subheader("Summarized Text")
                summarized_text = pipe(pdf_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
                st.text_area("Summarized Text", summarized_text, height=200)
    else:
        text_input = st.text_area("Enter Text:")
        
        if st.button("Summarize"):
            st.subheader("Summarized Text")
            summarized_text = pipe(text_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            st.text_area("Summarized Text", summarized_text, height=200)

if __name__ == "__main__":
    main()
