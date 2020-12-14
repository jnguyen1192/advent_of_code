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


def get_sum_left_memory(lines):
    class SumLeftMemory:
        def __init__(self):
            self.mask = ""
            self.memory = {}

        def update_mask(self, line):
            self.mask = line[len("mask = "):]

        def exec(self, line):
            """Rule
            0 or 1 overwrites the corresponding bit in the value
            X leaves the bit in the value unchanged

            Ex:
            mem[8] = 11

            value:  000000000000000000000000000000001011  (decimal 11)
            mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
            result: 000000000000000000000000000001001001  (decimal 73)


            """

            def get_bit_value(value):
                return f'{value:036b}'

            def get_numbers_from_string(line):
                import re
                return list(map(int,re.findall(r'\d+', line)))

            def rule_part_1():
                index_memory, value = get_numbers_from_string(line)
                bit_value = get_bit_value(value)
                res = ""
                for i in range(len(self.mask)):
                    if self.mask[-(i+1)] == "1":
                        res += "1"
                    elif self.mask[-(i+1)] == "0":
                        res += "0"
                    else:
                        res += bit_value[-(i+1)]
                res = res[::-1]
                #print(res)
                self.memory[index_memory] = int(res, 2)
            #rule_part_1()


            def rule_part_2():
                index_memory, value = get_numbers_from_string(line)
                bit_value = get_bit_value(index_memory)
                #print(index_memory, bit_value)
                res = [""]  # every res
                for i in range(len(self.mask)):
                    if self.mask[-(i+1)] == "1":
                        for j in range(len(res)):
                            res[j] += "1"
                        #res += "1" # add 1 in every res
                    elif self.mask[-(i+1)] == "0":
                        for j in range(len(res)):
                            res[j] += bit_value[-(i+1)]
                        #res += bit_value[-(i+1)]# add same value in every res
                    else:
                        # double the res
                        tmp = res.copy()
                        for j in range(len(res)):
                            res[j] += "1"  # with 1
                            tmp[j] += "0"  # and 0
                        res = res + tmp
                        #res += "X"  # double the res with 0 and 1

                for j in range(len(res)):
                    res[j] = res[j][::-1]
                #res = res[::-1] # reverse all values
                #print(res)
                for j in range(len(res)):
                    #print(int(res[j], 2))
                    self.memory[int(res[j], 2)] = value
                #self.memory[index_memory] = int(res, 2)  # write on all values
            rule_part_2()

    slm = SumLeftMemory()
    for line in lines:
        if "mask = " in line:
            slm.update_mask(line)  # Update msk
        else:
            slm.exec(line)  # use mem to add on sum

    #print(slm.memory)
    return sum(slm.memory.values())


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        #res = output_file("test_1")  # get output_1
        pred = get_sum_left_memory(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test_2")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        pred = get_sum_left_memory(lines)  # process
        print(pred)
        assert(str(pred) == res[0])  # check https://github.com/busdriverbuddha/aoc2020_solutions/blob/main/day13.py



if __name__ == '__main__':
    unittest.main()
