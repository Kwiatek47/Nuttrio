from langchain.agents import AgentExecutor, create_react_agent, ZeroShotAgent
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_ollama import OllamaLLM
from langchain.tools import tool
from agent.prompts import system_prompt
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv
from agent.tools.json_insert import json_insert
from agent.tools.json_search import json_search

load_dotenv()

# Model
llm = OllamaLLM(model="llama3.1:latest")

# Tools
os.environ["TAVILY_API_KEY"] = os.getenv("TVLY_API")
search = TavilySearch(max_results=2)

tools = [search, json_insert, json_search]
tool_names = [tool.name for tool in tools]

# Prompt
prompt = ZeroShotAgent.create_prompt(
    tools=tools,
    prefix=system_prompt(),
    suffix="Begin!\n\nQuestion: {input}\n{agent_scratchpad}",
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"]
)

# Agent
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# Executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# Function to run the agent with a given prompt
def run_llama(prompt_text: str) -> str:
    result = agent_executor.invoke({"input": prompt_text})
    return result.get("output", "[Brak odpowiedzi]")
