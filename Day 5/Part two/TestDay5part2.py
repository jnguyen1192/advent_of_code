import unittest


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


class Polymer:
    # the polymer is represented as a string
    def __init__(self, polymer):
        self.polymer = list(polymer)

    # constraint same type oposite polarity nothing happens
    def is_same_type_opposite_polarity(self,new_polymer, x, X):
        if (new_polymer[x].islower() and new_polymer[X].isupper() and new_polymer[x].lower() == new_polymer[X].lower()) or (new_polymer[x].isupper() and new_polymer[X].islower() and new_polymer[x].lower() == new_polymer[X].lower()):
            return True
        return False

    # only couple with same type and opposite are removed
    def update_polymer(self, new_polymer, x, X):
        #print(self.polymer)
        if self.is_same_type_opposite_polarity(new_polymer, x, X):
            del new_polymer[x]
            del new_polymer[x]
            #self.polymer = self.polymer[:x] + self.polymer[X:]
            #self.polymer = self.polymer[:x] + self.polymer[X:]
            return -2
        return 0

    def update_all_polymer(self, new_polymer):
        # manage current position
        j = 0
        # except the last character
        for i in range(len(new_polymer)-1+j):
            i = self.update_polymer(new_polymer, j, j+1)
            # stay at the same position if the position has been removed
            j = j + 1 + i
        return new_polymer

    def get_new_polymer(self, new_polymer):
        new_polymer = self.update_all_polymer(list(new_polymer))
        return ''.join(new_polymer)

    def get_new_polymer_by_removing_all_by_char(self, char):
        polymer_removed_by_char = "".join(self.polymer)
        polymer_removed_by_char = polymer_removed_by_char.replace(char.lower(), "")
        polymer_removed_by_char = polymer_removed_by_char.replace(char.upper(), "")
        #print(polymer_removed_by_char)
        return polymer_removed_by_char

    def get_best_new_polymer_by_removing_all(self):
        min = len(self.polymer) + 1
        for char in "abcdefghijklmnopqrstuvwxyz":
            new_polymer = self.get_new_polymer_by_removing_all_by_char(char)
            tmp = len(self.get_new_polymer(new_polymer))
            if tmp < min:
                min = tmp
        return min


def day_5_part_2(text):
    input_polymer = text.split('\n')[0]
    # TODO process
    polymer = Polymer(input_polymer)
    min_polymer_length = polymer.get_best_new_polymer_by_removing_all()
    return min_polymer_length


class TestDay5part2(unittest.TestCase):

    def test_day_5_part_2(self):
        text = input_file()
        #res = output_file()
        pred = day_5_part_2(text)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
