import unittest
import day1

class test_day1(unittest.TestCase):
    def test_replace_digits(self):
        results = {"two1nine": "219",
             "eightwothree": "823",
             "abcone2threexyz": "123",
             "xtwone3four": "2134",
             "4nineeightseven2": "49872",
             "zoneight234": "18234",
             "7pqrstsixteen": "76"}
        
        for line, result in results.items():
            self.assertEqual(day1.replace_digits(line), result)

    def test_calculate_line(self):
        results = {"219": 29,
                   "823": 83,
                   "123": 13,
                   "49872": 42}
        
        for line, result in results.items():
            self.assertEqual(day1.calculate_line(line), result)

    def test_integration(self):
        self.assertEqual(day1.day1_part2(), 281)