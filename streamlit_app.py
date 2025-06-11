import os
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import VertexAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import VertexAI
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

# Load environment
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Vertex AI client via env var
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Function to scrape Planto.ai homepage
@st.cache_data
def load_site_text(url: str):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    texts = [el.get_text() for el in soup.find_all(["h1","h2","h3","p","li"])]
    return "\n".join(texts)

# Prepare embeddings
@st.cache_resource
def get_vectorstore(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_text(text)
    embeddings = VertexAIEmbeddings()
    return FAISS.from_texts(docs, embeddings)

# Initialize Streamlit UI
st.set_page_config(page_title="Planto.ai Support (Gemini)")
st.title("Planto.ai Customer Support Chatbot (Gemini AI)")

# Load and index site content once
data = load_site_text("https://planto.ai/")
vectorstore = get_vectorstore(data)

# Set up QA chain with Vertex AI LLM
llm = VertexAI(
    model_name="text-bison@001",
    temperature=0.2,
    max_output_tokens=512
)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
query = st.text_input("Ask about Planto.ai:")
if query:
    with st.spinner("Gemini AI is thinking..."):
        response = qa.run(query)
    st.session_state.history.append((query, response))

# Display history
for q, a in st.session_state.history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Gemini AI:** {a}")
