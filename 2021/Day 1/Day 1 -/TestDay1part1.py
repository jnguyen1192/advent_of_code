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
    previous = 0
    c = 0
    for line in lines:
        if previous < int(line):
            c += 1
        #print(previous)
        previous = int(line)
    return c  # case it won't work


class TestDay1part1(unittest.TestCase):

    def test_day_1_part_1(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = count_previous_number(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
