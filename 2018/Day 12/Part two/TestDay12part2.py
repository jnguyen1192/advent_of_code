import unittest


def input_file():
    # return the input file in a text
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = file.read()
    file.close()
    return res


class GenerationPlant:
    # class that represent the rules for each generation of plants
    def __init__(self, input_line, constraints, number_of_generation=20):
        """

        :param input_line: the plant that will have generation
        :param constraints: the constraints for each generation
        """
        self.input_line = input_line
        self.generation = ""
        self.constraints = constraints
        self.number_of_generation = number_of_generation
        self.beginning = 0  # to the border
        self.pattern_finder = (0, 0, 0)  # number turn, size and difference between current and previous size

    def sum_number_pot_containing__plants(self):
        # return number of plant of the current generation
        # the iterator for each rules applied
        ind_beg = self.generation.find("#")
        generation = self.generation[ind_beg:]
        # reverse generation
        rev_generation = generation[::-1]
        ind_beg = rev_generation.find("#")
        generation = rev_generation[ind_beg:]
        # rebuild generation
        generation = generation[::-1]
        sum_pots = 0
        for key, pot in enumerate(generation):
            if pot == "#":
                sum_pots += key + self.beginning  # because first pot is -2
        return sum_pots

    def next_generation(self):
        # build the next generation and add it on the list of generation
        current_generation = self.generation
        # apply rule
        self.apply_rule(current_generation)

    def rebuild_generation(self, generation):
        # the iterator for each rules applied
        ind_beg = generation.find("#")
        generation = "...." + generation[ind_beg:]
        # reverse generation
        rev_generation = generation[::-1]
        ind_beg = rev_generation.find("#")
        generation = "...." + rev_generation[ind_beg:]
        # rebuild generation
        return generation[::-1]

    def apply_rule(self, generation):
        # apply rules to the generation
        generation = self.rebuild_generation(generation)
        generation_list = []
        # begin at the right pot and end at the right pot
        for i in range(3, len(generation)+1):
            match_find = False
            for key, value in self.constraints.items():
                if key == generation[i-3:i+2]:
                    # transform the pot
                    generation_list.append(value)
                    # increment the iterator
                    match_find = True
                    # interrupt the matcher
                    break
            if not match_find:
                generation_list.append(".")
        generation_after = "".join(generation_list)
        if generation_after.find("#") < 2:
            self.beginning -= 1
        if generation_after.find("#") > 2:
            self.beginning += 1
        # add on list generation the current generation
        self.generation = generation_after

    def execute(self):
        # process on plants
        # init the generation list
        self.generation = self.input_line
        # process with number of generation
        for i in range(self.number_of_generation):
            previous_size = self.sum_number_pot_containing__plants()
            self.next_generation()
            current_size = self.sum_number_pot_containing__plants()
            # part 2 implementation of solution from Youtube
            if self.pattern_finder[2] == current_size - previous_size:
                break
            self.pattern_finder = (i + 1, current_size, current_size - previous_size)  #  @source https://www.youtube.com/watch?v=TeC3Wdg_3zI

    def visualize(self):
        # return the result
        number_of_current_generation, current_size, difference = self.pattern_finder
        # equation that represent number of generation less the pattern generation multiply by the difference and add by the current size
        return (self.number_of_generation - number_of_current_generation) * difference + current_size


def data_retrieve(lines):
    # return the new lines traited
    string_parse = "initial state: "
    input_line = lines[0][len(string_parse):]
    lines.pop(0)
    lines.pop(0)
    constraints = {}
    for line in lines:
        constraints[line[:5]] = line[9]
    return input_line, constraints


def data_preparation(input_line, constraints):
    # return the value of input
    return input_line, constraints


def day_12_part_2(lines):
    # data retrieve
    input_line, constraints = data_retrieve(lines)
    # data preparation
    input_line, constraints = data_preparation(input_line, constraints)
    # data modelisation
    plants_life_being = GenerationPlant(input_line, constraints, 50000000000)
    # data analyse
    plants_life_being.execute()
    # data visualize
    sum_number_of_plants_big_generation = plants_life_being.visualize()
    return str(sum_number_of_plants_big_generation)


class TestDay12part2(unittest.TestCase):

    def test_day_12_part_2(self):
        lines = input_file()
        res = output_file()
        pred = day_12_part_2(lines)
        assert(pred == res)


if __name__ == '__main__':
    unittest.main()
