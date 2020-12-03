import unittest
from collections import Counter


def input_file():
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def get_nb_tree_encounter_product(lines):
    move_right = 3  # move 3 at right
    move_down = 1  # move 3 at bottom
    width_pattern = len(lines[0])  # get width pattern
    height_pattern = len(lines)  # get height pattern
    pattern_multiplication = int(height_pattern / width_pattern)  +  (height_pattern % width_pattern > 0)# estimate pattern multiplication
    map = []  # initialize map
    for line in lines:  # get first pattern
        line_map = []  # init line
        for col in line:  #  for each column
            line_map.append(col)  # add a tree or an open path
        map.append(line_map)  # add a line in the map

    move_list = [(1, 1),
                 (3, 1),
                 (5, 1),
                 (7, 1),
                 (1, 2)]

    # count tree
    def get_nb_tree_encounter_using_map_and_moves(map, move):
        current_pos = (0, 0)  # start at the top-left
        nb_tree_encounter = 0  # initialize the count
        while current_pos[1] < height_pattern - 1:  # browse until the end
            current_pos = ((current_pos[0] + move[0]) % width_pattern, (current_pos[1] + move[1]))
            if map[current_pos[1]][current_pos[0]] == "#":
                nb_tree_encounter += 1
        return nb_tree_encounter
    nb_tree_encounter_product = 1  # initialize the count
    for move in move_list:
        nb_tree_encounter_product *= get_nb_tree_encounter_using_map_and_moves(map, move)

    return nb_tree_encounter_product  # case it won't work


class TestDay3part2(unittest.TestCase):

    def test_day_3_part_2(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_tree_encounter_product(lines)  # process
        print(pred)  # print
        #assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
