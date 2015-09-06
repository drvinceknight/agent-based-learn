from __future__ import division # include __future__ module in this case so a specific division can give decimal points.
import random
import ablearn
import matplotlib.pyplot as pl
import matplotlib.cm as cm
from collections import defaultdict
from matplotlib.patches import Rectangle

#import axelrod.matrix as axl

class Simulation:

    def __init__(self,tog, na, ge, rpg, dr, mr, er, isd=False):
        global env, ga, plt
        self.tog = tog
        self.na = na
        self.ge = ge
        self.rpg = rpg
        self.dr = dr
        self.mr = mr
        self.er = er
        self.isd = isd
        ag = ablearn.Agent()
        if self.tog=='pd': # prisoners' dilemma
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                bimatrix=[[[3, 3], [0, 5]],
                                          [[5, 0], [1, 1]]])
        elif self.tog =='psr': # paper-scissors-rock
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                bimatrix=[[[0, 0], [-1, 1], [1,-1]],
                                            [[1,-1], [0, 0], [-1, 1]],
                                            [[-1, 1], [1, -1], [0,0]]])
        elif self.tog=='mp': # matching pennies
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                bimatrix=[[[1,-1], [-1,1]],
                                        [[-1,1], [1,-1]]])
        elif self.tog=='bos': # battle of sexes
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                 bimatrix=[[[2, 1], [0, 0]],
                                            [[0, 0], [1, 2]]])
        elif self.tog=='hd': # chicken/hawk and dove
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                 bimatrix=[[[0, 0], [3, 1]],
                                            [[1, 3], [2, 2]]])
        elif self.tog=='sh': # stag hunt
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                 bimatrix=[[[5, 5], [0, 1]],
                                            [[1, 0], [1, 1]]])
        elif self.tog=='cs': # choosing sides
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                 bimatrix=[[[1, 1], [0, 0]],
                                            [[0, 0], [1, 1]]])
        elif self.tog=='axl':
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                bimatrix=[[[3.0, 3.0], [1.7414999999999998, 1.759], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.3924999999999998, 1.4175], [1.2814999999999999, 1.3065000000000002], [1.6260000000000001, 1.6485000000000003]],
                                         [[1.759, 1.7414999999999998], [1.7752499999999998, 1.7752499999999998], [1.1430000000000002, 1.9754999999999998], [0.7505, 2.1430000000000002], [0.881, 2.1485], [1.549, 1.8615], [1.6625, 1.7774999999999999], [1.592, 1.8495000000000001]],
                                         [[3.0, 3.0], [1.9754999999999998, 1.1430000000000002], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.3380000000000003, 1.3380000000000003], [1.0790000000000002, 1.0864999999999998], [1.348, 1.3029999999999997]],
                                         [[3.0, 3.0], [2.1430000000000002, 0.7505], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.2479999999999998, 1.2479999999999998], [1.083, 1.0855000000000001], [1.293, 1.2005000000000003]],
                                         [[3.0, 3.0], [2.1485, 0.881], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.236, 1.2385], [1.1045, 1.1195000000000002], [1.32, 1.23]],
                                         [[1.4175, 1.3924999999999998], [1.8615, 1.549], [1.3380000000000003, 1.3380000000000003], [1.2479999999999998, 1.2479999999999998], [1.2385, 1.236], [1.31575, 1.31575], [1.1590000000000003, 1.1715], [1.3755000000000002, 1.3604999999999998]],
                                         [[1.3065000000000002, 1.2814999999999999], [1.7774999999999999, 1.6625], [1.0864999999999998, 1.0790000000000002], [1.0855000000000001, 1.083], [1.1195000000000002, 1.1045], [1.1715, 1.1590000000000003], [1.115, 1.115], [1.4449999999999998, 1.3800000000000003]],
                                         [[1.6485000000000003, 1.6260000000000001], [1.8495000000000001, 1.592], [1.3029999999999997, 1.348], [1.2005000000000003, 1.293], [1.23, 1.32], [1.3604999999999998, 1.3755000000000002], [1.3800000000000003, 1.4449999999999998], [1.4842500000000003, 1.4842500000000003]]])

        elif self.tog=='axlrand':
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                bimatrix=[[[3.0, 3.0], [1.725, 1.7474999999999998], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.3875000000000002, 1.4125], [1.1880000000000002, 1.2129999999999999], [1.5879999999999999, 1.613], [2.25, 2.255]],
                                         [[1.7474999999999998, 1.725], [1.76175, 1.76175], [1.158, 1.943], [0.7610000000000001, 2.101], [0.8779999999999999, 2.1355], [1.5525, 1.9075], [1.6360000000000003,1.7385000000000002], [1.5599999999999998, 1.8125], [2.5725000000000002, 1.535]],
                                         [[3.0, 3.0], [1.943, 1.158], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.342, 1.342], [1.1090000000000002, 1.1115], [1.3794999999999997, 1.3344999999999998], [2.7405, 1.098]],
                                         [[3.0, 3.0], [2.101, 0.7610000000000001], [3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.262, 1.2645], [1.067, 1.0695000000000001], [1.3249999999999997, 1.2175], [2.9989999999999997, 0.5315]],
                                         [[3.0, 3.0], [2.1355, 0.8779999999999999],[3.0, 3.0], [3.0, 3.0], [3.0, 3.0], [1.265, 1.2674999999999996], [1.1565, 1.1590000000000003], [1.314, 1.214], [2.9515000000000002, 0.6739999999999999]],
                                         [[1.4125, 1.3875000000000002], [1.9075, 1.5525], [1.342, 1.342], [1.2645, 1.262], [1.2674999999999996, 1.265], [1.315, 1.315], [1.1465, 1.159], [1.412, 1.3844999999999998], [2.4229999999999996, 1.8105]],
                                         [[1.2129999999999999, 1.1880000000000002], [1.7385000000000002, 1.6360000000000003], [1.1115, 1.1090000000000002], [1.0695000000000001, 1.067], [1.1590000000000003, 1.1565], [1.159, 1.1465], [1.0975, 1.0975], [1.3234999999999997, 1.2710000000000001], [2.2885, 2.0185000000000004]],
                                         [[1.613, 1.5879999999999999], [1.8125, 1.5599999999999998], [1.3344999999999998, 1.3794999999999997], [1.2175, 1.3249999999999997], [1.214, 1.314], [1.3844999999999998, 1.412], [1.2710000000000001, 1.3234999999999997], [1.5002499999999999, 1.5002499999999999], [2.3489999999999998, 2.069]],
                                         [[2.255, 2.25], [1.535, 2.5725000000000002], [1.098, 2.7405], [0.5315, 2.9989999999999997], [0.6739999999999999, 2.9515000000000002], [1.8105, 2.4229999999999996], [2.0185000000000004, 2.2885], [2.069, 2.3489999999999998], [2.2485, 2.2485]]])

        elif self.tog=='axlbasic':
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na,
                                bimatrix=[[[2.0, 2.0], [4.0, 1.5], [0.5, 3.0], [2.3020000000000005, 2.217], [2.515, 2.4900000000000007]],
                                        [[1.5, 4.0], [3.0, 3.0], [0.0, 5.0], [1.4955, 4.002999999999999], [3.0, 3.0]],
                                        [[3.0, 0.5], [5.0, 0.0], [1.0, 1.0], [3.07, 0.48250000000000004], [1.0199999999999998, 0.9949999999999999]],
                                        [[2.217, 2.3020000000000005], [4.002999999999999, 1.4955], [0.48250000000000004, 3.07], [2.2459999999999996, 2.2459999999999996], [2.275, 2.2649999999999997]],
                                        [[2.4900000000000007, 2.515], [3.0, 3.0], [0.9949999999999999, 1.0199999999999998], [2.2649999999999997, 2.275], [3.0, 3.0]]])

        else:
            env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(
                                number_of_agents=self.na, bimatrix=[[[1,1], [1,1]],
                                                                    [[1,1], [1,1]]])

        ga = ablearn.algorithms.genetic.Genetic(generations=self.ge, rounds_per_generation=self.rpg,
                            death_rate=self.dr, mutation_rate=self.mr, exploitation_rate=self.er)
        if self.isd == False:
            ga.assign_strategies(env.row_agents, env.row_strategies)
            ga.assign_strategies(env.col_agents, env.col_strategies)
        else:
            ga.assign_strategies_initial_distribution(env.row_agents, env.row_strategies, env.number_of_agents, self.isd)
            ga.assign_strategies_initial_distribution(env.col_agents, env.col_strategies, env.number_of_agents, self.isd)

        self.row_accumulated_strategies = [[] for r in range(len(env.row_strategies))]
        self.col_accumulated_strategies = [[] for c in range(len(env.col_strategies))]

        if len(env.row_strategies) == len(env.col_strategies):
            self.strategies_history = [[] for r in range(len(env.row_strategies))]
        else:
            longer = max(env.row_strategies, env.col_strategies)
            self.strategies_history = [[] for r in range(len(longer))]


    def run(self, plot=False, stack=False):
        if plot==True:
            pl.ion()
            pl.ylim(0, 1)
            pl.xlabel("Generations")
            pl.ylabel("Probability")
            for k in range(len(env.row_strategies)):
                c = cm.copper((k + 1) / len(env.row_strategies))
                pl.plot(self.row_accumulated_strategies[k], color=c, label="Row strategies: %s" % (k + 1))
            for k in range(len(env.col_strategies)):
                c = cm.winter((k + 1) / len(env.row_strategies))
                pl.plot(self.col_accumulated_strategies[k], color=c, label="Col strategies: %s" % (k + 1))
            #pl.legend(bbox_to_anchor=(0.7, 0.85), loc=2, prop={'size':7})
            pl.legend(loc=2, prop={'size':7})
            pl.draw()

        self.generations_passing(ga.generations, ga.rounds_per_generation, env.number_of_agents, env.row_agents, env.col_agents, plot, stack)

    def generations_passing(self, generations, rounds_per_generation, number_of_agents, row_agents, col_agents, plot, stack):
        for g in range(generations):
            print "\nGeneration %i of %i" % (g + 1, generations)
            for a in range(int(number_of_agents / 2)):
                row_agents[a].utility = 0
                col_agents[a].utility = 0
            for r in range(rounds_per_generation):
        #        print "\tRound %i of %i" % (r + 1, rounds)
                env.interact()
            self.distributions(env.number_of_agents, row_agents, col_agents, env.row_strategies, env.col_strategies, plot)

        if stack==True:
            b = range(len(self.strategies_history))
            for k in range(len(self.strategies_history)):
                b[k] = 'Strategy %r' % (k + 1)

            print self.strategies_history
            print b

            fig, ax = pl.subplots()
            stack_coll = ax.stackplot(range(1, generations + 1), self.strategies_history[0:], label=str(b[0:]))
            proxy_rects = [Rectangle((0, 0), 1, 1, fc=pc.get_facecolor()[0]) for pc in stack_coll]
            ax.set_xlabel('Generations')
            ax.set_xlim(1, generations)
            ax.set_ylabel('Agents')
            ax.set_title('Stackplot')
            ax.legend(proxy_rects, b)
            pl.show()

        if plot==True:
            pl.show(block=True)

    def proportion_classified_strategies(self, agents, strategies):
        frequency_per_strategy_per_agent = []
        for s in strategies:
            frequency_per_strategy_per_agent.append(0)
            for a in agents:
                if a.strategies == s:
                    frequency_per_strategy_per_agent[-1] += 1
        return [f / len(agents) for f in frequency_per_strategy_per_agent]

    def total_classified_strategies(self, row_agents, row_strategies, col_agents, col_strategies):
        frequency_per_strategy_for_sum = []

        if row_strategies >= col_strategies:
            for rs in row_strategies:
                frequency_per_strategy_for_sum.append(0)
                for ra in row_agents:
                    if ra.strategies == rs:
                        frequency_per_strategy_for_sum[rs] += 1
            for cs in col_strategies:
                for ca in col_agents:sss
                    if ca.strategies == cs:
                        frequency_per_strategy_for_sum[cs] += 1
        else:
            for cs in col_strategies:
                frequency_per_strategy_for_sum.append(0)
                for ca in col_agents:
                    if ca.strategies == cs:
                        frequency_per_strategy_for_sum[cs] += 1
            for rs in row_strategies:
                for ra in row_agents:
                    if ra.strategies == rs:
                        frequency_per_strategy_for_sum[rs] += 1

        return [f for f in frequency_per_strategy_for_sum]

    def distributions(self, number_of_agents, row_agents, col_agents, row_strategies, col_strategies,plot):
        self.row_strategies_distribution = self.proportion_classified_strategies(row_agents, row_strategies)
        for rs in range(len(row_strategies)):
             self.row_accumulated_strategies[rs].append(self.row_strategies_distribution[rs])
        self.col_strategies_distribution = self.proportion_classified_strategies(col_agents, col_strategies)
        for cs in range(len(col_strategies)):
             self.col_accumulated_strategies[cs].append(self.col_strategies_distribution[cs])

        self.total_strategies_per_generation = self.total_classified_strategies(row_agents, row_strategies, col_agents, col_strategies)
        for sh in range(len(self.strategies_history)):
            self.strategies_history[sh].append(self.total_strategies_per_generation[sh])

        print "\n Row players' strategy distribution:"
        print "\t", self.row_strategies_distribution
        print "\n Column players' strategy distribution:"
        print "\t", self.col_strategies_distribution

        ga.kill_agents(env.row_agents, env.number_of_agents, env.number_of_row_agents, env.row_strategies)
        ga.kill_agents(env.col_agents, env.number_of_agents, env.number_of_col_agents, env.col_strategies)
        print "Row agents eliminated", (number_of_agents / 2) - len(env.col_agents)
        print "Col agents eliminated", (number_of_agents / 2) - len(env.row_agents)
        ga.reproduce_agents(env.row_agents, env.number_of_agents, env.number_of_row_agents, env.row_strategies)
        ga.reproduce_agents(env.col_agents, env.number_of_agents, env.number_of_col_agents, env.col_strategies)

        if plot==True:
            for k in range(len(env.row_strategies)):
                c = cm.copper((k + 1) / len(env.row_strategies))
                pl.plot(self.row_accumulated_strategies[k], color=c, label="Row strategies: %s" % (k + 1))
            for k in range(len(env.col_strategies)):
                c = cm.winter((k + 1) / len(env.row_strategies))
                pl.plot(self.col_accumulated_strategies[k], color=c, label="Col strategies: %s" % (k + 1))
            pl.draw()
