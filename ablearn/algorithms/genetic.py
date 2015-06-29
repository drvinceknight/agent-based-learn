import random
	
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
		self.number_of_deaths_per_generation = int(number_of_agents * death_rate)
		self.mutation_rate = mutation_rate
