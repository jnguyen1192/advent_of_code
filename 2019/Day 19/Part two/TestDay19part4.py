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


class TestDay19part6(unittest.TestCase):

    def test_day_19_part_6(self):
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
                        debug = "addition " + str(third_param) + " " + str(first_param) + " + " + str(second_param) + " " \
                                + str(len(code)) + " " + str(third_param) + " " + str(len(code) - third_param)
                        if first_param > len(code):
                            code += [0] * (1 + first_param - len(code))
                        tmp = code[first_param] + code[second_param]
                        code[third_param] = tmp
                        i += 4
                    elif opcode == 2:  # multiplication
                        # case param 3
                        debug = "multiplication " + str(third_param) + " " + str(first_param) + " + " + str(second_param) + " " \
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
                        debug = "input_test" + str(first_param) + str(len(code))
                        if first_param >= len(code):
                            code += [0] * (1 + first_param - len(code))
                            debug += " " + str(len(code))
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

        def print_somethings(somethings, square_size, x, y):
            max_x = max([x for x, y in somethings])
            max_y = max([y for x, y in somethings])
            str_int = ""
            for j in range(max_y + 1):
                for i in range(max_x + 1):
                    if (i, j) == (x, y):
                        str_int += "O"
                    elif (i, j) in somethings:
                        str_int += "#"
                    else:
                        str_int += "."
                str_int += "\n"
            print(str_int)

        def is_something(x, y):
            #print("Is_something")

            code = [int(val) for val in text.split(",")]
            i = 0
            value, code, i = process(y, x, i, code, True)
            #value, code, i = process(0, y, i, code, False)
            #print(x, y, value)
            if value == 1:
                return True
            return False

        def get_current_size_square(somethings):
            # Get width current line
            somethings = sorted(somethings, key=lambda x: x[1])
            last_y = somethings[-1][1]
            #print(somethings[-2:])
            width_line = 0
            first_x = 10000000000000
            for something in somethings:
                if something[1] == last_y:
                    if something[0] < first_x:
                        first_x = something[0]
                    width_line += 1
            #print("width_line",width_line)
            # get the height of first x of last line
            square_size = 0
            for i in range(width_line):
                if (first_x + i, last_y - i) in somethings:
                    square_size += 1
                else:
                    break
            # TODO remove the somethings before last_y - square_size
            for something in somethings:
                if something[1] < last_y - square_size:
                    somethings.remove(something)
            return (first_x, last_y - square_size + 1), square_size, somethings

        def print_tractor_beam(y_range_max, x_range_max, square_size, y_range_min):
            c = 0
            somethings = []
            something_detected = False
            last_something_length = 0
            last_square_size = 0
            for y in range(y_range_min, y_range_max):
                #print(y)
                current_somethings = []
                x = last_something_length
                while True:
                    if is_something(x, y):
                        # Si c'est la premiere detection, on ajoute la largeur précédente des choses
                        if not something_detected:
                            for i in range(last_something_length):
                                if x >= x_range_max:
                                    break
                                somethings.append((x, y))
                                current_somethings.append((x, y))
                                x += 1
                                c += 1
                            something_detected = True
                            continue
                        # Sinon nous ajoutons les nouvelles choses
                        somethings.append((x, y))
                        current_somethings.append((x, y))
                        c += 1
                    # si il y a eu une detection et un nouveau point
                    elif something_detected or x == 1000:
                        x += 1
                        break
                    #print(y, x, something_detected, somethings)
                    x += 1

                # get length current somethings
                last_something_length = len(current_somethings) - 1
                something_detected = False
                # TODO check the current size of square
                (x_square, y_square), current_size_square, somethings = get_current_size_square(somethings)
                if last_square_size < current_size_square:
                    last_square_size = current_size_square
                    print((x_square, y_square), current_size_square, len(somethings))
                if current_size_square == square_size:
                    print((x_square, y_square), current_size_square)
                    break
            print_somethings(somethings, 10, x_square, y_square)
            #print(c)
            #print(len(somethings))
            #print(len(list(set(somethings))))
            #print(somethings)


        square_size = 100
        i = 0
        y_range_max = 10000
        x_range_max = 10000
        #print_tractor_beam(y_range_max, x_range_max, square_size, 0) # 9 s for 50, 50
        def get_first_x(y):
            x = 0
            while True:
                if is_something(x, y):
                    return x
                x += 1

        def get_diag_using(x, y):
            c = 0
            for j in range(10000):
                #print((first_x - j, y + j))
                if not is_something(x + j, y - j):
                    break
                c+= 1
            return c
        def get_less_x_y_using_random_y_and_goal(y, goal):
            y_less = y
            for i in range(10000):
                # reprend le first x en fonction de y
                new_y = y - i
                print(new_y)
                new_first_x = get_first_x(new_y)
                if get_diag_using(new_first_x, new_y) == goal:
                    y_less = new_y
                    x_less = new_first_x
                else:
                    break
            return (x_less, y_less - goal + 1)
        # TODO
        goal = 100

        # on commence au hasard
        y = 500

        # on recupere le premier x de la ligne 500
        def search_goal(y, goal=0, incr=500):
            first_x = get_first_x(y)
            # on calcul la diagonal a partir de y
            c = get_diag_using(first_x, y)
            print((get_first_x(y), y), c)
            if c == goal:
                # TODO get the min y
                (new_x, new_y) = get_less_x_y_using_random_y_and_goal(y, goal)
                print(c, (new_x, new_y))
                return (new_x, new_y)
            if c < goal:
                return search_goal(y + int(incr/2), goal, int(incr/2))
            else:
                return search_goal(y - int(incr/2), goal, int(incr/2))
        print(search_goal(y, 100))
            # en remontant vers le haut

        #









if __name__ == '__main__':
    unittest.main()
