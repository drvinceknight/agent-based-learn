import unittest
import ablearn
import random

class SimulationTesting(unittest.TestCase):
    def test_initialisation(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=100, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation()

        self.assertEqual(sim.row_accumulated_strategies, [[], []])
        self.assertEqual(sim.col_accumulated_strategies, [[], []])

        for s in range(len(env.row_agents)):
            self.assertTrue(env.row_agents[s].strategies in env.row_strategies)
            self.assertTrue(env.col_agents[s].strategies in env.col_strategies)

        sim.run()

        self.assertEqual(env.row_agents[48].strategies, 0)
        self.assertEqual(env.col_agents[48].strategies, 1)

    def test_run(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=100, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation()

    def test_generations_passing(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=100, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation()

        env.interact()
        self.assertNotEqual(env.row_agents[-1].utility, 0)
        self.assertNotEqual(env.col_agents[-1].utility, 0)

    def test_proportion_classified_strategies(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=100, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation()

    def test_distributions(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=100, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation()
