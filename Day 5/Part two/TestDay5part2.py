import unittest


def input_file():
    # read lines of input file
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


def day_5_part_2(lines):
    return lines


class TestDay5part1(unittest.TestCase):

    def test_day_5_part_2(self):
        lines = input_file()
        #res = output_file()
        pred = day_5_part_2(lines)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
