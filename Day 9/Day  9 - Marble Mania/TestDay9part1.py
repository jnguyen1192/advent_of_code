import unittest
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
        self.numero = numero  # numeroted from one to N
        self.score = score

    def add_point(self, points):
        # add point into player score
        self.score += points

    def get_numero(self):
        # return the numero of the player
        return self.numero

    def get_score(self):
        # return the current score of the player
        return self.score


class MarbleGame:
    # class that representing the game with the list of marble, the current position, the players, the limit of last marble points and the associatives rules
    def __init__(self, number_players, limit_marble_points=25, marbles=[0], current_location_marble=0, current_marble_points=1, num_turn_player=0):
        self.number_players = number_players
        self.players = self.init_players()
        self.limit_marble_points = limit_marble_points + 1
        self.marbles = marbles
        self.current_location_marble = current_location_marble  # from 0 to N
        self.current_marble_points = current_marble_points  # from 0 to N
        self.num_turn_player = num_turn_player

    def get_current_num_player(self):
        # return the current num of player
        return self.num_turn_player

    def next_player(self):
        # go to the next player
        self.num_turn_player = (self.num_turn_player + 1) % self.number_players  # % for go from last player to first player

    def increment_marble_points(self):
        # increment the number of marble points
        self.current_marble_points += 1

    def increment_current_location_marble(self):
        # increment the next marble location in a circle
        self.current_location_marble += 1 % len(self.marbles)

    def new_marble_value(self):
        # return the new value of marble after multiple by 23 found
        self.current_marble_points = self.marbles[self.current_location_marble - 1]

    def get_current_marble_points(self):
        # return the current marble points
        return self.current_marble_points

    def get_current_location_marble(self):
        # return the current location of marble
        return self.current_location_marble

    def remove_current_marble(self):
        # remove the marble on the current location marble
        self.marbles.pop(self.get_current_location_marble())

    def insert_special_marble(self):
        # insert a marble points with the value+1 of its left side
        value_left_marble_points = self.marbles[self.get_current_location_marble()-1]
        # insert the marble points
        self.marbles.insert(self.get_current_location_marble(), value_left_marble_points)

    def insert_marble_without_constraints(self):
        # insert a marble in the next location marble
        self.next_marble()
        self.marbles.insert(self.get_current_location_marble()+1, self.get_current_marble_points()) # using clockwise
        self.next_marble()

    def something_differently_happened(self, current_num_player):
        # keep marble that would be placed to points
        keep_marble_points_that_would_be_placed = self.get_current_marble_points()  #  + 1 because it is the next
        # add this marble points into the current player score
        self.players[current_num_player].add_point(keep_marble_points_that_would_be_placed)
        # get back from 7 location from current location marble
        self.get_back_from_current_location()
        # keep value of marble 7 counter-clockwise
        keep_marble_placed_before_removed = self.marbles[self.get_current_location_marble()]
        # add marble point on 7 counter-clockwise to the current player score
        self.players[current_num_player].add_point(keep_marble_placed_before_removed)
        # marble 7 in counter-clockwise from the current marble is removed
        self.remove_current_marble()

    def get_back_from_current_location(self, number=7):
        self.current_location_marble -= number
        # it is a circle, we need to treat the special case at the left
        if self.current_location_marble < 0:
            self.current_location_marble += len(self.marbles)

    def insert_marble_with_constraints(self, current_num_player):
        # rule : a player insert a marble with the next marble in clockwise
        if self.get_current_marble_points() % 23 != 0:
            self.insert_marble_without_constraints()
        else:
            # rule : something differently happens for multiple of 23
            self.something_differently_happened(current_num_player)
            # immediatly located clockwise after the marble removed and become the new current marble plus one
        # increment marble points
        self.increment_marble_points()

    def next_marble(self):
        # rule : circle, increment by one until every marble has a number
        # move to one on clockwise
        self.current_location_marble += 1
        if self.current_location_marble % len(self.marbles) == 0:
            self.current_location_marble = 0

    def init_players(self):
        # return the list of player
        players = []
        for i in range(self.number_players):
            # we create the player with the number of player
            players.append(Player(i+1))  # ordered from one to number players + 1
        return players

    def step_game(self, debug=False):
        # in each step of the game
        # we move to the next player
        self.next_player()
        # the current player insert a marble and the table is update
        current_num_player = self.get_current_num_player()
        self.insert_marble_with_constraints(current_num_player)
        if debug:
            self.pretty_print()

    def rank_print(self):
        r_print = ""
        for player in self.players:
            r_print += str(player.get_numero()) + "\t\t\t\t\t" + str(player.get_score()) + "\n"
        print(r_print)

    def pretty_print(self):
        # print the execution like the example on advent of code
        curr_loc_marble = self.get_current_location_marble()
        marbles_print = ""
        for value in self.marbles[:curr_loc_marble]:
            marbles_print += " " + str(value) + " "

        marbles_print += "(" + str(self.marbles[curr_loc_marble]) + ")"

        for value in self.marbles[curr_loc_marble+1:]:
            marbles_print += " " + str(value) + " "
        print('[', self.num_turn_player, ']\t', marbles_print, '\t')

    def exec(self, debug=False):
        # execute the game until the marble points limit is reached
        while self.current_marble_points < self.limit_marble_points:
            self.step_game(debug)
        if debug:
            self.rank_print()

    def get_highest_score(self):
        # return the highest score from the players
        highest_score = 0
        for player in self.players:
            player_score = player.get_score()
            if highest_score < player_score:
                highest_score = player_score
        return highest_score


def data_retrieve(text):
    raw_nodes = [tuple(parse("{} players; last marble is worth {} points", l)) for l in
                 text.split('\n')]  # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py
    # data transformation
    return map(int, raw_nodes[0])


def day_9_part_1(text):
    # data retrieve
    number_players, last_marble_worth_point = data_retrieve(text)
    # data modelisation
    marble_game = MarbleGame(number_players, last_marble_worth_point)
    # data analysis
    marble_game.exec(False)
    # data visualisation
    highest_score = marble_game.get_highest_score()
    return str(highest_score)


class TestDay9part1(unittest.TestCase):

    def test_day_9_part_1(self):
        text = input_file()
        res = output_file()
        pred = day_9_part_1(text)
        assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
