import unittest
import ablearn

class AgentTesting(unittest.TestCase):

    def test_initialisation(self):
        strategies = ['R', 'P', 'S']
        agent = ablearn.Agent(strategies)
        self.assertEqual(agent.strategies, strategies)
        self.assertEqual(agent.utility, 0)
        self.assertFalse(agent.label)

    def test_labelling(self):
        strategies = ['R', 'P', 'S']
        agent = ablearn.Agent(strategies, label=5)
        self.assertEqual(agent.strategies, strategies)
        self.assertEqual(agent.utility, 0)
        self.assertEqual(agent.label, 5)

    def test_increment_utility(self):
        strategies = ['R', 'P', 'S']
        agent = ablearn.Agent(strategies, label=5)
        self.assertEqual(agent.utility, 0)
        agent.increment_utility()
        self.assertEqual(agent.utility, 1)
        agent.increment_utility(5)
        self.assertEqual(agent.utility, 6)
        agent.increment_utility(-3)
        self.assertEqual(agent.utility, 3)
        agent.increment_utility(0)
        self.assertEqual(agent.utility, 3)
