import unittest
import day7

class test_day7(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(day7.part1(), 6440)
        # self.assertEqual(day7.part2(), 71504)