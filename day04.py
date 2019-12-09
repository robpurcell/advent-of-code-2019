def is_six_digits(num):
    return len(str(num)) == 6


def is_in_range(num, start, end):
    return start < num < end


def contains_double_digits(num):
    num_str = str(num)
    i = 0

    for c in num_str[:-1]:
        if c == num_str[i + 1]:
            return True
        i += 1
    return False


def double_not_part_of_wider_group(num):
    num_str = str(num)

    for c in num_str:
        if num_str.count(c) == 2:
            return True
    return False


def digits_dont_decrease(num):
    num_str = str(num)
    count = 0

    for c in num_str[:-1]:
        if int(c) > int(num_str[count + 1]):
            return False
        count += 1
    return True


if __name__ == '__main__':
    scope = '172851-675869'
    i, j = scope.split("-")
    valid_passwords = 0

    for x in range(int(i), int(j)):
        if is_six_digits(x) and \
                is_in_range(x, int(i), int(j)) and \
                contains_double_digits(x) and \
                digits_dont_decrease(x):
            valid_passwords += 1

    print(f"Part1: Number of valid passwords = {valid_passwords}")

    valid_passwords = 0
    for x in range(int(i), int(j)):
        if is_six_digits(x) and \
                is_in_range(x, int(i), int(j)) and \
                double_not_part_of_wider_group(x) and \
                digits_dont_decrease(x):
            valid_passwords += 1

    print(f"Part1: Number of valid passwords = {valid_passwords}")
