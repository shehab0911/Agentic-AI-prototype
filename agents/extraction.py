# Extraction Agent
# Extracts fields from documents using OCR and NLP

def extract_fields_from_pdf(pdf_path):
    """
    Simulate field extraction from PDF using OCR and NLP.
    In a real system, use pytesseract for OCR and spaCy for NLP.
    Here, we mock the output for demo purposes.
    """
    import os
    filename = os.path.basename(pdf_path).lower()
    # Mock extraction based on filename
    if "invoice" in filename:
        return {
            'document_type': 'Commercial Invoice',
            'fields': {
                'invoice_date': '2025-07-01',
                'lc_expiry_date': '2025-07-10',
                'lc_reference': 'LC123456',
                'currency': 'USD',
                'goods_description': 'Cotton T-Shirts',
                'quantity': 1000,
                'date': '2025-07-01'
            }
        }
    elif "b_l" in filename or "billoflading" in filename or "bol" in filename:
        return {
            'document_type': 'Bill of Lading',
            'fields': {
                'shipment_date': '2025-07-05',
                'latest_shipment_date': '2025-07-10',
                'port_of_loading': 'Chittagong',
                'port_of_discharge': 'Rotterdam',
                'clauses': '',
                'consignee': 'Bank of Europe',
                'signed': True,
                'stamped': True,
                'num_originals': 3,
                'goods_description': 'Cotton T-Shirts',
                'quantity': 1000
            }
        }
    else:
        return {
            'document_type': 'Unknown',
            'fields': {}
        }
