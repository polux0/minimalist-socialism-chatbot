import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from chat import query

st.set_page_config(page_title="Minimalist Socialism Chatbot - An LLM-powered Streamlit app")

# Sidebar contents
with st.sidebar:
    # st.title('💬 Minimalist Socialism Chatbot')
    st.markdown(
        """
        <h1 style="text-align: center;">
            💬 Minimalist Socialism Chatbot
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [OpenAI/GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5) LLM model
    ''')
    st.markdown("<hr>", unsafe_allow_html=True)
    # st.markdown("<hr>")
    st.write('Made with ❤️ by [Jesse](https://t.me/jesseforyou) & [Aleksa](https://t.me/alexusnavas)')
    st.write('Deep gratitude to [The Commons Hub](https://twitter.com/CCommonsHub/status/1681235908752752641) without whose support this would not have been possible! ❤️')

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm Minimalist Socialism Chatbot, How may I help You?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    response = query(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))