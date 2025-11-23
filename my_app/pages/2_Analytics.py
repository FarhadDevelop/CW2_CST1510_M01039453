import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cyber Incidents Analytics", page_icon="📊", layout="wide")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to view the analytics.")
    if st.button("Go to login page"):
        st.switch_page("Home.py")      # back to the first page
    st.stop()

st.title("📊 Cyber Incidents Analytics")

# Security metrics
st.header("Security Metrics")
st.write("Here you can find various security metrics and visualizations.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Threats Detected", 247, delta="+12")

with col2:
    st.metric("Vulnerabilities Found", 58, delta="-3")

with col3:
    st.metric("Incidents Resolved", 189, delta="+7")

# Threat data
threat_data = {
    "Malware": 120,
    "Phishing": 80,
    "Ransomware": 30,
    "DDoS": 17,
    "Intrusion": 46
}

st.header("Threat Data")
threat_df = pd.DataFrame({
    "Threat Type": list(threat_data.keys()),
    "Count": list(threat_data.values())
})

fig_threats = px.bar(threat_df, x="Threat Type", y="Count", title="Threat Types Distribution", color="Count")
st.plotly_chart(fig_threats, use_container_width=True)

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.success("You have been logged out.")
    st.switch_page("Home.py")