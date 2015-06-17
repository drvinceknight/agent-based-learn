import unittest
import ablearn

class TestInitialFunction(unittest.TestCase):

    def test_initial_function(self):
        self.assertEqual(ablearn.initial_function(5), 7)
