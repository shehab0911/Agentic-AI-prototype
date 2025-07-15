# Agentic AI Trade Document Validator Prototype

This prototype demonstrates an agent-based architecture for validating trade documents (Commercial Invoice, Bill of Lading) using OCR, NLP, and configurable rules.

## Structure

- agents/: Modular agents for extraction, validation, discrepancy, and reporting
- orchestrator.py: Orchestrates the workflow
- main.py: Entry point (API/UI)
- rules/: JSON rule configs
- sample_docs/: Place sample PDFs here

## Setup

1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run main.py`
