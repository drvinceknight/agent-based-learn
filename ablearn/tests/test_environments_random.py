import unittest
import ablearn
import random

class RandomTesting(unittest.TestCase):
	random.seed(0)
	def test_initialisation(self):
		number_of_agents = 10
		randomtest = ablearn.environments.randomenv.randomenv(number_of_agents)
		self.assertEqual(randomtest.number_of_agents, number_of_agents)
	# Test 
	def test_transform_bimatrix_strategies_to_row_and_column_strategies(self):
		number_of_agents = 10
		row_strategies = [[ 4, 0 ], [ 5, 2 ]]
		col_strategies = [[ 4, 5 ], [ 0, 2 ]] 
		row_number_of_strategies = range(len(row_strategies))  
		col_number_of_strategies = range(len(col_strategies[0]))
		randomtest = ablearn.environments.randomenv.randomenv(number_of_agents)
		randomtest.assign_strategies(row_strategies, col_strategies, row_number_of_strategies, col_number_of_strategies)
		self.assertEqual(randomtest.row_strategies, row_strategies) 
		self.assertEqual(randomtest.col_strategies, col_strategies)
		self.assertEqual(randomtest.row_number_of_strategies, row_number_of_strategies)
		self.assertEqual(randomtest.col_number_of_strategies, col_number_of_strategies)
	"""
	Test for the creation of agents with random strategies. Was not able to use random.seed to prove the same strategies are produced.
	"""
	def test_to_create_agents_with_random_strategies(self):
		random.seed(0)
		number_of_agents = 10
		row_strategies = [[ 4, 0 ], [ 5, 2 ]]
		col_strategies = [[ 4, 5 ], [ 0, 2 ]] 
		row_number_of_strategies = range(len(row_strategies))  
		col_number_of_strategies = range(len(col_strategies[0]))
		randomtest = ablearn.environments.randomenv.randomenv(number_of_agents)
		randomtest.assign_strategies(row_strategies, col_strategies, row_number_of_strategies, col_number_of_strategies)
		
		row_agents = [ablearn.population.agents.Agent(random.choice(row_number_of_strategies)) for h in range(number_of_agents)]
		
		col_agents = [ablearn.population.agents.Agent(random.choice(col_number_of_strategies)) for h in range(number_of_agents)]
		self.assertEqual(len(randomtest.row_agents), len(row_agents))
		self.assertEqual(len(randomtest.col_agents), len(col_agents))

	def test_interaction_increases_utility(self):
		"""
		Needs fix, most of the time the test fails. This because of the random assignment of strategies.  
		"""
		random.seed(0)
		number_of_agents = 10
		row_strategies = [[ 4, 0 ], [ 5, 2 ]]
		col_strategies = [[ 4, 5 ], [ 0, 2 ]] 
		row_number_of_strategies = range(len(row_strategies))  
		col_number_of_strategies = range(len(col_strategies[0]))
		randomtest = ablearn.environments.randomenv.randomenv(number_of_agents)
		randomtest.assign_strategies(row_strategies, col_strategies, row_number_of_strategies, col_number_of_strategies)
		
		row_agents = [ablearn.population.agents.Agent(random.choice(row_number_of_strategies)) for h in range(number_of_agents)]
		
		col_agents = [ablearn.population.agents.Agent(random.choice(col_number_of_strategies)) for h in range(number_of_agents)]
		
		row_agents[0].utility += row_strategies[row_agents[0].strategies][col_agents[0].strategies]

		col_agents[0].utility += col_strategies[row_agents[0].strategies][col_agents[0].strategies]

		self.assertEqual(randomtest.row_agents[0].utility, row_agents[0].utility)
		self.assertEqual(randomtest.col_agents[0].utility, col_agents[0].utility)

	def testing_regulating_agents_population(self):
		random.seed(0)
		number_of_agents = 10
		row_strategies = [[ 4, 0 ], [ 5, 2 ]]
		col_strategies = [[ 4, 5 ], [ 0, 2 ]] 
		row_number_of_strategies = range(len(row_strategies))  
		col_number_of_strategies = range(len(col_strategies[0]))
		randomtest = ablearn.environments.randomenv.randomenv(number_of_agents)
		randomtest.assign_strategies(row_strategies, col_strategies, row_number_of_strategies, col_number_of_strategies)
		
		row_agents = [ablearn.population.agents.Agent(random.choice(row_number_of_strategies)) for h in range(number_of_agents)]
		col_agents = [ablearn.population.agents.Agent(random.choice(col_number_of_strategies)) for h in range(number_of_agents)]
		row_agents.sort(key=lambda x: x.utility)
		col_agents.sort(key=lambda x: x.utility)

		randomtest.regulating_agent_population()		
		self.assertEqual(randomtest.row_agents[0], row_agents[0])
		self.assertEqual(randomtest.col_agents[0], col_agents[0])
		self.assertEqual(randomtest.row_agents[-1], row_agents[-1])
		self.assertEqual(randomtest.col_agents[-1], col_agents[-1])
		


