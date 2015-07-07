import unittest
import ablearn

class BiMatrixTesting(unittest.TestCase):
    def test_initialisation(self):
        BiMatrix = [[[1, 3], [3, 2]], [[5, 2], [3, 2]]]
        rules = ablearn.rules.BiMatrix(BiMatrix)
        self.assertEqual(rules.bimatrix, BiMatrix)

    def test_play(self):
        BiMatrix = [[[1, 3], [3, 2]], [[5, 2], [3, -6]]]
        rules = ablearn.rules.BiMatrix(BiMatrix)
        self.assertEqual(rules.play(0, 1), [3, 2])
        self.assertEqual(rules.play(0, 0), [1, 3])
        self.assertEqual(rules.play(1, 0), [5, 2])
        self.assertEqual(rules.play(1, 1), [3, -6])

    def test_repr(self):
        BiMatrix = [[[1, 3], [3, 2]], [[5, 2], [3, 2]]]
        rules = ablearn.rules.BiMatrix(BiMatrix)
        self.assertEqual(str(rules), str(BiMatrix))
