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


def get_nb_pass_valid(lines):
    nb_pass = 0  # initialize count valid pass
    for line in lines:  # for each lines
        raw_policy, raw_letter, password = line.split(" ")  # extract policy
        min_policy, max_policy = raw_policy.split("-")
        letter = raw_letter[0]  # the letter to test
        c = 0  # initialize count
        for letter_password in password:  # for each letter in password
            if letter == letter_password:  # case there was the letter to test in password
                c += 1  # increment count
        #print(c)
        if int(min_policy) <= c <= int(max_policy):
            #print(letter, "policy ok")
            nb_pass += 1  # increment count valid pass
    return nb_pass  # case it won't work


class TestDay2part1(unittest.TestCase):

    def test_day_2_part_1(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_pass_valid(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
