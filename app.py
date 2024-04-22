import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain 
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

load_dotenv()
st.title(
    "💬 Chat with a website"
)
groq_api_key = os.environ['GROQ_API_KEY']
openai_api_key = os.environ['OPENAI_API_KEY']
st.write(
    """
    This project uses OpenAI Embeddings and FAISS Library for creating and storing vectors. 
    The chat model used here is a llama 3 model with 7b parameters. This project also makes use 
    of groq's API which is a LPU inferencing engine for faster inferencing. 
    """
)
st.write(
    """
    You will have to create an OpenAI api key and enter it here in order to use this project.
    """
)
website = st.text_input("Enter website link here to proceed")
if website:
    if "vector" not in st.session_state:
        st.session_state.embeddings = OpenAIEmbeddings(
            openai_api_key=openai_api_key
        )
        st.session_state.loader = WebBaseLoader(website)
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 5000, 
            chunk_overlap = 1000
        )
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(
            st.session_state.docs
        )
        st.session_state.vector = FAISS.from_documents(
            st.session_state.final_documents,
            st.session_state.embeddings
        )

    llm = ChatGroq(
        groq_api_key = groq_api_key, 
        model_name = 'llama3-8b-8192'
    )

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the questions based on the provided context only.
        Provide the most accurate response. 
        <context>
        {context}
        <context>
        Questions:{input}
        """
    )

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    prompt = st.text_input("Input your question here", disabled = not website)

    if prompt: 
        response = retrieval_chain.invoke({"input" : prompt})
        st.write(response['answer'])