import streamlit as st
import requests

API_URL = "https://flowise-psoe.onrender.com/api/v1/prediction/22e839bc-9d09-4b55-9f32-907bd60e1061"

st.set_page_config(page_title="Flowise Q&A Assistant", layout="centered")
st.title("🧠 Ask a Question from the Document")

question = st.text_input("Enter your question")

if st.button("Ask") and question.strip():
    with st.spinner("Getting answer from your agent..."):
        try:
            response = requests.post(
                API_URL,
                headers={"Content-Type": "application/json"},
                json={"question": question}
            )
            if response.ok:
                st.success("Answer:")
                st.write(response.json().get("text", "No answer returned."))
            else:
                st.error(f"Error: {response.status_code} — {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
