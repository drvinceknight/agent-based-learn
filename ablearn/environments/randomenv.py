import random
import copy
from ablearn.rules import *
from ablearn.population import *
import ablearn

b = [[[4, 4],[0, 5]], [[5, 0],[2, 2]]]

class randomenv:
	
	"""
	This class will contain most of the procedures in the current algorithm(genetic).
	"""
	
	"""
	POPULATING
	"""

	def __init__(self, number_of_agents):
		self.number_of_agents = 10
			
	def assign_strategies(self, row_strategies, col_strategies, row_number_of_strategies, col_number_of_strategies, initial_strategy_distribution=False):
		"""
		Creating a population with individual strategies. I still haven't been able to pull a bimatrix from the rules module. For now I created a bimatrix b, just to test the method works for assigning row/column strategies from a bimatrix
		"""
		#Creates a strategy matrix for row strategies, from the given BiMatrix:
		self.row_strategies = []
		for d in range(len(b)):
			rl = []
			for e in  range(len(b[d])):
				r = b[d][e][0] 
				rl.append(r)
			self.row_strategies.append(rl)
		#Creates a strategy matrix for column strategies, from the given BiMatrix:
		self.col_strategies = []
		for f in range(len(b)):
			cl = []
			for g in  range(len(b[d])):
				c = b[f][g][1] 
				cl.append(c)
			self.col_strategies.append(cl)
		#Determine how many possible strategies for each type of agent.
		self.row_number_of_strategies = range(len(row_strategies))
		self.col_number_of_strategies = range(len(col_strategies[0]))
		#Create row and column agents, and assign random strategy to each according to the type of agent.
		if not initial_strategy_distribution:
			self.row_agents = [agents.Agent(random.choice(self.row_number_of_strategies)) for h in range(self.number_of_agents)]
			
			self.col_agents = [agents.Agent(random.choice(self.col_number_of_strategies)) for h in range(self.number_of_agents)]

		#else: "commented out,  ask if initial_strategy_distribution should be included in the genetic algorithm instead.

	"""
	INTERACTION
	"""

	def interaction(self):
		random.seed(0)
		for i in range(self.number_of_agents):
			self.row_agents[i].utility += self.row_strategies[self.row_agents[i].strategies][self.col_agents[i].strategies]

			self.col_agents[i].utility += self.col_strategies[self.row_agents[i].strategies][self.col_agents[i].strategies]
	
	"""
	REGULATING THE POPULATION
	"""


	"""

	def regulating_agent_population(self):
	
	This last section is not completed yet, I want to ask if there is a possible way of finding the position of an instance in a list by looking for a specific value in attribute, something like: row_agents.utility.index(min(row_agents.utility)). And with this to create a specific function to delete or if its max value, to reproduce the agent.
	
	For now I only have the function below for eliminating agents, but it eliminates all agents with a  certain value, and I fear that there might be more than one agent with a minimum value at some point.

	The test for this last section is also not written yet.
	"""
	"""

		d = 0
		while d < genetic.Genetic.number_of_deaths_per_generation:
			# Eliminate row agent with lowest utility.
			self.row_agents = [row_agents[k] for row_agents[k] in row_agents if row_agents[k].utility != min(([e.utility for e in self.row_agents])
			
			# Reproduce row agent with highest utility.


			# Eliminate row agent with lowest utility.
			self.col_agents = [col_agents[k] for col_agents[k] in col_agents if col_agents[k].utility != min(([e.utility for e in self.col_agents])


			# Reproduce row agent with highest utility.

	"""

