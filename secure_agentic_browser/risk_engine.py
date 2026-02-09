def calculate_risk(hidden_texts, injections, deceptive_buttons, action_type):
    risk = 0
    reasons = []

    if injections:
        risk += 30
        reasons.append("Prompt injection detected")

    if hidden_texts:
        risk += 25
        reasons.append("Hidden malicious text found")

    if deceptive_buttons:
        risk += 20
        reasons.append("Deceptive UI elements detected")

    if action_type in ["password", "download"]:
        risk += 25
        reasons.append("Sensitive action requested")

    return risk, reasons
