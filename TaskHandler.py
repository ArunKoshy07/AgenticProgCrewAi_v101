from config import Config
from AgentHandler import AgentHandler
from crewai import Task,Agent

class TaskHandler:
    def __init__(self, task_key, agent_instance:Agent=None,config_path='config.json'):
        self.config = Config.from_json(config_path)
        
        if task_key not in self.config.tasks:
            raise ValueError(f"Task key '{task_key}' not found in registry.")
        
        self.task_config = self.config.tasks[task_key]
        self.agent_handler = AgentHandler(agent_key=self.task_config.agent_key,agent_instance=agent_instance,config_path=config_path)
        self.agent_instance = self.agent_handler.get_agent_instance()
        self.task_instance = None

    def create_task(self):
        self.task_instance = Task(
            description=self.task_config.description,
            expected_output=self.task_config.expected_output,
            agent=self.agent_instance
        )
        return self.task_instance

    def get_task_instance(self):
        if self.task_instance is None:
            self.create_task()
        return self.task_instance

    def display_task_info(self):
        if self.task_instance is None:
            self.create_task()
        print(f"Task Description: {self.task_instance.description}")
        print(f"Expected Output: {self.task_instance.expected_output}")
        print("Agent Info:")
        self.agent_handler.display_agent_info()

# Example usage
if __name__ == "__main__":
    task_handler = TaskHandler(
        task_key="task1"
    )
    task_instance = task_handler.get_task_instance()
    task_handler.display_task_info()
    # Now you can use task_instance for further operations