def get_opcode(instruction):
    return int(str(instruction)[-2:])


def process(input_program, offset=0, input_id=0):
    opcode = get_opcode(input_program[offset])
    instruction = get_instruction(input_program, offset, opcode)

    if opcode == 1:
        input_program = add(instruction, input_program)
        offset += 4
    elif opcode == 2:
        input_program = multiply(instruction, input_program)
        offset += 4
    elif opcode == 3:
        input_program[instruction[1]] = input_id
        offset += 2
    elif opcode == 4:
        print(f"Output: {input_program[instruction[1]]} at offset: {offset}")
        offset += 2
    elif opcode == 99:
        return input_program
    else:
        exit(1)

    return process(input_program, offset, input_id)


def get_instruction(input_program, instruction_pointer, opcode):
    if opcode == 99:
        return [input_program[instruction_pointer + 0]]
    elif opcode == 3 or opcode == 4:
        return input_program[instruction_pointer + 0], \
               input_program[instruction_pointer + 1]
    else:
        return input_program[instruction_pointer + 0], \
               input_program[instruction_pointer + 1], \
               input_program[instruction_pointer + 2], \
               input_program[instruction_pointer + 3]


def get_parameter_modes(instruction):
    full_instruction = str(instruction).zfill(5)
    return tuple(int(x) for x in (full_instruction[-3:-2], full_instruction[-4:-3], full_instruction[-5:-4]))


def get_input_value(input_program, param, mode):
    if mode == 0:
        return input_program[param]
    else:  # Immediate mode
        return param


def add(instruction, input_program):
    mode1, mode2, mode3 = get_parameter_modes(instruction[0])

    input_1 = get_input_value(input_program, instruction[1], mode1)
    input_2 = get_input_value(input_program, instruction[2], mode2)

    sum_of_inputs = input_1 + input_2
    output_index = instruction[3]  # Always in position mode

    input_program[output_index] = sum_of_inputs
    return input_program


def multiply(instruction, input_program):
    mode1, mode2, mode3 = get_parameter_modes(instruction[0])

    input_1 = get_input_value(input_program, instruction[1], mode1)
    input_2 = get_input_value(input_program, instruction[2], mode2)

    sum_of_inputs = input_1 * input_2
    output_index = instruction[3]  # Always in position mode

    input_program[output_index] = sum_of_inputs
    return input_program


def process_input(instruction, input_program):
    mode1, mode2, mode3 = get_parameter_modes(instruction[0])

    return get_input_value(input_program, instruction[1], mode1)


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
