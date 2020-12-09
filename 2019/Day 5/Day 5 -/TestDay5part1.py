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


def day_5_part_1(text):
    raw_events = sorted(tuple(parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", l)) for l in text.split('\n')) # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py

    return raw_events


def work_way(lines):
    # data transformation
    # max R, L, U, D
    def get_max(card, line):
        max = 0
        for line in lines:
            cur_max = 0
            for i in line:
                if i[0] == card:
                    cur_max += i[1]
            if cur_max > max:
                max = cur_max
        return max

    # we found that it will be a matrix like the example
    R_max = get_max("R", lines)
    L_max = get_max("L", lines)
    U_max = get_max("U", lines)
    D_max = get_max("D", lines)
    # we build the matrix
    width = R_max + L_max + 1
    height = U_max + D_max + 1
    o_point = (D_max, L_max)
    print("width", width)
    print("height", height)
    print("Build begin")
    matrix = []
    for i in range(height):
        line = []
        for j in range(width):
            if (i, j) == o_point:
                line.append(2)
            else:
                line.append(0)
        matrix.append(line)
    print("Build end")

    # move function
    def move(cur_pos, the_move, matrix):
        if the_move[0] == "R":
            for i in range(the_move[1]):
                matrix[cur_pos[0]][cur_pos[1] + i] += 1
            return cur_pos[0], cur_pos[1] + the_move[1]
        if the_move[0] == "L":
            for i in range(the_move[1]):
                matrix[cur_pos[0]][cur_pos[1] - i] += 1
            return cur_pos[0], cur_pos[1] - the_move[1]
        if the_move[0] == "U":
            for i in range(the_move[1]):
                matrix[cur_pos[0] + i][cur_pos[1]] += 1
            return cur_pos[0] + the_move[1], cur_pos[1]
        if the_move[0] == "D":
            for i in range(the_move[1]):
                matrix[cur_pos[0] - i][cur_pos[1]] += 1
            return cur_pos[0] - the_move[1], cur_pos[1]

    # we add the first line one the matrix
    move_line_1 = o_point
    for the_move in lines[0]:
        move_line_1 = move(move_line_1, the_move, matrix)
    # we add the second line on the matrix
    move_line_2 = o_point
    for the_move in lines[1]:
        move_line_2 = move(move_line_2, the_move, matrix)

    # data encoding
    intersec = []
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 2:
                intersec.append((i, j))
                matrix[i][j] = "x"
            elif matrix[i][j] == 4:
                matrix[i][j] = "o"
            else:
                matrix[i][j] = " "

    # data modeling
    # find the min of distance to 'o'
    def md(o, p):
        return abs(o[1] - p[1]) + abs(o[0] - p[0])

    md_inter = [md(o_point, p) for p in intersec]
    print(min(md_inter))


# data visualisation
# for line in matrix[::-1]:
#    print(line)

class TestDay5part1(unittest.TestCase):

    def test_day_5_part_1(self):
        text = input_file()
        #res = output_file()
        #pred = day_2_part_1(text)

        def process(text, value):
            i = 0
            code = [int(val) for val in text.split(",")]
            #print(code)
            #code[1] = noun
            #code[2] = verb
            length = len(code)
            first_param = 0
            second_param = 0
            try:
                while i < length:
                    # TODO add mode on opcode
                    # add 0 at the beginning of 1
                    tmp_cur = code[i]
                    str_opcode = str(tmp_cur)
                    while len(str_opcode) < 5:
                        str_opcode = "0" + str_opcode
                    opcode = int(str_opcode[3:])
                    # TODO add pos and imm
                    if opcode == 1 or opcode == 2:
                        # case param 1
                        if int(str_opcode[2]) == 0:  # position
                            first_param = code[code[i + 1]]
                        else:
                            first_param = code[i + 1]
                        # case param 2
                        if int(str_opcode[1]) == 0:  # position
                            second_param = code[code[i + 2]]
                        else:
                            second_param = code[i + 2]
                    if opcode == 1:  # addition
                        # case param 3
                        if int(str_opcode[0]) == 0:  # position
                            code[code[i + 3]] = first_param + second_param
                        else:
                            code[i + 3] = first_param + second_param
                        i += 3
                    elif opcode == 2:  # multiplication
                        # case param 3
                        if int(str_opcode[0]) == 0:  # position
                            code[code[i + 3]] = first_param * second_param
                        else:
                            code[i + 3] = first_param * second_param
                        i += 3
                    # TODO code 3 and code 4
                    elif opcode == 3:  # as input_test 3, 50 => 3 take input_test and save to address 50
                        code[code[i + 1]] = value
                        i += 1
                    elif opcode == 4:  # as output_1 4, 50 => 4 output_1 the value at address 50
                        code[i + 1] = code[code[i + 1]]
                        #print("as input_test 3, 50 => 3 take input_test and save to address 50")
                        i += 1
                    elif code[i] == 99:
                        break
                    i += 1
                    #print(i, code)
            except:
                return -1
                #print(i, code)

                #print(code[i], i, length)
            #print(code)
            return code[i-1]


        # @source : https://github.com/dan144/aoc-2019/blob/master/5.py because value
        print(process(text, 1))


if __name__ == '__main__':
    unittest.main()
