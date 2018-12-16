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


class Elve:
    """
    An Elve has a recipe position and value
    """
    def __init__(self, current_recipe_position, current_recipe_value):
        """
        An Elf use those parameter build new recipe
        :param current_recipe_position:
        :param current_recipe_value:
        """
        self.current_recipe_position = current_recipe_position
        self.current_recipe_value = current_recipe_value

    def get_current_recipe_position(self):
        """
        :return:  the current recipe position
        """
        return self.current_recipe_position

    def get_current_recipe_value(self):
        """
        :return:  the current recipe value
        """
        return self.current_recipe_value

    def set_current_recipe_position(self, position):
        """
        set the current recipe position
        """
        self.current_recipe_position = position

    def set_current_recipe_value(self, value):
        """
        set the current recipe value
        """
        self.current_recipe_value = value


class ChocolateChartsManager:
    """
    Chocolate charts manager permits us to know what happened each turn
    """
    def __init__(self, after_number_recipe=9, first_recipe=3, second_recipe=7):
        """
        The value of the first recipe are 3 and 7 for the two elves
        :param after_number_recipe: number of recipe from the beginning of recipe list
        :param first_recipe: recipe of the first elve
        :param second_recipe: recipe of the second elve
        """
        self.after_number_recipe = after_number_recipe
        self.first_elve = Elve(0, first_recipe)
        self.second_elve = Elve(1, second_recipe)
        self.recipes = str(first_recipe) + str(second_recipe)

    def sum_recipes(self):
        """
        Calculate the sum of recipe value of both elves
        :return: the sum of recipe
        """
        return self.first_elve.get_current_recipe_value() + self.second_elve.get_current_recipe_value()

    def next_elves_position(self):
        """
        Move the two elves using the rule that
        the next position is the current recipe
        value plus the current position plus one
        in the list of recipe
        """
        first_elve_move = (self.first_elve.get_current_recipe_position() + self.first_elve.get_current_recipe_value() + 1) % len(self.recipes)
        self.first_elve.set_current_recipe_position(first_elve_move)
        self.first_elve.set_current_recipe_value(int(self.recipes[first_elve_move]))

        second_elve_move = (self.second_elve.get_current_recipe_position() + self.second_elve.get_current_recipe_value() + 1) % len(self.recipes)
        self.second_elve.set_current_recipe_position(second_elve_move)
        self.second_elve.set_current_recipe_value(int(self.recipes[second_elve_move]))

    def execute(self, debug=False):
        # process on recipes
        i = 0
        # exit when the input found
        while self.recipes.find(str(self.after_number_recipe)) == -1:
            # sum of two elves recipe
            sum_ = self.sum_recipes()
            # add the number
            self.recipes = self.recipes + str(sum_)
            # move the elves
            self.next_elves_position()
            #print(i)
            if debug:
                if i % 1000000:
                    print(i, " ", len(self.recipes))
                    #self.print_step(i)

    def print_step(self, i):
        """
        print each step
        """
        #print(self.recipes)

    def visualize(self):
        """
        Get the index of first 5 digits of the ten digits score found
        :return:ten digits in string format
        """
        return len(self.recipes) - len(str(self.after_number_recipe))


def data_retrieve(lines):
    # return the new lines traited
    return lines


def data_preparation(data):
    # return the value of input
    return int(data[0])


def day_14_part_2(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    number_after_recipe = data_preparation(data)
    # data modelisation
    chocolate_charts_manager = ChocolateChartsManager(number_after_recipe)
    # data analyse
    chocolate_charts_manager.execute(True)
    # data visualize
    number_of_recipe_on_the_left_score_found = chocolate_charts_manager.visualize()
    return number_of_recipe_on_the_left_score_found


class TestDay14part2(unittest.TestCase):

    def test_day_14_part_2(self):
        lines = input_file()
        res = output_file()
        pred = day_14_part_2(lines)
        print(pred)
        #assert(pred == res)

    def test_chain_code(self):
        from itertools import chain
        string = "hello world"
        for c in chain(string):
            print(c)
        print((chain(string)))
        print(chain(string)[0])


if __name__ == '__main__':
    unittest.main()
