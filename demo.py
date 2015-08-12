import ablearn
ga = ablearn.algorithms.genetic.Genetic(generations=10, rounds_per_generation=1, death_rate=0.8, mutation_rate=0.5, exploitation_rate=1, initial_strategy_distribution=False)
ag = ablearn.Agent()
#env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=200, bimatrix=[[[3,3], [0,5]], [[5,0], [1,1]]])
env = ablearn.environments.bimatrix_random_environment.BiMatrixRandomEnv(number_of_agents=200, bimatrix=[[[1,-1], [-1,1]], [[-1,1], [1,-1]]])
sim = ablearn.simulation.simulation.Simulation()
sim.run()
