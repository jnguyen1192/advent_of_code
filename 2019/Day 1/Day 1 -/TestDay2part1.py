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


def find_checksum(lines):
    two = 0
    three = 0
    # browse each lines
    for line in lines:
        # init bool to false for unique comparaison
        twobool = False
        threebool = False
        # count each letter
        c = Counter(line)
        for val in c:
            if c[val] == 2 and not twobool:
                twobool = True
                two += 1
            if c[val] == 3 and not threebool:
                threebool = True
                three += 1
    return str(two * three)


class TestDay1part1(unittest.TestCase):

    def test_day_1_part_1(self):
        lines = input_file()
        res = output_file()
        pred = find_checksum(lines)
        print(sum([int((int(l)/3))-2 for l in lines]))
        #assert(sum([int(l) for l in lines]) == res[0])


if __name__ == '__main__':
    unittest.main()
