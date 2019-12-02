def process(input_program, offset=0):
    instruction = get_instruction(input_program, offset)
    opcode = instruction[0]

    if opcode == 1:
        input_program = add(instruction, input_program)
    elif opcode == 2:
        input_program = multiply(instruction, input_program)
    elif opcode == 99:
        return input_program
    else:
        exit(1)

    return process(input_program, offset + 4)


def get_instruction(input_program, instruction_pointer):
    if instruction_pointer + 4 > len(input_program):
        return [input_program[instruction_pointer + 0]]
    else:
        return input_program[instruction_pointer + 0], \
               input_program[instruction_pointer + 1], \
               input_program[instruction_pointer + 2], \
               input_program[instruction_pointer + 3]


def add(instruction, input_program):
    parameter1_address = instruction[1]
    parameter2_address = instruction[2]
    sum_of_inputs = input_program[parameter1_address] + input_program[parameter2_address]
    output_index = instruction[3]

    input_program[output_index] = sum_of_inputs
    return input_program


def multiply(instruction, input_file):
    parameter1_address = instruction[1]
    parameter2_address = instruction[2]
    product_of_inputs = input_file[parameter1_address] * input_file[parameter2_address]
    output_index = instruction[3]

    input_file[output_index] = product_of_inputs
    return input_file


def initial_setup(initial_program, noun, verb):
    initial_program[1] = noun
    initial_program[2] = verb


if __name__ == '__main__':
    with open("day02-input.txt") as f:
        line = f.readline()

        program = [int(x) for x in line.split(",")]

        initial_setup(program, 12, 2)
        output = process(program)[0]

        print(f"Part 1: Value at position 0 = {output}")

        for i in range(100):
            for j in range(100):
                program = [int(x) for x in line.split(",")]
                initial_setup(program, i, j)
                output = process(program)[0]

                if output == 19690720:
                    print(f"Part 2: Answer = {(100 * i) + j}")