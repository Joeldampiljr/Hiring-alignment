import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

# Function to write to Google Sheet
def append_to_gsheet(name, user_code, answer):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = st.secrets["gcp_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Hiring Responses").sheet1
    sheet.append_row([name, user_code, answer])

# Step 3: Show result
if st.button("Submit"):
    append_to_gsheet(name, user_code, answer)
    st.success(f"Thanks, {name}! Your response is saved under code {user_code}.")
    st.write("✅ Your answer helps us understand how your mindset fits a role and our culture.")
