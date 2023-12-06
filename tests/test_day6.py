import unittest
import day6

class test_day5(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(day6.part1(), 35)