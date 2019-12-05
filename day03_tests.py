import unittest

import day03


class MyTestCase(unittest.TestCase):
    def test_manhattan_distance(self):
        p = (0, 0)
        q = (3, 3)
        self.assertEqual(6, day03.manhattan_distance(p, q))

    def test_add_vectors(self):
        p = (0, 0)
        q = (3, 3)
        self.assertEqual((3, 3), day03.add_vectors(p, q))

    def test_move_right(self):
        p = (0, 0)
        self.assertListEqual([((1, 0), None, 1), ((2, 0), None, 2)], day03.move(p, 2, (1, 0)))

    def test_trace_wire(self):
        p = (0, 0)
        self.assertListEqual([(1, 0), (2, 0)], [a for (a, b, c) in day03.trace_wire(p, day03.unpack_command('R2'))])
        self.assertEqual([(-1, 0), (-2, 0)], [a for (a, b, c) in day03.trace_wire(p, day03.unpack_command('L2'))])
        self.assertEqual([(0, 1), (0, 2)], [a for (a, b, c) in day03.trace_wire(p, day03.unpack_command('U2'))])
        self.assertEqual([(0, -1), (0, -2)], [a for (a, b, c) in day03.trace_wire(p, day03.unpack_command('D2'))])

    def test_calculate_route(self):
        commands = [('R', 8), ('U', 5), ('L', 5), ('D', 3)]
        expected = (3, 2)
        self.assertEqual(expected, day03.calculate_route(commands)[-1][0])

    def test_find_overlaps(self):
        c1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        c2 = "U62,R66,U55,R34,D71,R55,D58,R83"

        coords1 = [day03.unpack_command(s) for s in c1.split(",")]
        coords2 = [day03.unpack_command(s) for s in c2.split(",")]

        visited = day03.calculate_route(coords1, 'wire1')
        visited.extend(day03.calculate_route(coords2, 'wire2'))

        overlaps = day03.find_overlaps(visited)
        self.assertEqual(159, day03.find_min_manhattan(overlaps))

    def test_find_overlaps2(self):
        c1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        c2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

        coords1 = [day03.unpack_command(s) for s in c1.split(",")]
        coords2 = [day03.unpack_command(s) for s in c2.split(",")]

        visited = day03.calculate_route(coords1, 'wire1')
        visited.extend(day03.calculate_route(coords2, 'wire2'))

        overlaps = day03.find_overlaps(visited)
        self.assertEqual(135, day03.find_min_manhattan(overlaps))

    def test_steps_to_get_somewhere(self):
        wire = "R8,U5,L5,D2"
        wire_commands = [day03.unpack_command(s) for s in wire.split(",")]
        c = (3, 3)

        self.assertEqual(20, day03.find_steps_to(day03.calculate_route(wire_commands), c))

    def test_find_minimum_steps(self):
        wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"

        wire1_route = day03.calculate_route([day03.unpack_command(s) for s in wire1.split(",")], 'wire1')
        wire2_route = day03.calculate_route([day03.unpack_command(s) for s in wire2.split(",")], 'wire2')

        all_coordinates = wire1_route[:]
        all_coordinates.extend(wire2_route)
        overlaps = day03.find_overlaps(all_coordinates)

        self.assertEqual(610, day03.find_minimum_steps(overlaps, wire1_route, wire2_route))

    def test_find_minimum_steps_again(self):
        wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

        wire1_route = day03.calculate_route([day03.unpack_command(s) for s in wire1.split(",")], 'wire1')
        wire2_route = day03.calculate_route([day03.unpack_command(s) for s in wire2.split(",")], 'wire2')

        all_coordinates = wire1_route[:]
        all_coordinates.extend(wire2_route)
        overlaps = day03.find_overlaps(all_coordinates)

        self.assertEqual(410, day03.find_minimum_steps(overlaps, wire1_route, wire2_route))


if __name__ == '__main__':
    unittest.main()
