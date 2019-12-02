import unittest
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


def day_2_part_1(text):
    raw_events = sorted(tuple(parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", l)) for l in text.split('\n')) # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py

    return raw_events


class TestDay2part1(unittest.TestCase):

    def test_day_2_part_1(self):
        text = input_file()
        #res = output_file()
        #pred = day_2_part_1(text)
        d = {1: "add", 2: "mul", 3: "halt"}
        i = 0
        code = [int(val) for val in text.split(",")]
        code[1] = 12
        code[2] = 2
        length = len(code)
        while i < length:
            if code[i] == 1:
                code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
                i += 3
            elif code[i] == 2:
                code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
                i += 3
            elif code[i] == 99:
                break
            i += 1
            print(i, code)

            #print(code[i], i, length)

        print(code[0])
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
