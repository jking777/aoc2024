import re

from data.day3_data import sample_data, sample_data2, data


SAMPLE = False


def part1():
    DATA = sample_data() if SAMPLE else data()

    total = 0
    pat = "mul\\((\\d+),(\\d+)\\)"
    result = re.findall(pat, DATA)
    for t1, t2 in result:
        total += int(t1) * int(t2)
    print(f"Part 1:  {total}")


def part2():
    DATA = sample_data2() if SAMPLE else data()

    total = 0
    pat = r"mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)"
    is_do = True
    for match in re.finditer(pat, DATA):
        if match.group(3) is not None:
            is_do = True
        elif match.group(4) is not None:
            is_do = False
        else:
            if is_do:
                total += int(match.group(1)) * int(match.group(2))
    print(f"Part 2:  {total}")


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
