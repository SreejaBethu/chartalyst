import streamlit as st
import pandas as pd
from data_utils import clean_and_describe_data
from llm_agent import ask_question

st.set_page_config(page_title="Chartalyst", layout="wide")
st.title("📊 Chartalyst - Your AI-Powered Data Analyst")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    summary = clean_and_describe_data(df)
    st.markdown("### Dataset Summary")
    st.text(summary)

    question = st.text_input("Ask a question about your data:")
    if question:
        with st.spinner("Analyzing..."):
            response = ask_question(df, question)
            st.markdown("### 📌 Answer")
            st.write(response)
