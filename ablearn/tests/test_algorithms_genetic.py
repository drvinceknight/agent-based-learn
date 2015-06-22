import unittest
from ablearn.Abm import kill_one_agent_with_given_utility

class AgentTesting(unittest.TestCase):
	
	def test_killing_agents_correct(self):
		a = agents[2].utility
		u = utility
		if a == u:
			self.assertNotIn(agents[2], agents)
	
		

	def test_killing_agent_returns_error_if_agents_not_numbers(self):	
		self.kill = kill_one_agent_with_given_utility()
		self.assertRaises(ValueError, self.kill, 'ten', 0)

