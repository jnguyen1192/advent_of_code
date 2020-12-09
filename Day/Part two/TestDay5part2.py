import unittest
from parse import parse


def input_file():
    # return the input_test file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output_1 file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def day_5_part_2(text):
    raw_events = sorted(tuple(parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", l)) for l in text.split('\n'))  # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py

    return raw_events


class TestDay5part1(unittest.TestCase):

    def test_day_5_part_2(self):
        text = input_file()
        #res = output_file()
        pred = day_5_part_2(text)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
