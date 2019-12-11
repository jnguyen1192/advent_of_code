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


class TestDay11part1(unittest.TestCase):

    def test_day_11_part_1(self):
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

        def next_direction_using_output(output, cur_dir):
            directions = [(0, [("^", "<"), ("<", "v"), ("v", ">"), (">", "^")]), (1, [("^", ">"), (">", "v"), ("v", "<"), ("<", "^")])]
            for direction in directions:
                if direction[0] == output:
                    for dir in direction[1]:
                        if dir[0] == cur_dir:
                            return dir[1]

        def get_next_move_robot_forward_using_dir_and_pos(dir, pos):
            moves_forward = (("^", (0, -1)), ("<", (-1, 0)), ("v", (0, 1)), (">", (1, 0)))
            x, y = pos
            for move_forward in moves_forward:
                if dir == move_forward[0]:
                    x_incr, y_incr = move_forward[1]
                    return (x + x_incr, y + y_incr)

        def print_map(map, i):
            print("Iteration ", i)
            str_print = ""
            for i_l, l in enumerate(map):
                for i_el, el in enumerate(l):
                    str_print += map[i_l][i_el]
                str_print += "\n"
            print(str_print)

        code = [int(val) for val in text.split(",")]
        #print(process(0, 1, 0, code, False)[0])
        map = []
        y_range_max = 200
        x_range_max = 200
        y_beg_robot = int(y_range_max/2)
        x_beg_robot = int(x_range_max/2)
        for y in range(y_range_max):
            line = []
            for i in range(x_range_max):
                line.append('.')
            map.append(line)
        map[y_beg_robot][x_beg_robot] = "^"
        cur_robot_position = (x_beg_robot, y_beg_robot)
        nb_panel = set()
        trace_robot = [cur_robot_position]
        # first input 1 : white : #
        colors = [(0, '.', "black"), (1, '#', "white")]
        next_position = (0, 0)
        color_paint_on_cur_position = "."
        i = 1
        # color black : 0 at the beginning
        output = 0  # colors[0][0]
        # turn left : 0 at the begining
        cur_code = code.copy()
        i_code = 0

        while next_position != trace_robot[0] and i != 100000:
            print(len(cur_code))
            # use new color
            output, cur_code, i_code = process(0, output, i_code, cur_code.copy(), False)
            for color in colors:
                if color[0] == output:
                    # paint the current robot position to this color
                    color_paint_on_cur_position = color[1]

            # new direction
            x_cur, y_cur = cur_robot_position
            output, cur_code, i_code = process(0, output, i_code, cur_code.copy(), False)
            next_dir = next_direction_using_output(output, map[y_cur][x_cur])

            # stock position of paint
            nb_panel.add(cur_robot_position)
            #print(i, len(nb_panel), cur_robot_position)


            # new position
            cur_robot_position = get_next_move_robot_forward_using_dir_and_pos(next_dir, cur_robot_position)
            new_x_cur, new_y_cur = cur_robot_position


            #  new color
            output = map[new_y_cur][new_x_cur]
            print("output", output)
            # update map
            map[y_cur][x_cur] = color_paint_on_cur_position


            # update output using new color
            for color in colors:
                if color[1] == output:
                    # paint the current robot position to this color
                    output = color[0]

            map[new_y_cur][new_x_cur] = next_dir
            #print_map(map, i)
            # update position for loop
            next_position = cur_robot_position
            i += 1
        print_map(map, i)
        #print(trace_robot)
        # Never paint on the last panel
        print(len(nb_panel))
        #print(nb_panel)


if __name__ == '__main__':
    unittest.main()
