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


class TestDay25part1(unittest.TestCase):

    def test_day_25_part_1(self):
        text = input_file()


        class Intcode:
            def __init__(self, code, i=0, phase=False, rb=0):
                self.code = code + [0] * 100000
                self.i = i
                self.phase = phase
                self.rb = rb

            def run(self, input, phase_setting=None, output=None):
                if phase_setting is not None:
                    self.phase = True
                while True:
                    #print(self.i, self.code[self.i])
                    if self.code[self.i] == 99:
                        break
                    str_opcode = str(self.code[self.i])
                    while len(str_opcode) < 5:
                        str_opcode = "0" + str_opcode
                    opcode = int(str_opcode[3:])

                    # add pos, imm and rela
                    # case param 1
                    if int(str_opcode[2]) == 0:  # position
                        first_param = self.code[self.i + 1]
                    elif int(str_opcode[2]) == 2:  # relative
                        first_param = self.code[self.i + 1] + self.rb
                        #print("Relative case", first_param, self.rb)
                    else:
                        first_param = self.i + 1
                    # case param 2
                    if int(str_opcode[1]) == 0:  # position
                        second_param = self.code[self.i + 2]
                    elif int(str_opcode[1]) == 2:  # relative
                        second_param = self.code[self.i + 2] + self.rb
                    else:
                        second_param = self.i + 2
                    # case param 3
                    if int(str_opcode[0]) == 0:  # position
                        third_param = self.code[self.i + 3]
                    elif int(str_opcode[0]) == 2:  # relative
                        third_param = self.code[self.i + 3] + self.rb
                    else:
                        third_param = self.i + 3

                    if opcode == 1:  # addition
                        self.code[third_param] = self.code[first_param] + self.code[second_param]
                        self.i += 4
                    elif opcode == 2:  # multiplication
                        self.code[third_param] = self.code[first_param] * self.code[second_param]
                        self.i += 4
                    elif opcode == 3:  # as input 3, 50 => 3 take input and save to address 50
                        if self.phase:
                            self.code[first_param] = phase_setting
                            self.phase = False
                        else:
                            #print("Input case", self.i, self.code[first_param], input, first_param)
                            self.code[first_param] = input
                        self.i += 2
                    elif opcode == 4:  # as output 4, 50 => 4 output the value at address 50
                        # print("as input 3, 50 => 3 take input and save to address 50")
                        self.i += 2
                        output = self.code[first_param]
                        return output
                    elif opcode == 5:  # jump-if-true
                        if self.code[first_param]:
                            self.i = self.code[second_param]
                        else:
                            self.i += 3
                    elif opcode == 6:  # jump-if-false
                        if self.code[first_param]:
                            self.i += 3
                        else:
                            self.i = self.code[second_param]
                    elif opcode == 7:  # less than
                        if self.code[first_param] < self.code[second_param]:
                            self.code[third_param] = 1
                        else:
                            self.code[third_param] = 0
                        self.i += 4
                    elif opcode == 8:  # equals
                        if self.code[first_param] == self.code[second_param]:
                            self.code[third_param] = 1
                        else:
                            self.code[third_param] = 0
                        self.i += 4
                    elif opcode == 9:  # relative mode
                        self.rb += self.code[first_param]
                        self.i += 2
                    else:
                        self.i += 1
                return output

        def run_command(ic, command):
            inputs = [ord(c) for c in command]
            #print(command, inputs)
            outputs = []
            for input_ in inputs:
                #print("Before output", input_, chr(input_))
                output = ic.run(input_)
                #print(output)
                outputs.append(output)

            str_ascii = ""
            str_ascii += ''.join(chr(i) for i in outputs)
            print(str_ascii)

        def get_map_using_ascii_program(code):
            str_ascii = ""
            value = 0
            ascii_program = []
            map = []
            ic = Intcode(code)
            while True:
                if str_ascii == "Command?":
                    run_command(ic, "south\n")
                    continue
                else:
                    value = ic.run(value)
                #print(value)
                #print(process(0, 0, 0, code, False))
                if value != 10:
                    ascii_program.append(value)
                if value == 10:
                    #print(ascii_program)
                    # transform ascii to letter
                    str_ascii = ""
                    str_ascii += ''.join(chr(i) for i in ascii_program)
                    print("Current str_ascii", str_ascii)
                    map.append(ascii_program)
                    ascii_program = []
        code = [int(val) for val in text.split(",")]
        print(get_map_using_ascii_program(code))





if __name__ == '__main__':
    unittest.main()
