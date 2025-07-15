# Orchestrator
# Sequences the workflow and tracks state

from agents.extraction import extract_fields_from_pdf
from agents.validation import load_rules, validate_fields
from agents.discrepancy import aggregate_discrepancies
from agents.report import generate_report


def process_documents(pdf_paths, rules_path):
    """
    Orchestrates the agent workflow for a list of PDF paths.
    Returns the final report string.
    """
    rules = load_rules(rules_path)
    extracted = {}
    # Extraction phase
    for pdf in pdf_paths:
        result = extract_fields_from_pdf(pdf)
        doc_type = result['document_type']
        if doc_type == 'Commercial Invoice':
            extracted['invoice'] = result['fields']
        elif doc_type == 'Bill of Lading':
            extracted['b_l'] = result['fields']
        elif doc_type != 'Unknown':
            extracted[doc_type.lower().replace(' ', '_')] = result['fields']
    # Add LC info if needed (mocked for demo)
    extracted['lc'] = {
        'latest_shipment_date': '2025-07-10',
        'port_of_loading': 'Chittagong',
        'destination_port': 'Rotterdam',
        'consignee': 'Bank of Europe',
        'currency': 'USD',
        'expiry_date': '2025-07-10',
        'reference': 'LC123456'
    }
    # Validation phase
    discrepancies = []
    # Validate each doc type
    for doc_type, fields in extracted.items():
        if doc_type in ['invoice', 'b_l']:
            discrepancies += validate_fields(doc_type.title().replace('_', ' '), {**fields, **extracted['lc']}, rules)
    # Cross-document validation
    if 'invoice' in extracted and 'b_l' in extracted:
        cross_fields = {'invoice': extracted['invoice'], 'b_l': extracted['b_l'], 'lc': extracted['lc']}
        discrepancies += validate_fields('Invoice + B/L', cross_fields, rules)
    # Discrepancy aggregation
    discrepancies = aggregate_discrepancies(discrepancies)
    # Report
    return generate_report(discrepancies)
