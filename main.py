import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Load the Groq API key (only necessary for Groq)
groq_api_key = os.getenv("GROQ_API_KEY")
api_key = st.sidebar.text_input("Enter your API Key:", type="password")

# LangChain API and Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"

# Streamlit app title and sidebar configuration
st.title("Q&A Chatbot")
model = st.sidebar.selectbox("Select Open Source Model", ["gemma2-9b-it", "llama-3.3-70b-versatile","llama3-70b-8192"])  # Adding GPT for testing
role = st.sidebar.selectbox("Select the role", ["হিরো আলম", "Salman Khan","Amitab Bacchan", "Sahrukh Khan","Narendra Modi","ওবায়দুল কাদের"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Define the system prompt
system_prompt = "Do not give your openion and just You will replicate the exect funny talking style of {role} so that its super funny and try to draw their popular speech and use simple english."

# Create chat prompt template
prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{question}")])

# Function to generate response using Groq (or other models)
def generate_response(question, role, model, temperature, max_tokens, api_key):
    dynamic_prompt = system_prompt.format(role=role)
    updated_prompt = ChatPromptTemplate.from_messages([("system", dynamic_prompt), ("human", "{question}")])

    try:
        # Choose the correct model based on the selected option
        if model == "gemma2-9b-it":  # For Groq model
            llm = ChatGroq(model=model, groq_api_key=api_key)  # Correctly pass Groq API key
        else:  # For OpenAI model (if you need to handle OpenAI models)
            llm = ChatOpenAI(model=model, api_key=api_key)  # Pass OpenAI API key
        
        # Output parser
        output_parser = StrOutputParser()
        chain = updated_prompt | llm | output_parser
        
        # Generate the response
        answer = chain.invoke({'question': question})
        return answer
    except Exception as e:
        return f"Error: {e}"

# User input and response generation
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, role, model, temperature, max_tokens, api_key)
    st.write(f"{role} :{response}")
else:
    st.write("Please provide the user input.")
