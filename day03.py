def manhattan_distance(p, q):
    x1, y1 = p
    x2, y2 = q
    return abs(x1 - x2) + abs(y1 - y2)


def add_vectors(p, q):
    x1, y1 = p
    x2, y2 = q
    return x1 + x2, y1 + y2


# start: coordinate
# distance: scalar
# move: unit vector
def move(start, distance, direction, steps_moved=0, wire_id=None):
    new_coordinate = start
    coordinates_visited = []

    for x in range(distance):
        steps_moved += 1
        new_coordinate = add_vectors(new_coordinate, direction)
        coordinates_visited.append((new_coordinate, wire_id, steps_moved))

    return coordinates_visited


def trace_wire(start, command, steps_moved=0, wire_id=None):
    direction, magnitude = command

    if direction == 'R':
        return move(start, magnitude, (1, 0), steps_moved, wire_id)
    elif direction == 'L':
        return move(start, magnitude, (-1, 0), steps_moved, wire_id)
    elif direction == 'U':
        return move(start, magnitude, (0, 1), steps_moved, wire_id)
    elif direction == 'D':
        return move(start, magnitude, (0, -1), steps_moved, wire_id)
    else:
        return wire_id, start


def unpack_command(command):
    return command[0], int(command[1:])


def calculate_route(commands, wire_id=None):
    coords_visited = []
    position = (0, 0)
    steps_so_far = 0
    for c in commands:
        coords_visited.extend((trace_wire(position, c, steps_so_far, wire_id)))
        position = coords_visited[-1][0]
        steps_so_far = coords_visited[-1][2]
    return coords_visited


def get_commands(f):
    wire = f.readline()
    return [unpack_command(s) for s in wire.split(",")]


def find_overlaps(all_coordinates_visited):
    overlaps = []

    all_coordinates_visited.sort()
    for i in range(len(all_coordinates_visited)):
        if i != len(all_coordinates_visited) - 1 and \
                all_coordinates_visited[i][0] == all_coordinates_visited[i + 1][0] and \
                all_coordinates_visited[i][1] != all_coordinates_visited[i + 1][1]:
            overlaps.append(all_coordinates_visited[i][0])
    return overlaps


def find_min_manhattan(overlaps):
    distances = [manhattan_distance((0, 0), c) for c in overlaps]
    return min(distances)


def find_steps_to(wire, target):
    for c in wire:
        if c[0] == target:
            return c[2]


def find_minimum_steps(overlapping_coordinates, wire1_coords, wire2_coords):
    steps = 1_000_000
    for c in overlapping_coordinates:
        s1 = find_steps_to(wire1_coords, c)
        s2 = find_steps_to(wire2_coords, c)
        if steps > s1 + s2:
            steps = s1 + s2
    return steps


if __name__ == '__main__':
    with open("day03-input.txt") as f:
        commands1 = get_commands(f)
        commands2 = get_commands(f)

        all_coordinates = calculate_route(commands1, 'wire1')
        all_coordinates.extend(calculate_route(commands2, 'wire2'))

        print(f"Part 1: min distance = {find_min_manhattan(find_overlaps(all_coordinates))}")

    with open("day03-input.txt") as f:
        commands1 = get_commands(f)
        commands2 = get_commands(f)

        wire1_route = calculate_route(commands1, 'wire1')
        wire2_route = calculate_route(commands2, 'wire2')
        all_coordinates = wire1_route[:]
        all_coordinates.extend(wire2_route)
        overlaps = find_overlaps(all_coordinates)

        print(f"Part 1: min distance = {find_minimum_steps(overlaps, wire1_route, wire2_route)}")
