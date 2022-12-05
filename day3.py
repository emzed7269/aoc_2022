def day3data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip().split("\n")
        input_list = list(map(str, input_list))
        return input_list


day3puzzle = day3data("day3input.txt")
print(day3puzzle)


def first_star(puzzle: list) -> int:
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priority_list = [n for n in priority]
    duplicate_items = []
    total_sum = 0
    for rucksack in puzzle:
        compartment_size = len(rucksack)
        compartment_limit = int(compartment_size/2)
        first_compartment = [i for i in rucksack[:compartment_limit]]
        unique_items = [*set(rucksack[compartment_limit:compartment_size])]
        for item_type in unique_items:
            if item_type in first_compartment:
                duplicate_items.append(item_type)
    for duplicate_item in duplicate_items:
        total_sum += priority_list.index(duplicate_item)+1
    return total_sum


first_star(day3puzzle)


def second_star(puzzle: list) -> int:
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priority_list = [n for n in priority]
    duplicates = []
    total_sum = 0
    for n in range(len(puzzle)):
        if n % 3 == 0:
            elf_group = [i for i in puzzle[n:n+3]]
            for i in range(len(elf_group)):
                elf_group[i] = [*set(elf_group[i])]
            result = set.intersection(*map(set, elf_group))
            total_sum += priority_list.index(''.join(result)) +1
    return total_sum


second_star(day3puzzle)
