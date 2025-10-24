from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

chat_model = ChatOpenAI(
    model="google/gemini-2.5-pro",  # or gemini-2.5-pro if available
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class comedian."),
    ("human", "Tell me a joke about {topic}")
])

chain = prompt | chat_model | StrOutputParser()
result = chain.invoke({"topic": "beets"})
print("Gemini 2.5 Joke:", result)
