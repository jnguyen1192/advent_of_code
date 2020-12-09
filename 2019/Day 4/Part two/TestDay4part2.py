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


def day_4_part_1(text):
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

class TestDay4part1(unittest.TestCase):

    def test_day_4_part_1(self):
        text = input_file()
        #res = output_file()
        #pred = day_2_part_1(text)
        # data preparation
        range_ = [int(t) for t in text.split("-")]
        print(range)
        def is_criteria(pwd):
            str_pwd = str(pwd)
            if len(str_pwd) != 6:
                return False
            # two adjacents digits are the same
            try:
                for i_d, d in enumerate(str_pwd):
                    if str_pwd[i_d] == str_pwd[i_d + 1]:
                        break
            except:
                return False
            # never decrease
            for i_d, d in enumerate(str_pwd):
                if i_d + 1 < len(str_pwd):
                    if str_pwd[i_d] > str_pwd[i_d + 1]:
                        return False
            return True
        diff_pwd = 0
        for i in range(range_[0], range_[1]):
            if is_criteria(i):
                diff_pwd += 1
        print(diff_pwd)








        #code = [int(val) for val in text.split(",")]
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
