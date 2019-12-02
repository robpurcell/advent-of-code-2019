def calc_fuel(mass):
    fuel_required = (mass // 3) - 2
    return fuel_required


def calc_fuel_fuel(fuel_mass, acc=0):
    fuel_required = calc_fuel(fuel_mass)
    if fuel_required > 0:
        return calc_fuel_fuel(fuel_required, acc + fuel_required)
    else:
        return acc


with open("day01-input.txt") as f:
    total_fuel = 0

    for line in f:
        mass = int(line)
        total_fuel += calc_fuel(mass)

    print(f"Part 1: The total fuel is {total_fuel}")


if __name__ == '__main__':
    with open("day01-input.txt") as f:
        total_fuel = 0

        for line in f:
            mass = int(line)
            fuel = calc_fuel(mass)
            fuel_for_fuel_mass = calc_fuel_fuel(fuel)
            total_fuel += fuel + fuel_for_fuel_mass

        print(f"Part 2: The total fuel is {total_fuel}")
