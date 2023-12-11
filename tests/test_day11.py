import unittest
from day11 import *

class test_day11(unittest.TestCase):
    def test_taxi_cab_distance(self):
        self.assertEqual(taxi_cab_distance((6, 1), (11, 5)), 9)
        self.assertEqual(taxi_cab_distance((0, 4), (10, 9)), 17)
        self.assertEqual(taxi_cab_distance((11, 5), (11, 0)), 5)

    def test_integration(self):
        self.assertEqual(part1(), 374)
        self.assertEqual(part2(10), 1030)
        self.assertEqual(part2(100), 8410)