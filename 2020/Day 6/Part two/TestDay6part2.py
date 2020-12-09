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


def get_sum_group_count_yes_all(lines):
    letters = "abcdefghijklmnopqrstuvwxyz"  # initialize all char to count
    group_yes = []  # initialize group of yes
    group_count = dict()  # initialize each group letter count
    group_count["nb_group"] = 0

    def yes_all(group_count):
        for key in group_count:  # for each answer
            if group_count["nb_group"] == group_count[key] and key != "nb_group":  # if the number of yes equals number of people
                yield 1  # return 1

    for char in letters:  # for each letter
        group_count[char] = 0  # initialize count as 0
    for line in lines:  # for each people
        for char in line:  # for each yes answer
            group_count[char] += 1  # increment letter count
        if line == "":
            group_yes.append(sum(yes_all(group_count)))  # part 2 sum the values of all yes and add it to the final group to count yes
            for char in letters:  # for each letter
                group_count[char] = 0  # set char value to 0
            group_count["nb_group"] = 0  # set the value to nb group to 0
        else:
            group_count["nb_group"] += 1  # increment nb_group
    group_yes.append(sum(yes_all(group_count)))  # get the sum of all yes for each group

    return sum(group_yes)  # return nb of valid password


class TestDay6part2(unittest.TestCase):

    def test_day_6_part_2(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_sum_group_count_yes_all(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
