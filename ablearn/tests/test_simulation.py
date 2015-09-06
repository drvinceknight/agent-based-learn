import unittest
import ablearn
import random

class SimulationTesting(unittest.TestCase):
    def test_initialisation_initial_parameters_and_assigning_initial_strategies(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=50, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=2, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation(tog='mp', na=50, ge=2, rpg=5, dr=0.5, mr=0.1, er=0.1)

        self.assertEqual(sim.tog, 'mp')
        self.assertEqual(sim.na, 50)
        self.assertEqual(sim.ge, 2)
        self.assertEqual(sim.rpg, 5)
        self.assertEqual(sim.dr, 0.5)
        self.assertEqual(sim.mr, 0.1)
        self.assertEqual(sim.er, 0.1)
        self.assertEqual(sim.row_accumulated_strategies, [[], []])
        self.assertEqual(sim.col_accumulated_strategies, [[], []])
        self.assertTrue(sim.strategies_history)

        for s in range(len(env.row_agents)):
            self.assertTrue(env.row_agents[s].strategies in env.row_strategies)
            self.assertTrue(env.col_agents[s].strategies in env.col_strategies)

        #self.assertEqual(env.row_agents[4].strategies, 1)
        #self.assertEqual(env.col_agents[1].strategies, 1)

        sim.run()

        self.assertNotEqual(env.row_agents[0].strategies, False)
        self.assertNotEqual(env.col_agents[0].strategies, False)


    def test_generations_passing_assert_possible_values_for_utilities_in_types_of_agents(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=2, rounds_per_generation=5, death_rate=0.3, mutation_rate=0.5, exploitation_rate=0.9, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation(tog='2', na=50, ge=2, rpg=5, dr=0.5, mr=0.1, er=0.1)

        ga.assign_strategies(env.row_agents, env.row_strategies)
        ga.assign_strategies(env.col_agents, env.col_strategies)


        sim.generations_passing(ga.generations, ga.rounds_per_generation, env.number_of_agents, env.row_agents, env.col_agents, plot=False, stack=False)
        env.interact()
        a = [env.row_agents[i].utility for i in range(len(env.row_agents))]
        b = [env.col_agents[i].utility for i in range(len(env.col_agents))]

        self.assertIn(1, a)
        self.assertIn(-1, a)
        self.assertIn(1, b)
        self.assertIn(-1, b)

    def test_proportion_classified_strategies_for_creating_lists_of_accumulated_strategies(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[3,3], [0,5]], [[5,0], [1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=2, rounds_per_generation=1, death_rate=0.1, mutation_rate=0.1, exploitation_rate=0.9, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation(tog='mp', na=100, ge=2, rpg=5, dr=0.5, mr=0.1, er=0.1)

        self.assertEqual(sim.row_accumulated_strategies, [[], []])
        self.assertEqual(sim.col_accumulated_strategies, [[], []])

        random.seed(1)
        ga.assign_strategies(env.row_agents, env.row_strategies)
        ga.assign_strategies(env.col_agents, env.col_strategies)
        sim.generations_passing(2, 2, 100, env.row_agents, env.col_agents, plot=False, stack=False)

        self.assertNotEqual(sim.row_accumulated_strategies, [[], []])
        self.assertNotEqual(sim.col_accumulated_strategies, [[], []])

    def test_total_classified_strategies_values_for_stackplot(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[3,3], [0,5]], [[5,0], [1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=2, rounds_per_generation=1, death_rate=0.1, mutation_rate=0.1, exploitation_rate=0.9, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation(tog='mp', na=100, ge=2, rpg=5, dr=0.5, mr=0.1, er=0.1)

        self.assertEqual(sim.strategies_history, [[], []])

        random.seed(1)
        ga.assign_strategies(env.row_agents, env.row_strategies)
        ga.assign_strategies(env.col_agents, env.col_strategies)
        sim.generations_passing(2, 2, 100, env.row_agents, env.col_agents, plot=False, stack=False)

        self.assertNotEqual(sim.strategies_history, [[], []])
        self.assertEqual(sim.strategies_history[0][0]+sim.strategies_history[1][0], 100)
        self.assertEqual(sim.strategies_history[0][1]+sim.strategies_history[1][1], 100)

    def test_distributions_not_empty_lists(self):
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=2, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        sim = ablearn.simulation.simulation.Simulation(tog='2', na=50, ge=2, rpg=5, dr=0.5, mr=0.1, er=0.1)

        sim.run()
        ga.assign_strategies(env.row_agents, env.row_strategies)
        ga.assign_strategies(env.col_agents, env.col_strategies)
        env.interact()

        sim.distributions(env.number_of_agents, env.row_agents, env.col_agents, env.row_strategies, env.col_strategies, plot=False)

        self.assertNotEqual(sim.row_strategies_distribution, [[], []])
        self.assertNotEqual(sim.col_strategies_distribution, [[], []])
