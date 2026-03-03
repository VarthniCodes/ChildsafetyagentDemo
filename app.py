from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulated database: We ONLY store risk events, not full chats.
risk_events = []

# Simple Risk Detection Engine
# In a real app, this would use an AI model like Perspective API or a custom LLM
BANNED_KEYWORDS = {
    "grooming": ["don't tell your parents", "send me a photo", "our secret"],
    "bullying": ["loser", "kill yourself", "hate you"],
    "self-harm": ["hurt myself", "end it all"]
}

def analyze_text(text):
    text = text.lower()
    for category, keywords in BANNED_KEYWORDS.items():
        for word in keywords:
            if word in text:
                return category
    return None

@app.route('/')
def dashboard():
    # Sort events by newest first
    sorted_events = sorted(risk_events, key=lambda x: x['timestamp'], reverse=True)
    return render_template('dashboard.html', events=sorted_events)

@app.route('/monitor', methods=['POST'])
def monitor_message():
    """
    Simulates a message being sent from a child's device.
    """
    data = request.json
    message_text = data.get("message", "")
    
    risk_found = analyze_text(message_text)
    
    if risk_found:
        event = {
            "id": len(risk_events) + 1,
            "category": risk_found.upper(),
            "snippet": f"...{message_text[-20:]}", # Only store a small snippet for context
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Action Required"
        }
        risk_events.append(event)
        return jsonify({"status": "alert", "nudge": "Hey, stay safe! Remember not to share secrets with strangers."})
    
    return jsonify({"status": "clear"})

if __name__ == '__main__':
    app.run(debug=True)