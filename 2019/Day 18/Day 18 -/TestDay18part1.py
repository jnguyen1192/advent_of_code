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


class TestDay18part1(unittest.TestCase):

    def test_day_18_part_1(self):
        text = input_file()

        lines = text.split("\n")
        alphabet = "abdefghijklmopqrstuvwxyz"
        def get_object_pos(lines):
            begin = (0, 0) #  (x, y)
            keys = []
            doors = []
            walls = []
            points = []
            for i_line, line in enumerate(lines):
                for i_column, column in enumerate(line):
                    if column == "@":
                        begin = (i_column, i_line)
                    elif column == "#":
                        walls.append((i_column, i_line))
                    elif column == ".":
                        points.append((i_column, i_line))
                    else:
                        if column.islower():
                            keys.append((column, (i_column, i_line)))
                            points.append((i_column, i_line))
                        else:
                            doors.append((column, (i_column, i_line)))
            keys = sorted(keys)
            doors = sorted(doors)
            return begin, keys, doors, points
        begin, keys, doors, points = get_object_pos(lines)

        def get_next_move(begin, points, previous_moves=[], nb_move=0):
            # look around begin
            next_moves = []
            x, y = begin
            cards = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
            for pos in cards:
                if pos in points and pos not in previous_moves:
                    next_moves.append(pos)
            previous_moves.append(begin)
            return next_moves, previous_moves, nb_move + 1

        def pos_is_in_keys(pos, keys):
            # key[0] = 'a'
            # key[1] = (x, y)
            for key in keys:
                if key[1] == pos:
                    return True
            return False

        def get_key_in_pos(pos, keys):
            # key[0] = 'a'
            # key[1] = (x, y)
            for key in keys:
                if key[1] == pos:
                    return key
            return None

        def get_adjacent_keys(begin, keys, nb_move):
            x, y = begin
            adjacent_keys = []
            cards = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
            for pos in cards:
                if pos_is_in_keys(pos, keys):
                    key = get_key_in_pos(pos, keys)
                    adjacent_key = (key[0], nb_move, key[1])
                    adjacent_keys.append(adjacent_key)
            return adjacent_keys

        def get_next_possible_keys(begin, points, keys):
            possible_keys = [] #  ('a', nb_move, (x, y))
            next_moves = [begin]
            previous_moves = []
            nb_move = 0
            while len(next_moves) != 0:
                for begin in next_moves:
                    # get adjacent keys
                    possible_keys += get_adjacent_keys(begin, keys, nb_move)
                    # first get_next_move
                    current_next_moves, current_previous_moves, nb_move = get_next_move(begin, points, previous_moves, nb_move)
                    next_moves += current_next_moves
                    previous_moves += current_previous_moves
                    print("possible_keys", possible_keys)
                    print("next_moves", next_moves, nb_move)
            #print(next_moves, previous_moves, nb_move)
            return possible_keys





        print(begin)
        print(keys)
        print(doors)

        print(lines)
        print("get_next_possible_keys", get_next_possible_keys(begin, points, keys))











if __name__ == '__main__':
    unittest.main()
