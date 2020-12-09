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


class TestDay13part2(unittest.TestCase):

    def test_day_13_part_2(self):
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

        def print_game(game):
            str_game = ""
            for y, line in enumerate(game):
                for x, column in enumerate(line):
                    str_game += str(game[y][x])
                str_game += "\n"
            print(str_game, flush=True)

        code = [int(val) for val in text.split(",")]

        def joystick_position(sequence):
            if len(sequence) == 0:
                return 0
            c = 1
            ball = (0, 0)
            paddle = (0, 0)
            while c < len(sequence):
                if c % 3 == 0:
                    x, y, o = sequence[i:i + 3]
                    if o == 4:
                        ball = (x, y)
                    if o == 3:
                        paddle = (x, y)
            if paddle[0] == ball[0]:
                return 0
            elif paddle[0] > ball[0]:
                return -1
            else:
                return 1

        def game_state(new_input, code, i):
            input = new_input
            sequence = []
            y_max = 30
            x_max = 40
            game = []
            for line in range(y_max+1):
                new_line = []
                for column in range(x_max+1):
                    new_line.append(" ")
                game.append(new_line)
            c = 1
            while True:
                input, code, i = process(0, input, i, code, False)
                sequence.append(input)
                if len(sequence) > 3 and sequence[-3] == -1 and sequence[-2] == 0:
                    current_score = sequence[-1]
                    print("current_score", current_score)
                if c % 3 == 0:
                    x, y, o = sequence[-3:]
                    if o == 0:
                        game[y][x] = " "
                    elif o == 1:
                        game[y][x] = "w"
                    elif o == 2:
                        game[y][x] = "b"
                    elif o == 3:
                        game[y][x] = "_"
                    elif o == 4:
                        game[y][x] = "o"
                    else:
                        game[y][x] = o
                #print(i, code[i], current_score)
                c += 1
                if code[i] == 99:
                    print_game(game)
                    break
            return code, i + 1, sequence



        code[0] = 1
        i = 0
        sequence = []
        while True:
            code, i, sequence = game_state(joystick_position(sequence), code, i)
            print("New state")





if __name__ == '__main__':
    unittest.main()
