from flask import Flask, render_template, request
from agent import run_agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        result = run_agent(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)