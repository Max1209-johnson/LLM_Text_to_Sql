from dotenv import load_dotenv
load_dotenv() ## load all the enviroment


import streamlit as st
import os
import sqlite3

import google.generativeai as genai


## Configure our API Key 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide query as response 
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt, question])
    return response.text

## Function to retrieve from SQL DataBase
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in row:
        print(row)
    return rows


##Define Your Prompt

prompt={
""" 





"""
}


##streamlit App


st.set_page_config(page_title=" I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")


question=st.text_input("Input:", key=" input")

submit=st.button("Ask the question")



## If the submit is click

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is")

    for row in data:
        print(row)
        st.header(row)




