import random
import ablearn
from ablearn.environments import BiMatrixRandomEnv as env

class Genetic:
	"""
    For now only values this values have been placed.
	"""
	def __init__(self, generations, rounds_per_generation, death_rate, number_of_deaths_per_generation, mutation_rate):
		""""
		INITIALIZATION
		"""
		self.generations = generations
		self.rounds_per_generation = rounds_per_generation
		self.death_rate = death_rate
		self.number_of_deaths_per_generation = int(death_rate * 10) #ablearn.environments.BiMatrixRandomEnv.number_of_agents)
		self.mutation_rate = mutation_rate

	def assign_strategies(self):
	 	for r in env.row_agents:r.strategy=random.choice(env.row_strategies)
		for c in env.col_agents:c.strategy=random.choice(env.col_strategies)

	def kill_agents(self):
		""" Eliminating row and column agents with lowest utilities
		"""
		d = 0
		while d < self.number_of_deaths_per_generation:
			env.row_agents.sort(key=lambda x: x.utility)
			del env.row_agents[0]
			env.col_agents.sort(key=lambda x: x.utility)
			del env.col_agents[0]
			d += 1

	def reproduce_agents(self):
		""" Reproducing row and column agents with highest utilities """
		while len(env.row_agents) < env.number_of_row_agents:
			env.row_agents.sort(key=lambda x: x.utility)
			env.row_agents.append(copy.deepcopy(env.row_agents[-1]))
		while len(env.col_agents) < env.number_of_col_agents:
			env.col_agents.sort(key=lambda x: x.utility)
			env.col_agents.append(copy.deepcopy(env.col_agents[-1]))
