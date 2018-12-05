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


def write_in__res_file(text):
    # read line of output file
    file = open("res", "w")
    file.write(text)
    file.close()


class Polymer:
    # the polymer is represented as a string
    def __init__(self, polymer):
        self.polymer = list(polymer)

    # constraint same type oposite polarity nothing happens
    def is_same_type_opposite_polarity(self, x, X):
        if (self.polymer[x].islower() and self.polymer[X].isupper() and self.polymer[x].lower() == self.polymer[X].lower()) or (self.polymer[x].isupper() and self.polymer[X].islower() and self.polymer[x].lower() == self.polymer[X].lower()):
            return True
        return False

    # only couple with same type and opposite are removed
    def update_polymer(self, x, X):
        #print(self.polymer)
        if self.is_same_type_opposite_polarity(x, X):
            del self.polymer[x]
            del self.polymer[x]
            #self.polymer = self.polymer[:x] + self.polymer[X:]
            #self.polymer = self.polymer[:x] + self.polymer[X:]
            return -2
        return 0

    def update_all_polymer(self):
        # manage current position
        j = 0
        # except the last character
        for i in range(len(self.polymer)-1+j):
            i = self.update_polymer(j, j+1)
            # stay at the same position if the position has been removed
            j = j + 1 + i

    def get_new_polymer(self):
        self.update_all_polymer()
        return ''.join(self.polymer)


def day_5_part_1(text):
    # TODO input
    input_polymer = text.split('\n')[0]
    # TODO process
    polymer = Polymer(input_polymer)
    new_polymer = polymer.get_new_polymer()
    return new_polymer


class TestDay5part1(unittest.TestCase):

    def test_day_5_part_1(self):
        text = input_file()
        #res = output_file()
        pred = day_5_part_1(text)

        write_in__res_file(pred)
        print((len(pred)))
        #print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
