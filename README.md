# ChildsafetyagentDemo
# 🐾 Neoclaw: Privacy-First Child Safety Monitoring

**Neoclaw** is an AI-powered safety layer designed to protect children from digital risks like grooming, cyberbullying, and emotional distress—without compromising their right to privacy.

## 🚀 The Vision
In an era of constant digital interaction, children are vulnerable to online predators and toxic behavior. Neoclaw acts as a real-time guardian that monitors conversation text, detects risks, and provides immediate interventions.

### Key Pillars:
- **Real-Time Intervention:** Nudges children with supportive or cautionary messages the moment a risk is detected.
- **Privacy-First:** We do **NOT** store full chat histories. We only log high-risk "Events" for parental review.
- **Two-Way Monitoring:** Detects incoming threats (grooming) and outgoing behavior (bullying).

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3 (WhatsApp-inspired UI)
- **Deployment:** Render
- **Engine:** Keyword-based Risk Detection (Scalable to LLM/Transformers)

---

## 📂 Project Structure
- `app.py`: The core logic, risk detection engine, and API routes.
- `templates/dashboard.html`: The Parent Dashboard for monitoring alerts.
- `templates/child_ui.html`: The simulation interface acting as a "Child's Device."
- `requirements.txt`: Necessary libraries for cloud deployment.

---

Access the Dashboards:

Parent Dashboard: https://childsafetyagentdemo.onrender.com/
Child Hub (Simulator): https://childsafetyagentdemo.onrender.com/child-device
