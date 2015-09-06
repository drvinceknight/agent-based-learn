class Agent:
    """
    A generic class for agents that will be used by the library
    """

    """ INITIALIZATION """
    def __init__(self, strategies=False, label=False): # The properties each agent will have.
        self.strategies = strategies # Strategy the agent will use.
        self.utility = 0 # Utility the agent will obtain.
        self.label = label # If required a label to track a specific agent.

    def increment_utility(self, amount=1): # How much their utility will increase
        self.utility += float(amount) # Utility for each agent will increase in this amount.
