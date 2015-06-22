from ablearn.Abm import Agent 
import unittest

class AgentTesting(unittest.TestCase):
	def setUp(self):
		self.agent= Agent('strategy')

	def test_strategy_for_agent(self):	
