import streamlit as st
from pole_emploi_agent import create_pole_emploi_agent, process_user_input

st.set_page_config(page_title="Pôle Emploi GPT", page_icon="🤖")
st.title("Pôle Emploi GPT")

@st.cache_resource
def get_agent():
    return create_pole_emploi_agent()

agent = get_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Comment puis-je vous aider dans votre recherche d'emploi ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = process_user_input(agent, prompt)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
