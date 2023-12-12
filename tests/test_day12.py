import unittest
from day12 import *

class test_day12(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(part1(), 21)
        self.assertEqual(part2(), 525152)