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
                    else:
                        first_param = self.i + 1
                    # case param 2
                    if int(str_opcode[1]) == 0:  # position
                        second_param = self.code[self.i + 2]
                    elif int(str_opcode[1]) == 2:  # relative
                        second_param = code[self.i + 2] + self.rb
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
                        tmp = self.code[first_param] + self.code[second_param]
                        self.code[third_param] = tmp
                        self.i += 4
                    elif opcode == 2:  # multiplication
                        # case param 3
                        tmp = self.code[first_param] * self.code[second_param]
                        self.code[third_param] = tmp
                        self.i += 4
                    elif opcode == 3:  # as input 3, 50 => 3 take input and save to address 50
                        if self.phase:
                            self.code[first_param] = phase_setting
                            self.phase = False
                        else:
                            self.code[first_param] = input
                        self.i += 2
                    elif opcode == 4:  # as output 4, 50 => 4 output the value at address 50
                        # print("as input 3, 50 => 3 take input and save to address 50")
                        self.i += 2
                        output = self.code[first_param]
                        break
                    elif opcode == 5:  # jump-if-true
                        if self.code[first_param] != 0:
                            self.i = self.code[second_param]
                        else:
                            self.i += 3
                    elif opcode == 6:  # jump-if-false
                        if self.code[first_param] == 0:
                            self.i = self.code[second_param]
                        else:
                            self.i += 3
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

        code = [int(val) for val in text.split(",")]
        nb_computers = 50
        computers = []
        i_value = 0
        First_computer = Intcode(code)
        print(First_computer.run(255))
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
