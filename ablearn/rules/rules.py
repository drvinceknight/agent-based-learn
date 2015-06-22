class BiMatrix:
    def __init__(self, bimatrix):
        self.bimatrix = bimatrix

    def play(self, index_1, index_2):
        return self.bimatrix[index_1][index_2]

    def __repr__(self):
        return str(self.bimatrix)
