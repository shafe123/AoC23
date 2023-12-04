import unittest
import day4

class test_day4(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(day4.day4_part1(), 13)
        self.assertEqual(day4.day4_part2(), 30)