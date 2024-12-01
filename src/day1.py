from data.day1_data import sample_data, data
import numpy as np


DATA = data()


def part1():
    l1, l2 = DATA
    l1 = sorted(l1)
    l2 = sorted(l2)
    assert len(l1) == len(l2)

    deltas = [abs(x[0] - x[1]) for x in zip(l1, l2)]
    delta_sum = sum(deltas)
    print(delta_sum)


def part2():
    l1, l2 = DATA
    l1 = sorted(l1)
    l2 = sorted(l2)
    assert len(l1) == len(l2)

    values, counts = np.unique(l2, return_counts=True)
    assert len(values) == len(counts)

    count_map = dict()
    for i in range(len(values)):
        count_map[values[i]] = counts[i]

    scores = list()
    for value in l1:
        count = count_map.get(value, 0)
        scores.append(value * count)

    scores_sum = sum(scores)
    print(f"Part 2:  {scores_sum}")


def main():
    part2()


if __name__ == "__main__":
    main()
