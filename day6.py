def day6data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read()
        input_list = list(map(str, input_list))
        return input_list


day6puzzle = day6data("day6input.txt")


def both_stars(puzzle: list, distinct_chars: int) -> list:
    for n in range(len(puzzle) - distinct_chars):
        subroutine = set([x for x in puzzle[n:n+distinct_chars]])
        if len(subroutine) == distinct_chars:
            return n+distinct_chars


first_star = both_stars(day6puzzle, 4)
second_star = both_stars(day6puzzle, 14)
