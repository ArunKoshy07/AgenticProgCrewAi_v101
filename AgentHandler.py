from config import Config
from ModelHandler import ModelHandler
from crewai import Agent

class AgentHandler:
    def __init__(self, agent_key,agent_instance:Agent=None, config_path='config.json'):
        self.config = Config.from_json(config_path)
        
        if agent_key not in self.config.agents:
            raise ValueError(f"Agent key '{agent_key}' not found in registry.")
        
        self.agent_config = self.config.agents[agent_key]
        print(self.agent_config.model_name)
        self.model_handler = ModelHandler(model_key=self.agent_config.model_name, config_path= config_path)
        self.agent_instance = agent_instance

    def create_agent(self):
        model_instance = self.model_handler.get_model_instance()
        self.agent_instance = Agent(
            role= self.agent_config.role,
            goal=self.agent_config.goal,
            backstory=self.agent_config.backstory,
            allow_delegation=self.agent_config.allow_delegation,
            verbose=self.agent_config.verbose,
            model_instance= model_instance
        )
        # Include any additional properties from agent_config
        for key, value in self.agent_config.dict(exclude_unset=True).items():
            if key not in ["role", "goal", "backstory", "allow_delegation", "verbose", "model_name"]:
                print(key)
                setattr(self.agent_instance, key, value)

    def get_agent_instance(self):
        if self.agent_instance is None:
            self.create_agent()
        return self.agent_instance

    def display_agent_info(self):
        if self.agent_instance is None:
            self.create_agent()
        print(f"Role: {self.agent_instance.role}")
        print(f"Goal: {self.agent_instance.goal}")
        print(f"Backstory: {self.agent_instance.backstory}")
        print(f"Allow Delegation: {self.agent_instance.allow_delegation}")
        print(f"Verbose: {self.agent_instance.verbose}")
        # # Display any additional properties
        # for key, value in self.agent_instance.items():
        #     if key not in ["role", "goal", "backstory", "allow_delegation", "verbose", "model_instance"]:
        #         print(f"{key}: {value}")
        self.model_handler.display_model_info()

# Example usage
if __name__ == "__main__":
    agent_handler = AgentHandler(
        agent_key="agent1"
    )
    agent_instance = agent_handler.get_agent_instance()
    agent_handler.display_agent_info()
    # Now you can use agent_instance for further operations