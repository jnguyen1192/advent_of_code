import unittest


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


def sum_lines(lines):
    return sum([int(line) for line in lines])


class TestDay1part1(unittest.TestCase):

    def test_day_1_part_1(self):
        lines = input_file()
        res = output_file()
        assert(sum_lines(lines) == res[0])


if __name__ == '__main__':
    unittest.main()