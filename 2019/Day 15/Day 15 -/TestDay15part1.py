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


class TestDay15part1(unittest.TestCase):

    def test_day_15_part_1(self):
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

        def print_map(walls, possible_move, begin_pos, oxygen_pos):
            # print the map
            # get min_x and min_ y
            min_x = 100000000
            min_y = 100000000
            max_x = 0
            max_y = 0
            for x, y in walls:
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > min_y:
                    max_y = y
            for x, y in possible_move:
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > min_y:
                    max_y = y
            if oxygen_pos != None:
                o_x, o_y = oxygen_pos
                if o_x < min_x:
                    min_x = o_x
                if o_y < min_y:
                    min_y = o_y
                if o_x > max_x:
                    max_x = o_x
                if o_y > min_y:
                    max_y = o_y
            #print("min", min_y, min_x)
            # normalize the coords
            #print("walls", walls)
            #print("possible_move", possible_move)
            new_walls = []
            for i_, coord in enumerate(walls):
                x, y = coord
                new_walls.append((x - min_x, y - min_y))
            #print("new walls", new_walls)
            new_possible_move = []
            for i_, coord in enumerate(possible_move):
                x, y = coord
                new_possible_move.append((x - min_x, y - min_y))
            #print("new_possible_move", new_possible_move)
            x, y = begin_pos
            new_begin_pos = (x - min_x, y - min_y)
            if oxygen_pos != None:
                x, y = oxygen_pos
                new_oxygen_pos = (x - min_x, y - min_y)
            map = []
            # create the map
            for j in range(max_y + 2 - min_y):
                line = []
                for i in range(max_x + 2 - min_x):
                    line.append(" ")
                map.append(line)
            #print(map)
            # update the map
            # add walls
            #print("walls", walls)
            for x, y in new_walls:
                #print("coord", y, x)
                #print("map", len(map), len(map[0]))
                map[y][x] = "#"
            # add_possible_move
            for x, y in new_possible_move:
                map[y][x] = "."
            # add begin_pos
            x, y = new_begin_pos
            map[y][x] = "D"
            # add oxygen_pos
            if oxygen_pos != None:
                x, y = new_oxygen_pos
                map[y][x] = "O"
            # print the empty map
            map_str = ""
            for i_j, j in enumerate(map):
                for i_i, i in enumerate(j):
                    map_str += map[i_j][i_i]
                map_str += "\n"
            print(map_str)

        code = [int(val) for val in text.split(",")]
        # output
        # 0 nothing
        # 1 move
        # 2 end
        # input
        # 1 north
        # 2 south
        # 3 west
        # 4 east
        #manhanttan distance to know the beginning and the end

        i = 0
        output_ = -1
        input_ = 1  # north beginning
        begin_pos = (0, 0)
        current_pos = begin_pos
        oxygen_pos = None
        possible_move = []
        walls = []
        while output_ != 2:
            i = 0
            print(i, input_, output_, code[i:i + 5])
            output_, code, i = process(0, input_, i, code, False)
            cur_x, cur_y = current_pos
            if input_ == 1:
                new_pos = (cur_x, cur_y - 1)
            elif input_ == 2:
                new_pos = (cur_x, cur_y + 1)
            elif input_ == 3:
                new_pos = (cur_x - 1, cur_y)
            elif input_ == 4:
                new_pos = (cur_x + 1, cur_y)
            else:
                print(input_)
                print("Error wrong input")
            if output_ == 0:
                walls.append(new_pos)
                input_ = (input_ % 4) + 1
            elif output_ == 1:
                current_pos = new_pos
                possible_move.append(new_pos)
            elif output_ == 2:
                # TODO end
                oxygen_pos = new_pos
                print("End on position ", new_pos)
            else:
                print(output_)
                print("Error wrong output")
            print_map(walls, possible_move, begin_pos, oxygen_pos)








if __name__ == '__main__':
    unittest.main()
