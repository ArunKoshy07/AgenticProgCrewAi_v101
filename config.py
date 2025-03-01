from pydantic import BaseModel
from typing import Dict
import json


class ModelConfig(BaseModel):
    """
    Model configuration
    """
    model_name: str
    base_url: str

class Config(BaseModel):
    models: Dict[str, ModelConfig]

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