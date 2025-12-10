import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
st.set_page_config(page_title="💬 AI Assistant", page_icon="💬", layout="wide")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to access the chat.")
    if st.button("Go to login page"):
        st.switch_page("Home.py")      # back to the first page
    st.stop()


# Page title and caption
st.title("💬 AI Assistant")
st.caption("Powered by GPT-4o")

# Domain selection
domain = st.selectbox("Select Domain", ["Cybersecurity", "Data Science", "IT"])

# Initialize session state with system prompt for the selected domain
if "system_prompt" not in st.session_state or st.session_state.get("domain") != domain:
    st.session_state.domain = domain
    if domain == "Cybersecurity":
        st.session_state.system_prompt = (
            """You are a cybersecurity expert. 
            Analyze incidents, threats, and vulnerabilities. 
            Provide technical guidance using MITRE ATT&CK, CVE references.
            Prioritize actionable recommendations."""
        )
    elif domain == "Data Science":
        st.session_state.system_prompt = (
            """You are a data science expert. 
            Help with data analysis, visualization, statistical methods, and machine learning. 
            Explain concepts clearly and suggest appropriate techniques."""
        )
    elif domain == "IT":
        st.session_state.system_prompt = (
            """You are an IT operations expert. 
            Help troubleshoot issues, optimize systems, manage tickets, and provide infrastructure guidance. 
            Focus on practical solutions."""
        )

    # Reset messages when domain changes
    st.session_state.messages = [{"role": "system", "content": st.session_state.system_prompt}]
    st.session_state.domain = domain
    st.info(f"Domain changed to **{domain}**. Chat history reset.")
    st.rerun()

# Sidebar with controls
with st.sidebar:
    st.subheader("Chat Controls")
    
    # Display message count
    message_count = len([m for m in st.session_state.messages if m["role"] != "system"])
    st.metric("Messages", message_count)

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [{"role": "system", "content": st.session_state.system_prompt}]
        st.rerun()

# Display all previous messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Get user input based on domain
if domain == "Cybersecurity":
    prompt = st.chat_input("Ask about cybersecurity...")
elif domain == "Data Science":
    prompt = st.chat_input("Ask about data science...")
elif domain == "IT":
    prompt = st.chat_input("Ask about IT operations...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenAI API with streaming
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.messages,
        stream=True
    )

    # Display streaming response
    with st.chat_message("assistant"):
        container = st.empty()
        full_reply = ""

        # Process each chunk as it arrives
        for chunk in completion:
            delta = chunk.choices[0].delta
            if delta.content:
                full_reply += delta.content
                container.markdown(full_reply + "▌")  # Add cursor effect

        # Remove cursor and show final response
        container.markdown(full_reply)   

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_reply})