import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatOllama(model="qwen2.5:0.5b", temperature=0)
tools = [TavilySearch()]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant. Use tools when needed.",
)


def main():
    print("Hello from langchain agent")
    result = agent.invoke(
        {"messages": [HumanMessage(content="Search for Chief Architect jobs in LinkedIn portal in Bangalore")], "response_format": AgentResponse}
    )
    print(result["messages"][-1].content)
    


if __name__ == "__main__":
    main()