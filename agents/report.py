
# Report Agent
# Generates a user-readable summary

def generate_report(discrepancies):
    if not discrepancies:
        return "All checks passed. No discrepancies found."
    report_lines = ["Discrepancy Report:"]
    for d in discrepancies:
        report_lines.append(f"Rule {d['rule_id']}: {d['description']} (Severity: {d['severity']}, Action: {d['action']})")
    return "\n".join(report_lines)
