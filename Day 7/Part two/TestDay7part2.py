import unittest
import numpy as np


def input_file():
    # return the input file in a text
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def day_7_part_2(lines):
    return lines


class TestDay7part2(unittest.TestCase):

    def test_day_7_part_2(self):
        text = input_file()
        #res = output_file()
        pred = day_7_part_2(text)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
