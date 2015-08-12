import unittest
import ablearn
import random

class EnvironemntTesting(unittest.TestCase):
    def test_initialisation(self):
        bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
        env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=bimatrix)
        self.assertRaises(AttributeError, lambda: len(env.agents))
        self.assertEqual(env.number_of_row_agents, 10)
        self.assertEqual(env.number_of_col_agents, 10)
        self.assertEqual(set([agent.__class__.__name__ for agent in
            env.row_agents]), set(['Agent']))
        self.assertEqual(set([agent.__class__.__name__ for agent in
            env.col_agents]), set(['Agent']))

    def test_strategies_to_utilities(self):
        bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
        env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=bimatrix)
        test_strategies = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        for strat in test_strategies:
            self.assertEqual(env.strategies_to_utilities(strat),
                    bimatrix[strat[0]][strat[1]])

    def test_randomly_pair_agents(self):
        bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
        env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=bimatrix)
        pairs = env.randomly_pair_agents()
        self.assertEqual(len(pairs), env.number_of_agents / 2)
        self.assertTrue(all([set([pair[0]]) < set(env.row_agents) and
                        set([pair[1]]) < set(env.col_agents) for pair in pairs]))
        self.assertEqual(set([pair[0] for pair in pairs]), set(env.row_agents))
        self.assertEqual(set([pair[1] for pair in pairs]), set(env.col_agents))

    def test_interact(self):
        bimatrix =[[[1, 2], [4, 5]], [[5, 1], [6, 1]], [[5, 1], [8, 2]]]
        env = ablearn.environments.BiMatrixRandomEnv(number_of_agents=20,
                bimatrix=bimatrix)

        for ra, ca in zip(env.row_agents, env.col_agents):
            ra.strategies = random.choice(env.row_strategies)
            ca.strategies = random.choice(env.col_strategies)
            self.assertEqual(ra.utility, 0)
            self.assertEqual(ca.utility, 0)

        env.interact()

        for ra, ca in zip(env.row_agents, env.col_agents):
            self.assertEqual(ra.utility, bimatrix[ra.strategies][ca.strategies][0])
            self.assertEqual(ca.utility, bimatrix[ra.strategies][ca.strategies][1])
