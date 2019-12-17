import unittest
from parse import parse
import copy
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


class TestDay14part1(unittest.TestCase):

    def test_day_14_part_1(self):
        text = input_file()
        lines = text.split("\n")
        chemicals = []
        for line in lines:
            raw = line.split(" => ")
            input_chemicals_raw, output_chemical_raw = raw
            input_chemicals = [(i[0], i[1]) for i in [input_chemical_raw.split(" ") for input_chemical_raw in input_chemicals_raw.split(", ")]]
            output_chemical = output_chemical_raw.split(" ")
            output_chemical = (output_chemical[0], output_chemical[1])
            chemicals.append((output_chemical, input_chemicals))
        print(chemicals)
        # How to build FUEL ?
        def how_to_build(chemical_name, multiplicator=1):
            for chemical in chemicals:
                if chemical[0][1] == chemical_name:
                    # need to know how to build each element
                    nb_builded = int(chemical[0][0])
                    # convert chmical if nb_builded != 1
                    if nb_builded != 1:
                        #print(chemical[0], chemical[1])
                        inputs = [(int(i[0])*multiplicator, i[1]) for i in chemical[1]]
                        output = (int(chemical[0][0]) * multiplicator, chemical[0][1])
                        return (output, inputs), int(nb_builded)
                    return chemical, nb_builded

        nb_ore = 0
        fuel = how_to_build("FUEL")
        print("how_to_build(\"FUEL\")", how_to_build("FUEL"))

        for fuel_input in fuel[0][1]:
            input_fuel = how_to_build(fuel_input[1], fuel[1])
            # convert into the same dimension of fuel
            print("how_to_build(fuel_input[1])", how_to_build(fuel_input[1]))
            for fuel_input_input in input_fuel[0][1]:
                ORE = how_to_build(fuel_input_input[1], input_fuel[1])
                print(ORE)
                nb_ore += ORE[0][1][0][0]
                print(how_to_build(fuel_input_input[1], input_fuel[1]))

        print(nb_ore)






if __name__ == '__main__':
    unittest.main()
