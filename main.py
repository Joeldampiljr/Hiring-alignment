import streamlit as st

# Page setup
st.set_page_config(page_title="Strengths & Culture Fit", layout="centered")

# Title
st.title("🧠 Strengths & Culture Match")
st.write("Discover how your thinking style and values align with our team roles.")

# Step 1: Ask for basic info
name = st.text_input("What’s your name?")
user_code = st.text_input("Create a 5-digit code to save your result")

# Step 2: Sample behavior-based question
st.markdown("### 🔍 When you post something and no one reacts to it, what do you usually do?")
answer = st.radio("Choose one:",
    [
        "Wait and hope someone notices eventually",
        "Ask for feedback so I can improve",
        "Feel discouraged and stop posting for now",
        "Keep going—results take time anyway"
    ])

# Step 3: Show result
if st.button("Submit"):
    st.success(f"Thanks, {name}! Your response is saved under code {user_code}.")
    st.write("✅ Your answer helps us understand how your mindset fits a role and our culture.")

