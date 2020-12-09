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


def day_2_part_2(text):
    raw_events = sorted(tuple(parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", l)) for l in text.split('\n'))  # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py

    return raw_events


class TestDay5part1(unittest.TestCase):

    def test_day_2_part_2(self):
        text = input_file()
        #res = output_file()
        #pred = day_2_part_2(text)
        #print(pred)
        text = input_file()
        #res = output_file()
        #pred = day_2_part_1(text)

        def process(noun, verb, text):
            i = 0
            code = [int(val) for val in text.split(",")]
            #print(code)
            code[1] = noun
            code[2] = verb
            length = len(code)
            try:
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
            except:
                return -1
                #print(i, code)

                #print(code[i], i, length)
            return code[0]

        noun = 0
        verb = 0
        while noun < 99:
            while verb < 99:
                output = process(noun, verb, text)
                #print(noun, verb, output_1)
                if output == 19690720:
                    print(100 * noun + verb)
                    break
                verb += 1
            verb = 0
            noun += 1

        #assert(pred == res
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
