import os
from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI

load_dotenv()

def ask_question(df, query: str) -> str:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    agent = create_pandas_dataframe_agent(llm, df, verbose=False)
    try:
        response = agent.run(query)
    except Exception as e:
        response = f"Error: {str(e)}"
    return response
