from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Storage for the Parent Dashboard
risk_events = []

# AI Risk Engine (Expanded)
RISK_PATTERNS = {
    "GROOMING": ["secret", "don't tell", "meet me", "send photo", "address"],
    "BULLYING": ["ugly", "stupid", "hate you", "loser", "kill yourself"],
}

@app.route('/')
def parent_dashboard():
    return render_template('dashboard.html', events=risk_events)

@app.route('/child-sim')
def child_simulation():
    return render_template('child_ui.html')

@app.route('/process_chat', methods=['POST'])
def process_chat():
    data = request.json
    sender = data.get("sender") # "Stranger" or "Child"
    message = data.get("message", "").lower()
    
    response = {"status": "ok", "nudge": None}

    # Only analyze messages coming FROM the Stranger
    if sender == "Stranger":
        for category, keywords in RISK_PATTERNS.items():
            if any(word in message for word in keywords):
                # 1. Trigger the Alert for Parents
                risk_events.append({
                    "category": category,
                    "snippet": message[:30] + "...",
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })
                # 2. Trigger the Nudge for the Child
                response = {
                    "status": "risk_detected",
                    "nudge": "🚩 Neoclaw Tip: Be careful! It's never okay for someone to ask you to keep secrets from your parents."
                }
                
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
