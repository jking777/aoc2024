import os


aoc_day_num = 5

local_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}.txt')


def parse_rules(text: list[str]) -> list[tuple[int, int]]:
    result = []
    for line in text:
        toks = line.split("|")
        result.append((int(toks[0]), int(toks[1])))
    return result


def parse_pages(text: list[str]) -> list[list[int]]:
    result = []
    for line in text:
        toks = line.split(",")
        result.append([int(x) for x in toks])
    return result


def sample_data() -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]
    pages = [
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47",
    ]
    return parse_rules(rules), parse_pages(pages)


def data() -> tuple[list[tuple[int, int]], list[list[int]]]:
    with open(local_file, 'r') as inp:
        file_data = inp.read().splitlines()

    rules = []
    updates = []
    is_rules = True
    for line in file_data:
        if len(line) == 0:
            is_rules = False
        else:
            if is_rules:
                rules.append(line)
            else:
                updates.append(line)

    return parse_rules(rules), parse_pages(updates)
