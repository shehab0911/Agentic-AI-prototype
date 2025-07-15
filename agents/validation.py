# Validation Agent
# Loads rules and validates extracted fields
import json

def load_rules(rule_path):
    with open(rule_path, 'r') as f:
        return json.load(f)

def validate_fields(document_type, fields, rules):
    discrepancies = []
    for rule in rules:
        if rule['document_type'] == document_type or rule['document_type'] == 'Invoice + B/L':
            try:
                # Prepare a local context for eval
                context = {'b_l': fields, 'invoice': fields, 'lc': fields}
                # For cross-doc rules, expect both invoice and b_l in fields
                if rule['document_type'] == 'Invoice + B/L' and 'invoice' in fields and 'b_l' in fields:
                    context = {'invoice': fields['invoice'], 'b_l': fields['b_l'], 'lc': fields.get('lc', {})}
                result = eval(rule['validation_logic'], {}, context)
                if result == 'fail':
                    discrepancies.append({
                        'rule_id': rule['rule_id'],
                        'description': rule['description'],
                        'severity': rule['severity'],
                        'action': rule['action_on_failure']
                    })
            except Exception as e:
                discrepancies.append({
                    'rule_id': rule['rule_id'],
                    'description': f"Rule error: {str(e)}",
                    'severity': rule.get('severity', 'Unknown'),
                    'action': 'Error'
                })
    return discrepancies
