import unittest

import day02


class MyTestCase(unittest.TestCase):
    def test_opdcode_determined_correctly(self):
        instruction = 1002
        opcode = day02.get_opcode(instruction)
        self.assertEqual(2, opcode)

    def test_get_modes(self):
        instruction = 1002
        expected = 0, 1, 0
        self.assertEqual(expected, day02.get_parameter_modes(instruction))

    def test_add_mode(self):
        input_program = [1101, 100, -1, 4, 0]

        expected = [1101, 100, -1, 4, 99]
        self.assertEqual(expected, day02.process(input_program))


if __name__ == '__main__':
    unittest.main()
