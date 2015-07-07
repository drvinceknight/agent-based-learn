import ablearn

class Environment:
    def __init__(self, number_of_agents):
        self.number_of_agents = number_of_agents
        self.agents = [ablearn.Agent() for k in range(self.number_of_agents)]
