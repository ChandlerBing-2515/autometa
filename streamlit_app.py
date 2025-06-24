import streamlit as st
import os
import fitz  # PyMuPDF
import docx
import pandas as pd

def extract_text(file):
    ext = file.name.split('.')[-1].lower()
    text = ""
    if ext == 'pdf':
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    elif ext == 'docx':
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    elif ext == 'txt':
        text = file.read().decode("utf-8")
    else:
        text = "Unsupported format."
    return text

def generate_metadata(text):
    words = text.split()
    word_freq = pd.Series(words).value_counts().head(5)
    metadata = {
        "Title": words[0] if words else "N/A",
        "Top Keywords": ', '.join(word_freq.index),
        "Word Count": len(words),
        "Preview": ' '.join(words[:40])
    }
    return metadata

st.title("📄 Automated Metadata Generator")

uploaded_file = st.file_uploader("Upload your document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    text = extract_text(uploaded_file)
    if text:
        metadata = generate_metadata(text)
        st.subheader("📋 Metadata Output")
        for key, val in metadata.items():
            st.markdown(f"**{key}**: {val}")
        st.download_button("Download Metadata as CSV", pd.DataFrame([metadata]).to_csv(index=False), file_name="metadata.csv")
    else:
        st.error("Could not extract text.")

