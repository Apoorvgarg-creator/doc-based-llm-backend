from langchain.llms import Ollama
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.ollama import OllamaEmbeddings
from langchain.prompts import PromptTemplate
import os
from utils.extract_text import extract_pdf_content 
from langchain.chains import RetrievalQA

PERSIST_DIRECTORY = 'docs/chroma/'

def create_upload_folder():
    if not os.path.exists(PERSIST_DIRECTORY):
        os.makedirs(PERSIST_DIRECTORY)

def loadPdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return pages


# Function to answer question based on PDF text
def answer_question_util(pdf_path, question, filename):
    # Extract text from PDF
    pages = loadPdf(pdf_path)
    text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=150,
    length_function=len
    )
    docs = text_splitter.split_documents(pages)

    embedding = OllamaEmbeddings()

    # Create the vector store
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory=PERSIST_DIRECTORY
    )
    
    llm = Ollama(model="llama2")
    
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)# Run chain
    qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    # chain_type="map_reduce",
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

    result = qa_chain({"query": question})
    answer = result["result"]
    
    return answer
