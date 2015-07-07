class BiMatrix:
    """
    A class for a bi matrix.
    """
    def __init__(self, bimatrix):
        self.bimatrix = bimatrix

    def play(self, index_1, index_2):
        """Returns the score when given two indices"""
        return self.bimatrix[index_1][index_2]

    def __repr__(self):
        return str(self.bimatrix)
