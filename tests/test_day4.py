import unittest
import day4

class test_day4(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(day4.day4_part1(), 8)
        # self.assertEqual(day4.day4_part2(), 2286)