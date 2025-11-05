# 🇮🇳 SahayakAI — Government Scheme Eligibility & Recommendation Agent

**SahayakAI** is an Agentic AI system that helps Indian citizens discover the most suitable Government schemes and checks eligibility through natural language conversation.  

This project supports **digital inclusion & social welfare awareness**, especially for students, women, farmers, and low-income households.

---

##  Features

- 🤖 Conversational AI that understands user needs
- ✅ Eligibility checking using rules + AI reasoning
- 🧠 Powered by **Google Gemini**
- 📂 Includes government schemes dataset (CSV/JSON)
- 🎛️ Works with Streamlit UI
- 💡 Asks follow-up questions to refine eligibility
- 🎯 India-centric civic AI solution
- 🪄 Expandable & beginner-friendly project

---

##  Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM | **Google Gemini API** |
| Agent Framework | LangChain |
| Frontend | Streamlit |
| Storage | Local JSON/CSV (Govt Schemes DB) |

---

##  System Architecture

User → Streamlit UI
→ Gemini Model (LLM Reasoning)
→ Rule-based Eligibility Logic + Schemes DB
→ Results / Recommendations


##  Project Structure

sahayakai/
│── app.py # Main Streamlit app
│── .env # API key
│── requirements.txt # Dependencies
│── data/
│ └── schemes.json # Govt schemes dataset
│── utils/
│ └── agent_logic.py # AI logic + eligibility functions
│── README.md

yaml
Copy code

---

##  Setup & Installation

### ✅ 1. Clone the Repo

```bash
git clone <your-repo-link>
cd sahayakai
✅ 2. Create Virtual Environment
bash
Copy code
python -m venv venv
Activate it:

Windows

bash
Copy code
venv\Scripts\activate
Mac/Linux

bash
Copy code
source venv/bin/activate
✅ 3. Install Requirements
bash
Copy code
pip install -r requirements.txt
✅ 4. Add Gemini API Key
Create a .env file:
GEMINI_API_KEY=your_api_key_here

▶️ Run the Application
bash
Copy code
streamlit run app.py
Open browser → http://localhost:8501

##  Example Query
I'm a 20-year-old female from Maharashtra. Family income 1.5 LPA. Are there scholarships or women-centric welfare schemes available?

✅ Output:
swift
Copy code
✅ Eligible Schemes:
• NSP National Scholarship
• Maharashtra Post-Matric Scholarship
• Sukanya Samriddhi Yojana
• Women Skill Development Grants

📎 I can share links, required docs & application steps.
📊 Sample Govt Scheme Dataset (schemes.json)
json
Copy code
[
  {
    "name": "PM Kisan Samman Nidhi",
    "category": "Farmer Support",
    "eligibility": "Small & marginal farmers with landholding",
    "income_limit": "No strict limit",
    "state": "All India"
  },
  {
    "name": "National Scholarship Portal",
    "category": "Education",
    "eligibility": "Students from low-income families",
    "income_limit": "Up to 4 LPA",
    "state": "All India"
  }
]
🧠 How It Works
Step	AI Behavior
Collect details	Age, state, income, occupation
Analyze	Compare w/ eligibility rules
Ask questions	e.g., “Are you a student/farmer?”
Recommend	Best schemes + eligibility status
Assist	Provide links, docs list & guidance

#3 Use Cases
Students searching scholarships

Farmers seeking subsidies/support

Women empowerment schemes

Housing, gas, pension, health cards

Social welfare eligibility assistance

🌟 Future Enhancements
🔗 Direct govt portal links

🗂️ Document upload + OCR assistance

🎙️ Voice chat (Hindi/Marathi)

📍 Automatic state-wise scheme filtering

🌐 WhatsApp bot/API version

🧾 PDF output: recommended schemes report

👨‍💻 Developer
Ayushi Nagpure
B.Tech — Computer Science (Final Year)
Gen-AI Project | Civic Tech
