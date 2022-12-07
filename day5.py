import re


def day5data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read()
        input_list = re.split("\n\n|\n", input_list)
        input_list = list(map(str, input_list))
        return input_list


day5puzzle = day5data("day5input.txt")


def list_split(puzzle: list) -> list:
    for i in puzzle:
        if 'move' in i:
            puzzle_split = puzzle.index(i)
            crates_build = puzzle[:puzzle_split]
            directions = puzzle[puzzle_split:]
            break
    for n in range(len(crates_build)):
        row = crates_build[n]
        crates_build[n] = [(row[i:i+4]) for i in range(0, len(row), 4)]
    for n in range(len(directions)):
        row = directions[n].replace('move ', '')
        directions[n] = re.split(" from | to ", row)
    crates_build.pop(len(crates_build)-1)
    return crates_build, directions


crates, guidelines = list_split(day5puzzle)


def first_star(puzzle: list, movements: list) -> str:
    horizontal_display = list(map(list, zip(*puzzle)))
    usable_display = [[x for x in sublist if x != '    ' and x != '   '] for sublist in horizontal_display]
    top_crates_str = ''
    for n in movements:
        n_of_crates = int(n[0])
        initial_stack = int(n[1]) - 1
        destination = int(n[2]) - 1
        while n_of_crates > 0:
            usable_display[destination].insert(0, usable_display[initial_stack][0])
            usable_display[initial_stack].pop(0)
            n_of_crates -= 1
    for t in range(len(usable_display)):
        top_crates_str += usable_display[t][0][1]
    return top_crates_str


fs = first_star(crates, guidelines)
print(fs)
