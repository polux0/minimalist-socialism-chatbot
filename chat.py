from langchain.chains.question_answering import load_qa_chain
from models import models
from load_embeddings import load_embeddings
from dotenv import load_dotenv
load_dotenv()

def query(prompt: str):

    # question = "How do we know that our senses give us correct representations of the objects we perceive through them?"
    # question = "What was the real crime of the French branches of the International?"
    # question = "I was wondering what are Marx's critiques of capitalism?"
    # question = "Would you help me understand what are some ways to reimagine capitalism according to socialists?"

    embeddings = load_embeddings()
    relevant_documents = embeddings.similarity_search(prompt, include_metadata=True)
    chat = models.get_gpt_llm()
    # run the chain by passing the output of the similarity search
    # https://python.langchain.com/docs/modules/chains/additional/question_answering
    chain = load_qa_chain(chat, chain_type="stuff")
    response = chain.run(input_documents=relevant_documents, question=prompt)
    return response