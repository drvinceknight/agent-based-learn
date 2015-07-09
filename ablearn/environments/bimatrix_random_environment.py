import ablearn
import random

class BiMatrixRandomEnv():
	def __init__(self, number_of_agents, bimatrix):
		self.number_of_agents = number_of_agents
		self.number_of_row_agents = number_of_agents / 2
		self.number_of_col_agents = number_of_agents / 2

		self.bimatrix = bimatrix

		self.number_of_row_strategies = len(bimatrix)
		self.number_of_col_strategies = len(bimatrix[0])

		self.row_strategies = range(self.number_of_row_strategies)
		self.col_strategies = range(self.number_of_col_strategies)

		self.row_agents = [ablearn.Agent(random.choice(self.row_strategies)) for k in
				range(self.number_of_row_agents)]
		self.col_agents = [ablearn.Agent(random.choice(self.col_strategies)) for k in
				range(self.number_of_col_agents)]

	def interact(self):
		pairs = self.randomly_pair_agents()
		for ra, ca in pairs:
			utility = self.strategies_to_utilities([ra.strategy, ca.strategy])
			ra.increment_utility(utility[0])
			ca.increment_utility(utility[1])

	def strategies_to_utilities(self, strategy):	
		return self.bimatrix[strategy[0]][strategy[1]]

	def randomly_pair_agents(self):
		random.shuffle(self.row_agents)
		random.shuffle(self.col_agents)
		return zip(self.row_agents, self.col_agents)
