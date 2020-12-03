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

from pprint import pprint
def get_nb_tree_encounter(lines):
    move_right = 3  # move 3 at right
    move_down = 1  # move 3 at bottom
    current_pos = (0, 0)  # start at the top-left
    nb_tree_encounter = 0
    width_pattern = len(lines[0])  # get width pattern
    height_pattern = len(lines)  # get height pattern
    pattern_multiplication = int(height_pattern / width_pattern)  +  (height_pattern % width_pattern > 0)# estimate pattern multiplication
    map = []  # initialize map
    for line in lines:  # get first pattern
        line_map = []
        for col in line:
            line_map.append(col)
        map.append(line_map)
    while current_pos[1] < height_pattern - 1:
        current_pos = ((current_pos[0] + move_right) % width_pattern, (current_pos[1] + move_down))
        #print(current_pos , height_pattern, len(map))
        if map[current_pos[1]][current_pos[0]] == "#":
            nb_tree_encounter += 1
    #pprint(map)


    # loop until the bottom is reached
    #  navigate on first pattern



    # move and counting until the bottom

    return nb_tree_encounter  # case it won't work


class TestDay3part2(unittest.TestCase):

    def test_day_3_part_2(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_tree_encounter(lines)  # process
        print(pred)  # print
        #assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
