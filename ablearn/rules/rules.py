class BiMatrix:
    def __init__(self, bimatrix):
        self.bimatrix = bimatrix
	
    
	def play(self, index_1, index_2):
		return self.bimatrix[index_1][index_2]
		#play_row = self.row_strategies[self.row_agents[i].strategies][self.col_agents[i].strategies]
		#play_col = self.col_strategies[self.row_agents[i].strategies][self.col_agents[i].strategies]


	def __repr__(self):
		return str(self.bimatrix)
