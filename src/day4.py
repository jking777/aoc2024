from typing import Tuple

from data.day4_data import sample_data, data


DATA = data()


class CompassExtractor:
    def __init__(self, data: list[str]) -> None:
        self.data = data
        self.row_count = len(self.data)
        self.col_count = len(self.data[0])
        for line in self.data:
            assert len(line) == self.col_count

    def n(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            r = row - i
            if r >= 0:
                result += self.data[r][col]
        return result

    def s(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            r = row + i
            if r < self.row_count:
                result += self.data[r][col]
        return result

    def e(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            c = col + i
            if c < self.col_count:
                result += self.data[row][c]
        return result

    def w(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            c = col - i
            if c >= 0:
                result += self.data[row][c]
        return result

    def nw(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            r = row - i
            c = col - i
            if r >= 0 and c >= 0:
                result += self.data[r][c]
        return result

    def ne(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            r = row - i
            c = col + i
            if r >= 0 and c < self.col_count:
                result += self.data[r][c]
        return result

    def sw(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            r = row + i
            c = col - i
            if r < self.row_count and c >= 0:
                result += self.data[r][c]
        return result

    def se(self, row: int, col: int) -> str:
        result = self.data[row][col]
        for i in range(1, 4):
            r = row + i
            c = col + i
            if r < self.row_count and c < self.col_count:
                result += self.data[r][c]
        return result

    def all_directions(self, row: int, col: int) -> list[str]:
        result = list()
        result.append(self.n(row, col))
        result.append(self.s(row, col))
        result.append(self.e(row, col))
        result.append(self.w(row, col))
        result.append(self.ne(row, col))
        result.append(self.nw(row, col))
        result.append(self.se(row, col))
        result.append(self.sw(row, col))
        return result


class ExExtractor:
    def __init__(self, data: list[str]) -> None:
        self.data = data
        self.row_count = len(self.data)
        self.col_count = len(self.data[0])
        for line in self.data:
            assert len(line) == self.col_count

    def x(self, row: int, col: int) -> Tuple[str, str]:
        return (
            self.data[row - 1][col - 1] + self.data[row][col] + self.data[row + 1][col + 1],
            self.data[row + 1][col - 1] + self.data[row][col] + self.data[row - 1][col + 1],
        )


def part1():
    ext = CompassExtractor(DATA)
    total = 0
    for row in range(ext.row_count):
        for col in range(ext.col_count):
            if DATA[row][col] == "X":
                words = ext.all_directions(row, col)
                for w in words:
                    if w == "XMAS":
                        total += 1

    print(f"Part 1:  {total}")


def is_mas(word: str) -> bool:
    return word == "MAS" or word == "SAM"


def part2():
    ext = ExExtractor(DATA)
    total = 0
    for row in range(1, ext.row_count - 1):
        for col in range(1, ext.col_count - 1):
            if DATA[row][col] == "A":
                words = ext.x(row, col)
                if is_mas(words[0]) and is_mas(words[1]):
                    total += 1

    print(f"Part 2:  {total}")


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
