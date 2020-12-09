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


def get_sum_group_count_yes(lines):
    letters = "abcdefghijklmnopqrstuvwxyz"  # initialize all char to count
    group_yes = []  # initialize group of yes
    group_count = {}  # initialize each group letter count
    for char in letters:  # for each letter
        group_count[char] = 0  # initialize count as 0
    for line in lines:  # for each people
        for char in line:  # for each yes answer
            group_count[char] = 1  # set letter count to one
        if line == "":
            group_yes.append(sum(group_count.values()))  # sum the values of yes and add it to the final group to count yes
            group_count = {}  # clear group yes count
    group_yes.append(sum(group_count.values()))  # sum the values of yes and add it to the final group to count yes

    return sum(group_yes)  # return nb of valid password


class TestDay6part1(unittest.TestCase):

    def test_day_6_part_1(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_sum_group_count_yes(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
