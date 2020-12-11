import unittest


def input_file(suffix):
    file = open('input_' + suffix, 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file(number):
    file = open('output_'+str(number), 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def get_differences(lines):
    adapters = []
    for line in lines:
        adapters.append(int(line))
    adapters.sort()
    #print(adapters)
    differences = {1: 1,
                   2: 1,
                   3: 1}
    for index, adapter in enumerate(adapters[:-1]):  # count difference
        #print(adapter, adapters[index + 1], abs(adapter - adapters[index + 1]))
        differences[abs(adapter - adapters[index + 1])] += 1
    return differences[1],  differences[3]


def get_seats_occupied(lines):

    def get_next_seat(x, y, x_incr, y_incr, old_map):
        i = 1
        while True:
            if not(0 <= y + y_incr * i < len(old_map) and 0 <= x + x_incr * i < len(old_map[0])):
                break
            if old_map[y + y_incr * i][x + x_incr * i] != ".":
                return old_map[y + y_incr * i][x + x_incr * i]

            i += 1
        return "."

    def get_nb_adjacent_part_2(x, y, old_map, occupied):
        nb_adjacent = 0
        if y + 1 < len(old_map):
            if get_next_seat(x, y, 0, 1, old_map) == occupied:  # bas old_map[y + 1][x]
                nb_adjacent += 1
        if y + 1 < len(old_map) and x - 1 >= 0:
            if get_next_seat(x, y, -1, 1, old_map) == occupied:  # bas gauche old_map[y + 1][x - 1]
                nb_adjacent += 1
        if x - 1 >= 0:
            if get_next_seat(x, y, -1, 0, old_map) == occupied:  # gauche old_map[y][x - 1]
                nb_adjacent += 1
        if y - 1 >= 0:
            if get_next_seat(x, y, 0, -1, old_map) == occupied:  # haut old_map[y - 1][x]
                nb_adjacent += 1
        if y + 1 < len(old_map) and x + 1 < len(old_map[0]):
            if get_next_seat(x, y, 1, 1, old_map) == occupied:  # bas droite old_map[y + 1][x + 1]
                nb_adjacent += 1

        if x + 1 < len(old_map[0]):
            if get_next_seat(x, y, 1, 0, old_map) == '#':  # droite old_map[y][x + 1]
                nb_adjacent += 1

        if y - 1 >= 0:
            if x - 1 >= 0:
                if get_next_seat(x, y, -1, -1, old_map) == '#':  # haut gauche old_map[y - 1][x - 1]
                    nb_adjacent += 1
            if x + 1 < len(old_map[0]):
                if get_next_seat(x, y, 1, -1, old_map) == '#':  # haut droite old_map[y - 1][x + 1]
                    nb_adjacent += 1
        return nb_adjacent

    def get_nb_adjacent_part_1(x, y, old_map, occupied):
        nb_adjacent = 0
        if y + 1 < len(old_map):
            if old_map[y + 1][x] == occupied:  # bas
                nb_adjacent += 1
        if y + 1 < len(old_map) and x - 1 >= 0:
            if old_map[y + 1][x - 1] == occupied:  # bas gauche
                nb_adjacent += 1
        if x - 1 >= 0:
            if old_map[y][x - 1] == occupied:  # gauche
                nb_adjacent += 1
        if y - 1 >= 0:
            if old_map[y - 1][x] == occupied:  # haut
                nb_adjacent += 1
        if y + 1 < len(old_map) and x + 1 < len(old_map[0]):
            if old_map[y + 1][x + 1] == occupied:  # bas droite
                nb_adjacent += 1

        if x + 1 < len(old_map[0]):
            if old_map[y][x + 1] == '#':  # droite
                nb_adjacent += 1

        if y - 1 >= 0:
            if x - 1 >= 0:
                if old_map[y - 1][x - 1] == '#':  # haut gauche
                    nb_adjacent += 1
            if x + 1 < len(old_map[0]):
                if old_map[y - 1][x + 1] == '#':  # haut droite
                    nb_adjacent += 1
        return nb_adjacent

    old_map = lines.copy()
    new_map = [line.replace("#", ".").replace("L", ".")for line in lines]
    first_loop = True
    i = 0
    while old_map != new_map:
        i += 1
        if not first_loop:
            old_map = new_map.copy()
        else:
            new_map = old_map.copy()
            first_loop = False
        for y, line in enumerate(old_map):
            for x, column in enumerate(new_map):
                if old_map[y][x] == "L":  # If a seat is empty
                    if get_nb_adjacent_part_2(x, y, old_map, "#") == 0:  # no occupied seats adjacent to it
                        new_map[y] = new_map[y][:x] + '#' + new_map[y][x + 1:]  # the seat becomes occupied
                elif old_map[y][x] == "#":  # If a seat is occupied
                    if get_nb_adjacent_part_2(x, y, old_map, "#") >= 5:# 4: part1 # four or more seats adjacent to it
                        new_map[y] = new_map[y][:x] + 'L' + new_map[y][x + 1:]  # the seat becomes empty

    return sum([1 for line in new_map for char in line if char == "#"])  #  "OK"


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file(1)  # get output_1
        #res = output_file("test_1")  # get output_1
        pred = get_seats_occupied(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        pred = get_seats_occupied(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
