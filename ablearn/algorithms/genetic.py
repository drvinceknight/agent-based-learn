import random
import ablearn
import copy



class Genetic():
	"""
    For now only values this values have been placed.
	"""
	def __init__(self, generations, rounds_per_generation, death_rate,
				mutation_rate, exploitation_rate, initial_strategy_distribution=False):

		""""		INITIALIZATION		"""
		#global env_ob
		#env_ob = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=10, bimatrix=[[[0,1], [2,3]], [[4,5], [5,6]]])

		self.generations = generations
		self.rounds_per_generation = rounds_per_generation
		self.death_rate = death_rate
		self.mutation_rate = mutation_rate
		self.exploitation_rate = exploitation_rate

	def assign_strategies(self, agents, agents_strategies):
		""" Assigning random strategies to agents"""
		for a in agents:
			a.strategies=random.choice(agents_strategies)
			#print a.strategies

	def kill_agents(self, agents, number_of_agents, number_of_x_agents, agents_strategies):
		self.number_of_deaths_per_generation = int(self.death_rate * (number_of_x_agents))
		""" Eliminating row and column agents with lowest utilities	"""
		d = 0
		while d < self.number_of_deaths_per_generation:
			agents.sort(key=lambda x: x.utility)
			del agents[0]
			#self.reproduce_agents(agents, number_of_agents, number_of_x_agents, agents_strategies)
			d += 1

	def reproduce_agents(self, agents, number_of_agents, number_of_x_agents, agents_strategies):
		choice = int((number_of_agents - 2) / 2 * (self.exploitation_rate - 1)) - 1
		""" Reproducing row and column agents with highest utilities """
		while len(agents) < number_of_x_agents:
			agents.sort(key=lambda x: x.utility)
			agents.append(copy.deepcopy(random.choice(agents[choice:])))  # test random.choice
			if random.random() < self.mutation_rate: # test mutation rate
				 agents[-1].strategies = random.choice([s for s in agents_strategies if s != agents[-1].strategies])
