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
        self.assertEqual(expected, day02.process(input_program)[0])

    def test_jump_if_true_immediate(self):
        self.assertEqual(3, day02.jump_if_true([], [1105, 0, 10], 0))
        self.assertEqual(10, day02.jump_if_true([], [1105, 1, 10], 33))

    def test_jump_if_false_immediate(self):
        self.assertEqual(3, day02.jump_if_false([], [1105, 1, 10], 0))
        self.assertEqual(10, day02.jump_if_false([], [1105, 0, 10], 33))

    def test_jump_position_mode(self):
        input_program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(0, day02.process(input_program, 0, 0)[1][0])

        input_program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(1, day02.process(input_program, 0, 100)[1][0])

    def test_jump_immediate_mode(self):
        input_program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(0, day02.process(input_program, 0, 0)[1][0])

        input_program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(1, day02.process(input_program, 0, 100)[1][0])

    def test_jump_bigger_program(self):
        input_program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                         1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                         999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

        self.assertEqual(999, day02.process(input_program, input_id=5)[1][0])

    def test_equals_position_mode(self):
        input_program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(1, day02.process(input_program, input_id=8)[1][0])

        input_program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(0, day02.process(input_program, input_id=5)[1][0])

    def test_equals_immediate_mode(self):
        input_program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(1, day02.process(input_program, input_id=8)[1][0])

        input_program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(0, day02.process(input_program, input_id=5)[1][0])

    def test_equals_position_mode(self):
        input_program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(1, day02.process(input_program, input_id=8)[1][0])

        input_program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(0, day02.process(input_program, input_id=5)[1][0])

    def test_less_than_position_mode(self):
        input_program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(1, day02.process(input_program, input_id=5)[1][0])

        input_program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(0, day02.process(input_program, input_id=90)[1][0])

    def test_less_than_immediate_mode(self):
        input_program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(1, day02.process(input_program, input_id=5)[1][0])

        input_program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(0, day02.process(input_program, input_id=90)[1][0])


if __name__ == '__main__':
    unittest.main()
