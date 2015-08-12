import ablearn
from ablearn.population import *
from ablearn.environments import *
from ablearn.algorithms import *

class Simulation:

    def __init__(self):
        ag = ablearn.Agent()
        env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=10, bimatrix=[[[0,1], [2,3]], [[4,5], [5,6]]])
        ga = ablearn.algorithms.genetic.Genetic(generations=1, rounds_per_generation=1, death_rate=0.1, mutation_rate=0.5, exploitation_rate=0.5, initial_strategy_distribution=False)

        self.running = "This class should run the program."
        self.row_history=  [[] for e in range(len(env.row_strategies))]
        self.col_history = [[] for e in range(len(env.col_strategies))]

    def run(self):
        for g in range(ga.generations):
            # In a loop for every generation
            print "\n----------------------"
            print "\nGeneration: %s of %s" % (g + 1, ga.generations)
            for r in range(ga.rounds_per_generation):
                # Loop to repeat tournament for each generation
                print "\tRound: %s of %s" % (r + 1, ga.rounds_per_generation)
                # Reset all utilities before starting a tournament
                for k in range(env.number_of_agents):
                    env.row_agents[k].utility = 0
                    env.col_agents[k].utility = 0
                env.interact()
            # Calculate distributions and update history
            self.row_distribution = return_current_strategy_distribution(env.row_agents, env.row_strategies)
            for k in range(len(env.row_strategies)):
                self.row_history[k].append(self.row_distribution[k])
            self.col_distribution = return_current_strategy_distribution(env.col_agents, env.col_strategies)
            for k in range(len(env.col_strategies)):
                self.col_history[k].append(self.col_distribution[k])
            print "\nRow players strategy distribution:"
            print "\t", self.row_distribution
            print "\nCol players strategy distribution:"
            print "\t", self.col_distribution
            # Kill
            ga.kill_agents(env.row_agents)
            ga.kill_agents(env.col_agents)
            # Reproduce
            ga.reproduce_agents(env.row_agents, env.number_of_row_agents, env.row_strategies)
            ga.reproduce_agents(env.col_agents, env.number_of_col_agents, env.col_strategies)

        ga.assign_strategies(env.row_agents, env.row_strategies)
        ga.assign_strategies(env.row_agents, env.row_strategies)
        env.interact()
