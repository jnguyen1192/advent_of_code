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


class Position:
    """
    Position x, y
    """
    def __init__(self, x, y):
        """
        The position used on the grid
        :param x: x coordonate
        :param y: y coordonate
        """
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y


class Fighter:
    """
    An Elve has a recipe position and value
    """
    def __init__(self, classification, position, hit_points=200, hit_power=3):
        """
        An Elf is represented by his position and his
        :param classification: can be an Elve or a Gobelin
        :param position: use the class position
        :param hit_points: number of life points
        :param hit_power: number of damage with each attack
        """
        self.classification = classification
        self.position = position
        self.hit_points = hit_points
        self.hit_power = hit_power

    def is_alive(self):
        """
        To know if the elve is alive
        :return: True if the elve is alive
        """
        return self.hit_points > 0

    def get_hit_power(self):
        """
        The number of damage
        :return: the number of damage the enemy will receive
        """
        return self.hit_power

    def attack(self, fighter):
        """
        attack an ennemy and with attack damage
        """
        fighter.has_been_attack(self)

    def has_been_attack(self, fighter):
        """
        Damage the fighter receive by another fighter
        :param fighter: the fighter that attack the current fighter
        """
        self.hit_points -= fighter.get_hit_power()

    def move(self, fighters, walls):

    def step(self):
        # TODO nothing
        # TODO attack
        # TODO move
        pass

    def choose_enemy(self):
        #TODO parameter, the list of enemy
        pass


class BeverageBanditsManager:
    """
    Beverage bandits manager permits us to know what happened each turn
    """
    def __init__(self, fighters, walls):
        self.fighters = fighters
        self.walls = walls

    def get_fighters(self):
        return self.fighters

    def get_elves(self):
        elves = []
        for fighter in self.fighters:
            elves.append(fighter)
        return elves

    def get_gobelins(self):
        gobelins = []
        for fighter in self.fighters:
            gobelins.append(fighter)
        return gobelins

    def get_walls(self):
        return self.walls

    def extract_result(self, sum_):
        """
        Extract the result from the sum of each elves values
        :param sum_: sum of elves value
        :return: a list or a value
        """
        sum_extract = []
        if sum_/10 >= 1:
            # case superior by ten
            sum_extract.append(int(str(sum_)[0]))
            sum_extract.append(int(str(sum_)[1]))
            return sum_extract
        else:
            # case inferior by ten
            return [sum_]

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
        while len(self.recipes) < self.after_number_recipe + 10:
            # sum of two elves recipe
            sum_ = self.sum_recipes()
            # split the result if > %10
            #extract_sum = self.extract_result(sum_)
            self.recipes = self.recipes + str(sum_)
            # move the elves
            self.next_elves_position()
            if debug:
                self.print_step(i)
            i += 1

    def print_step(self, i):
        """
        print each step
        """
        import sys
        print(str(i))
        #print(self.recipes)

    def visualize(self):
        """
        Get the ten digits after the number of recipes in input
        :return:ten digits in string format
        """
        return "".join(self.recipes[self.after_number_recipe:self.after_number_recipe+10])


def data_retrieve(lines):
    # return the new lines traited
    return lines


def data_preparation(data):
    # return the value of input
    return int(data[0])


def day_15_part_1(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    object_builder = ObjectBuilder(lines)
    # data modelisation
    chocolate_charts_manager = ChocolateChartsManager(number_after_recipe)
    # data analyse
    chocolate_charts_manager.execute(False)
    # data visualize
    ten_digits_after = chocolate_charts_manager.visualize()
    return ten_digits_after


class TestDay15part1(unittest.TestCase):

    def test_day_15_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_15_part_1(lines)
        #assert(pred == res)



if __name__ == '__main__':
    unittest.main()
