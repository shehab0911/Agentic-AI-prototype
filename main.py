
# Entry point for the prototype
# Simple Streamlit UI for demo
import streamlit as st
from orchestrator import process_documents
import os

st.title("Agentic AI Trade Document Validator Prototype")

uploaded_files = st.file_uploader("Upload Invoice and Bill of Lading PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    # Save uploaded files to temp dir
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    file_paths = []
    for file in uploaded_files:
        file_path = os.path.join(temp_dir, file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        file_paths.append(file_path)
    # Run the agentic pipeline
    rules_path = os.path.join("rules", "trade_rules.json")
    report = process_documents(file_paths, rules_path)
    st.subheader("Validation Report")
    st.code(report)
