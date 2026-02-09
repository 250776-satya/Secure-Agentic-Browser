def enforce_policy(risk_score):
    if risk_score >= 70:
        return "BLOCK"
    elif risk_score >= 40:
        return "CONFIRM"
    else:
        return "ALLOW"
