import requests
import json
import streamlit as st

url = 'http://localhost:11434/api/generate'
    
headers = {
    'Content-Type': 'application/json'
}


def generate_response(prompt, option):
    st.session_state.conversation_history.append(prompt)
    full_prompt = "\n".join(st.session_state.conversation_history)
    
    # Determine the model based on the option (use this instead of a IF-ELIF)
    model = {'Normal': 'mistral', 'Pirate': 'pirate', 'Mafia Boss': 'mafia'}.get(option, 'mistral')

    data = {
        'model': model,
        'stream': False,
        'prompt': full_prompt
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Process the response
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        st.session_state.conversation_history.append(actual_response)
        print(st.session_state.conversation_history)
        return actual_response
    else:
        return f'Error: {response.status_code}, {response.text}'


def main():
    if 'conversation_history' not in st.session_state:
        st.session_state['conversation_history'] = []
    
    last_selected_option = st.session_state.get('last_selected_option', '')

    st.set_page_config(page_title="AI Chatbot", page_icon='🤖')
    st.header('AI ChatBot')
    
    # Dropdown for selecting who to talk to
    option = st.selectbox(
        'Who would you like to talk to?',
        ('Normal','Mafia Boss', 'Pirate'))

    # Reset conversation history if the option has changed
    if option != last_selected_option:
        st.session_state['conversation_history'] = []
        st.session_state['last_selected_option'] = option

    # Chat input
    messages = st.container(height=400)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        response = generate_response(prompt, option)
        role = {"Normal": "Chat", "Mafia Boss": "Mafia Boss", "Pirate": "Pirate"}.get(option, "Chat")
        messages.chat_message("assistant").write(f"{role}: {response}")

if __name__ == '__main__':
    main()