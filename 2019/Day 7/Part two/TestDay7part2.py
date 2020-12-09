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


class TestDay7part2(unittest.TestCase):
    def test_day_7_part_2(self):
        text = input_file()

        def process(phase_setting, value, i, code, phase):
            length = len(code)
            end = False
            debug = ""
            try:
                while i < length:
                    # add mode on opcode

                    if code[i] == 99:
                        #print("exit")
                        end = True
                        break
                    debug = "before cast " + str(i) + " " + str(code[i]) + " " + str(len(code))
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
                        try:
                            third_param = code[i + 3]
                        except:
                            third_param = 0
                    else:
                        third_param = i + 3

                    debug = "after params " + str(third_param) + " " + str(first_param) + " + " + str(second_param)

                    if opcode == 1:  # addition
                        # case param 3
                        debug = "addition " + str(third_param) + " " + str(first_param) + " + " + str(second_param)
                        tmp = code[first_param] + code[second_param]
                        code[third_param] = tmp
                        i += 4
                    elif opcode == 2:  # multiplication
                        # case param 3
                        debug = "multiplication"
                        tmp = code[first_param] * code[second_param]
                        code[third_param] = tmp
                        i += 4
                    # TODO code 3 and code 4
                    elif opcode == 3:  # as input_test 3, 50 => 3 take input_test and save to address 50
                        debug = "input_test"
                        if phase:
                            code[first_param] = phase_setting
                            phase = False
                        else:
                            code[first_param] = value
                        i += 2
                    elif opcode == 4:  # as output_1 4, 50 => 4 output_1 the value at address 50
                        debug = "output_1"
                        # print("as input_test 3, 50 => 3 take input_test and save to address 50")
                        i += 2
                        value = code[first_param]
                        return value, i, end, code, phase
                    elif opcode == 5:  # jump-if-true
                        debug = "j true"
                        if code[first_param] != 0:
                            i = code[second_param]
                        else:
                            i += 3
                    elif opcode == 6:  # jump-if-false
                        debug = "j false"
                        if code[first_param] == 0:
                            i = code[second_param]
                        else:
                            i += 3
                    elif opcode == 7:  # less than
                        debug = "less"
                        if code[first_param] < code[second_param]:
                            code[third_param] = 1
                        else:
                            code[third_param] = 0
                        i += 4
                    elif opcode == 8:  # equals
                        debug = "equals"
                        if code[first_param] == code[second_param]:
                            code[third_param] = 1
                        else:
                            code[third_param] = 0
                        i += 4
                    else:
                        i += 1
                    #print(i)
                    # print(i, code)
            except Exception as e:
                print(e)
                print(i, code[i-2:i+2], debug)
                return value, i, end, code, phase

            return value, i, end, code, phase

        # @source : https://github.com/dan144/aoc-2019/blob/master/5.py because value
        # be careful with i += ?
        def ACS(A, B, C, D, E):
            # Initiate feedback_loop
            end_a, end_b, end_c, end_d, end_e = (False, False, False, False, False)
            i_a, i_b, i_c, i_d, i_e = (0, 0, 0, 0, 0)  # inputs
            o_a, o_b, o_c, o_d, o_e = (0, 0, 0, 0, 0)  # ouputs
            p_a, p_b, p_c, p_d, p_e = (True, True, True, True, True)  # phase_setting
            code = [int(val) for val in text.split(",")]
            c_a, c_b, c_c, c_d, c_e = (code.copy(), code.copy(), code.copy(), code.copy(), code.copy())  # codes

            # add feedback_loop here
            while True:
                #print(c_a, c_b, c_c, c_d, c_e)
                #print(end_a, end_b, end_c, end_d, end_e)
                if not end_a:
                    o_a, i_a, end_a, c_a, p_a = process(A, o_e, i_a, c_a, p_a)
                    #print(c_a)

                if not end_b:
                    o_b, i_b, end_b, c_b, p_b = process(B, o_a, i_b, c_b, p_b)
                #print(end_b)

                if not end_c:
                    o_c, i_c, end_c, c_c, p_c = process(C, o_b, i_c, c_c, p_c)
                    #   print(end_c)

                if not end_d:
                    o_d, i_d, end_d, c_d, p_d = process(D, o_c, i_d, c_d, p_d)

                if not end_e:
                    #print(c_e[i_e], i_e)
                    o_e, i_e, end_e, c_e, p_e = process(E, o_d, i_e, c_e, p_e)
                    #print(o_a, o_b, o_c, o_d, o_e)
                else:
                    break

            return o_e, str(A)+str(B)+str(C)+str(D)+str(E)

        # get all combination between 0-4 with only one
        def is_i_unique(i):
            unique = []
            if len(str(i)) != 5:
                return False
            for j in str(i):
                # check if it is between 0-4
                if int(j) not in range(5, 10):
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
        for i in range(98765+1):
            if is_i_unique(i):
                uniques.append([int(j) for j in str(i)])
        outputs = []

        for i_i, i in enumerate(uniques):
            outputs.append(ACS(*i))
        outputs = sorted(outputs, reverse=True)
        print(outputs[0][0])


if __name__ == '__main__':
    unittest.main()
