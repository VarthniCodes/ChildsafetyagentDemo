from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Only storing risk events for privacy-first compliance
risk_events = []

# Logic for different types of risk
STRANGER_RISKS = ["secret", "meet me", "don't tell", "send pic"]
CHILD_BULLYING = ["hate you", "loser", "stupid", "ugly", "shut up"]

@app.route('/')
def parent_dashboard():
    # Sort events so newest is on top
    sorted_events = sorted(risk_events, key=lambda x: x['timestamp'], reverse=True)
    return render_template('dashboard.html', events=sorted_events)

@app.route('/child-device')
def child_device():
    return render_template('child_ui.html')

@app.route('/process_message', methods=['POST'])
def process_message():
    data = request.json
    sender = data.get("sender")
    message = data.get("message", "").lower()
    
    response = {"status": "clear", "nudge": ""}

    if sender == "Stranger":
        # Check for Grooming/Predatory behavior
        if any(word in message for word in STRANGER_RISKS):
            alert = {"category": "GROOMING RISK", "snippet": message, "timestamp": datetime.now().strftime("%H:%M:%S")}
            risk_events.append(alert)
            response = {
                "status": "danger",
                "nudge": "🚩 Neoclaw: This person is asking for secrets. Please reach out to your parents immediately."
            }
            
    elif sender == "Child":
        # Check for Bullying behavior
        if any(word in message for word in CHILD_BULLYING):
            alert = {"category": "CHILD BULLYING", "snippet": message, "timestamp": datetime.now().strftime("%H:%M:%S")}
            risk_events.append(alert)
            response = {
                "status": "warning",
                "nudge": "💡 Neoclaw: Think before you hurt others. Is this message kind?"
            }
                
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
