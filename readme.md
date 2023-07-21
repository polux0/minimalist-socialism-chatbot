# Minimalist Socialism Chatbot

This repository contains a minimalist socialism chatbot application. Follow the steps below to set up and run the application:

1. **Create virtual environment**
python3 -m venv /your_location/minimalist-socialism-chatbot
source /your_location/minimalist-socialism-chatbot/bin/activate


2. **Upgrade `pip` and install `setuptools`**
pip install --upgrade pip
pip install setuptools


3. **Install necessary dependencies**
pip install -r requirements.txt


4. **Setup environment variables**
cp .env.example .env


5. **Run the application**
streamlit run minimalist_socialism_chatbot_app.py


Alternatively, if you'd like to create your own embeddings:

1. **Create your own data directory**
2. **Modify `DATA_DIRECTORY` in `.env` file according to the directory that you created & set your `OPENAI_API_KEY`**
3. **Generate embeddings and run the application**

python create_embeddings.py
streamlit run minimalist_socialism_chatbot_app.py