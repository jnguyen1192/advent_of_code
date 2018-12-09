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
        self.num = numero  # numeroted from one to N
        self.score = score


class MarbleGame:
    # class that representing the game with the list of marble, the current position, the players, the limit of last marble points and the associatives rules
    def __init__(self, number_players, limit_marble_points=5, marbles=[0], current_location_marble=0, current_marble_value=0, num_turn_player=0):
        self.number_players = number_players
        self.number_players = self.init_players()
        self.limit_marble_points = limit_marble_points
        self.marbles = marbles
        self.current_location_marble = current_location_marble  # from 0 to N
        self.current_marble_points = current_marble_value  # from 0 to N
        self.num_turn_player = num_turn_player

    def add_point(self):
        # TODO add points to player
        pass

    def remove_marble(self):
        # TODO remove the marble from the list
        pass

    def get_current_num_player(self):
        # return the current num of player
        return self.num_turn_player


    def next_player(self):
        # go to the next player
        self.num_turn_player += 1 % self.number_players  # % for go from last player to first player

    def increment_marble_points(self):
        self.current_marble_points += 1

    def new_marble_value(self):
        self.current_marble_points = self.marbles[self.current_location_marble - 1]

    def insert_marble(self, num_player):
        # rule : a player insert a marble with the next marble in clockwise
        self.next_marble()
        self.marbles.insert(self.current_location_marble, )
        self.next_marble()
        # TODO rule : something differently happens for multiple of 23
        #        keep marble that would be placed to points
        #        marble 7 in counter-clockwise from the current marble is removed and add to points
        # immediatly located clockwise after the marble removed and become the new current marble plus one

    def next_marble(self):
        # rule : circle, increment by one until every marble has a number
        if self.current_location_marble % len(self.marbles) - 1 == 0:
            self.current_location_marble = 0
        else:
            # move to one on clockwise
            self.current_location_marble += 1

    def init_players(self):
        # return the list of player
        players = []
        for i in range(self.number_players):
            # we create the player with the number of player
            players.append(Player(i+1))  # ordered from one to number players + 1
        return players

    def step_game(self):
        # TODO in each step of the game
        # the current player insert a marble and the table is update
        current_num_player = self.get_current_num_player()
        self.insert_marble(current_num_player)
        # we move to the next player
        self.next_player()

    def pretty_print(self):
        # print the execution like the example on advent of code
        print('[', self.num_turn_player, ']\t', self.marbles)

    def exec(self):
        # execute the game until the marble points limit is reached
        while self.current_marble_points < self.limit_marble_points:
            self.step_game()
            self.pretty_print()


def day_9_part_2(text):
    # data retrieve
    raw_nodes = [tuple(parse("Step {} must be finished before step {} can begin.", l)) for l in
                 text.split('\n')]  # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py
    print(raw_nodes)
    return str(0)


class TestDay9part2(unittest.TestCase):

    def test_day_9_part_2(self):
        text = input_file()
        res = output_file()
        pred = day_9_part_2(text)
        assert(pred == res[0])

    def test_code(self):
        list = [2, 3, 5]
        marble = 6
        list.insert(2, marble)
        print(list)


if __name__ == '__main__':
    unittest.main()
