🛡️ Secure Agentic Browser
Defending AI Agents Against Malicious Web Interactions

📌 Overview
Secure Agentic Browser is a security framework designed to protect AI-powered browser agents from malicious web content, including prompt injection, hidden DOM attacks, and deceptive UI manipulation.
Traditional browser security is built for humans, not autonomous AI agents. This project introduces real-time detection, risk scoring, and explainable decision-making tailored specifically for agentic browsers.

🚀 Key Capabilities

🔍 Prompt injection detection (visible & hidden content)
🧩 DOM-based malicious content analysis
⚠️ Dynamic risk scoring per interaction
🚦 Policy-based action mediation (ALLOW / CONFIRM / BLOCK)
📖 Human-readable security explanations
🌐 Web-based frontend for live testing

User / AI Agent
      ↓
Playwright Browser
      ↓
DOM Analyzer
      ↓
Threat Detector
      ↓
Risk Engine
      ↓
Policy Engine
      ↓
Decision + Explanation

⚔️ Attack Scenarios Covered

Prompt injection via visible text
 (e.g., “Ignore previous instructions”)
 Hidden malicious text using CSS
 (display:none, tiny fonts)
 JavaScript-based dynamic DOM injection
 Deceptive buttons and fake forms
 Phishing-style login pages

⚔️ Attack Scenarios Covered

Prompt injection via visible text
 (e.g., “Ignore previous instructions”)
 Hidden malicious text using CSS
 (display:none, tiny fonts)
 JavaScript-based dynamic DOM injection
 Deceptive buttons and fake forms
 Phishing-style login pages

📂 Repository Structure
 SECURE_AGENTIC_BROWSER/
│
├── app.py                  # Flask web application
├── agent.py                # Core agent logic
├── dom_analyzer.py         # DOM extraction & analysis
├── threat_detector.py      # Prompt injection detection
├── risk_engine.py          # Risk scoring engine
├── policy_engine.py        # Security policy decisions
│
├── templates/
│   └── index.html          # Frontend UI
│
├── static/
│   └── style.css           # Styling
│
└── README.md               # Documentation

▶️ Installation & Setup
 1️⃣ Clone Repository
  git clone <your-github-repo-link>
  cd SECURE_AGENTIC_BROWSER

 2️⃣ Install Dependencies
  pip install flask playwright beautifulsoup4

 3️⃣ Install Playwright Browser
  playwright install

 4️⃣ Run the Application
  python app.py

 5️⃣ Open in Browser
  http://127.0.0.1:5000

📊 Sample Output

 Risk Score: 50
 Decision: CONFIRM
 Reasons:
  Hidden malicious text detected
  Sensitive action requested

📈 Evaluation Metrics

Prompt Injection Detection Accuracy
False Positive / False Negative Rate
Task Completion Success Rate
Security Decision Explainability
Performance & Latency Overhead

🏆 Hackathon Relevance

✔ Solves a real-world AI security problem
✔ Designed specifically for agentic browsers
✔ Explainable & transparent decisions
✔ Scalable architecture
✔ Production-ready foundation

🔮 Future Enhancements

ML-based adaptive threat detection
Browser extension implementation
Advanced deceptive UI detection
Performance benchmarking dashboard
Enterprise-level API support

🎥 Demo

📺 Demo Video:
👉 (Add YouTube / Drive link here)

👨‍💻 Team & Submission

Developed for PS-4: Securing Agentic Browsers Against Malicious Web Interactions
Hackathon Submission

📎 License

This project is developed for educational and hackathon purposes.
