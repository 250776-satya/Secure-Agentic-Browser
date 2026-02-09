SUSPICIOUS_PHRASES = [
    "ignore previous instructions",
    "system message",
    "you are chatgpt",
    "override your goal",
    "act as"
]

def detect_prompt_injection(text):
    detected = []
    lower = text.lower()
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in lower:
            detected.append(phrase)
    return detected


def detect_deceptive_buttons(buttons):
    deceptive = []
    for b in buttons:
        label = (b["text"] or "").lower()
        action = (b["action"] or "").lower()

        if "login" in label and "download" in action:
            deceptive.append(label)

    return deceptive
