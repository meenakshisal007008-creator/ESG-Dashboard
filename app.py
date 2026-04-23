import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ESG Dashboard", layout="wide")

# ---------------- BANNER (SMALL & CENTERED) ----------------
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    try:
        st.image("banner.png", width=700)
    except:
        st.warning("⚠️ banner.png not found. Keep image in same folder.")

# ---------------- RUNNING TITLE ----------------
st.markdown("""
<div style='width:100%; background-color:#166534; padding:10px; border-radius:6px; margin-top:-10px;'>
<marquee style='color:white; font-size:16px;'>
🌱 ESG Intelligence Platform | Real-Time Sustainability Insights | Risk Analytics | Data-Driven Decisions
</marquee>
</div>
""", unsafe_allow_html=True)

# ---------------- USER GUIDE ----------------
st.markdown("## 🎯 About This Tool")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 👥 Who is this for?

    - Business leaders evaluating sustainability performance  
    - Investors assessing ESG risks  
    - Analysts comparing ESG across companies  
    - Students & researchers learning ESG models  
    """)

with col2:
    st.markdown("""
    ### 🧭 How to use?

    1. Enter company name & select industry  
    2. Ensure company has **real ESG data**  
    3. Adjust values (0–100 scale)  
    4. Click **Calculate ESG Score**  
    5. View results  

    💡 Higher score = Better sustainability  
    """)

st.markdown("---")

# ---------------- COMPANY INPUT ----------------
st.markdown("## 📥 Enter Company ESG Data")

col1, col2 = st.columns(2)

company_list = [
    "TCS", "Infosys", "Reliance Industries", "HDFC Bank",
    "ICICI Bank", "Wipro", "Adani Enterprises",
    "ITC", "L&T", "Axis Bank", "Other (Type Manually)"
]

with col1:
    selected_company = st.selectbox("Select Company", company_list)

    if selected_company == "Other (Type Manually)":
        company = st.text_input("Enter Company Name")
    else:
        company = selected_company

with col2:
    industry = st.selectbox(
        "Industry",
        [
            "IT", "Banking", "Manufacturing", "Energy",
            "Healthcare", "Retail", "Telecommunications",
            "Infrastructure", "Pharmaceuticals", "FMCG",
            "Automobile", "Real Estate"
        ]
    )

# ---------------- ESG INPUTS ----------------
st.markdown("## ESG Inputs")

# Environmental
st.markdown("### 🌿 Environmental")
col1, col2 = st.columns(2)

with col1:
    renewable = st.slider("Renewable Energy (%)", 0, 100, 50)
    emissions = st.slider("Carbon Emissions (lower is better)", 0, 100, 50)

with col2:
    waste = st.slider("Waste Management Efficiency", 0, 100, 50)
    water = st.slider("Water Usage Efficiency", 0, 100, 50)

# Social
st.markdown("### 👥 Social")
col1, col2 = st.columns(2)

with col1:
    employee = st.slider("Employee Satisfaction", 0, 100, 50)
    diversity = st.slider("Diversity & Inclusion", 0, 100, 50)

with col2:
    safety = st.slider("Workplace Safety", 0, 100, 50)
    community = st.slider("Community Engagement", 0, 100, 50)

# Governance
st.markdown("### 🏛 Governance")
col1, col2 = st.columns(2)

with col1:
    transparency = st.slider("Transparency", 0, 100, 50)
    ethics = st.slider("Business Ethics", 0, 100, 50)

with col2:
    board = st.slider("Board Effectiveness", 0, 100, 50)
    compliance = st.slider("Regulatory Compliance", 0, 100, 50)

# ---------------- CALCULATE ----------------
if st.button("🚀 Calculate ESG Score"):

    env_score = (renewable + (100 - emissions) + waste + water) / 4
    soc_score = (employee + diversity + safety + community) / 4
    gov_score = (transparency + ethics + board + compliance) / 4
    total_score = (env_score + soc_score + gov_score) / 3

    st.markdown("## 📊 ESG Performance Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Environmental", round(env_score, 2))
    col2.metric("Social", round(soc_score, 2))
    col3.metric("Governance", round(gov_score, 2))
    col4.metric("Overall ESG", round(total_score, 2))

    st.markdown("---")

    # Risk Indicators
    st.markdown("## ⚠ Risk Indicators")

    risks = []

    if emissions > 70:
        risks.append("🔴 High Emissions Risk")
    if employee < 40:
        risks.append("🔴 Poor Employee Satisfaction")
    if transparency < 40:
        risks.append("🔴 Weak Governance")

    if not risks:
        risks.append("🟢 Low ESG Risk")

    for r in risks:
        st.error(r)

    st.markdown("---")

    # Insights
    st.markdown("## 📈 ESG Impact Insights")

    insights = []

    insights.append("🌱 Improve renewable energy usage" if renewable < 60 else "🌱 Strong renewable energy usage")
    insights.append("👥 Improve employee satisfaction" if employee < 60 else "👥 Strong employee engagement")
    insights.append("🏛 Improve governance transparency" if transparency < 60 else "🏛 Strong governance")

    for i in insights:
        st.info(i)