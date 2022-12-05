import re


def day4data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip()
        input_list = re.split(",|-|\n", input_list)
        input_list = list(map(int, input_list))
        return input_list


day4puzzle = day4data("day4input.txt")


def first_star(puzzle: list) -> int:
    total_sum = 0
    for n in range(len(puzzle)):
        if n % 4 == 0:
            pairs = [i for i in puzzle[n:n + 4]]
            first_lower, first_upper, second_lower, second_upper = pairs[0], pairs[1], pairs[2], pairs[3]
            lower_diff = first_lower - second_lower
            upper_diff = first_upper - second_upper
            if lower_diff >= 0 >= upper_diff:
                total_sum += 1
            elif lower_diff <= 0 <= upper_diff:
                total_sum += 1
    return total_sum


first_star(day4puzzle)


def second_star(puzzle: list) -> int:
    total_count = 0
    for n in range(len(puzzle)):
        if n % 4 == 0:
            pairs = [i for i in puzzle[n:n + 4]]
            first_lower, first_upper, second_lower, second_upper = pairs[0], pairs[1], pairs[2], pairs[3]
            if second_lower <= first_upper <= second_upper:
                total_count += 1
            elif first_lower <= second_upper <= first_upper:
                total_count += 1
    return total_count


print(second_star(day4puzzle))
