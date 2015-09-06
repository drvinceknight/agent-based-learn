import unittest
import ablearn
import random


class GATesting(unittest.TestCase):  #This class is to test the Genetic Algotihm

	def test_for_initialisation_without_initial_strategy_distribution(self): 	#This method is to test the initial settings for the algorithm.
		generations = 1
		rounds_per_generation = 1
		death_rate = 0.1
		mutation_rate = 0.5
		exploitation_rate = 0.5
		choice = int(20 / 2 * (1 - exploitation_rate) + 0.05) - 1

		gen = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation,
		death_rate, mutation_rate, exploitation_rate)

		self.assertEqual(gen.generations, generations)
		self.assertEqual(gen.rounds_per_generation, rounds_per_generation)
		self.assertEqual(gen.death_rate, death_rate)
		self.assertEqual(gen.mutation_rate, mutation_rate)
		self.assertEqual(gen.exploitation_rate, exploitation_rate)

	def test_assign_strategies(self):
		generations = 1
		rounds_per_generation = 1
		death_rate = 0.1
		number_of_deaths_per_generation = int(death_rate * 10)
		mutation_rate = 0.5
		exploitation_rate = 0.5
		choice = int(20 / 2 * (1 - exploitation_rate) + 0.05) -1

		gen = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation,
		 			death_rate, mutation_rate, exploitation_rate)
		bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
		env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20, bimatrix=bimatrix)

		random.seed(1)
		for ra, ca in zip(env.row_agents, env.col_agents):
			ra.strategy = 0
			ca.strategy = 0

		gen.assign_strategies(env.row_agents, env.row_strategies)
		gen.assign_strategies(env.col_agents, env.col_strategies)
		# Asserting row agents random strategies
		self.assertEqual(env.row_agents[2].strategy, 1)
		self.assertEqual(env.row_agents[1].strategy, 2)
		self.assertEqual(env.row_agents[0].strategy, 0)
		# Asserting col agents random strategies
		self.assertEqual(env.col_agents[3].strategy, 1)
		self.assertEqual(env.col_agents[2].strategy, 0)
		self.assertEqual(env.col_agents[1].strategy, 0)
		self.assertEqual(env.col_agents[0].strategy, 1)

		self.assertEqual(len(str(env.row_agents[0].strategy)), 1) #(env.row_agents[0].strategy, 1)
		self.assertEqual(len(str(env.col_agents[0].strategy)), 1) #(env.col_agents[3].strategy, 1)

	def test_for_initialisation_without_initial_strategy_distribution(self):
		generations = 1
		rounds_per_generation = 1
		death_rate = 0.6
		mutation_rate = 0.5
		exploitation_rate = 0
		choice = int(20 / 2 * (1 - exploitation_rate) + 0.05) - 1

		gen = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation,
		 			death_rate, mutation_rate, exploitation_rate, initial_strategy_distribution=True)
		env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
					bimatrix=[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]])

		self.col_stras=[0,1]
		self.row_stras=[0,1]
		self.col_stra_dist=[0.45,0.55]
		self.row_stra_dist=[0.1,0.9]
		self.number_of_agents=200
		self.number_of_row_agents=100
		self.number_of_col_agents=100
		self.col_numb_stra=[int(self.col_stra_dist[k]*self.number_of_row_agents) for k in range(len(self.col_stras))]
		self.row_numb_stra=[int(self.row_stra_dist[k]*self.number_of_col_agents) for k in range(len(self.row_stras))]

		gen.final_agent_strategies = []
		gen.assign_strategies_initial_distribution(env.row_agents, self.row_stras,
		 		self.number_of_agents, self.row_stra_dist)
		# Asserting row agents correct strategies distribution
		self.assertEqual(gen.final_agent_strategies.count(0), 10)
		self.assertEqual(gen.final_agent_strategies.count(1), 90)

		gen.final_agent_strategies = []
		gen.assign_strategies_initial_distribution(env.col_agents, self.col_stras,
		 		self.number_of_agents, self.col_stra_dist)
		# Asserting col agents correct strategies distribution
		self.assertEqual(gen.final_agent_strategies.count(0), 45)
		self.assertEqual(gen.final_agent_strategies.count(1), 55)

	def test_kill_agents(self):
		generations = 1
		rounds_per_generation = 1
		death_rate = 0.6
		mutation_rate = 0.5
		exploitation_rate = 0
		choice = int(20 / 2 * (1 - exploitation_rate) + 0.05) - 1

		gen = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation,
		 			death_rate, mutation_rate, exploitation_rate)


		env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]])

		random.seed(2)
		utilities = [25, 6, 8, 100, 12, 7, 9, 1000, 51, 60]
		for r in env.row_agents:r.utility=random.choice(utilities)
		for c in env.col_agents:c.utility=random.choice(utilities)

		# Before kill function number of agents is 10 for each.
		self.assertEqual(len(env.row_agents), 10)
		self.assertEqual(len(env.col_agents), 10)

		gen.kill_agents(env.row_agents, env.number_of_agents, env.number_of_row_agents, env.row_strategies)
		gen.kill_agents(env.col_agents, env.number_of_agents, env.number_of_col_agents, env.col_strategies)

		# After kill function with 0.6 death rate, number of agents is 4 for each.
		self.assertTrue(gen.number_of_deaths_per_generation)
		self.assertEqual(len(env.row_agents), 4)
		self.assertEqual(len(env.col_agents), 4)

	def test_reproduce_agents(self):
		generations = 1
		rounds_per_generation = 1
		death_rate = 0.6
		mutation_rate = 0.9 # set mutation rate at 0 to be able to test exploitation.
		exploitation_rate = 1 # exploitation set to 1 (100%) meaning the agent with highest utility will be reproduced.
		choice = int((20 / 2) * (exploitation_rate - 1) + 0.05) - 1

		gen = ablearn.algorithms.genetic.Genetic(generations, rounds_per_generation,
		 			death_rate, mutation_rate, exploitation_rate)
		bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
		env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=bimatrix)

		random.seed(2) # Assign utilities to the agents to be able to test.
		utilities = [25, 6, 8, 100, 12, 7, 9, 1000, 51, 60]
		for r in env.row_agents:r.utility=random.choice(utilities)
		for c in env.col_agents:c.utility=random.choice(utilities)

		gen.kill_agents(env.row_agents, env.number_of_agents, env.number_of_row_agents, env.row_strategies)
		gen.kill_agents(env.col_agents, env.number_of_agents, env.number_of_col_agents, env.col_strategies)

		self.assertEqual(len(env.row_agents), 4) # After kill command and before reproduce, length of row agents 10.
		self.assertEqual(len(env.col_agents), 4) # After kill command and before reproduce, length of row agents 10.

		gen.reproduce_agents(env.row_agents, env.number_of_agents, env.number_of_row_agents, env.row_strategies)
		gen.reproduce_agents(env.col_agents, env.number_of_agents, env.number_of_col_agents, env.col_strategies)

		self.assertEqual(len(env.row_agents), 10) # After reproduce command, length of row agents 10.
		self.assertEqual(len(env.col_agents), 10) # After reproduce command, length of column agents 10.

		# Testing for exploitation rate at 100% for row agents, last and second to last row agents have the same utility.
		self.assertEqual(env.row_agents[-1].utility, env.row_agents[-2].utility )
		# Testing for exploitation rate at 100% for column agents, last and second to last column agents have the same utility.
		self.assertEqual(env.col_agents[-1].utility, env.col_agents[-2].utility )
