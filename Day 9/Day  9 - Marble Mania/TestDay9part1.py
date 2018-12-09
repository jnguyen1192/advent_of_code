import unittest
import string
from parse import parse


def input_file():
    # return the input file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def day_9_part_1(text):
    # data retrieve
    raw_nodes = [tuple(parse("Step {} must be finished before step {} can begin.", l)) for l in
                 text.split('\n')]  # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py

    return str(0)


class TestDay9part1(unittest.TestCase):

    def test_day_9_part_2(self):
        text = input_file()
        res = output_file()
        pred = day_9_part_1(text)
        assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
