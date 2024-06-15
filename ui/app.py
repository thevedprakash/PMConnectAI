import streamlit as st
import subprocess
from typing import List

def run_script(email_ids: List[str]):
    for email in email_ids:
        # Call the script and pass the email ID
        process = subprocess.Popen(['python3', 'src/main.py'], stdin=subprocess.PIPE, text=True)
        process.communicate(email)

st.title("Conversation Trigger")

email_list = st.text_area("Enter email IDs (one per line):")
if st.button("Start Conversations"):
    email_ids = [email.strip() for email in email_list.splitlines() if email.strip()]
    if email_ids:
        run_script(email_ids)
        st.success("Conversations started for the provided email IDs.")
    else:
        st.error("Please enter at least one email ID.")
