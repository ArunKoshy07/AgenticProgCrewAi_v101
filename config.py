from pydantic import BaseModel
from typing import Dict
import json


class ModelConfig(BaseModel):
    model_name: str
    base_url: str

class AgentConfig(BaseModel):
    role: str
    goal: str
    backstory: str
    allow_delegation: bool
    verbose: bool
    model_name: str

    class Config:
        extra = "allow"  # Allow extra fields

class TaskConfig(BaseModel):
    description: str
    expected_output: str
    agent_key: str

class CrewConfig(BaseModel):
    agents: list
    tasks: list
    verbose: bool

class Config(BaseModel):
    models: Dict[str, ModelConfig]
    agents: Dict[str, AgentConfig]
    tasks: Dict[str, TaskConfig]
    crews: Dict[str, CrewConfig]

    @classmethod
    def from_json(cls, path: str):
        with open(path, 'r') as file:
            data = json.load(file)
        return cls(**data)



if __name__ == "__main__":
    config = Config.from_json('./model_registry.json')
    print(config)
    print(config.models)
    print(config.models['llama'])
    print(config.models['llama'].model_name)
    print(config.models['llama'].base_url)