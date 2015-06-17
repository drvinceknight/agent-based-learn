import unittest
import ablearn

class TestPopulationClass(unittest.TestCase):

    def test_that_initialises_correctly(self):
        p = ablearn.Population()
        self.assertEqual(p.n, 500)

    def test_that_increase_population_works(self):
        p = ablearn.Population()
        p.increase_population(10)
        self.assertEqual(p.n, 510)
