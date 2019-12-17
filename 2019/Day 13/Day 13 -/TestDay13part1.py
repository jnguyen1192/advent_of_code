import unittest
from parse import parse
import copy
from pprint import pprint


def input_file():
    # return the input file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class TestDay13part1(unittest.TestCase):

    def test_day_13_part_1(self):
        text = input_file()

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
                    elif opcode == 3:  # as input 3, 50 => 3 take input and save to address 50
                        debug = "input"
                        if phase:
                            code[first_param] = phase_setting
                            phase = False
                        else:
                            code[first_param] = value
                        i += 2
                    elif opcode == 4:  # as output 4, 50 => 4 output the value at address 50
                        debug = "output"
                        # print("as input 3, 50 => 3 take input and save to address 50")
                        i += 2
                        value = code[first_param]
                        return value, code, i#i, end, code, phase
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
                    elif opcode == 9:  # relative mode
                        rb += code[first_param]
                        i += 2
                    else:
                        i += 1
                    #print(i)
                    # print(i, code)
            except Exception as e:
                print(e)
                print(i, code[i-2:i+8], debug)
                return value, i, end, code, phase
            return value, code, i#, i, end, code, phase

        code = [int(val) for val in text.split(",")]

        input = 0
        i = 0
        sequence = []
        c = 1
        tiles = []
        while True:
            input, code, i = process(0, input, i, code, False)
            sequence.append(input)
            if c % 3 == 0:
                if input == 2:
                    tiles.append((sequence[-3], sequence[-2]))
            c += 1
            if code[i] == 99:
                break
        print(sequence)
        print(len(tiles))





if __name__ == '__main__':
    unittest.main()
