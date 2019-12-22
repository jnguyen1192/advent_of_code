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


class TestDay22part2(unittest.TestCase):

    def test_day_22_part_2(self):
        text = input_file()

        # parse the text
        def get_shuffle_process(text):
            lines = text.split("\n")
            process = []
            # for each line get the
            for line in lines:
                if line[:3] == "cut":
                    process.append(("cut", int(line.split(" ")[1])))
                elif line[:9] == "deal with":
                    process.append(("increment", int(line.split(" ")[3])))
                elif line == "deal into new stack":
                    process.append(("new_stack", None))
            return process

        def position_incr(your_deck_length, position, incr):
            return (incr * position) % your_deck_length

        def position_new_stack(your_deck_length, position):
            return your_deck_length - 1 - position

        def position_cut(your_deck_length, position, cut):
            return (position - cut) % your_deck_length

        def get_position_process(proccess, card=0, N=10, nb_times=1):
            your_deck_length = N
            position = card
            print(proccess)
            old_position = position
            nb_times_real = nb_times % N
            for i in range(nb_times_real):
                for p in proccess:
                    if p[0] == "cut":
                        position = position_cut(your_deck_length, position, p[1])
                    if p[0] == "increment":
                        position = position_incr(your_deck_length, position, p[1])
                    if p[0] == "new_stack":
                        position = position_new_stack(your_deck_length, position)
                print((i/nb_times_real) * 100, "%")
                old_position = position
            return position
        card = 2019
        nb_card = 119315717514047
        nb_times = 101741582076661
        print(get_position_process(get_shuffle_process(text), card, nb_card, nb_times))



if __name__ == '__main__':
    unittest.main()
