# -*- coding: utf-8 -*-

import unittest
from .context import fizzbuzz

class FizzBuzzTestSuite(unittest.TestCase):

    def test_it_returns_Fizz_for_input_value_3(self):
        self.assertEqual(fizzbuzz.percolate(3), 'Fizz')

    def test_it_returns_Fizz_for_input_value_12(self):
        self.assertEqual(fizzbuzz.percolate(12), 'Fizz')

    def test_it_returns_Buzz_for_input_value_5(self):
        self.assertEqual(fizzbuzz.percolate(5), 'Buzz')

    def test_it_returns_Buzz_for_input_value_85(self):
        self.assertEqual(fizzbuzz.percolate(85), 'Buzz')

    def test_it_returns_FizzBuzz_for_input_value_15(self):
        self.assertEqual(fizzbuzz.percolate(15), 'FizzBuzz')

    def test_it_returns_FizzBuzz_for_input_value_75(self):
        self.assertEqual(fizzbuzz.percolate(75), 'FizzBuzz')

    def test_it_returns_4_for_input_value_4(self):
        self.assertEqual(fizzbuzz.percolate(4), '4')

    def test_it_processes_the_numbers_1_through_100(self):
        self.assertEqual(fizzbuzz.process(range(1,17)), 
        "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n")

if __name__ == '__main__':
    unittest.main()