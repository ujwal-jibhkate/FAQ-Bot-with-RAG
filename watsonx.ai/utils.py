from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# WML python SDK
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM

url = "https://us-south.ml.cloud.ibm.com"

watsonx_project_id = "--Enter Your Project ID--"

api_key = "--Enter your API key--"


def get_model(model_type,max_tokens,min_tokens,decoding,temperature):

    generate_params = {
        GenParams.MAX_NEW_TOKENS: max_tokens,
        GenParams.MIN_NEW_TOKENS: min_tokens,
        GenParams.DECODING_METHOD: decoding,
        GenParams.TEMPERATURE: temperature
    }

    model = Model(
        model_id=model_type,
        params=generate_params,
        credentials={
            "apikey": api_key,
            "url": url
        },
        project_id=watsonx_project_id
        )

    return model

def get_lang_chain_model(model_type,max_tokens,min_tokens,decoding,temperature):

    base_model = get_model(model_type,max_tokens,min_tokens,decoding,temperature)
    langchain_model = WatsonxLLM(model=base_model)

    return langchain_model

# Specify model parameters
model_type = "meta-llama/llama-2-70b-chat"
max_tokens = 1000
min_tokens = 100
decoding = DecodingMethods.GREEDY
temperature = 0.1

# Get the watsonx model that can be used with LangChain
model = get_lang_chain_model(model_type, max_tokens, min_tokens, decoding, temperature)

file_path = "--Enter a path of your PDF file--"

loaders = [PyPDFLoader(file_path)]

index = VectorstoreIndexCreator(
    embedding=HuggingFaceEmbeddings(),
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)).from_loaders(loaders)

chain = RetrievalQA.from_chain_type(llm=model,
                                    chain_type="stuff",
                                    retriever=index.vectorstore.as_retriever(),
                                    input_key="prompt")

