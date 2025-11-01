import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# -------------------------------
# ✅ Configuration
# -------------------------------

st.set_page_config(page_title="SahayakAI – Govt Scheme Recommender", layout="wide")

# Load dataset (if used in your prompt)
df = pd.read_csv("schemes.csv")

# Configure Gemini API key
genai.configure(api_key="AIzaSyA4SUhQEM5djXJvekn_6cpe-bZX8wNQ67M")  # 🔑 Replace with your valid key

# Initialize model
model = genai.GenerativeModel("gemini-2.5-pro")

# -------------------------------
# 🧠 Prompt Template
# -------------------------------

prompt_template = """
You are SahayakAI, an assistant that recommends Government schemes in India.

User details:
Age: {age}
Category: {category}
State: {state}
Income: {income}
Need: {need}

You also have access to a dataset of government schemes (in context), with scheme names, eligibility, benefits, and target audience.

Using reasoning + dataset knowledge, return:
- Scheme Name
- Benefits
- Eligibility
- Documents Required
- Why this fits the user

Be structured, bullet-pointed, and helpful.
"""

# -------------------------------
# 🎨 Streamlit UI
# -------------------------------

st.title("🇮🇳 SahayakAI – Govt Scheme Eligibility Assistant")

with st.sidebar:
    st.header("Enter Your Details")

    age = st.number_input("Age", min_value=1, max_value=100)
    category = st.selectbox("Category", ["Student", "Farmer", "Woman", "Senior Citizen", "Entrepreneur", "Unemployed", "Other"])
    state = st.text_input("State (e.g. Maharashtra)")
    income = st.selectbox("Income Level", ["Below 2L", "2L - 5L", "5L - 10L", "Above 10L"])
    need = st.multiselect("Your Need", ["Education", "Healthcare", "Housing", "Startup Funding", "Pension", "Employment", "Skill Training", "Subsidy"])

    submit = st.button("Find Schemes ✅")

# -------------------------------
# 🚀 Generate Response
# -------------------------------

if submit:
    with st.spinner("Finding schemes..."):
        # Fill in the prompt
        user_prompt = prompt_template.format(
            age=age,
            category=category,
            state=state,
            income=income,
            need=", ".join(need)
        )

        # Generate result using Gemini
        response = model.generate_content(user_prompt)
        result = response.text

    st.subheader(" Recommended Govt Schemes")
    st.write(result)

    # -------------------------------
    # 🔗 Add Official Scheme Links
    # -------------------------------
    scheme_links = {
        "Pradhan Mantri Kaushal Vikas Yojana": "https://www.pmkvyofficial.org/",
        "PM Kisan Samman Nidhi": "https://pmkisan.gov.in/",
        "Stand Up India": "https://www.standupmitra.in/",
        "Mudra Yojana": "https://www.mudra.org.in/",
        "Atal Pension Yojana": "https://www.npscra.nsdl.co.in/scheme-details.php",
        "National Apprenticeship Promotion Scheme": "https://apprenticeshipindia.gov.in/",
        "Chief Minister Employment Generation Programme": "https://mahaswayam.gov.in/",
        "PMEGP": "https://www.kviconline.gov.in/pmegp/",
        "Digital India": "https://digitalindia.gov.in/"
    }

    st.markdown("---")
    st.markdown("### 🌐 Official Scheme Portals")

    found_any = False
    for scheme, url in scheme_links.items():
        if scheme.lower() in result.lower():
            found_any = True
            st.markdown(
                f"""
                <div style='margin-top:0.8em; background:#f0f7ff; padding:10px 14px; border-left:4px solid #004aad; border-radius:6px;'>
                    <b style='color:#004aad;'>{scheme}</b>: 
                    <a href='{url}' target='_blank' style='color:#0066cc; text-decoration:none; font-weight:500;'>Apply on Official Portal</a>
                </div>
                """, unsafe_allow_html=True)

    if not found_any:
        st.info("No official scheme links found in this response.")
