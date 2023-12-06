import unittest
import day6

class test_day6(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(day6.part1(), 288)
        self.assertEqual(day6.part2(), 71504)