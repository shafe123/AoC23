import unittest
from day9 import *

class test_day9(unittest.TestCase):
    def integration_test(self):
        self.assertEqual(part1(), 114)
        self.assertEqual(part1(), 2)