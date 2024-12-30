from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import AzureChatOpenAI
import os

os.environ["OPENAI_API_TYPE"]    = "azure"
os.environ["OPENAI_API_VERSION"] = "--Enter your API version--"
os.environ["azure_endpoint"]     = "--Enter your endpoint--"
os.environ["OPENAI_API_KEY"]     = "--Enter API key--"

model = AzureChatOpenAI(
    azure_endpoint=os.getenv("azure_endpoint"),
    deployment_name="--Enter Your Deployment name--",
    model_name="gpt-35-turbo", 
    temperature=0
    )


file_path = "" # Enter your file location

loaders = [PyPDFLoader(file_path)]

index = VectorstoreIndexCreator(
    embedding=HuggingFaceEmbeddings(),
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)).from_loaders(loaders)

chain = RetrievalQA.from_chain_type(llm=model,
                                    chain_type="stuff",
                                    retriever=index.vectorstore.as_retriever(),
                                    input_key="prompt")
