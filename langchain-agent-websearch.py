import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from tavily import TavilyClient

load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
      query: The query to search for
    Returns:
      The search result
    """
    print(f"Searching for {query}")
    #return "Bangalore is cool"
    response = tavily_client.search(query)
    return response

llm = ChatOllama(model="qwen2.5:0.5b", temperature=0)
tools = [search]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant. Use tools when needed.",
)


def main():
    print("Hello from langchain agent")
    result = agent.invoke(
        {"messages": [HumanMessage(content="Search for positions in LinkedIn for Head of Architecture in Bangalore")]}
    )
    print(result["messages"][-1].content)
    


if __name__ == "__main__":
    main()