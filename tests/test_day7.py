import unittest
import day7

class test_day7(unittest.TestCase):
    def check_typing(self):
        results = {'JJJJJ': day7.CamelHand.Types.Five}

        for key, result in results:
            hand = day7.CamelHand(key)
            self.assertEqual(hand.type, result)

    def test_integration(self):
        self.assertEqual(day7.part1(), 5905)