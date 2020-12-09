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
        tmp = int(line)  # convert string to int
        numbers.append(tmp)  # add on list
        if len(numbers) == 1:  # case it is the first number
            first = tmp  # intitialise first for the first time
            continue  # loop again
        if first + tmp == 2020:  # check the sum of two numbers
            return first * tmp  # special case at the first iteration

    for i, v in enumerate(numbers):  # browse using index
        if i == 0:  # case it is the first iteration
            continue  # loop again
        for j, w in enumerate(numbers):  # browse using index
            if j > i:  # case the second number is less than the first number
                if v + w == 2020:  # check the sum
                    return v * w  # return the product
    return -1  # case it won't work


class TestDay1part1(unittest.TestCase):

    def test_day_1_part_1(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = find_sum_2020(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
