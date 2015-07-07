import random
import copy
from ablearn.rules import *
from ablearn.population import *
import ablearn

random.seed(0)

b = [[[4, 4],[0, 5]], [[5, 0],[2, 2]]]
"""
COMMENTED OUT BECAUSE TO MAKE TESTS WORK.



def eliminate_low_utility_agent(agents):
	#Sort row agents for eliminating.
	agents.sort(key=lambda x: x.utility)
	# Eliminate row agent with lowest utility.
	del agents[0]
			
def reproduce_high_utility_agent(agents, mutation_rate, agent_number_of_strategies):
	#Sort row agents for reproducing.
	agents.sort(key=lambda x: x.utility)
	# Reproduce row agent with highest utility.
	agents.append(copy.deepcopy(agents[-1]))
	if random.random() < mutation_rate:
		agents[-1].strategies = random.choice([ s for s in self.agent_number_of_strategies if s != agents[-1].strategies])
"""			
		
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
	
		for i in range(self.number_of_agents):
			self.row_agents[i].utility += self.row_strategies[self.row_agents[i].strategies][self.col_agents[i].strategies]

			self.col_agents[i].utility += self.col_strategies[self.row_agents[i].strategies][self.col_agents[i].strategies]
	
	"""
	REGULATING THE POPULATION
	"""

	def regulating_agent_population(self):
		"""	
		
		"""
	

		d = 0
		while d < 10: #algorithms.genetic.Genetic.number_of_deaths_per_generation:  COMMENTED OUT BECAUSE REFERENCE DID NOT WORK.
			"""
		COMMENTED OUT BECAUSE REFERENCE DID NOT WORK.
		while d < algorithms.genetic.Genetic.number_of_deaths_per_generation: 
			# Eliminate row agent with lowest utility.
			eliminate_low_utility_agent(self.row_agents)
			# Reproduce row agent with highest utility.
			reproduce_high_utility_agent(self.row_agents, algorithms.genetic.Genetic.mutation_rate, self.row_number_of_strategies)

			# Eliminate column agent with lowest utility.
			eliminate_low_utility_agent(self.col_agents)
			# Reproduce column agent with highest utility.
			reproduce_high_utility_agent(self.col_agents, algorithms.genetic.Genetic.mutation_rate, self.col_number_of_strategies)

			"""
			#Sort row agents for eliminating.
			self.row_agents.sort(key=lambda x: x.utility)
			# Eliminate row agent with lowest utility.
			del self.row_agents[0]
	
			#Sort row agents for reproducing.
			self.row_agents.sort(key=lambda x: x.utility)
			# Reproduce row agent with highest utility.
			self.row_agents.append(copy.deepcopy(self.row_agents[-1]))
			if random.random() < 0.4: #algorithms.genetic.Genetic.mutation_rate:
				self.row_agents[-1].strategies = random.choice([ s for s in self.row_number_of_strategies if s != self.row_agents[-1].strategies])

			#Sort column agents for eliminating.
			self.col_agents.sort(key=lambda x: x.utility)
			# Eliminate column agent with lowest utility.
			del self.col_agents[0]
							
			#Sort column agents for reproducing.
			self.col_agents.sort(key=lambda x: x.utility)
			# Reproduce column agent with highest utility.
			self.col_agents.append(copy.deepcopy(self.col_agents[-1]))
			if random.random() < 0.4: #algorithms.genetic.Genetic.mutation_rate:
				self.col_agents[-1].strategies = random.choice([ s for s in self.col_number_of_strategies if s != self.col_agents[-1].strategies])

			d += 1
