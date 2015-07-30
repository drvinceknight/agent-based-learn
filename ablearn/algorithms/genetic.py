import random
import ablearn
from ablearn.environments import *

class Genetic():
	"""
    For now only values this values have been placed.
	"""
	def __init__(self, generations, rounds_per_generation, death_rate, number_of_deaths_per_generation, mutation_rate, exploitation_rate, initial_strategy_distribution=False):
		""""
		INITIALIZATION
		"""
		self.generations = generations
		self.rounds_per_generation = rounds_per_generation
		self.death_rate = death_rate
		self.number_of_deaths_per_generation = int(death_rate * 10) #ablearn.environments.BiMatrixRandomEnv.number_of_agents)
		self.mutation_rate = mutation_rate
		self.exploitation_rate = exploitation_rate
		global env_ob
		env_ob = BiMatrixRandomEnv(number_of_agents=20, bimatrix=[[[0,1], [2,3]], [[4,5], [5,6]]])
		choice = int(env_ob.number_of_agents / 2 * (1 - self.exploitation_rate))

	def assign_strategies(self):
		""" Assigning random strategies to agents"""
		if not initial_strategy_distribution:
			""" Assigning random strategies with no initial distribution"""
		 	for r in env_ob.row_agents:r.strategy=random.choice(env_ob.row_strategies)
			for c in env_ob.col_agents:c.strategy=random.choice(env_ob.col_strategies)
		else:
			""" Assigning random strategies with initial distribution """
			for r in env_ob.row_agents:r.strategy=random.choice(strategy for strategy in initial_strategy_distribution[0] for count in range(initial_strategy_distribution[0][strategy]env_ob.row_strategies)
			for c in env_ob.col_agents:c.strategy=random.choice(env_ob.col_strategies)


	def kill_agents(self):
		""" Eliminating row and column agents with lowest utilities
		"""
		d = 0
		while d < self.number_of_deaths_per_generation:
			env_ob.row_agents.sort(key=lambda x: x.utility)
			del env_ob.row_agents[0]
			env_ob.col_agents.sort(key=lambda x: x.utility)
			del env_ob.col_agents[0]
			d += 1

	def reproduce_agents(self):
		""" Reproducing row and column agents with highest utilities """
		while len(env_ob.row_agents) < env_ob.number_of_row_agents:
			env_ob.row_agents.sort(key=lambda x: x.utility)
			env_ob.row_agents.append(copy.deepcopy(random.choice(env_ob.row_agents[choice:])))  # test random.choice
			if random.random() < mutation_rate: # test mutation rate
				 row_agents[-1].strategy = random.choice([s for s in r_s if s != row_agents[-1].strategy])

		while len(env_ob.col_agents) < env_ob.number_of_col_agents:
			env_ob.col_agents.sort(key=lambda x: x.utility)
			env_ob.col_agents.append(copy.deepcopy(random.choice(env_ob.col_agents[choice:])))  # test random.choice
			if random.random() < mutation_rate: # test mutation rate
				col_agents[-1].strategy = random.choice([s for s in r_s if s != col_agents[-1].strategy])