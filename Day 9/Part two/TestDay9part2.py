import unittest
import string
from parse import parse


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


class Player:
    # class that representing each player with his numero and his score
    def __init__(self, numero, score=0):
        self.num = numero
        self.score = score


class MarbleGame:
    # class that representing the game with the list of marble, the current position, the players, the limit of last marble points and the associatives rules
    def __init__(self, players, limit_marble_points=5, marbles=[0], current_marble=0, num_turn_player=0):
        self.players = players
        self.limit_marble_points = limit_marble_points
        self.marbles = marbles
        self.current_marble = current_marble # from 0 to N
        self.num_turn_player = num_turn_player

    def add_point(self):
        # TODO add points to player
        pass

    def remove_marble(self):
        # TODO remove the marble from the list
        pass

    def insert_marble(self, player):
        # rule : a player insert a marble with the next marble in clockwise
        self.next_marble()

        self.next_marble()
        # rule : something differently happens for multiple of 23
        # keep marble that would be placed to points
        # marble 7 in counter-clockwise from the current marble is removed and add to points
        # immediatly located clockwise after the marble removed and become the new current marble plus one

    def next_marble(self):
        # rule : circle, increment by one until every marble has a number
        if self.current_marble % len(self.marbles) - 1 == 0:
            self.current_marble = 0
        else:
            # move to one on clockwise
            self.current_marble += 1




def day_9_part_2(text):
    # data retrieve
    raw_nodes = [tuple(parse("Step {} must be finished before step {} can begin.", l)) for l in
                 text.split('\n')]  # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py

    return str(0)


class TestDay9part2(unittest.TestCase):

    def test_day_9_part_2(self):
        text = input_file()
        res = output_file()
        pred = day_9_part_2(text)
        assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
