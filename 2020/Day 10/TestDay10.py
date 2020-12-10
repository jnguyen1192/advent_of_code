import unittest


def input_file(suffix):
    file = open('input_' + suffix, 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file(number):
    file = open('output_'+str(number), 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def get_differences(lines):
    adapters = []
    for line in lines:
        adapters.append(int(line))
    adapters.sort()
    #print(adapters)
    differences = {1: 1,
                   2: 1,
                   3: 1}
    for index, adapter in enumerate(adapters[:-1]):  # count difference
        #print(adapter, adapters[index + 1], abs(adapter - adapters[index + 1]))
        differences[abs(adapter - adapters[index + 1])] += 1
    return differences[1],  differences[3]


def get_chain_outlet(lines):
    difference_1, difference_3 = get_differences(lines)
    return difference_1 * difference_1


def get_all_distinct_number_chain_outlet(lines):  #  https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd
    result = {0: 1}  # init first combination
    adapters = [int(line) for line in lines]  # get each element
    for adapter in sorted(adapters):  # for each element
        result[adapter] = 0  # begin with value 0
        if adapter - 1 in result:  # case before number
            result[adapter] += result[adapter - 1]  # add result of before number
        if adapter - 2 in result:  # case before -2 number
            result[adapter] += result[adapter - 2]  # add result of before -2 number
        if adapter - 3 in result:  # case before -3 number
            result[adapter] += result[adapter - 3]  # add result of before -3    number
    print(result)
    return result[max(adapters)]


class TestDay10(unittest.TestCase):

    def test_day_10_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file(1)  # get output_1
        res = output_file("test_1")  # get output_1
        pred = get_chain_outlet(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_day_10_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        pred = get_all_distinct_number_chain_outlet(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
