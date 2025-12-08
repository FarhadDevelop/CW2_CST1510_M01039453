import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")

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

st.title("📊 Multi-Domain Intelligence Platform Analytics")

# Domain selection
domain = st.selectbox("Select Domain", ["Cybersecurity", "Data Science", "IT"])

# Depending on the selected domain, show relevant analytics
if domain == "Cybersecurity":
    st.header("Cybersecurity Analytics")
    st.write("Here you can find various cybersecurity analytics and visualizations.")
    
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

    threat_df = pd.DataFrame(list(threat_data.items()), columns=["Threat Type", "Count"])
    fig = px.bar(threat_df, x="Threat Type", y="Count", title="Threats by Type", color="Count")
    st.plotly_chart(fig, use_container_width=True)

elif domain == "Data Science":
    st.header("Data Science Analytics")
    st.write("Here you can find various data science analytics and visualizations.")
    
    # Model performance metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", "92.5%")
    
    with col2:
        st.metric("Precision", "89.3%")
    
    with col3:
        st.metric("Recall", "90.1%")
    
    # Training history
    history = pd.DataFrame({
        "epoch": [1, 2, 3, 4, 5],
        "loss": [0.65, 0.48, 0.35, 0.28, 0.22],
        "accuracy": [0.70, 0.80, 0.85, 0.90, 0.94]
    })

    fig = px.line(history, x="epoch", y=["loss", "accuracy"], title="Training History", labels={"value": "Metric Value", "epoch": "Epoch"})
    st.plotly_chart(fig, use_container_width=True)
    
elif domain == "IT":
    st.header("IT Analytics")
    st.write("Here you can find various IT analytics and visualizations.")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("CPU Usage", "65%", delta="-5%")
    
    with col2:
        st.metric("Memory Usage", "72%", delta="+0.3 GB")
    
    with col3:
        st.metric("Uptime", "99.98%", delta="+0.1%")
    
    # Resource usage over time
    usage = {
        "time": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "24:00"],
        "CPU": [55, 60, 70, 65, 75, 80, 65],
        "Memory": [60, 62, 68, 70, 74, 76, 72]
    }

    fig = px.line(usage, x="time", y=["CPU", "Memory"], title="Resource Usage Over Time", labels={"value": "Usage (%)", "time": "Time"})
    st.plotly_chart(fig, use_container_width=True)

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.success("You have been logged out.")
    st.switch_page("Home.py")