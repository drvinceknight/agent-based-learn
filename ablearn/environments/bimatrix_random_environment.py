import ablearn
import random

class BiMatrixRandomEnv():
	""" This class will create the row and column agents for the 2 player game
		, and will make them interact (compete) with each other randomly in order
		to obtain which	strategy for each type of agent is the one that generates
		more utility(fittest)
	"""

	""" INITIALIZATION"""

	def __init__(self, number_of_agents, bimatrix): # The needed input for this class.

		self.number_of_agents = number_of_agents # Total number of agents before determining what type of agents they are.
		self.number_of_row_agents = number_of_agents / 2 # Split number of agents and determine how many row agents.
		self.number_of_col_agents = number_of_agents / 2 # Split number of agents and determine how many column agents.

		self.bimatrix = bimatrix # For our interactions the bimatrix gives the strategy payoff for each type of agent.

		self.number_of_row_strategies = len(bimatrix) # Count the number of strategies available for each row agent.
		self.number_of_col_strategies = len(bimatrix[0]) # Count the number of strategies available for each column agent.

		self.row_strategies = range(self.number_of_row_strategies) # A strategy number for row agents is assigned.
		self.col_strategies = range(self.number_of_col_strategies) # A strategy number for column agents is assigned

		self.row_agents = [ablearn.Agent() for k in
				range(self.number_of_row_agents)] # Creates row agents without strategies
		self.col_agents = [ablearn.Agent() for k in
				range(self.number_of_col_agents)] # Creates column agents without strategies

	def interact(self): # This function will make row agents interact (compete) against column agents.
		""" Agents interact and get a resulting utility from the interaction"""
		pairs = self.randomly_pair_agents() # Pairs a row agent with a column agent.
		for ra, ca in pairs:
			utility = self.strategies_to_utilities([ra.strategies, ca.strategies]) # Variable that is equivalent to the utility each row and column agent get from the interaction.
			ra.increment_utility(utility[0]) # Increments each row agent's utility.
			ca.increment_utility(utility[1]) # Increments each column agent's utility.

	def strategies_to_utilities(self, strategy): # Transform value of strategy to the corresponding utility.
		""" Utility from each interacting pair of agents for each agents is determined"""
		return self.bimatrix[strategy[0]][strategy[1]] # Returns the payoff pair equivalent to the pair of utilities one for each type of agent.

	def randomly_pair_agents(self): # Randomly pairs agents
		""" Each row agent and column agent will be paired with their counterparts """
		random.shuffle(self.row_agents) # Randomly shuffle the row agents in the list.
		random.shuffle(self.col_agents) # Randomly shuffle the column agents in the list.
		return zip(self.row_agents, self.col_agents) # Create pairs of random row and column agents.
