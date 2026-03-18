import streamlit as st
from main import run_system
import json

st.set_page_config(page_title="CuraBot", page_icon="🩺")

st.title("🩺 CuraBot AI Doctor")
st.caption("Educational only")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Enter symptoms (e.g., fever, cough)")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    result = run_system(user_input)

    reply = f"""
### 🧾 Diagnosis

📊 **Confidence**
{result['confidence']}

📌 **Evidence**
{result['evidence']}

➡️ **Next Step**
{result['next_step']}

⚠️ **Bias Check**
{result['bias']}
"""

    reply += "\n\n```json\n" + json.dumps(result, indent=2) + "\n```"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
