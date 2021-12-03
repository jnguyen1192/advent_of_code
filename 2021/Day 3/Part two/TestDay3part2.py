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


def get_life_support_rating(lines):
    def get_common_bit_more(bit_dict_raw):
        c = 0
        for bit in bit_dict_raw:
            if bit == "1":
                c += 1
        return "1" if c >= len(bit_dict_raw)/2 else "0"

    def get_common_bit_fewer(bit_dict_raw):
        c = 0
        for bit in bit_dict_raw:
            if bit == "1":
                c += 1
        return "1" if c < len(bit_dict_raw)/2 else "0"

    def get_bit_dict(bit_list):
        bit_dict = {}
        for i, bit in enumerate(lines[1]):
            bit_dict[i] = []
        for dynamic in bit_list:
            for i, bit in enumerate(dynamic):
                bit_dict[i].append(bit)
        return bit_dict

    dynamic_list = lines
    res_more = []
    for i in range(len(lines[1])):
        common_bit_more = get_common_bit_more(get_bit_dict(dynamic_list)[i])
        res_more.append(common_bit_more)
        tmp = []
        for dynamic in dynamic_list:
            if dynamic[i] == common_bit_more:
                tmp.append(dynamic)
        dynamic_list = tmp
        if len(dynamic_list) == 1:
            res_fewer = dynamic_list[0]
            break
        #print(dynamic_list)
    dynamic_list = lines
    res_fewer = []
    for i in range(len(lines[1])):
        common_bit_fewer = get_common_bit_fewer(get_bit_dict(dynamic_list)[i])
        res_fewer.append(common_bit_fewer)
        tmp = []
        for dynamic in dynamic_list:
            if dynamic[i] == common_bit_fewer:
                tmp.append(dynamic)
        dynamic_list = tmp
        if len(dynamic_list) == 1:
            res_fewer = dynamic_list[0]
            break
        #print(dynamic_list)
    #print(res_more, res_fewer)

    pc1 = 0
    pc2 = 0
    for i, bit in enumerate(res_more[::-1]):
        pc1 += (2**i) * int(bit)
    for i, bit in enumerate(res_fewer[::-1]):
        pc2 += (2**i) * int(bit)
    print(pc1, pc2)
    return pc1 * pc2# case it won't work


class TestDay3part2(unittest.TestCase):

    def test_day_3_part_2(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_life_support_rating(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
