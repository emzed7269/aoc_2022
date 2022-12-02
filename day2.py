import re


def day2data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip()
        input_list = re.split('\n| ', input_list)
        input_list = list(map(str, input_list))
        return input_list


day2puzzle = day2data('day2input.txt')

print(day2data("day2input.txt"))
