import unittest
from parse import parse


def input_file():
    # return the input_test file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output_1 file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class TestDay7part1(unittest.TestCase):
    def test_day_7_part_1(self):
        text = input_file()

        def process(text, phase_setting, value):
            i = 0
            code = [int(val) for val in text.split(",")]
            length = len(code)
            phase = True

            try:
                while i < length:
                    # add mode on opcode
                    # add 0 at the beginning of 1
                    tmp_cur = code[i]
                    str_opcode = str(tmp_cur)
                    while len(str_opcode) < 5:
                        str_opcode = "0" + str_opcode
                    opcode = int(str_opcode[3:])
                    # add pos and imm
                    # case param 1
                    if int(str_opcode[2]) == 0:  # position
                        first_param = code[i + 1]
                    else:
                        first_param = i + 1
                    # case param 2
                    if int(str_opcode[1]) == 0:  # position
                        second_param = code[i + 2]
                    else:
                        second_param = i + 2
                    # case param 2
                    if int(str_opcode[0]) == 0:  # position
                        third_param = code[i + 3]
                    else:
                        third_param = i + 3
                    #print(value, i, code[79], code[:i+1])
                    if code[i] == 99:
                        #print("exit")
                        break
                    if opcode == 1:  # addition
                        # case param 3
                        code[third_param] = code[first_param] + code[second_param]
                        i += 4
                    elif opcode == 2:  # multiplication
                        # case param 3
                        code[third_param] = code[first_param] * code[second_param]
                        i += 4
                    # code 3 and code 4
                    elif opcode == 3:  # as input_test 3, 50 => 3 take input_test and save to address 50
                        if phase:
                            code[first_param] = phase_setting
                            phase = False
                        else:
                            code[first_param] = value
                        i += 2
                    elif opcode == 4:  # as output_1 4, 50 => 4 output_1 the value at address 50
                        value = code[first_param]
                        # print("as input_test 3, 50 => 3 take input_test and save to address 50")
                        i += 2
                    elif opcode == 5:  # jump-if-true
                        if code[first_param] != 0:
                            i = code[second_param]
                        else:
                            i += 3
                    elif opcode == 6:  # jump-if-false
                        if code[first_param] == 0:
                            i = code[second_param]
                        else:
                            i += 3
                    elif opcode == 7:  # less than
                        if code[first_param] < code[second_param]:
                            code[third_param] = 1
                        else:
                            code[third_param] = 0
                        i += 4
                    elif opcode == 8:  # equals
                        if code[first_param] == code[second_param]:
                            code[third_param] = 1
                        else:
                            code[third_param] = 0
                        i += 4
                    else:
                        i += 1
                    # print(i, code)
            except Exception as e:
                print('except', e, i, code[i], value)
                return value
                # print(i, code)

                # print(code[i], i, length)
            # print(code)
            return value

        # @source : https://github.com/dan144/aoc-2019/blob/master/5.py because value
        # be careful with i += ?
        def ACS(A, B, C, D, E):
            # first step
            # first setting input_test
            o_a = process(text, A, 0)

            o_b = process(text, B, o_a)

            o_c = process(text, C, o_b)

            o_d = process(text, D, o_c)

            o_e = process(text, E, o_d)
            #o_e = process_2(D, o_d, text)
            return o_e, str(A)+str(B)+str(C)+str(D)+str(E)

        # get all combination between 0-4 with only one
        def is_i_unique(i):
            unique = []
            if len(str(i)) != 5:
                return False
            for j in str(i):
                # check if it is between 0-4
                if int(j) not in range(5):
                    return False
                else:
                    # check if it is unique
                    try:
                        test = unique.index(int(j))
                        return False
                    except:
                        unique.append(int(j))
            return True

        # 01234 or 31240 for example
        uniques = []
        for i in range(43210+1):
            if is_i_unique(i):
                uniques.append([int(j) for j in str(i)])
        outputs = []
        for i in uniques:
            outputs.append(ACS(*i))
        outputs = sorted(outputs, reverse=True)
        print(outputs[0][0])


if __name__ == '__main__':
    unittest.main()
