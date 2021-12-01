import unittest


def input_file(suffix):
    file = open('input_' + suffix, 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file(number):
    file = open('output_'+str(number), 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res

import re


class M(int):
    def __sub__(self, y): return M(int(self) * y)

    def __add__(self, y): return M(int(self) + y)

    def __mul__(self, y): return M(int(self) + y)


def get_sum_resulting_values(lines): # Darkrai469 https://www.reddit.com/r/adventofcode/comments/kfeldk/2020_day_18_solutions/
    return sum(eval(re.sub(r'(\d+)', r'M(\1)', e).replace('*', '-')) for e in lines)  # get nb cubes


def get_sum_resulting_values_part_2(lines):
    return sum(eval(re.sub(r'(\d+)', r'M(\1)', e).replace('*', '-').replace('+', '*')) for e in lines)


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        res = output_file("1")  # get output_1
        pred = get_sum_resulting_values(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        res = output_file("2")  # get output_1
        pred = get_sum_resulting_values_part_2(lines)  # process
        print(pred) # https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/ popodiloco
        assert(str(pred) == res[0])


if __name__ == '__main__':
    unittest.main()
