import re


def day2data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip()
        input_list = re.split('\n| ', input_list)
        input_list = list(map(str, input_list))
        return input_list


day2puzzle = day2data('day2input.txt')
print(day2puzzle)


def first_star(puzzle: list) -> list:
    move_score = {'X': 1, 'Y': 2, 'Z': 3}
    move_equivalence = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    move_wins = {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
    total_score = 0
    for n in range(len(puzzle)):
        if puzzle[n] in move_equivalence:
            le_move = puzzle[n]
            puzzle[n] = move_equivalence[le_move]
        if n % 2 == 1:
            if puzzle[n] == puzzle[n-1]:
                total_score += move_score[puzzle[n]] + 3
            elif puzzle[n] == move_wins[puzzle[n-1]]:
                total_score += move_score[puzzle[n]] + 6
            else:
                total_score += move_score[puzzle[n]]
    return total_score


print(first_star(day2puzzle))

