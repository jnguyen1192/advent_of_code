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
        for key in password_to_check:  # for each keys
            if key in fields_valid:  # is key valid
                nb_key_in_password += 1  # increment nb key
        if nb_key_in_password >= len(fields_valid):  # test if nb key is correct
            return True
        return False


    fields_valid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # all key present and valid

    password_to_check = {}  # initialize a password
    passwords_to_check = []  # initialize password list

    for line in lines:  # for each line
        for code in line.split(" "):  # get the keys
            if line == "":  # case it is a blank line
                passwords_to_check.append(password_to_check)  # add a new password on list
                password_to_check = {}  # clear the password
                continue
            key, value = code.split(":")  # extract key and value
            password_to_check[key] = value  # add a new value on dict with its key
    passwords_to_check.append(password_to_check)  # add the last new password on list

    nb_valid_password = 0  # initialize nb valid password
    #nb_password = 0
    for password_to_check in passwords_to_check:  # for each passwords
        #nb_password += 1
        if is_valid_password(fields_valid, password_to_check):  # check if it is valid
            nb_valid_password += 1  # increment nb valid password
    # password last check
    return nb_valid_password  # return nb of valid password


class TestDay4part1(unittest.TestCase):

    def test_day_4_part_1(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_valid_password(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
