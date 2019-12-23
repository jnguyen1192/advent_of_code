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


class TestDay23part1(unittest.TestCase):

    def test_day_23_part_1(self):
        text = input_file()

        def process(phase_setting, value, i, code, phase):
            length = len(code)
            rb = 0
            end = False
            debug = ""
            try:
                while i < length or code[i] != 99:
                    print(i)
                    # add mode on opcode
                    #print("i", i, length, code[i:i+10])
                    if code[i] == 99:
                        print("exit")
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
                        if third_param >= len(code):
                            code += [0] * (third_param + 1 - len(code))
                        tmp = code[first_param] + code[second_param]
                        code[third_param] = tmp
                        i += 4
                    elif opcode == 2:  # multiplication
                        # case param 3
                        debug = "multiplication"
                        tmp = code[first_param] * code[second_param]
                        if third_param >= len(code):
                            code += [0] * (third_param + 1 - len(code))
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
                        return value, i, code
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
                print("exception :", i, code[i-2:i+2], debug)
                return value, i, code

            return value, i, code

        code = [int(val) for val in text.split(",")]
        nb_computers = 50
        computers = []
        i_value = 0
        print(process(0, 0, i_value, code, False))
        """for i in range(nb_computers):
            current_value, current_code, current_i = process(0, i, i_value, code, False)
            computers.append((i, current_code, current_i))
            print("Computer", i, "added")
        print(computers)
        """
        # 50 computers with same "code"
        #print(process(0, 25, 0, code, False))
        # Computers from 0 to 49
        # Packet: X, Y
        # NIC: puzzle input ("code")
        # send: (destination_address, X, Y)
        # receive:  packet empty -> -1
        #           provide X value of next packet, receive another Y value for the same packet
        #           packet removed from the queue  after read











if __name__ == '__main__':
    unittest.main()
