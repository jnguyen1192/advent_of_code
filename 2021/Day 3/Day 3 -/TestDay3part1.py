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


def get_power_consumption(lines):
    bit_dict = {}
    for i, bit in enumerate(lines[1]):
        bit_dict[i]= []
    for line in lines:
        for i, bit in enumerate(line):
            bit_dict[i].append(bit)
    def get_common_bit(bit_dict_raw):
        c = 0
        print(bit_dict_raw)
        for bit in bit_dict_raw:
            if bit == "1":
                c += 1
        return "1" if c > len(bit_dict_raw)/2 else "0"
    common_bit_gamma = []
    for i in range(len(lines[1])):
        common_bit_gamma.append(get_common_bit(bit_dict[i]))
    common_bit_epsilon = ["1" if bit == "0" else "0" for bit in common_bit_gamma]
    pc1 = 0
    pc2 = 0
    print(common_bit_gamma, common_bit_epsilon)
    for i, bit in enumerate(common_bit_gamma[::-1]):
        pc1 += (2**i) * int(bit)
    for i, bit in enumerate(common_bit_epsilon[::-1]):
        pc2 += (2**i) * int(bit)
    print(pc1, pc2)
    return pc1 * pc2# case it won't work


class TestDay3part1(unittest.TestCase):

    def test_day_3_part_1(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_power_consumption(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
