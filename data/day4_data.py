import os


aoc_day_num = 4

local_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}.txt')


def sample_data() -> list[str]:
    return [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]


def data() -> list[str]:
    with open(local_file, 'r') as inp:
        return inp.read().splitlines()
