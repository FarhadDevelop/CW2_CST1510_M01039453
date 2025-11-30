import streamlit as st
from openai import OpenAI
from data.db import connect_database
from data.incidents import get_all_incidents

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
st.set_page_config(page_title="AI Incident Analyzer", page_icon="🔍", layout="wide")

st.title("🔍 AI Incident Analyzer")

# Fetch all incidents from the database
conn = connect_database()
incidents = get_all_incidents(conn)

if not incidents.empty:
    incident_records = incidents.to_dict(orient="records")
else:
    incident_records = []

incident_list = [
    f"{inc['incident_id']} - {inc['category']} ({inc['severity']})"
    for inc in incident_records
]

selected_idx = st.selectbox(
"Select an incident to analyze:", 
range(len(incident_list)), 
format_func=lambda x: incident_list[x]
)

incident = incidents.iloc[selected_idx]

# Display incident details
st.subheader("Incident Details")
st.write(f"**Incident ID:** {incident['incident_id']}")
st.write(f"**Category:** {incident['category']}")
st.write(f"**Severity:** {incident['severity']}")
st.write(f"**Description:** {incident['description']}")
st.write(f"**Status:** {incident['status']}")

# Analyze incident with AI
if st.button("🤖 Analyze with AI", type="primary"):
    with st.spinner("AI analyzing incident..."):
            
        analysis_prompt = f"""Analyze this cybersecurity incident:
              
        Type: {incident['category']}
        Severity: {incident['severity']}
        Description: {incident['description']}
        Status: {incident['status']}
              
        Provide:
        1. Root cause analysis
        2. Immediate actions needed
        3. Long-term prevention measures
        4. Risk assessment"""   
        
        # Call ChatGPT API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": "You are a cybersecurity expert."
                 },
                {"role": "user", 
                 "content": analysis_prompt
                 }
            ],
            stream=True
        )

        # Display AI analysis
        st.subheader("🧠 AI Analysis")
        st.write(response.choices[0].message.content)

conn.close()