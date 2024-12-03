import os
from typing import Tuple, List


aoc_day_num = 2

local_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}.txt')


def sample_data() -> List[List[int]]:
    return [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def data() -> List[List[int]]:
    with open(local_file, 'r') as inp:
        lines = inp.read().splitlines()

    l = list()
    for line in lines:
        l.append([int(x) for x in line.split()])

    return l
