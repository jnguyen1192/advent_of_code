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


class TestDay24part2(unittest.TestCase):

    def test_day_24_part_2(self):
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
            bugs = sorted(bugs, key=lambda x: x[1])
            str_state = ""
            for y in range(y_max + 1):
                for x in range(x_max + 1):
                    if (x, y) in bugs:
                        str_state += "#"
                    else:
                        str_state += "."
                str_state += "\n"
            return str_state

        def get_adjacent_bugs(bugs, x, y):
            debug = None
            adjacent_bugs = []
            # top
            try:
                if (x, y - 1) in bugs:
                    adjacent_bugs.append((x, y - 1))
            except:
                debug = None
            # right

            try:
                if (x + 1, y) in bugs:
                    adjacent_bugs.append((x + 1, y))
            except:
                debug = None
            # bottom
            try:
                if (x, y + 1) in bugs:
                    adjacent_bugs.append((x, y + 1))
            except:
                debug = None
            # left
            try:
                if (x - 1, y) in bugs:
                    adjacent_bugs.append((x - 1, y))
            except:
                debug = None
            return adjacent_bugs

        def next_step(bugs, x_max, y_max):
            new_bugs = []
            for y in range(y_max + 1):
                for x in range(x_max + 1):
                    nb_adjacent_bugs = len(get_adjacent_bugs(bugs, x, y))
                    if (x, y) in bugs:
                        # new bugs if one adjacent bug
                        if nb_adjacent_bugs == 1:
                            new_bugs.append((x, y))
                        # bug dies if not adjacent bug
                    else:
                        # empty space infested if one or two bugs are adjacent
                        if nb_adjacent_bugs == 1 or nb_adjacent_bugs == 2:
                            new_bugs.append((x, y))

            return new_bugs

        bugs, x_max, y_max = read_input(text)

        # print("Initial state\n" + get_str_state(bugs, x_max, y_max))
        def get_nb_bugs_after_x_minutes(bugs, x_max, minutes=200):
            next_bugs = bugs
            i = 0
            while i < minutes:
                print(i)
                next_bugs = next_step(next_bugs, x_max, y_max)
                i += 1
            return len(next_bugs)
                # print("After " + str(i + 1) + " minute\n" + get_str_state(next_bugs, x_max, y_max))

        #print(get_nb_bugs_after_x_minutes(bugs, x_max))
        # print("Biodiversity rating:", get_biodiversity_rating(bugs, x_max))
        depths_bugs = [(0, bugs)]

        def get_next_less_depth_bugs(bugs, x_max, y_max):
            current_bugs = bugs
            # less depth
            # top
            if (2, 1) in bugs:
                for x in range(5):
                    current_bugs.append((x, -1))
            # right
            if (3, 2) in bugs:
                for y in range(5):
                    current_bugs.append((5, y))
            # bot
            if (2, 3) in bugs:
                for x in range(5):
                    current_bugs.append((x, 5))
            # left
            if (1, 2) in bugs:
                for y in range(5):
                    current_bugs.append((-1, y))
            # next step
            next_bugs = next_step(current_bugs, x_max, y_max)
            for next_bug in next_bugs:
                x, y = next_bug
                # remove bugs with (x, y) not between 0 and 4
                # remove the middle bug (2, 2)
                if x not in range(x_max+1) or y not in range(y_max + 1) or (x, y) == (2, 2):
                    next_bugs.remove(next_bug)
            return next_bugs

        def get_next_plus_depth_bugs(bugs):
            next_bugs = []
            # plus depth
            # top
            c_top = 0
            for x in range(5):
                if (x, 0) == bugs:
                    c_top += 1
            if c_top == 1 or c_top == 2:
                next_bugs.append((2, 1))
            # right
            c_right = 0
            for y in range(5):
                if (4, y) == bugs:
                    c_right += 1
            if c_right == 1 or c_right == 2:
                next_bugs.append((3, 2))
            # bot
            # count top bugs
            c_bot = 0
            for x in range(5):
                if (x, 4) == bugs:
                    c_bot += 1
            if c_bot == 1 or c_bot == 2:
                next_bugs.append((2, 3))
            # left
            c_left = 0
            for y in range(5):
                if (0, y) == bugs:
                    c_left += 1
            if c_left == 1 or c_left == 2:
                next_bugs.append((1, 2))
            return next_bugs

        next_depths_bugs = depths_bugs
        current_depth_bugs = depths_bugs[0]
        current_depth = current_depth_bugs[0]
        current_bugs = current_depth_bugs[1]
        next_less_depth_bugs = get_next_less_depth_bugs(current_bugs, x_max, y_max)
        next_plus_depth_bugs = get_next_plus_depth_bugs(current_bugs)
        next_depths_bugs.append((current_depth - 1, next_less_depth_bugs))
        next_depths_bugs.append((current_depth + 1, next_plus_depth_bugs))
        # update current bugs
        current_bugs = next_step(bugs, x_max, y_max)
        for i, next_depth_bug in enumerate(next_depths_bugs):
            if next_depth_bug[0] == current_depth_bugs:
                next_depths_bugs[i] = (current_bugs, current_bugs)
        # sort the depth bugs
        next_depths_bugs = sorted(next_depths_bugs)
        str_depths_bugs = ""
        for next_depth_bug in next_depths_bugs:
            str_depths_bugs += "Depth " + str(next_depth_bug[0]) + ":\n" + get_str_state(next_depth_bug[1], x_max, y_max)
        print(str_depths_bugs)


if __name__ == '__main__':
    unittest.main()
