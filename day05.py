import day02



if __name__ == '__main__':
    with open("day05-input.txt") as f:
        line = f.readline()

        program = [int(x) for x in line.split(",")]

        print(f"Part 1")
        output = day02.process(program,  input_id=1)[0]

