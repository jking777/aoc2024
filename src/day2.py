from typing import List

from data.day2_data import sample_data, data


DATA = data()


def is_positive(value: int) -> bool:
    return value > 0


def is_negative(value: int) -> bool:
    return value < 0


def is_safe(row: List[int]) -> bool:
    assert len(row) > 1

    deltas = list()
    for i in range(1, len(row)):
        deltas.append(row[i] - row[i - 1])

    for d in deltas:
        if abs(d) < 1 or abs(d) > 3:
            return False

    # all positive or all negative?
    if deltas[0] > 0:
        comp = is_positive
    else:
        comp = is_negative

    for d in deltas:
        if not comp(d):
            return False

    return True


def is_conditionally_safe(row: List[int]) -> bool:
    if is_safe(row):
        return True

    if row[1] - row[0] > 0:
        comp = is_positive
    else:
        comp = is_negative

    for i in range(1, len(row) - 1):
        delta = row[i + 1] - row[i]
        bad_direction = not comp(delta)
        if abs(delta) < 1 or abs(delta) > 3 or bad_direction:
            del row[i]
            return is_safe(row)

    return False


def is_conditionally_safe_brute(row: List[int]) -> bool:
    if is_safe(row):
        return True

    for i in range(len(row)):
        temp = row.copy()
        del temp[i]
        if is_safe(temp):
            return True

    return False


def part1():
    safe_count = 0

    for row in DATA:
        if is_safe(row):
            safe_count += 1

    print(f"Part 1: {safe_count}")


def part2():
    safe_count = 0

    for row in DATA:
        if is_conditionally_safe_brute(row):
            safe_count += 1

    print(f"Part 2: {safe_count}")


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
