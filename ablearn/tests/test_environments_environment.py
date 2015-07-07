import unittest
import ablearn

class EnvironemntTesting(unittest.TestCase):
    def test_initialisation(self):
        env = ablearn.environments.Environment(number_of_agents=20)
        self.assertEqual(len(env.agents), 20)
        self.assertEqual(env.number_of_agents, 20)
        self.assertEqual(set([agent.__class__.__name__ for agent in
            env.agents]), set(['Agent']))
