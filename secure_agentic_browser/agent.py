from playwright.sync_api import sync_playwright
from dom_analyzer import find_hidden_text
from threat_detector import detect_prompt_injection
from risk_engine import calculate_risk
from policy_engine import enforce_policy

URL = "https://example.com"   # test URL

def run_agent(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        html = page.content()
        visible_text = page.inner_text("body")

        hidden_texts = find_hidden_text(html)
        injections = detect_prompt_injection(visible_text)

        action_type = "password"

        risk, reasons = calculate_risk(
            hidden_texts,
            injections,
            deceptive_buttons=[],
            action_type=action_type
        )

        decision = enforce_policy(risk)

        browser.close()

        return {
            "score": risk,
            "decision": decision,
            "reasons": reasons
        }
        

if __name__ == "__main__":
    run_agent("https://example.com")




