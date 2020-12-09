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


class TestDay20part1(unittest.TestCase):

    def test_day_20_part_1(self):
        text = input_file()
        # TODO 1: Extract the input_test as :
        #   First extract the map using #, . and empty
        #   For each "." near empty determine the portal to assign
        #   For each portal
        #       Find the next possible portal

        # TODO 2: Find less path algorithm:
        #   input_test: a coord(x, y)
        #   ouput: a list [(portal1, portal2, number_steps), ...]
        #   declare a list of path
        #   declare a list of steps
        #   increment the coord(x, y) on all cards
        #   while there was a list of steps:
        #       if there was more than one card
        #           for each card:
        #           duplicate the list of steps and add the new card
        #       else there was only one card
        #           add the new card on the current list of steps
        #       elif there was a portal
        #           add on the list of path the current list of steps as (portal1, portal2, number_steps)
        #       elif there was no new card
        #           remove the current list
        #   Select the mininum of each duplicate(portal1,portal2,X) and remove the others on list of path
        #   return the list of path

        # TODO 3:  We obtains a list:
        #       (AA, PE, 4)
        #       (PE, PN, X1) need to use less path
        #       (PN, SJ, X2) need to use less path
        #       etc ...
        #   Then find the shortest path between AA to ZZ using the graph obtains

        # TODO 4: Print the number of steps used from AA to ZZ










if __name__ == '__main__':
    unittest.main()
