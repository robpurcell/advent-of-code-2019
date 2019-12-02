def process(input_content, offset=0):
    instruction = get_program_line(input_content, offset)
    opcode = instruction[0]

    if opcode == 1:
        input_content = add(instruction, input_content)
    elif opcode == 2:
        input_content = multiply(instruction, input_content)
    elif opcode == 99:
        return input_content
    else:
        exit(1)

    return process(input_content, offset + 4)


def get_program_line(input_file, offset):
    if offset + 4 > len(input_file):
        return [input_file[offset + 0]]
    else:
        return input_file[offset + 0], input_file[offset + 1], input_file[offset + 2], input_file[offset + 3]


def add(instruction, input_file):
    parameter1_address = instruction[1]
    parameter2_address = instruction[2]
    sum_of_inputs = input_file[parameter1_address] + input_file[parameter2_address]
    output_index = instruction[3]

    input_file[output_index] = sum_of_inputs
    return input_file


def multiply(instruction, input_file):
    parameter1_address = instruction[1]
    parameter2_address = instruction[2]
    product_of_inputs = input_file[parameter1_address] * input_file[parameter2_address]
    output_index = instruction[3]

    input_file[output_index] = product_of_inputs
    return input_file


def initial_setup(initial_program):
    initial_program[1] = 12
    initial_program[2] = 2


if __name__ == '__main__':
    with open("day02-input.txt") as f:
        line = f.readline()
        program = [int(x) for x in line.split(",")]

        initial_setup(program)
        value = process(program)[0]

        print(f"Part 1: Value at position 0 = {value}")
