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


class TestDay24part1(unittest.TestCase):

    def test_day_24_part_1(self):
        text = input_file()

        bugs = []
        def read_input(text):
            x_max, y_max = (0, 0)
            lines = text.split("\n")
            for y, line in enumerate(lines):
                for x, column in enumerate(line):
                    if column == "#":
                        bugs.append((x, y))
                    x_max = x
                y_max = y
            return bugs, x_max, y_max

        def get_str_state(bugs, x_max, y_max):
            bugs = sorted(bugs, key=lambda x:x[1])
            str_state = ""
            for y in range(y_max + 1):
                for x in range(x_max + 1):
                    if (x, y) in bugs:
                        str_state += "#"
                    else:
                        str_state += "."
                str_state += "\n"
            return str_state

        def get_biodiversity_rating(bugs, x_max):
            sum = 0
            for bug in bugs:
                sum += 2**(bug[1] * (x_max + 1) + bug[0])
            return sum

        def get_adjacent_bugs(bugs, x, y):
            debug = None
            adjacent_bugs = []
            # top
            try:
                if (x, y-1) in bugs:
                    adjacent_bugs.append((x, y-1))
            except:
                debug = None
            # right

            try:
                if (x+1, y) in bugs:
                    adjacent_bugs.append((x+1, y))
            except:
                debug = None
            # bottom
            try:
                if (x, y+1) in bugs:
                    adjacent_bugs.append((x, y+1))
            except:
                debug = None
            # left
            try:
                if (x-1, y) in bugs:
                    adjacent_bugs.append((x-1, y))
            except:
                debug = None
            return adjacent_bugs

        def next_step(bugs, x_max, y_max):
            new_bugs = []
            for y in range(y_max + 1):
                for x in range(x_max + 1):
                    nb_adjacent_bugs = len(get_adjacent_bugs(bugs, x, y))
                    if (x, y) in bugs:
                        # bug dies if not adjacent bug
                        if nb_adjacent_bugs == 1:
                            new_bugs.append((x, y))
                    else:
                        # empty space infested if one or two bugs are adjacent
                        if nb_adjacent_bugs == 1 or nb_adjacent_bugs == 2:
                            new_bugs.append((x, y))

            return new_bugs

        bugs, x_max, y_max = read_input(text)
        #print("Initial state\n" + get_str_state(bugs, x_max, y_max))
        def get_biodiversity_rating_first_layout_appears_twice(bugs, x_max):
            next_bugs = bugs
            biodiversity_ratings = []
            while True:
                biodiversity_rating = get_biodiversity_rating(next_bugs, x_max)
                if biodiversity_rating in biodiversity_ratings:
                    return biodiversity_rating
                biodiversity_ratings.append(biodiversity_rating)
                next_bugs = next_step(next_bugs, x_max, y_max)
                #print("After " + str(i + 1) + " minute\n" + get_str_state(next_bugs, x_max, y_max))
        print(get_biodiversity_rating_first_layout_appears_twice(bugs, x_max))
            #print("Biodiversity rating:", get_biodiversity_rating(bugs, x_max))











if __name__ == '__main__':
    unittest.main()
