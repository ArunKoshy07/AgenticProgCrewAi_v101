from crewai import LLM
from config import Config

class ModelHandler:
    def __init__(self, model_key, config_path='model_registry.json'):
        self.config = Config.from_json(config_path)
        print(self.config)
        
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

# Example usage
if __name__ == "__main__":
    model_handler = ModelHandler(
        model_key="llama"
    )
    llm_instance = model_handler.get_model_instance()
    print(llm_instance.model_name,llm_instance.base_url)
    # Now you can use llm_instance for further operations