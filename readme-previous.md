1. Create virtual enviornment
python3 -m venv /your_location/minimalist-socialism-chatbot
2. Activate virtual enviornment
source /your_location/minimalist-socialism-chatbot/bin/activate
3. Upgrade `pip` 
pip install --upgrade pip
4. Install `setuptools`
pip install setuptools
5. Install necessary dependencies
pip install -r requierments.txt
6. Setup enivornment variables
cp .env example .env
7. Run application
streamlit run minimalist_socialism_chatbot_app.py

Alternatively, if you'd like to create your own embeddings: 

0. Create your own data directory
1. Modify `DATA_DIRECTORY` from `.env` in accordance with directory you created & set your `OPENAI_API_KEY`
2. Generate embeddings 
python create_embeddings.py
3. Run application
streamlit run minimalist_socialism_chatbot_app.py