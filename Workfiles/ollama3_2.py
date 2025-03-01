from crewai.llm import LLM
from pydantic import BaseModel


class Dog(BaseModel):
    name: str
    age: int
    breed: str


llm = LLM(model="ollama/llama3.2:latest",base_url="http://localhost:11434")

response = llm.call(
    "Analyze the following messages and return the name, age, and breed. "
    "Meet Kona! She is 3 years old and is a black german shepherd."
)
print(response)

# Output:
# Dog(name='Kona', age=3, breed='black german shepherd')