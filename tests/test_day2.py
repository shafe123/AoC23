import unittest
import day2

class test_day1(unittest.TestCase):
    def test_split_pulls(self):
        results = {
            "3 blue, 4 red": {'blue': 3, 'red': 4},
            "2 green": {'green': 2}
        }
        
        for line, result in results.items():
            self.assertEqual(day2.split_pulls(line), result)

    def test_can_play(self):
        results = [
            ({'blue': 3, 'red': 4}, True),
            ({'green': 20}, False)
        ]
        
        for pull, result in results:
            self.assertEqual(day2.can_play(pull), result)

    def test_power_set(self):
        results = [
            ({'blue': 3, 'red': 4}, 12)
        ]

        for pull, result in results:
            self.assertEqual(day2.power_set(pull), result)

    def test_integration(self):
        self.assertEqual(day2.day2_part1(), 8)
        self.assertEqual(day2.day2_part2(), 2286)