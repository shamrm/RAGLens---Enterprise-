import streamlit as st

# Import your RAG function
from NFIPRagLens import ask_question

# Temporary placeholder (remove once connected)
def ask_question(question):
    return "This is a placeholder response from the NFIP chatbot."

# Page config
st.set_page_config(
    page_title="NFIP Flood Insurance Chatbot",
    page_icon="🌊",
    layout="centered"
)

# Title
st.title("🌊 Flood Insurance Chatbot")
st.caption("Ask questions about FEMA's NFIP Flood Insurance Manual (03/2025)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question about flood insurance...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Searching NFIP manual..."):
            try:
                answer = ask_question(user_input)
                st.markdown(answer)
            except Exception as e:
                st.error(f"Error: {e}")
                answer = "Sorry, something went wrong."

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# Clear chat button
if st.button("🗑️ Clear chat"):
    st.session_state.messages = []
    st.experimental_rerun()
