import unittest
import day5

class test_day5(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(day5.part1(), None)
        self.assertEqual(day5.part2(), None)