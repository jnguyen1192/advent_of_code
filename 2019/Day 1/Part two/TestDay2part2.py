import unittest


def input_file():
    # read lines of input_test file
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    # read line of output_1 file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def count_similar_char(str1, str2):
    # return the number of same occurence between two strings
    # init acc
    acc = 0
    # browse in string length
    for i in range(len(str1)):
        # compare each char
        if str1[i] == str2[i]:
            # increment acc
            acc += 1
    return acc


def sub_str(str1, str2):
    # substract two string and give the final string result
    # init str result
    str_res = ""
    # browse in string length
    for i in range(len(str1)):
        # compare each char
        if str1[i] == str2[i]:
            # add char to the final string result
            str_res += str1[i]
    return str_res


def best_match_str(lines):
    # return the two strings that matches the best except the same strings
    # init variables
    line1_res = ""
    line2_res = ""
    count_similar = 0
    # browse lines of file
    for line1 in lines:
        # browse lines of file for each line
        for line2 in lines:
            # process only if lines are different
            if line1 != line2:
                # count
                count = count_similar_char(line1, line2)
                # get the best different strings except the same
                if count > count_similar and count != len(line1):
                    count_similar = count
                    # keep result lines
                    line1_res = line1
                    line2_res = line2
    return line1_res, line2_res


class TestDay1part2(unittest.TestCase):

    def test_day_1_part_2(self):
        lines = input_file()
        #res = output_file()
        #line1_res, line2_res = best_match_str(lines)
        fuels = []
        for fuel in lines:
            tmp_fuel = []
            current_fuel = int(fuel)
            while current_fuel > 0:
                int_fuel = int(current_fuel/3)-2
                if int_fuel > 0:
                    tmp_fuel.append(int_fuel)
                else:
                    tmp_fuel.append(0)
                current_fuel = int_fuel
            fuels.append(sum(tmp_fuel))
        print(sum(fuels))



        #assert(sub_str(line1_res, line2_res) == res[0])


if __name__ == '__main__':
    unittest.main()
