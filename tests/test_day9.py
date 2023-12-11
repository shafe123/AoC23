import unittest
from day9 import *

class test_day9(unittest.TestCase):
    def test_integration(self):
        self.assertEqual(part1(), 114)