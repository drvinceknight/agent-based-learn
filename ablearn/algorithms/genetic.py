import random
import ablearn
import copy



class Genetic():
	"""
    This class acts as a simple Genetic Algorithm for interaction of row and column players
	"""

	""""		INITIALIZATION		"""
	def __init__(self, generations, rounds_per_generation, death_rate,
				mutation_rate, exploitation_rate, initial_strategy_distribution=False): # This are the needed input for this class
		self.generations = generations # Number of generations. Times the simulated environment will run.
		self.rounds_per_generation = rounds_per_generation # The number of time the simulation will run for each geneartion.
		self.death_rate = death_rate # Equivalent to the percentage of agents that will die at the end of each generation. An equal number of agents with random or the best strategies will be created for the next generation.
		self.mutation_rate = mutation_rate # Mutation in this code allows to create an agent with different strategy than the best strategy in the previous generation. A high value will allow our new agents to mutate more often, and a low will do the opposite.
		self.exploitation_rate = exploitation_rate # This value will give us the percentage of the population that will not pass their strategies to the new agents. A value of 1 (100%) will allow only the agent with the highest utility to pass on her strategy to the new agents.

	def assign_strategies(self, agents, agents_strategies): # This function is run once the column and row agents are created, and it will randomly assign them a strategy to use.
		""" Assigning random strategies to agents"""
		for a in agents: # Iterate through agents.
			a.strategies=random.choice(agents_strategies) # Assign a random strategy to each agent.
			#print a.strategies

	def assign_strategies_initial_distribution(self, agents, agents_strategies, number_of_agents, agent_initial_distribution):
		self.final_agent_strategies = []
		agents_number_of_strategies=[int(agent_initial_distribution[k]*int(number_of_agents / 2)) for k in range(len(agents_strategies))]
		for k in range(len(agents_strategies)):
			for s in range(agents_number_of_strategies[k]):
				if k==agents_strategies[k]:
					self.final_agent_strategies.append(agents_strategies[k])
		random.shuffle(self.final_agent_strategies)
		#print self.final_agent_strategies
		for a in agents:
			a.strategies=self.final_agent_strategies[agents.index(a)]

	def kill_agents(self, agents, number_of_agents, number_of_x_agents, agents_strategies): # This function will kill the calculated number of agents from the death rate after each generation.
		self.number_of_deaths_per_generation = int(self.death_rate * (number_of_x_agents)) # This variable represents the number of agents that will be killed after each generation.
		""" Eliminating row and column agents with lowest utilities	"""
		d = 0
		while d < self.number_of_deaths_per_generation:
			agents.sort(key=lambda x: x.utility) # Sort agents according to utility from low to high.
			del agents[0] # Kills agents with lowest utility (payoff)
			d += 1

	def reproduce_agents(self, agents, number_of_agents, number_of_x_agents, agents_strategies): # Creates each generation the equal number of agents killed per generation.
		choice = int((number_of_agents / 2) * (self.exploitation_rate - 1 ) + 0.05) - 1 # Calculates how many agents will be taken in account for passing on their strategies to the new agents.
		""" Reproducing row and column agents with highest utilities """
		while len(agents) < number_of_x_agents:
			agents.sort(key=lambda x: x.utility) # Sort agents according to utility (payoff) from low to high.
			agents.append(copy.deepcopy(random.choice(agents[choice:])))  # Creates an agent and assigns her a strategy according to the exploitation rate.
			if random.random() < self.mutation_rate: # How frequently the new agents will be mutated, and assigned a different strategy from the best of the previous generation.
				 agents[-1].strategies = random.choice([s for s in agents_strategies if s != agents[-1].strategies]) # Select a strategy for each new agent different from the best of the current generation.
