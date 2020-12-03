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
    width_pattern = len(lines[0])  # get width pattern
    height_pattern = len(lines)  # get height pattern
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
                 (1, 2)]  # intialize moves to do

    # count tree
    def get_nb_tree_encounter_using_map_and_moves(map, move):  # function to use in first part
        current_pos = (0, 0)  # start at the top-left
        nb_tree_encounter = 0  # initialize the count
        while current_pos[1] < height_pattern - 1:  # browse until the end
            current_pos = ((current_pos[0] + move[0]) % width_pattern, (current_pos[1] + move[1])) # add a move
            if map[current_pos[1]][current_pos[0]] == "#":  # test if there was a tree
                nb_tree_encounter += 1  # add into the count
        return nb_tree_encounter  # return the nb of tree encounter

    nb_tree_encounter_product = 1  # initialize the count
    for move in move_list:  # for each moves in the move list
        nb_tree_encounter_product *= get_nb_tree_encounter_using_map_and_moves(map, move)  # get the number of tree encounter and multiply

    return nb_tree_encounter_product  # case it won't work


class TestDay3part2(unittest.TestCase):

    def test_day_3_part_2(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_tree_encounter_product(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
