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
    Position y, x
    """
    def __init__(self, y, x):
        """
        The position used on the grid
        :param x: x coordonate
        :param y: y coordonate
        """
        self.y = y
        self.x = x

    def get_position(self):
        return self.y, self.x

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x


class Fighter:
    """
    An Elve has a recipe position and value
    """
    def __init__(self, position, classification, map=[], fighters=[], hit_points=200, hit_power=3):
        """
        An Elf is represented by his position and his
        :param classification: can be an Elve or a Gobelin
        :param position: use the class position
        :param hit_points: number of life points
        :param hit_power: number of damage with each attack
        """
        self.position = position
        self.classification = classification
        self.map = map
        self.fighters = fighters
        self.hit_points = hit_points
        self.hit_power = hit_power

    def get_position(self):
        """
        Get the position of the cart
        :return: the position y x of the current cart
        """
        return self.position

    def get_classification(self):
        return self.classification

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
        pass

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
    def __init__(self, fighters, map):
        self.fighters = fighters
        self.map = map

    def get_fighters(self):
        return self.fighters

    def get_elves(self):
        elves = []
        for fighter in self.fighters:
            if fighter.get_classification() == "E":
                elves.append(fighter)
        return elves

    def get_gobelins(self):
        gobelins = []
        for fighter in self.fighters:
            if fighter.get_classification() == "G":
                gobelins.append(fighter)
        return gobelins

    def next_elves_position(self):
        pass

    def execute(self, debug=False):
        # process on recipes
        pass


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
        return ""

    def get_enemies(self, fighter):
        # return the enemies of the current fighter
        # get the current classification
        fighter_class = fighter.get_classification()
        if fighter_class == "G":
            return self.get_elves()
        if fighter_class == "E":
            return self.get_gobelins()

    def is_case_available(self, y, x):
        if self.map[y][x] == "#":
            return False
        for fighter in self.get_fighters():
            # get fighter position
            fighter_position_y = fighter.get_position().get_y()
            fighter_position_x = fighter.get_position().get_x()
            # test fighter and wall existence
            if fighter_position_y == y and fighter_position_x == x:
                return False
        return True

    def is_case_available_without_current_fighter(self, y, x, current_fighter):
        if self.map[y][x] == "#":
            return False
        # get current fighter position
        current_fighter_position_y = current_fighter.get_position().get_y()
        current_fighter_position_x = current_fighter.get_position().get_x()
        for fighter in self.get_fighters():
            # get fighter position
            fighter_position_y = fighter.get_position().get_y()
            fighter_position_x = fighter.get_position().get_x()
            if not (
                    current_fighter_position_y == fighter_position_y and current_fighter_position_x == fighter_position_x):
                # test fighter and wall existence
                if fighter_position_y == y and fighter_position_x == x:
                    return False
        return True

    def is_case_on_cases(self, cases, y, x):
        for case in cases:
            if case[0] == y and case[1] == x:
                return True
        return False

    def get_adjacent_available_case(self, cases, y, x):
        adjacent_available = []
        # 4 adjacent
        # test if there was no # or fighter
        if self.is_case_available(y - 1, x) and not self.is_case_on_cases(cases, y - 1, x):
            adjacent_available.append((y - 1, x))
            # left
        if self.is_case_available(y, x - 1) and not self.is_case_on_cases(cases, y, x - 1):
            adjacent_available.append((y, x - 1))
            # right
        if self.is_case_available(y, x + 1) and not self.is_case_on_cases(cases, y, x + 1):
            adjacent_available.append((y, x + 1))
            # down
        if self.is_case_available(y + 1, x) and not self.is_case_on_cases(cases, y + 1, x):
            adjacent_available.append((y + 1, x))
        return adjacent_available

    def get_range_from_enemies(self, current_fighter, enemies):
        """
        Using the map we locate every adjacent available case
        :param enemies: list of enemies
        """
        in_range = []
        for enemy in enemies:
            # get enemy position
            current_enemy_position_y = enemy.get_position().get_y()
            current_enemy_position_x = enemy.get_position().get_x()
            # 4 adjacent
            # test if there was no # or fighter
            # up
            if self.is_case_available_without_current_fighter(current_enemy_position_y - 1, current_enemy_position_x, current_fighter):
                in_range.append((current_enemy_position_y - 1, current_enemy_position_x))
            # left
            if self.is_case_available_without_current_fighter(current_enemy_position_y, current_enemy_position_x - 1, current_fighter):
                in_range.append((current_enemy_position_y, current_enemy_position_x - 1))
            # right
            if self.is_case_available_without_current_fighter(current_enemy_position_y, current_enemy_position_x + 1, current_fighter):
                in_range.append((current_enemy_position_y, current_enemy_position_x + 1))
            # down
            if self.is_case_available_without_current_fighter(current_enemy_position_y + 1, current_enemy_position_x, current_fighter):
                in_range.append((current_enemy_position_y + 1, current_enemy_position_x))
        return in_range

    def add_enemies_on_map(self, enemies):
        for enemy in enemies:
            self.map[enemy.get_position().get_y()][enemy.get_position().get_x()] = enemy.get_classification()

    def add_range_enemies_on_map(self, in_range):
        for ir in in_range:
            self.map[ir[0]][ir[1]] = "?"

    def add_reachable_enemies_on_map(self, reachable_enemies):
        for re in reachable_enemies:
            self.map[re[0]][re[1]] = "@"

    # TODO Targets current with list enemies
    def print_first_fighter_target(self):
        print("Targets :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        self.map[current_fighter.get_position().get_y()][current_fighter.get_position().get_x()] = current_fighter.get_classification()
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # print enemies
        self.add_enemies_on_map(enemies)
        self.print_map()

    # TODO In range current with list enemies and walls
    def print_range_enemies_with_walls(self):
        print("In range :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        # print range of enemies
        self.add_range_enemies_on_map(in_range)
        # print enemies
        self.add_enemies_on_map(enemies)
        #self.print_map()
        pass

    def add_current_fighter_on_map(self, current_fighter):
        self.map[current_fighter.get_position().get_y()][
            current_fighter.get_position().get_x()] = current_fighter.get_classification()

    def get_reachable_area(self, current_fighter):
        # get available adjacent case
        adjacent_available = []
        # look case adjacent from the current fighter
        # get current fighter position
        current_fighter_position_y = current_fighter.get_position().get_y()
        current_fighter_position_x = current_fighter.get_position().get_x()
        adjacent_available = adjacent_available + self.get_adjacent_available_case(adjacent_available, current_fighter_position_y,
                                                                                   current_fighter_position_x)
        old_length = len(adjacent_available)
        while True:
            for aa in adjacent_available:
                adjacent_available = adjacent_available + self.get_adjacent_available_case(adjacent_available, aa[0], aa[1])
            if len(adjacent_available) == old_length:
                break
            old_length = len(adjacent_available)
        #for aa in adjacent_available:
        #    self.map[aa[0]][aa[1]] = "Y"
        return adjacent_available

    def get_reachable_enemies(self, current_fighter, in_range):
        # get reachable area
        # a reachable area is an area wich our current fighter can move
        reachable_enemies = []
        reachable_area = self.get_reachable_area(current_fighter)
        for ir in in_range:
            if self.is_case_on_cases(reachable_area, ir[0], ir[1]):
                reachable_enemies.append(ir)
        return reachable_enemies

    # TODO Reachable current with list enemies reachable
    def print_reachable_enemies_with_walls(self):
        print("Reachable :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        reachable = self.get_reachable_enemies(current_fighter, in_range)
        #self.get_reachable_area(current_fighter)
        self.add_current_fighter_on_map(current_fighter)
        self.add_enemies_on_map(enemies)
        self.add_reachable_enemies_on_map(reachable)
        self.print_map()

    # TODO Nearest for each dot put the number of case to reach enemy
    def print_nearest_enemies_reachable(self):
        print("Nearest :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        reachable = self.get_reachable_enemies(current_fighter, in_range)

    # TODO Chosen return the coordonate to attack
    def print_chosen_enemy_reachable(self):
        print("Chosen :")

    # TODO Move_to_chosen move to the chosen using priority of x and y
    def print_move_to_enemy_reachable(self):
        print("Move :")

    def print_order_fighter_on_map(self):
        for index, fighter in enumerate(self.fighters):
            self.map[fighter.get_position().get_y()][fighter.get_position().get_x()] = str(index+1)
        self.print_map()

    def print_map(self):
        """
        print the map
        """
        str_map = ""
        for line in self.map:
            str_map += "".join(line) + "\n"
        print(str_map)

class ObjectBuilder:
    """
    Builder to instanciate objects from the input
    """
    def __init__(self, lines):
        self.carts = []
        self.lines = lines
        self.fighters = self.build_fighters()
        self.map = self.build_map()

    def print_carts(self):
        # print the map using the matrix map
        print(self.carts)

    def find_all_fighter(self, line, y, fighter):
        x = 0
        # classification
        # first iteration
        while line.find(fighter, x) != -1:
            x = line.find(fighter, x)
            if x == -1:
                break
            finder = y, x, fighter
            yield tuple(finder)
            x += 1

    def build_map(self):
        # return the matrix of the map
        map = []
        for line in self.lines:
            line_list = []
            for i in line:
                line_list.append(i)
            map.append(line_list)
        self.map = map
        # remove fighters from the map
        self.remove_fighters_from_map(self.fighters)
        return map

    def build_fighters(self):
        # return a list of carts as (x, y, direction of cart)
        fighters = []
        fighters_object = []
        y = 0
        for line in self.lines:
            elves = self.find_all_fighter(line, y, "E")
            if elves != 0:
                fighters += [e for e in self.find_all_fighter(line, y, "E")]
            gobelins = self.find_all_fighter(line, y, "G")
            if gobelins != 0:
                fighters += [g for g in self.find_all_fighter(line, y, "G")]
            y += 1
        fighters = sorted(fighters)
        # browse on list of tuple
        for fighter in fighters:
            # create each cart object
            fighters_object.append(Fighter(Position(fighter[0], fighter[1]), fighter[2]))
        # remove the carts from the map
        return fighters_object

    def remove_fighters_from_map(self, fighters_object):
        for fighter in fighters_object:
            self.map[fighter.get_position().get_y()][fighter.get_position().get_x()] = "."

    def get_fighters(self):
        """
        Give us the fighters on a list
        :return: fighters[]
        """
        return self.fighters

    def get_map(self):
        """
        Give us the map on a matrix
        :return: map[][]
        """
        return self.map


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
    #object_builder.print_order_fighter_on_map()
    beverate_bandit_manager = BeverageBanditsManager(object_builder.get_fighters(), object_builder.get_map())
    #beverate_bandit_manager.print_first_fighter_target()
    #beverate_bandit_manager.print_range_enemies_with_walls()
    beverate_bandit_manager.print_reachable_enemies_with_walls()
    beverate_bandit_manager.print_nearest_enemies_reachable()
    beverate_bandit_manager.print_chosen_enemy_reachable()
    beverate_bandit_manager.print_move_to_enemy_reachable()
    # data analyse
    #chocolate_charts_manager.execute(False)
    # data visualize
    #ten_digits_after = chocolate_charts_manager.visualize()
    return str(0)


class TestDay15part1(unittest.TestCase):

    def test_day_15_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_15_part_1(lines)
        #assert(pred == res)



if __name__ == '__main__':
    unittest.main()
