import random
import ablearn
	

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

	def kill_agents(self):
		""" Eliminating row and column agents with lowest utilities 
		"""
		d = 0
		while d < self.number_of_deaths_per_generation:
			ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.row_agents.sort(key=lambda x: x.utility)
			del ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.row_agents[0]
			ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.col_agents.sort(key=lambda x: x.utility)
			del ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.col_agents[0]
			d += 1

	def reproduce_agents(self):
		""" Reproducing row and column agents with highest utilities """
		while len(ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.row_agents) < ablearn.number_of_row_agents:
			ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.row_agents.sort(key=lambda x: x.utility)
			ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.row_agents.append(copy.deepcopy(self.row_agents[-1]))
		while len(ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.col_agents) < ablearn.number_of_col_agents:
			ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.col_agents.sort(key=lambda x: x.utility)
			ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv.col_agents.append(copy.deepcopy(self.col_agents[-1]))

