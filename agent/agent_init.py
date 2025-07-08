from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama3.1")

prompt = PromptTemplate.from_template(
    """Jesteś dietetykiem, który zbiera informacje na temat żywienia swoich klientów, Twoim zadaniem jest kolekcjonowanie 
    danych od użytkownika do bazy danych oraz podsumowanie ich za pomocą wykresów oraz możliwych promptow: {user_input}"""
)

chain = LLMChain(llm=llm, prompt=prompt)

def run_llama(user_input: str):
    return chain.run(user_input)