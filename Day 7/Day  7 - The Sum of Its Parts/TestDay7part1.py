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


class Correct_order:
    # class to execute the correct order list
    def __init__(self, raw_nodes, first_letters):
        self.raw_nodes = raw_nodes
        self.available_letters = sorted(first_letters)
        self.correct_order_string = ""

    def get_available_letters(self):
        # return available letters
        return self.available_letters

    def add_available_letter(self, available_letter):
        # add an available letter in our list of letter sorted
        self.available_letters = list(sorted(set(self.available_letters + [available_letter])))

    def add_correct_order(self, letter):
        # add an available letter in our list of letter sorted
        self.correct_order_string = self.correct_order_string + str(letter)

    def get_prerequite_letters(self, letter):
        # return all prerequite letters
        prerequite_letters = []
        for raw in self.raw_nodes:
            if raw[1] == letter:
                prerequite_letters.append(raw[0])
        return prerequite_letters

    def is_all_prerequite(self, prerequite_letters):
        # constraint with all prerequite
        available_letters = self.get_available_letters()
        for letter in prerequite_letters:
            if letter in available_letters:
                return False
            elif letter not in self.get_correct_order_string():
                return False
        return True

    def get_available_letter_without_preprequite_letters(self):
        # return avaible letter respecting the constraint of prerequite letters
        available_letters = self.get_available_letters()
        for available_letter in available_letters:
            prerequite_letters = self.get_prerequite_letters(available_letter)
            if self.is_all_prerequite(prerequite_letters):
                return available_letter
        return available_letters[0]

    def get_available_letter(self):
        # return the available letter order by alpha
        available_letter = self.get_available_letter_without_preprequite_letters()
        # remove the letter
        self.available_letters.remove(available_letter)
        # add this letter to the correct order list
        self.add_correct_order(available_letter)
        return available_letter

    def next_step(self):
        # get_child of next available
        available_letter = self.get_available_letter()
        # add all child on available list
        for raw in self.raw_nodes:
            if raw[0] == available_letter:
                self.add_available_letter(raw[1])

    def exec(self):
        # execute the brute force
        while len(self.available_letters) != 0:
            self.next_step()

    def get_correct_order_string(self):
        # return the correct order string
        return self.correct_order_string


def get_first_letters(letters, raw_nodes):
    # return the first letters of the workflow
    first_letters = []
    # find all first value of the worflow
    for letter in letters:
        find_value = False
        for raw in raw_nodes:
            if letter == raw[1]:
                find_value = True
                break
        if not find_value:
            first_letters.append(letter)
    return first_letters


def day_7_part_1(text):
    # data prepare
    raw_nodes = [tuple(parse("Step {} must be finished before step {} can begin.", l)) for l in text.split('\n')] # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py
    # data transform
    letters = set([raw[0] for raw in raw_nodes] + [raw[1] for raw in raw_nodes])
    first_letters = get_first_letters(letters, raw_nodes)
    # data model
    correct_order = Correct_order(raw_nodes, first_letters)
    # data analysis
    correct_order.exec()
    # data visualize
    return correct_order.get_correct_order_string()


class TestDay7part1(unittest.TestCase):

    def test_day_7_part_1(self):
        text = input_file()
        res = output_file()
        pred = day_7_part_1(text)
        assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
