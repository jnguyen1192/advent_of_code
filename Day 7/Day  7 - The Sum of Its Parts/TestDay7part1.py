import unittest
import numpy as np
from parse import parse
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


class Node_before:
    def __init__(self, before, current):
        self.before = before
        self.current = current

    def get_current_value(self):
        return self.current - 1

    def get_before(self):
        return self.before

    def get_current(self):
        return self.current


class Ordered_nodes:

    def __init__(self, first_letter, nodes):
        self.letters = [first_letter]
        self.values = [0]
        self.nodes = nodes

    def add_node_before(self, node):
        letter = node.get_before()

        # case letter already exist
        if node.get_before() in self.letters:
            # decrement its value
            self.decrement_value_using_letter(letter)
        # case current letter doesn't exist
        if node.get_current() not in self.letters:
            # nothing to do
            return False
        # case before letter doesn't exist
        else:
            # TODO order by [1] or [0] the raw_nodes
            # add on letters with value of current letter - 1
            self.letters.append(node.get_before())
            current_value_less_one = self.get_value_using_letter(node.get_current()) - 1
            self.values.append(current_value_less_one)
        return True

    def get_value_using_letter(self, letter):
        # get letter num
        letter_num = 0
        for index, value in enumerate(self.letters):
            if letter == value:
                letter_num = index
        return self.values[letter_num]

    def decrement_value_using_letter(self, letter):
        # get letter num
        letter_num = 0
        for index, value in enumerate(self.letters):
            if letter == value:
                letter_num = index
        self.values[letter_num] = self.values[letter_num] - 1

    def execute_logic(self):
        # stop when there wasn't nodes to analyse
        while len(self.nodes) != 0:
            for index, node in enumerate(self.nodes):
                is_proceed = self.add_node_before(node)
                if is_proceed:
                    del self.nodes[index]

    def get_ordered_instructions(self):
        # init instructions
        instructions = ""
        # init dictionnary
        dictionary = {}
        for index, letter in enumerate(self.letters):
            dictionary[letter] = self.values[index]
        pprint(dictionary)
        # sort dictionnary by value https://stackoverflow.com/questions/20944483/python-3-sort-a-dict-by-its-values
        s = [(k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=True)]
        for k, v in s:
            # add into instruction
            instructions += k
            # TODO ordered by letter order
        return instructions[::-1]
        # KS

def day_7_part_1(text):
    # TODO
    # data prepare
    raw_nodes = [tuple(parse("Step {} must be finished before step {} can begin.", l)) for l in text.split('\n')] # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py
    pprint(raw_nodes)
    nodes = []
    # create nodes
    for raw_node in raw_nodes:
        nodes.append(Node_before(raw_node[0], raw_node[1]))
    #letters_to_test
    letters_to_test = set()
    # get letter to test
    for raw_node in raw_nodes:
        letters_to_test.add(raw_node[0])
        letters_to_test.add(raw_node[1])
    # get letter at the end
    for last_probably_letter in letters_to_test:
        find_last_letter = True
        for couple in raw_nodes:
            if couple[0] == last_probably_letter:
                find_last_letter = False
                break
        if find_last_letter:
            print("last_probably_letter ", last_probably_letter)
    # search model
    # affect value on E equals 0
    # search before letter of E
    # affect value on before letter of E
    ordered_nodes = Ordered_nodes("E", nodes)
    #
    # couple (C, A)
    """
    E = 0
    B = E - 1
    D = E - 1
    F = E - 1
    A = B - 1
    A = D - 1
    C = A - 1
    C = F - 1
    """
    # affect each variable a value
    # TODO swap variable
    # execute logic
    ordered_nodes.execute_logic()
    # print ordered_instruction
    """print(C)
    print(A)
    print(B)
    print(D)
    print(F)
    print(E)
    """
    return ordered_nodes.get_ordered_instructions()


class TestDay7part1(unittest.TestCase):

    def test_day_7_part_1(self):
        text = input_file()
        #lines.sort()
        #res = output_file()
        pred = day_7_part_1(text)
        print("less to zero")
        for i in range(-4, 0):
            print("i ", i)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
