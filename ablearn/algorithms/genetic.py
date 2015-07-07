import random
import ablearn
from ablearn.environments.randomenv import * 	

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
		self.number_of_deaths_per_generation = int(death_rate * 10) #ablearn.environments.randomenv.randomenv.__init__.number_of_agents)
		self.mutation_rate = mutation_rate
