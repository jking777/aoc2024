import os
from typing import Tuple, List


aoc_day_num = 1

local_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}.txt')


def sample_data() -> Tuple[List[int], List[int]]:
    return [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]


def data() -> Tuple[List[int], List[int]]:
    with open(local_file, 'r') as inp:
        lines = inp.read().splitlines()

    l1 = list()
    l2 = list()
    for line in lines:
        t1, t2 = line.split()
        l1.append(int(t1))
        l2.append(int(t2))

    return l1, l2
