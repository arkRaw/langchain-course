from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
# from langchain_ollama import ChatOllama
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_deepseek import ChatDeepSeek
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """ Scheme for a source used by the agent"""

    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description= "List of sources to generate the answer")

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
    # Default Ollama context is 4096 tokens; Tavily JSON fills it before the model can answer.
    # llm = ChatOllama(model="gpt-oss:latest", temperature=0, num_ctx=8192)
    # llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    llm = ChatDeepSeek(model="deepseek-chat")
    tools = [TavilySearch(max_results=3)]
    agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
    response = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="search for jobs of Software engineer with 5+ years of experience on linkedin in Delhi NCR region and list the details"
                )
            ]
        }
    )

    if structured := response.get("structured_response"):
        print("\nAnswer:", structured.answer)
        if structured.sources:
            print("\nSources:")
            for source in structured.sources:
                print(f"  - {source.url}")
    else:
        last_message = response["messages"][-1]
        print("\nAnswer:", last_message.content or "(empty — model ran out of context)")

if __name__ == "__main__":
    main()
