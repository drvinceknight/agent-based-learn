class Agent:
    """
    A generic class for agents that will be used by the library
    """
    def __init__(self, strategies, label=False):
        self.strategies = strategies
        self.utility = 0
        self.label = label

    def increment_utility(self, amount=1):
        self.utility += amount

		
