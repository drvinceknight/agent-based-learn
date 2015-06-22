from ablearn.Abm import ABM 
import unittest

class RulesTesting(unittest.TestCase):
	def setUp(self):
		self.ABM = ABM('number_of_agents', 'generations', 'rounds_per_generation', 'death_rate', 'number_of_deaths_per_generation', 'mutation_rate', 'row_strategies', 'col_strategies')

	def test_number_of_agents_is_a_number(self):
		self.assertRaises(ValueError, self.ABM.number_of_agents, 'two')
	def test_number_of_agents_is_integer(self):
		self.assertRaises(ValueError, self.ABM.number_of_agents, 5.1)

	def test_number_of_generations_is_a_number(self):
		self.assertRaises(ValueError, self.abm.generations, 'six')
	def test_number_of_generations_is_integer(self):
		self.assertRaises(ValueError, self.abm.generations, 3.3)

	def test_rounds_per_generation_is_a_number(self):
		self.assertRaises(ValueError, self.abm.rounds_per_generation, 'twelve')
	def test_rounds_per_generation_is_integer(self):
		self.assertRaises(ValueError, self.abm.rounds_per_generation, 1.4)

	def test_death_rate_is_a_number(self):
		self.assertRaises(ValueError, self.abm.death_rate, 'ten')

	def test_number_of_deaths_per_generation_is_a_number(self):
		self.assertRaises(ValueError, self.abm.number_of_deaths_per_generation, 'five')
	def test_number_of_deaths_per_generation_is_integer(self):
		self.assertRaises(ValueError, self.abm.number_of_deaths_per_generation, 0.7)
		
	def test_mutation_rate_is_a_number(self):
		self.assertRaises(ValueError, self.abm.mutation_rate, 'Eight')
	
	def test_row_strategies_is_a_number(self):
		self.assertRaises(ValueError, self.abm.row_strategies, '')

	def test_col_strategies_is_a_number(self):
		self.assertRaises(ValueError, self.abm.col_strategies, '')
