import unittest
import day8

class test_day8(unittest.TestCase):
    def integration_test(self):
        self.assertEqual(day8.part1(False), 12737)
        self.assertEqual(day8.part2(False), 9064949303801)