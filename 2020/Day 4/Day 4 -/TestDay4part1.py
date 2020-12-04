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


def get_nb_valid_password(lines):
    def is_valid_password(fields_valid, password_to_check):
        nb_key_in_password = 0
        for key in password_to_check:
            if key in fields_valid:
                nb_key_in_password += 1
        if nb_key_in_password >= len(fields_valid):  # low
            return True
        return False


    fields_valid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    password_to_check = {}
    passwords_to_check = []
    # cid
    for line in lines:
        for code in line.split(" "):
            if line == "":
                passwords_to_check.append(password_to_check)
                password_to_check = {}
                continue
            key, value = code.split(":")
            password_to_check[key] = value
    passwords_to_check.append(password_to_check)
    nb_valid_password = 0
    nb_password = 0
    for password_to_check in passwords_to_check:
        nb_password += 1
        if is_valid_password(fields_valid, password_to_check):
            nb_valid_password += 1
    # password last check
    print("nb_password", nb_password)

    return nb_valid_password#0#nb_tree_encounter_product  # case it won't work


class TestDay4part1(unittest.TestCase):

    def test_day_4_part_1(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_valid_password(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
