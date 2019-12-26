"""
Input:
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L

Want this:
       G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I

To look like:
{
    "COM": {"direct": None, "indirect": []}
    "B": {"direct": "COM" , "indirect": []}
    ..
    "D": {"direct": "C", "indirect": ["B", "COM"]}
    ..
"""


def find_direct_orbits(map):
    orbits = {}
    for o in map:
        inner, outer = str.split(o, ")")
        orbits[outer] = {"direct": inner, "indirect": []}

    return orbits


def find_all_orbits(orbits):
    """"Input looks like this:
        {
            "B": {"direct": "COM", "indirect": []},
            "C": {"direct": "B", "indirect": []},
            "D": {"direct": "C", "indirect": []}
    }"""
    complete_orbits = orbits.copy()
    for k, v in complete_orbits.items():
        direct_orbit = v.get("direct", None)
        if orbits.get(direct_orbit, None):
            indirect_orbits = orbits[direct_orbit].get("direct", None)
            v["indirect"].append(indirect_orbits)
            indirect_orbits = orbits[direct_orbit].get("indirect", [])
            v["indirect"].extend(indirect_orbits)
    return complete_orbits


def get_indirect_orbits(complete_orbits, start_orbit, orbits=None):
    if orbits is None:
        orbits = []
    direct_orbit = start_orbit.get("direct", None)
    if direct_orbit is None:
        return orbits
    else:
        orbits.append(direct_orbit)
        return get_indirect_orbits(complete_orbits, complete_orbits.get(direct_orbit, None), orbits)


def find_all_orbits_alt(orbits):
    complete_orbits = orbits.copy()
    for k, v in complete_orbits.items():
        direct_orbit = orbits.get(v.get("direct", None), None)
        if orbits.get(direct_orbit, None):
            indirect_orbits = get_indirect_orbits(complete_orbits, direct_orbit)
            v["indirect"].extend(indirect_orbits)
    return complete_orbits


def count_indirect(orbits):
    sum_of_indirect = 0
    for k, v in orbits.items():
        sum_of_indirect += len(v.get("indirect", []))
    return sum_of_indirect


def total_orbits(input_map):
    direct_orbits = find_direct_orbits(input_map)
    all_orbits = find_all_orbits_alt(direct_orbits)
    total_indirect_orbits = count_indirect(all_orbits)
    return len(direct_orbits) + total_indirect_orbits


if __name__ == '__main__':
    with open("day06-input.txt") as f:
        map_from_file = []
        for line in f:
            map_from_file.append(line)

    print(f"Part 1: Total orbits = {total_orbits(map_from_file)}")
