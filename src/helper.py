from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from typing import List
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings

def load_pdf_files(data):
    loader=DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Given a list of dccument objects, return a new list of document ojects containing only 'source' in  metadata and the original page_content"""

    minimal_docs:List[Document]=[]
    for doc in docs:
        src=doc.metadata.get("source")
        minimal_docs.append(Document
                            (
                            page_content=doc.page_content ,
                            metadata={"source":src}                         
                            )                            
)
    return minimal_docs

#split the Documents into smaller chunks
def text_split(minimal_docs):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    texts_chunk=text_splitter.split_documents(minimal_docs)
    return texts_chunk

#embeddings


def download_embeddings():
    """Download the embeddings from huggingface """
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    embeddings=HuggingFaceEmbeddings(
        model_name=model_name
    )
    return embeddings

embedding = download_embeddings()