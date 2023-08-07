# Minimalist Socialism Chatbot

This repository contains a minimalist socialism chatbot application. Follow the steps below to set up and run the application:

0. **Clone the repository**

git clone git@github.com:polux0/minimalist-socialism-chatbot.git or https://github.com/polux0/minimalist-socialism-chatbot.git

1. **Create virtual environment**
    1. python3 -m venv . 
    2. source ./bin/activate

2. **Upgrade `pip` and install `setuptools`**
pip install --upgrade pip
pip install setuptools

3. **Setup environment variables**
cp .env.example .env

4. **Install necessary dependencies**
pip install -r requirements.txt

5. **Create embeddings**
python create_embeddings.py

6. **Run the application**
streamlit run minimalist_socialism_chatbot_app.py
