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
    def is_digit_interval(min, max, nb_digit, key, password_to_check):
        if min <= int(password_to_check[key]) <= max and len(password_to_check[key]) == nb_digit and password_to_check[key].isnumeric():  # check rule with interval min max and length of digits
            return True
        return False

    def is_hgt_interval(min, max, unit, key, password_to_check):
        if password_to_check[key][-2:] == unit:  # check unit of height
            if min <= int(password_to_check[key][:-2]) <= max:  # check interval of height
                return True
            return False
        return False

    def is_valid_string(length, valid_chars, password):
        if len(password) == length:  # check length of chars
            for char in password:
                if char not in valid_chars:  # check if each char are in valid chars
                    return False
            return True

    def is_valid_integrity(key, password_to_check):
        if key == "byr":
            return is_digit_interval(192, 2002, 4, key, password_to_check)  # byr (Birth Year) - four digits; at least 1920 and at most 2002
        if key == "iyr":
            return is_digit_interval(2010, 2020, 4, key, password_to_check)  # iyr (Issue Year) - four digits; at least 2010 and at most 2020
        if key == "eyr":
            return is_digit_interval(2020, 2030, 4, key, password_to_check)  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030
        if key == "hgt":
            if password_to_check[key][-2:] == "cm":
                return is_hgt_interval(150, 193, "cm", key, password_to_check)  # If cm, the number must be at least 150 and at most 193
            elif password_to_check[key][-2:] == "in":
                return is_hgt_interval(59, 76, "in", key, password_to_check)  # If in, the number must be at least 59 and at most 76
            else:
                return False
        if key == "hcl":
            if password_to_check[key][0] == "#":
                return is_valid_string(6, "0123456789abcdef", password_to_check[key][1:])  # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
            return False
        if key == "ecl":
            if password_to_check[key] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:  # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
                return True
            return False
        if key == "pid":
            return is_valid_string(9, "0123456789", password_to_check[key])  # pid (Passport ID) - a nine-digit number, including leading zeroes
        if key == "cid":  # cid (Country ID) - ignored, missing or not
            return True

    def is_valid_password(fields_valid, password_to_check):
        nb_key_in_password = 0  # initialize nb key of password present and valid
        for key in password_to_check:  # check each key
            if not is_valid_integrity(key, password_to_check): # check rules before count
                return False
            if key in fields_valid:  # increment in the case the key and value is valid
                nb_key_in_password += 1

        if nb_key_in_password == len(fields_valid):  # check if there was all key present and valid, low need to be optimize
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


class TestDay4part2(unittest.TestCase):

    def test_day_4_part_2(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_valid_password(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
