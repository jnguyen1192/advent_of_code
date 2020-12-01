import unittest


def input_file():
    # read lines of input file
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def find_sum_2020_part2(lines):
    numbers = []
    for line in lines:  # browse each lines
        tmp = int(line)  # convert string into number
        numbers.append(tmp)  # fufill array number

    for i, v in enumerate(numbers):  # browse using index
        for j, w in enumerate(numbers):  # browse using index
            if j > i:  # the second number is less than the first number
                if v + w < 2020:  # the sum of two first number are less than 2020
                    for k, x in enumerate(numbers):  # browse using index
                        if k > j:  # the third number is less than the second number
                            if v + w + x == 2020:  # the sum of the three numbers are equals to 2020
                                return v * w * x  # return the product of the three numbers
    return -1  # if it won't find numbers


class TestDay1part2(unittest.TestCase):

    def test_day_1_part_2(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = find_sum_2020_part2(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check



        #assert(sub_str(line1_res, line2_res) == res[0])


if __name__ == '__main__':
    unittest.main()
