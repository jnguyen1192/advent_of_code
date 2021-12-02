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


def get_final_position(lines):
    cmd_dict = {"forward": (1, 0),
           "down": (0, 1),
           "up": (0, -1)}
    horizontal_depht = (0, 0)
    aim = 0
    for line in lines:  # for each lines
        cmd, X = line.split()
        X = int(X)
        aim += cmd_dict[cmd][1] * X
        horizontal_depht = (horizontal_depht[0] + cmd_dict[cmd][0] * X, horizontal_depht[1] + cmd_dict[cmd][0] * aim * X)

    return horizontal_depht[0] * horizontal_depht[1]  # case it won't work


class TestDay2part2(unittest.TestCase):

    def test_day_2_part_2(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_final_position(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
