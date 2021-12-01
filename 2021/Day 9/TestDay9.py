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


def get_first_number_not_follow_rule(lines, preamble_length):
    first_number_not_follow_rule = -1
    index_first_number_not_follow_rule = -1
    for index, line in enumerate(lines):
        if index < preamble_length:
            continue
        numbers_to_sum = [int(i) for i in lines[index-preamble_length: index]]  # get numbers before curent number
        sum_of_numbers = int(line)

        def is_sum_of_numbers(sum_of_numbers, numbers_to_sum):
            for index_1, number_1 in enumerate(numbers_to_sum):  # try each combination
                for index_2, number_2 in enumerate(numbers_to_sum):
                    if index_1 == index_2 or number_1 > sum_of_numbers or number_2 > sum_of_numbers:
                        continue
                    if number_1 + number_2 == sum_of_numbers:
                        return True
            return False

        #print(numbers_to_sum)
        if not is_sum_of_numbers(sum_of_numbers, numbers_to_sum):
            first_number_not_follow_rule = sum_of_numbers
            index_first_number_not_follow_rule = index
            break
    print(first_number_not_follow_rule, index_first_number_not_follow_rule)
    return first_number_not_follow_rule, index_first_number_not_follow_rule  # return accumlator in game console


def get_encryption_weakness(lines, preamble_length):
    def get_smallest_largest(numbers):
        smallest = 999999999
        largest = 0
        #print(numbers)
        for number in numbers:
            #print(number, smallest, largest)
            if number < smallest:
                smallest = number
            if number > largest:
                largest = number
        return smallest, largest

    first_number_not_follow_rule, index_first_number_not_follow_rule = get_first_number_not_follow_rule(lines, preamble_length)
    for index_min_range, min_range in enumerate([int(i) for i in lines[: index_first_number_not_follow_rule]]):  # find the encryption weakness before wrong number
        sum_range = min_range
        for index_max_range, max_range in enumerate([int(i) for i in lines[: index_first_number_not_follow_rule]]):  # sum until the end
            if index_min_range >= index_max_range:
                continue
            sum_range += max_range
            #print(sum_range, max_range)
            if sum_range == first_number_not_follow_rule:  # if it is equal return the encryption weakness
                #print(min_range, max_range)
                smallest, largest = get_smallest_largest([int(i) for i in lines[index_min_range: index_max_range + 1]])# get_smallest_largest
                return smallest + largest
            # if it is more than first_number_not_follow_rule continue
            if sum_range > first_number_not_follow_rule:
                break
    return -1


class TestDay8part1(unittest.TestCase):

    def test_day_9_part_1(self):
        lines = input_file("day")  # get input_test
        res = output_file(1)  # get output_1
        pred, _ = get_first_number_not_follow_rule(lines, 25)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_day_9_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file(2)  # get output_1
        pred = get_encryption_weakness(lines, 25)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
