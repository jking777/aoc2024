from data.day5_data import sample_data, data


RULES, UPDATES = sample_data()


def build_rules_map() -> dict[int, set[int]]:
    rules_map: dict[int, set[int]] = dict()
    for rule in RULES:
        rules_map.setdefault(rule[0], set())
        rules_map[rule[0]].add(rule[1])
    return rules_map


def is_update_bad(befores: set[int] | None, update: list[int], index: int) -> bool:
    if index == 0 or befores is None:
        return False
    for j in range(index):
        if update[j] in befores:
            return True
    return False


def part1():
    total = 0

    rules_map = build_rules_map()

    for update in UPDATES:
        bad_update = False
        for i in range(1, len(update)):
            befores = rules_map.get(update[i], None)
            bad_update = is_update_bad(befores, update, i)
            if bad_update:
                break

        if not bad_update:
            middle = len(update) // 2
            total += update[middle]

    print(f"Part 1:  {total}")


def part2():
    total = 0

    rules_map = build_rules_map()

    for update in UPDATES:
        update_was_bad = False
        for i in range(1, len(update)):
            befores = rules_map.get(update[i], None)
            if is_update_bad(befores, update, i):
                update_was_bad = True
                for j in range(i, len(update)):
                    if is_update_bad(befores, update, j):
                        swap_to = j - 1
                        while swap_to >= 0:
                            update[swap_to], update[swap_to + 1] = update[swap_to + 1], update[swap_to]
                            if is_update_bad(befores, update, swap_to):
                                swap_to -= 1
                            else:
                                break

                middle = len(update) // 2
                total += update[middle]
            if update_was_bad:
                break

    print(f"Part 2:  {total}")


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
