import unittest

import day02


class Day02TestCase(unittest.TestCase):

    def test_program_1(self):
        input_data = [1, 0, 0, 0, 99]
        expected = [2, 0, 0, 0, 99]
        self.assertListEqual(expected, day02.process(input_data))

    def test_program_2(self):
        input_data = [2, 3, 0, 3, 99]
        expected = [2, 3, 0, 6, 99]
        self.assertListEqual(expected, day02.process(input_data))

    def test_program_3(self):
        input_data = [2, 4, 4, 5, 99, 0]
        expected = [2, 4, 4, 5, 99, 9801]
        self.assertListEqual(expected, day02.process(input_data))

    def test_program_4(self):
        input_data = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertListEqual(expected, day02.process(input_data))


if __name__ == '__main__':
    unittest.main()
