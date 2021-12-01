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


def count_previous_number(lines):
    c = 0
    lines = [int(i) for i in lines]
    previous_sum = 20000
    for i, line in enumerate(lines):
        current_sum = sum(lines[i: i+3])
        if previous_sum <current_sum:
            c += 1
        previous_sum = current_sum
    return c  # case it won't work


class TestDay1part2(unittest.TestCase):

    def test_day_1_part_2(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = count_previous_number(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
