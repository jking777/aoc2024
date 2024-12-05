import os


aoc_day_num = 3

local_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}.txt')


def sample_data() -> str:
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def sample_data2() -> str:
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def data() -> str:
    with open(local_file, 'r') as inp:
        return inp.read()
