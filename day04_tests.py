import unittest

import day04


class MyTestCase(unittest.TestCase):
    def test_six_digits(self):
        self.assertTrue(day04.is_six_digits(123456))
        self.assertFalse(day04.is_six_digits(1234))
        self.assertFalse(day04.is_six_digits(12344567))

    def test_in_range(self):
        self.assertTrue(day04.is_in_range(372900, 172851, 675869))
        self.assertFalse(day04.is_in_range(12, 172851, 675869))
        self.assertFalse(day04.is_in_range(1_000_000, 172851, 675869))

    def test_contains_digits(self):
        self.assertTrue(day04.contains_digits(111111))
        self.assertTrue(day04.contains_digits(112211))
        self.assertTrue(day04.contains_digits(221111))
        self.assertTrue(day04.contains_digits(111122))
        self.assertFalse(day04.contains_digits(123456))
        self.assertFalse(day04.contains_digits(654321))

    def test_digits_increase(self):
        self.assertTrue(day04.digits_dont_decrease(111111))
        self.assertTrue(day04.digits_dont_decrease(112234))
        self.assertFalse(day04.digits_dont_decrease(223450))
        self.assertTrue(day04.digits_dont_decrease(123789))
        self.assertTrue(day04.digits_dont_decrease(123788))
        self.assertFalse(day04.digits_dont_decrease(123787))


if __name__ == '__main__':
    unittest.main()
