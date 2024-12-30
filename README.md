# FAQ Chatbot Using Retrieval-Augmented Generation (RAG)

This repository demonstrates a FAQ chatbot built using the Retrieval-Augmented Generation (RAG) approach. The project aims to streamline the process of retrieving and delivering FAQ-based information by leveraging Large Language Models (LLMs) integrated with a vector database for enhanced query resolution.

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Implementation](#implementation)
  - [Prerequisites](#prerequisites)
  - [Key Components](#key-components)
  - [Steps](#steps)
- [Acknowledgments](#acknowledgments)

## Overview
The chatbot uses RAG to address inefficiencies in static FAQ systems by combining an LLM with a custom knowledge base. By incorporating dynamic retrieval mechanisms, it ensures personalized and contextually accurate responses for user queries.

## Problem Statement
Traditional FAQ pages are static and often fail to address dynamic and evolving queries effectively. This creates inefficiencies for users, especially customer service representatives (CSRs), in retrieving relevant information promptly.

## Solution
To overcome these challenges, the FAQ chatbot integrates:
1. **Vector Database**: Stores FAQ data and enables efficient information retrieval.
2. **Large Language Model (LLM)**: Enhances responses by leveraging the retrieved data alongside its pre-trained knowledge.
3. **RAG Framework**: Combines the LLM's generative capabilities with the precision of information retrieval to provide accurate and context-aware responses.

### Why RAG?
Retrieval-Augmented Generation enhances the LLM's output by referencing an external knowledge base. It mitigates issues such as:
- Propagation of outdated or inaccurate information.
- Lack of specificity in responses.
- Difficulty in addressing domain-specific queries.

## Implementation

### Prerequisites
1. **Python 3.10 or 3.11**: Install a compatible Python environment.
2. **Required Libraries**: Listed in `requirements.txt`.

### Key Components
1. **Vector Database**: Used for storing and retrieving FAQ data.
2. **LangChain**: Facilitates prompt engineering and model chaining.
3. **LLM Integration**:
   - For **watsonx.ai**, the `meta-llama/llama-2-70b-chat` model is used for generating responses.
   - For **Azure OpenAI**, the `GPT-35-TURBO` model is used as the LLM.

### Steps
1. **Set Up Project Files**:
   - Clone this repository and navigate to the project directory.
   - Ensure the following files are in place:
     - `main.py`: Application entry point.
     - `utils.py`: Contains helper functions and configurations.
     - `requirements.txt`: Lists required Python libraries.

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Configure Settings**:
   - Open the `utils.py` file in a text editor or IDE.
   - Update the following fields with the appropriate values:
     - **For watsonx.ai**:
       - `PROJECT_ID`: Your watsonx.ai project ID.
       - `API_KEY`: Your watsonx.ai API key.
     - **For Azure OpenAI**:
       - `API_KEY`: Your Azure OpenAI subscription key.
       - `API_VERSION`: Version of the Azure OpenAI service you are using.
       - `ENDPOINT`: Endpoint URL for your Azure OpenAI instance.

4. **Run the Application**:
   ```bash
   streamlit run main.py

## Acknowledgments

This project utilizes modern LLM technologies and the RAG framework to solve real-world challenges in dynamic FAQ handling. Special thanks to the developers of watsonx.ai, Azure OpenAI, and open-source tools like LangChain for enabling this implementation.
