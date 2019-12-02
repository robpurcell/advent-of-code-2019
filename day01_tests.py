import unittest

import day01


class Day01TestCase(unittest.TestCase):
    def test_fuel_calculation(self):
        self.assertEqual(2, day01.calc_fuel(12))
        self.assertEqual(2, day01.calc_fuel(14))
        self.assertEqual(654, day01.calc_fuel(1969))
        self.assertEqual(33583, day01.calc_fuel(100756))

    def test_fuel_for_fuel_calculation(self):
        self.assertEqual(2, day01.calc_fuel_fuel(14))
        self.assertEqual(966, day01.calc_fuel_fuel(day01.calc_fuel(1969)) + day01.calc_fuel(1969))
        self.assertEqual(50346, day01.calc_fuel_fuel(day01.calc_fuel(100756)) + day01.calc_fuel(100756))


if __name__ == '__main__':
    unittest.main()
