from config import Config
from TaskHandler import TaskHandler
from AgentHandler import AgentHandler

class CrewHandler:
    def __init__(self, crew_key: str, config_path='config.json'):
        self.config = Config.from_json(config_path)
        self.crew_config = self.config.crews[crew_key]
        print(self.crew_config)
        self.verbose = self.crew_config.verbose
        self.agents = self.initialize_agents()
        self.tasks = self.initialize_tasks()
        self.cross_check_agents()

    def initialize_agents(self):
        agents = {}
        for agent_key in self.crew_config.agents:
            agent_config = self.config.agents[agent_key]
            agent_handler = AgentHandler(agent_key, agent_config.model_name, config_path='config.json')
            agent_instance = agent_handler.get_agent_instance()
            agents[agent_key] = agent_instance
        return agents

    def initialize_tasks(self):
        self.tasks = []
        for task_key in self.crew_config.tasks:
            print(task_key)
            task_config = self.config.tasks[task_key]
            print(self.agents[task_config.agent_key])
            task_handler = TaskHandler(task_key,self.agents.get(task_config.agent_key),config_path='config.json')
            task_instance = task_handler.get_task_instance()
            self.tasks.append(task_instance)
        return self.tasks

    def cross_check_agents(self):
        task_agents = {task["agagent_key"] for task in self.tasks}
        crew_agents = set(self.crew_config["agents"])

        missing_agents = task_agents - crew_agents
        if missing_agents:
            raise ValueError(f"Missing agents in crew config: {missing_agents}")

    def execute_tasks(self):
        for task in self.tasks:
            if self.verbose:
                print(f"Executing task: {task['description']}")
            agent = task["agent"]
            self.execute_task_with_agent(task, agent)

    def execute_task_with_agent(self, task, agent):
        if self.verbose:
            print(f"Agent {agent['role']} is executing task: {task['description']}")
        # Here you would add the logic to execute the task with the agent
        # For example, you might call a method on the agent object to perform the task
        # agent.perform_task(task)

    def display_crew_info(self):
        print("Crew Information:")
        print("Agents:")
        for agent_key, agent in self.agents.items():
            print(f" - {agent['role']}: {agent['goal']}")
        print("Tasks:")
        for task in self.tasks:
            print(f" - {task['description']} (Agent: {task['agent']['role']})")

# Example usage
if __name__ == "__main__":
    crew = CrewHandler("crew1")
    crew.display_crew_info()
    # crew.execute_tasks()