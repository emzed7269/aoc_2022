import re


def day2data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip()
        input_list = re.split('\n| ', input_list)
        input_list = list(map(str, input_list))
        return input_list


day2puzzle = day2data('day2input.txt')


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


first_star(day2puzzle)


day2puzzle = day2data('day2input.txt')


def second_star(puzzle: list) -> int:
    round_score = {'X': 0, 'Y': 3, 'Z': 6}
    move_score = {'A': 1, 'B': 2, 'C': 3}
    move_order = {'A': 'B', 'B': 'C', 'C': 'A'}
    total_score = 0
    for n in range(len(puzzle)):
        if n % 2 == 1:
            round_result = round_score[puzzle[n]]
            if round_result == 6:
                chosen_move = move_order[puzzle[n-1]]
            elif round_result == 3:
                chosen_move = puzzle[n-1]
            elif round_result == 0:
                chosen_move = move_order[move_order[puzzle[n-1]]]
            total_score += move_score[chosen_move] + round_result
    return total_score


second_star(day2puzzle)
print(second_star(day2puzzle))


