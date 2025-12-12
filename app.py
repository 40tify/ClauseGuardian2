import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(page_title="LMA Clause Guardian", layout="wide")

# Dummy AI analysis function
def mock_ai_analysis(clause):
    # In a real implementation, this would interface with an LLM
    return {
        "risk_score": random.randint(0, 100),
        "detected_risks": [
            "Ambiguous definition of EBITDA",
            "Missing cure period",
            "Insufficient notification deadline"
        ],
        "lma_standard": "The clause should clearly define EBITDA and include a 30-day notification period for any change of control.",
        "suggested_redline": "In case of a change of control, the borrower must provide a notification 30 days in advance."
    }

# Sidebar
st.sidebar.header("Clause Guardian Controls")
risk_appetite = st.sidebar.slider("Risk Appetite", 1, 3, 2, format="Low/Medium/High", value=2)
st.sidebar.metric("Documents Scanned Today", value=14)
st.sidebar.metric("Risk Averted", value="$2.5m")

# Main header
st.title("LMA Clause Guardian")
st.subheader("Automated LMA Compliance & Risk Engine")

# Input section
st.header("Paste Draft Loan Clause")
default_clause = (
    "Change of Control: The borrower must notify the lender of any change of control within 14 days."
)
clause_text = st.text_area("Draft Loan Clause", default_clause, height=200)

# Action button
if st.button("Analyze for LMA Compliance"):
    # Perform "analysis"
    results = mock_ai_analysis(clause_text)

    # Risk score card
    st.subheader("Risk Score")
    risk_score = results["risk_score"]
    color = "red" if risk_score > 70 else "orange" if risk_score > 40 else "green"
    st.markdown(f"<h1 style='color: {color};'>{risk_score}</h1>", unsafe_allow_html=True)

    # Expanders for analysis details
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("Detected Risks"):
            for risk in results["detected_risks"]:
                st.markdown(f"- {risk}")

    with col2:
        with st.expander("LMA Standard"):
            st.write(results["lma_standard"])

    with col3:
        with st.expander("Suggested Redline"):
            st.write(results["suggested_redline"])

# Download audit report button (simulated)
if st.button("Download Audit Report"):
    st.success("Audit report generated! (This is a simulation; no actual file is downloaded.)")

# Uncomment the following lines to integrate a real LLM later
# import openai
# def real_ai_analysis(clause):
#     response = openai.ChatCompletion.create(
#         model="your_model_id",
#         messages=[
#             {"role": "user", "content": f"Analyze this loan clause for LMA compliance: {clause}"}
#         ],
#     )
#     return response.choices[0].message['content']
