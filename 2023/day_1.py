from typing import List

from utils import read_lines, is_digit


names = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


class Day1:
    part_one_result = 0
    part_two_result = 0

    def __init__(self):
        self.lines = read_lines("day_1")

    @staticmethod
    def find_first_digit(line: List):
        gen = enumerate(i for i in line)
        while True:
            position, digit = next(gen)
            if is_digit(digit):
                return position, digit

    @staticmethod
    def find_first_word(line, reverse=False):
        results = {name if not reverse else name[::-1]: 99 for name, v in names.items()}
        for name, _ in results.items():
            try:
                results[name] = line.index(name)
            except ValueError:
                pass
        min_name = min(results, key=results.get)
        return results[min_name], names[min_name[::-1] if reverse else min_name]

    def parse_line(self, line: str, reverse: bool = False, str_too: bool = False):
        if reverse:
            line = line[::-1]
        pos, first = self.find_first_digit(line)
        if str_too:
            pos_w, first_w = self.find_first_word(line, reverse)
            if pos_w < pos:
                first = first_w
        return first

    def part_one(self):
        for line in self.lines:
            first = self.parse_line(line)
            second = self.parse_line(line, reverse=True)
            self.part_one_result += int(f"{first}{second}")

    def part_two(self):
        for line in self.lines:
            first = self.parse_line(line, str_too=True)
            second = self.parse_line(line, reverse=True, str_too=True)
            self.part_two_result += int(f"{first}{second}")


if __name__ == '__main__':
    day_1 = Day1()

    day_1.part_one()
    print(f"Part One result is: {day_1.part_one_result}")

    day_1.part_two()
    print(f"Part Two result is: {day_1.part_two_result}")
