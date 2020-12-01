import unittest
from collections import Counter


def input_file():
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def find_sum_2020(lines):
    numbers = []
    first = -1
    for line in lines:    # browse each lines
        tmp = int(line)
        numbers.append(tmp)
        if len(numbers) == 1:
            first = tmp
            continue
        if first + tmp == 2020:
            return first * tmp
    for i, v in enumerate(numbers):
        if i == 0:
            continue
        for j, w in enumerate(numbers):
            if j > i:
                if v + w == 2020:
                    return v * w
    return -1


class TestDay1part1(unittest.TestCase):

    def test_day_1_part_1(self):
        lines = input_file()
        res = output_file()
        pred = find_sum_2020(lines)
        print(pred)
        assert(str(pred) == res[0])


if __name__ == '__main__':
    unittest.main()
