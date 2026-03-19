import os

from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent to fetch information."""

    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the response from the agent with answers and sources"""

    answer:str = Field(description="The agent's answer to the question")
    sources:List[Source] = Field(default_factory=list, description="The sources used to answer the question")

llm = ChatOllama(model="qwen2.5:0.5b", temperature=0)
tools = [TavilySearch()]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant. Use tools when needed.",
    response_format=AgentResponse,
)


def main():
    print("Hello from langchain agent")
    result = agent.invoke(
        {"messages": [HumanMessage(content="Search for Chief Architect jobs in LinkedIn portal in Bangalore")]}
    )
    print(result)
    


if __name__ == "__main__":
    main()