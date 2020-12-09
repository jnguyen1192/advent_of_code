import unittest
from parse import parse
import copy
from pprint import pprint


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


class TestDay17part1(unittest.TestCase):

    def test_day_17_part_1(self):
        text = input_file()

        TILE = 35
        POINT = 46

        def process(phase_setting, value, i, code, phase):
            length = len(code)
            rb = 0
            end = False
            debug = ""
            try:
                while i < length:
                    # add mode on opcode
                    if code[i] == 99:
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
                    elif int(str_opcode[2]) == 2:  # relative
                        #print("relative mode", str(i + 1 + rb))
                        if i + 2 + rb > length and code[i] != 4:
                            code += [0] * (code[i + 1] + rb - len(code))
                        #debug = "here " + str(i + 1 + rb) + " " + str(len(code))
                        first_param = code[i + 1] + rb
                    else:
                        first_param = i + 1
                    debug = "first param " + str(first_param)
                    # case param 2
                    if int(str_opcode[1]) == 0:  # position
                        second_param = code[i + 2]
                    elif int(str_opcode[1]) == 2:  # relative
                        #print("relative mode")
                        second_param = code[i + 2] + rb
                    else:
                        second_param = i + 2

                    debug = "second param " + str(second_param)
                    # case param 2
                    if int(str_opcode[0]) == 0:  # position
                        try:
                            third_param = code[i + 3]
                        except:
                            third_param = 0
                        debug = " third param " + str(third_param)
                        debug += "\ncode[i] " + str(code[i])
                        # TODO dynamic list extension here
                        if third_param > length and code[i] != 4:
                            code += [0] * (third_param - len(code))
                    elif int(str_opcode[0]) == 2:  # relative
                        third_param = code[i + 3] + rb
                    else:
                        third_param = i + 3

                    debug = "after params " + str(third_param) + " " + str(first_param) + " + " + str(second_param)

                    if opcode == 1:  # addition
                        # case param 3
                        debug = "addition " + str(third_param) + " " + str(first_param) + " + " + str(second_param) + " "\
                                + str(len(code)) + " " + str(third_param) + " " + str(len(code) - third_param)
                        if first_param > len(code):
                            code += [0] * (1 + first_param - len(code))
                        tmp = code[first_param] + code[second_param]
                        code[third_param] = tmp
                        i += 4
                    elif opcode == 2:  # multiplication
                        # case param 3
                        debug = "multiplication " + str(third_param) + " " + str(first_param) + " + " + str(second_param) + " "\
                                + str(len(code)) + " " + str(len(code) - third_param)
                        if first_param >= len(code):
                            code += [0] * (1 + first_param - len(code))
                            debug += " " + str(len(code))
                        if third_param >= len(code):
                            code += [0] * (1 + third_param - len(code))
                            debug += " " + str(len(code))
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
                        return value, code, i#i, end, code, phase
                    elif opcode == 5:  # jump-if-true
                        debug = "j true " + str(first_param) + " " + str(second_param)
                        if first_param >= len(code):
                            code += [0] * (1 + first_param - len(code))
                            debug += " " + str(len(code))
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
                    elif opcode == 9:  # relative mode
                        rb += code[first_param]
                        i += 2
                    else:
                        i += 1
                    #print(i)
                    # print(i, code)
            except Exception as e:
                print(e)
                print(i, code[i:i+8], debug)
                return value, i, end, code, phase
            return value, code, i#, i, end, code, phase

        def get_map_using_ascii_program(code):
            i = 0
            value = 0
            ascii_program = []
            map = []
            while True:
                value, code, i = process(0, value, i, code, False)
                #print(process(0, 0, 0, code, False))
                if value != 10:
                    ascii_program.append(value)
                #print(i, value, code[i:i+5], code[code[i+3]])
                if len(ascii_program) == 0 and value == 10:
                    break
                if value == 10:
                    #print(ascii_program)
                    # transform ascii to letter
                    str_ascii = ""
                    for ascii in ascii_program:
                        if ascii == 35:
                            str_ascii += "#"
                        elif ascii == 46:
                            str_ascii += "."
                    print(str_ascii)
                    map.append(ascii_program)
                    ascii_program = []
            return map
        code = [int(val) for val in text.split(",")]
        map = get_map_using_ascii_program(code)

        sum = 0
        # get intersection
        for i_line, line in enumerate(map):
            print("line", line)
            for i_column, column in enumerate(line):
                try:
                    if map[i_line][i_column] == TILE and \
                            map[i_line + 1][i_column] == TILE and \
                            map[i_line][i_column + 1] == TILE and \
                            map[i_line - 1][i_column] == TILE and \
                            map[i_line][i_column - 1] == TILE:
                        print("hello")
                        sum += i_line * i_column
                except:
                    # out of range : border case
                    print("border")
        print("sum", sum)
        # 35 means #, 46 means ., 10 starts a new line of output_1 below the current one, and so on. (Within a line, characters are drawn left-to-right.)

        # # represents a scaffold and . represents open space.
        # The vacuum robot is visible as ^, v, <, or > depending on whether it is facing up, down, left, or right respectively.
        # When drawn like this, the vacuum robot is always on a scaffold;
        # if the vacuum robot ever walks off of a scaffold and begins tumbling through space uncontrollably, it will instead be visible as X

        # detect intersection O










if __name__ == '__main__':
    unittest.main()
