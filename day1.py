def day1data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip().split("\n")
        input_list = list(map(str, input_list))
        return input_list


day1puzzle = day1data("day1input.txt")


def first_star(puzzle: list) -> int:
    elf_carriage = []
    current_elf = 0
    for n in puzzle:
        if n != '':
            current_elf += int(n)
        else:
            elf_carriage.append(current_elf)
            current_elf = 0
    return max(elf_carriage)


first_star(day1puzzle)

