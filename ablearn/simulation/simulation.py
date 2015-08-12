import random
import ablearn

#ag = ablearn.Agent()
#env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=10, bimatrix=[[[0,1], [2,3]], [[4,5], [5,6]]])
#ga = ablearn.algorithms.genetic.Genetic(generations=1, rounds_per_generation=1, death_rate=0.1, mutation_rate=0.5, exploitation_rate=0.5, initial_strategy_distribution=False)


class Simulation:

    def __init__(self):
        self.running = "This class should run the program."
        global env, ga
        ag = ablearn.Agent()
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=100, bimatrix=[[[-1,1], [1,-1]], [[1,-1], [-1,1]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=100, rounds_per_generation=5, death_rate=0.5, mutation_rate=0.1, exploitation_rate=0.1, initial_strategy_distribution=False)
        ga.assign_strategies(env.row_agents, env.row_strategies)
        ga.assign_strategies(env.col_agents, env.col_strategies)
        self.row_accumulated_strategies = [[] for r in range(len(env.row_strategies))]
        self.col_accumulated_strategies = [[] for c in range(len(env.col_strategies))]

    def run(self):
        print env.row_agents[0].strategies
        print env.row_agents[1].strategies
        print env.row_agents[2].strategies
        print env.row_agents[3].strategies
        print env.row_agents[4].strategies
        print env.col_agents[0].strategies
        print env.col_agents[1].strategies
        print env.col_agents[2].strategies
        print env.col_agents[3].strategies
        print env.col_agents[4].strategies
        self.generations_passing(ga.generations, ga.rounds_per_generation, env.number_of_agents, env.row_agents, env.col_agents)

    def generations_passing(self, generations, rounds, number_of_agents, row_agents, col_agents):
        pass
    def proportion_classified_strategies(self, agents, strategies):
        pass
    def distributions(self, number_of_agents, row_agents, col_agents, row_strategies, col_strategies):
        pass
