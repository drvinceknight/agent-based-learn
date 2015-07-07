import unittest
import ablearn
import random


class GATesting(unittest.TestCase):  #This class is to test the Genetic Algotihm

	def test_for_initialisation_without_initial_strategy_distribution(self):  #This method is to test the initial settings for the algorithm.
		generations = 10
		rounds_per_generation = 10
		death_rate = .5
		number_of_deaths_per_generation = int(death_rate * 10) #ablearn.environments.randomenv.randomenv.__init__.number_of_agents)
		mutation_rate = .5
		# When no initial_strategy_distribution is chosen.
		random.seed(1)
		# row_agents = [Agent(random.choice(self.row_strategies)) for e in range(number_of_agents)], when assuming 2 agents and the strategies are assigned in the following way
		row_agents = [0, 1]
		# col_agents = [Agent(random.choice(self.col_strategies)) for e in range(number_of_agents)], when assuming 2 agents and the strategies are assigned in the following way
		col_agents = [0, 1]		

		genetic = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation, death_rate, number_of_deaths_per_generation, mutation_rate)
		self.assertEqual(genetic.generations, generations)
		self.assertEqual(genetic.rounds_per_generation, rounds_per_generation)
		self.assertEqual(genetic.death_rate, death_rate)
		self.assertEqual(genetic.number_of_deaths_per_generation, number_of_deaths_per_generation)
		self.assertEqual(genetic.mutation_rate, mutation_rate)

	"""	
	def test_for_initialisation_with_initial_strategy_distribution(self):  #This method is to test the initial settings for the algorithm.
		number_of_agents = 2
		generations = 10
		rounds_per_generation = 10
		death_rate = .5
		number_of_deaths_per_generation = int(number_of_agents * death_rate)
		mutation_rate = .5
		row_matrix = [[1, 3], [5, 3]]
		col_matrix = [[3, 2], [2, 2]]
		row_strategies = range(len(row_matrix))
		col_strategies = range(len(col_matrix))
		initial_strategy_distribution = 
		# With initial_strategy_distribution chosen.
		random.seed(1)
		#row_agents = [Agent(random.choice(strategy for strategy in initial_strategy_distribution[0] for count in range(initial_strategy_distribution[0][strategy)) for e in range(number_of_agents)]  # when assuming 2 agents and the strategies are assigned in the following way
		row_agents = [0, 1]
		#col_agents = [Agent(random.choice(strategy for strategy in initial_strategy_distribution[1] for count in range(initial_strategy_distribution[0][strategy)) for e in range(number_of_agents)]  # when assuming 2 agents and the strategies are assigned in the following way
		col_agents = [0, 1]		

		genetic = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation, death_rate, number_of_deaths_per_generation, mutation_rate)
		self.assertEqual(genetic.number_of_agents, number_of_agents)
		self.assertEqual(genetic.generations, generations)
		self.assertEqual(genetic.rounds_per_generation, rounds_per_generation)
		self.assertEqual(genetic.death_rate, death_rate)
		self.assertEqual(genetic.number_of_deaths_per_generation, number_of_deaths_per_generation)
		self.assertEqual(genetic.mutation_rate, mutation_rate)
		#self.assertEqual(genetic.row_agents, row_agents)  #Pops an error
		#self.assertEqual(genetic.col_agents, col_agents)  #Pops an error
	"""
		
		
		
		
			
	
