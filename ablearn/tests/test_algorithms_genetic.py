import unittest
import ablearn
import random


class GATesting(unittest.TestCase):  #This class is to test the Genetic Algotihm

	def test_for_initialisation_without_initial_strategy_distribution(self): 	#This method is to test the initial settings for the algorithm.
		generations = 10
		rounds_per_generation = 10
		death_rate = .5
		number_of_deaths_per_generation = int(death_rate * 10)
		mutation_rate = .5
		# When no initial_strategy_distribution is chosen.

		row_agents = [0, 1]
		col_agents = [0, 1]

		genetic = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation, death_rate, number_of_deaths_per_generation, mutation_rate)
		self.assertEqual(genetic.generations, generations)
		self.assertEqual(genetic.rounds_per_generation, rounds_per_generation)
		self.assertEqual(genetic.death_rate, death_rate)
		self.assertEqual(genetic.number_of_deaths_per_generation, number_of_deaths_per_generation)
		self.assertEqual(genetic.mutation_rate, mutation_rate)

	def test_assign_strategies(self):
		generations = 10
		rounds_per_generation = 10
		death_rate = .5
		number_of_deaths_per_generation = int(death_rate * 10)
		mutation_rate = .5
		# When no initial_strategy_distribution is chosen.
		row_agents = [0, 1]
		col_agents = [0, 1]


		gen = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation, death_rate, number_of_deaths_per_generation, mutation_rate)
		bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
		env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20, bimatrix=bimatrix)

		for ra, ca in zip(env.row_agents, env.col_agents):
			ra.strategy = random.choice(env.row_strategies)
			ca.strategy = random.choice(env.col_strategies)

		gen.assign_strategies()

		self.assertEqual(len(str(env.row_agents[0].strategy)), 1)
		self.assertEqual(len(str(env.col_agents[0].strategy)), 1)

	def test_kill_agents(self):
		generations=1
		rounds_per_generation=1
		death_rate=0.5
		number_of_deaths_per_generation=int(death_rate*20)
		mutation_rate=0.5

		gen = ablearn.algorithms.genetic.Genetic(generations,
				rounds_per_generation, death_rate,
				number_of_deaths_per_generation, mutation_rate)

		bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
		env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=bimatrix)

		gen.kill_agents()

		self.assertEqual(env.row_agents[0].utility, 0)
		self.assertEqual(env.col_agents[0].utility, 0)

	def test_reproduce_agents(self):
		generations=1
		rounds_per_generation=1
		death_rate=0.5
		number_of_deaths_per_generation=int(death_rate*20)
		mutation_rate=0.5


		gen = ablearn.algorithms.genetic.Genetic(generations,
				rounds_per_generation, death_rate,
				number_of_deaths_per_generation, mutation_rate)

		bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
		env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=bimatrix)

		gen.reproduce_agents()

		self.assertEqual(env.row_agents[-1].utility, 0)
		self.assertEqual(env.col_agents[-1].utility, 0)
		
