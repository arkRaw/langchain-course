import os
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

# tavily_client = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """Tool that searches the web for information
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily_client.search(query)

def main():
    print("Hello from langchain-course!")
    llm = ChatOllama(model="gpt-oss:latest", temperature=0)
    tools = [TavilySearch()]
    agent = create_agent(model=llm, tools=tools)
    response = agent.invoke({"messages": HumanMessage(content="search for 3 jobs of AI engineer using langchain on linkedin in Delhi NCR region and list the details")})
    print(response)

if __name__ == "__main__":
    main()
