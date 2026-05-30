'''import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.3
    )

    return llm'''

import streamlit as st
from langchain_groq import ChatGroq


def get_llm():

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=st.secrets["GROQ_API_KEY"],
        temperature=0.1
    )

    return llm