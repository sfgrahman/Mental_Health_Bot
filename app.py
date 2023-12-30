import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("Welcome to the Mental Health Chatbot API!")
#btn = st.button("Create Knowledgebase")
#if btn:
    #create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
st.markdown("""Few example questions:
            1. Who does mental illness affect?
            2. What treatment options are available?
            3. What is the difference between mental health professionals?
            
            """)