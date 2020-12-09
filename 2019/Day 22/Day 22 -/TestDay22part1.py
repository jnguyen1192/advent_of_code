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


class TestDay22part1(unittest.TestCase):

    def test_day_22_part_1(self):
        text = input_file()
        def your_deck(N):
            # cards 0 -> 10006
            # 0 on the top, 10006 on the bottom
            your_deck = []
            for n in range(N):
                your_deck.append(n)
            return your_deck

        #code = [int(val) for val in text.split(",")]

        #print(your_deck(10))
        def deal_into_new_stack(your_deck):
            # new stack is reverse list of "your deck"
            return your_deck[::-1]
        #print(deal_into_new_stack(your_deck(10)))

        def cut(your_deck, N):
            # cut N cards <-> new_deck[:3] to the end of the deck
            # cut -N cards <-> new_deck[:-4] to the begining of the deck
            return your_deck[N:] + your_deck[:N]
        #print(cut(your_deck(10), 3))
        #print(cut(your_deck(10), -4))

        def increment(your_deck, N):
            # increment N <-> Distribute the new deck using "your deck" and the corresponding increment modulo size_your_deck beginning with 0
            new_indexes = []
            size_deck = len(your_deck)
            i = 0
            j = 0
            while size_deck != len(new_indexes):
                new_indexes.append((i, your_deck[j]))
                i = (i + N) % size_deck
                j += 1
            new_indexes = sorted(new_indexes)
            return [your_deck_j for i, your_deck_j in new_indexes]
        #print(increment(your_deck(10), 3))

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
        #print(get_shuffle_process(text))

        def apply_process(proccess, N=10):
            yd = your_deck(N)
            for p in proccess:
                if p[0] == "cut":
                    yd = cut(yd, p[1])
                elif p[0] == "increment":
                    yd = increment(yd, p[1])
                if p[0] == "new_stack":
                    yd = deal_into_new_stack(yd)
            return yd

        def get_position_of_card(your_deck, card):
            for i, your_deck_card in enumerate(your_deck):
                if card == your_deck_card:
                    return i
            return -1



        nb_cards = 119315717514047
        nb_process = 101741582076661
        card = 2020
        print(get_position_of_card(apply_process(get_shuffle_process(text), nb_cards), card))












if __name__ == '__main__':
    unittest.main()
