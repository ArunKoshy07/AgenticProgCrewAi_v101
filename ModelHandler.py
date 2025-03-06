from crewai import LLM
from config import Config

class ModelHandler:
    def __init__(self, model_key, config_path='config.json'):
        self.config = Config.from_json(config_path)
        
        if model_key not in self.config.models:
            raise ValueError(f"Model key '{model_key}' not found in registry.")
        
        model_config = self.config.models[model_key]
        self.model_name = model_config.model_name
        self.base_url = model_config.base_url
        self.llm_instance = None

    def initialize_model(self):
        self.llm_instance = LLM(
            model=self.model_name,
            base_url=self.base_url
        )

    def get_model_instance(self):
        if self.llm_instance is None:
            self.initialize_model()
        return self.llm_instance
    
    def display_model_info(self):
        if self.llm_instance is None:
            self.initialize_model()
        print(f"Model Name: {self.model_name}")
        print(f"Base URL: {self.base_url}")

# Example usage
if __name__ == "__main__":
    model_handler = ModelHandler(
        model_key="deepseek"
    )
    model_handler.display_model_info()
    llm_instance = model_handler.get_model_instance()
    # Now you can use llm_instance for further operations