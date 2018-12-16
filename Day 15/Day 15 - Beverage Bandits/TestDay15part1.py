import unittest


def input_file():
    """
    Function to read the input file called 'input'
    :return: the lines of the file
    """
    # return the input file in a text
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    """
    Function to read the output file called 'output'
    :return: the text of the file
    """
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
        """
        Get the coordonate of the point
        :return: y and x coordonate
        """
        return self.y, self.x

    def get_y(self):
        """
        Get the coordonate on ordinate
        :return:y coordonate
        """
        return self.y

    def get_x(self):
        """
        Get the coordonate on absciss
        :return:x coordonate
        """
        return self.x


class Fighter:
    """
    A fighter has a lot of characteristics
    """
    def __init__(self, position, classification, map=[], fighters=[], hit_points=200, hit_power=3):
        """
        An Elf is represented by his position and his
        :param classification: can be an Elve or a Gobelin
        :param position: use the class position
        :param fighters: the fighters of the map
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
        """
        Get the classification of the fighter
        :return: 'E' for elfe and 'G' for gobelin
        """
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

    def move_to(self, y, x):
        """
        Move to a specific case
        :param y: y coordonate
        :param x: x coordonate
        """
        self.position = Position(y, x)

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
        """
        Constructor to build the battlefield
        :param fighters: the fighters containing elves and gobelins
        :param map: the map containing the walls
        """
        self.fighters = fighters
        self.map = map
    """
    Action tools
    """
    def next_elves_position(self):
        pass

    def step(self):
        """
        This function illustrate what happened in each step
        """
        # move each fighters by one step
        for fighter in self.fighters:
            self.move_fighter(fighter)
            self.attack_fighter(fighter)

    def execute(self, debug=False):
        # launch the battlefield
        i = 0
        if debug:
            print("Initially:")
            self.print_map()
        while i < 4:
            # compute a step
            self.step()
            if debug:
                if i > 1:
                    print("After ", i, " rounds:")
                else:
                    print("After ", i, " round:")
                self.print_map()
            i += 1

    def visualize(self):
        """
        Get the ten digits after the number of recipes in input
        :return:ten digits in string format
        """
        return ""

    def move_fighter(self, fighter):
        """
        Move the fighter using different rules on the map,
        In range, nearest, chosen, distance and step
        :param fighter:the fighter the will move
        """
        current_fighter = fighter
        # get the current fighter coordonate
        current_fighter_position_y = current_fighter.get_position().get_y()
        current_fighter_position_x = current_fighter.get_position().get_x()

        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # get the available case beside enemies
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        # case we are already beside an enemy
        if not self.is_case_on_cases(in_range, current_fighter_position_y, current_fighter_position_x):
            # get the reachable enemies that are not blocking by fighter or wall
            reachables = self.get_reachable_enemies(current_fighter, in_range)
            # case we can't move
            if len(reachables) != 0:
                # get the nearest available case beside enemies
                nearest = self.get_nearest_enemies(current_fighter, reachables)
                # chose the nearest case sorted by y and x coordonate
                chosen = nearest[0]
                # get the adjacent case distance to the chosen'+'
                # TODO Improve shortest way using personnalize logic
                # for each case available adjacent we note the number of case we need to reach our goal
                # we get the sum of each case and choose the minimum

                adjacent_case_to_move = self.get_adjacent_case_to_move(current_fighter, chosen)
                # move the current fighter
                current_fighter.move_to(*adjacent_case_to_move)

    def attack_fighter(self, fighter):
        """
        Attack if an enemy is around the current fighter,
        choose the lowest hit points and by coordonate.
        :param fighter:the fighter the will attack
        """
        # get the enemies around

        # case no enenmy => end function

        # order them by life, y and x

        # attack the first on the previous list
    """
    Getters
    """
    def get_fighters(self):
        """
        Get the list of fighters
        :return: the list of fighter objects
        """
        return self.fighters

    def get_elves(self):
        """
        Get the list of elves
        :return: the list of fighter objects with classification 'E'
        """
        elves = []
        for fighter in self.fighters:
            if fighter.get_classification() == "E":
                elves.append(fighter)
        return elves

    def get_gobelins(self):
        """
        Get the list of elves
        :return: the list of fighter objects with classification 'G'
        """
        gobelins = []
        for fighter in self.fighters:
            if fighter.get_classification() == "G":
                gobelins.append(fighter)
        return gobelins

    def get_enemies(self, fighter):
        """
        Get the list of enemies of the current fighter
        :param fighter: the current fighter
        :return: list of enemies of the current fighter
        """
        # get the current classification
        fighter_class = fighter.get_classification()
        if fighter_class == "G":
            return self.get_elves()
        if fighter_class == "E":
            return self.get_gobelins()

    def get_adjacent_enemies(self, fighter):
        """
        Get the enemies around the current fighter
        :param fighter:
        :return:
        """
        pass

    def get_adjacent_available_case(self, y, x, cases=[]):
        """
        Get the available adjacent case of a specific case
        :param cases: the list of cases to test
        :param y: y coordonate of the case
        :param x: x coordonate of the case
        :return: the list of available adjacent cases
        """
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
        Get the list of adjacent case available around enemies
        :param current_fighter:  the current fighter
        :param enemies: list of enemies
        :return: list of coordonate of cases
        """
        in_range = []
        for enemy in enemies:
            # get enemy position
            current_enemy_position_y = enemy.get_position().get_y()
            current_enemy_position_x = enemy.get_position().get_x()
            # test if there was no # or fighter in four adjacent side
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

    def get_reachable_area(self, current_fighter):
        """
        Get the available area move from the current fighter
        :param current_fighter: the current fighter
        :return: the list of coordonate of the available area move
        """
        # get available adjacent case
        adjacent_available = []
        # look case adjacent from the current fighter
        # get current fighter position
        current_fighter_position_y = current_fighter.get_position().get_y()
        current_fighter_position_x = current_fighter.get_position().get_x()
        # get adjacent case of the current fighter
        adjacent_available = adjacent_available + self.get_adjacent_available_case(current_fighter_position_y,
                                                                                   current_fighter_position_x,
                                                                                   adjacent_available)
        # get all case available for moving of the current fighter
        old_length = len(adjacent_available)
        while True:
            for aa in adjacent_available:
                adjacent_available = adjacent_available + self.get_adjacent_available_case(aa[0], aa[1], adjacent_available)
            if len(adjacent_available) == old_length:
                break
            old_length = len(adjacent_available)
        return adjacent_available

    def get_reachable_enemies(self, current_fighter, in_range):
        """
        Get the enemy that are reachable and not blocking by a fighter or a wall
        :param current_fighter: the current fighter
        :param in_range: list of coordonate of available case beside enemies
        :return: list of case beside enemies reachable
        """
        # get reachable area
        reachable_enemies = []
        # a reachable area is an area wich our current fighter can move
        reachable_area = self.get_reachable_area(current_fighter)
        # add the available case on reachable list
        for ir in in_range:
            if self.is_case_on_cases(reachable_area, ir[0], ir[1]):
                reachable_enemies.append(ir)
        return reachable_enemies

    def get_distances(self, y, x, reachables):
        """
        Get the distances of the list of reachable cases
        :param y: y coordonate
        :param x: x coordonate
        :param reachables: list of reachable cases
        :return: distances of reachable with their corresponding coordonate
        """
        # get current fighter position
        distances = []
        for reachable in reachables:
            t = abs(y - reachable[0]) + abs(x - reachable[1]), reachable[0], reachable[1]
            distances.append(tuple(t))
        # order the distance by distance
        distances = sorted(distances)
        return distances

    def get_nearest_enemies(self, current_fighter, reachables):
        """
        Get the list of nearest case using list of reachable cases
        :param current_fighter: the current fighter
        :param reachables: list of reachable cases
        :return: list of nearest case
        """
        nearest_enemies = []
        # get the current fighter coordonate
        current_fighter_position_y = current_fighter.get_position().get_y()
        current_fighter_position_x = current_fighter.get_position().get_x()
        distances = self.get_distances(current_fighter_position_y, current_fighter_position_x, reachables)
        # list of same distance of minimum distances
        for distance in distances:
            if distance[0] == distances[0][0]:
                nearest_enemies.append((distance[1], distance[2]))
        if len(nearest_enemies) == 0:
            return [(current_fighter_position_y, current_fighter_position_x)]
        return nearest_enemies

    def get_adjacent_case_to_move(self, current_fighter, chosen):
        """
        Get the best adjacent case to move
        :param current_fighter: the current fighter
        :param chosen: the chosen case beside enemy
        :return: the case with coordonate y and x
        """
        # get the current fighter coordonate
        current_fighter_position_y = current_fighter.get_position().get_y()
        current_fighter_position_x = current_fighter.get_position().get_x()
        # get the adjacent case of the current fighter
        adjacent_case_current_fighter = self.get_adjacent_available_case(current_fighter_position_y, current_fighter_position_x)
        # get the distances sorted by coordonate
        distances = self.get_distances(chosen[0], chosen[1], adjacent_case_current_fighter)
        return distances[0][1], distances[0][2]
    """
    Add objects on map
    """
    def add_current_fighter_on_map(self, current_fighter):
        """
        Add the current fighter on the map as 'E' for elve or 'G' for gobelin
        :param current_fighter: the current fighter
        """
        self.map[current_fighter.get_position().get_y()][
            current_fighter.get_position().get_x()] = current_fighter.get_classification()

    def add_chosen_enemy_on_map(self, chosen):
        """
        Add the chosen enemy on the map as '+'
        :param current_fighter: the current fighter
        """
        self.map[chosen[0]][chosen[1]] = "+"

    def add_enemies_on_map(self, enemies):
        """
        Add the enemies on map as 'G' for gobelins or 'E' for elves
        :param enemies: list of enemies
        """
        for enemy in enemies:
            self.map[enemy.get_position().get_y()][enemy.get_position().get_x()] = enemy.get_classification()

    def add_fighters_on_map(self, map):
        """
        Add the fighters on the map as 'G' for gobelins or 'E' for elves
        :param map: the map where we add the fighters
        """
        for fighter in self.fighters:
            map[fighter.get_position().get_y()][fighter.get_position().get_x()] = fighter.get_classification()

    def add_range_enemies_on_map(self, in_range):
        """
        Add the list of available adjacent case side on map as '?'
        :param in_range: list of coordonate of avalaible adjacent case side
        """
        for ir in in_range:
            self.map[ir[0]][ir[1]] = "?"

    def add_reachable_enemies_on_map(self, reachable_enemies):
        """
        Add the list of reachable case on map as '@'
        :param reachable_enemies: list of coordonate of reachable case
        """
        for re in reachable_enemies:
            self.map[re[0]][re[1]] = "@"

    def add_nearest_enemies_on_map(self, nearest_enemies):
        """
        Add the list of nearest case beside enemy on map as '@'
        :param nearest_enemies: list of coordonate of nearest case
        """
        for ne in nearest_enemies:
            self.map[ne[0]][ne[1]] = "!"
    """
    Boolean functions
    """
    def is_case_available(self, y, x):
        """
        Check if the case is available
        :param y: y coordonate
        :param x: x coordonate
        :return: True if the case is available
        """
        # test wall existence
        if self.map[y][x] == "#":
            return False
        for fighter in self.get_fighters():
            # get fighter position
            fighter_position_y = fighter.get_position().get_y()
            fighter_position_x = fighter.get_position().get_x()
            # test fighter existence
            if fighter_position_y == y and fighter_position_x == x:
                return False
        return True

    def is_case_available_without_current_fighter(self, y, x, current_fighter):
        """
        Check if the case is available but this time ignoring the current_fighter
        :param y: y coordonate
        :param x: x coordonate
        :param current_fighter: the current fighter
        :return: True if the case is available
        """
        # test wall existence
        if self.map[y][x] == "#":
            return False
        # get current fighter position
        current_fighter_position_y = current_fighter.get_position().get_y()
        current_fighter_position_x = current_fighter.get_position().get_x()
        for fighter in self.get_fighters():
            # get fighter position
            fighter_position_y = fighter.get_position().get_y()
            fighter_position_x = fighter.get_position().get_x()
            # test current fighter existence
            if not (current_fighter_position_y == fighter_position_y and current_fighter_position_x == fighter_position_x):
                # test fighter existence
                if fighter_position_y == y and fighter_position_x == x:
                    return False
        return True

    def is_case_on_cases(self, cases, y, x):
        """
        Check if the coordonate is in a specific list
        :param cases: the list of cases
        :param y: y coordonate of the case
        :param x: x coordonate of the case
        :return: True if the case exists on the specific list
        """
        for case in cases:
            if case[0] == y and case[1] == x:
                return True
        return False
    """
    Print examples
    """
    # Targets current with list enemies
    def print_first_fighter_target(self):
        """
        Print the targets example
        """
        print("Targets :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        self.map[current_fighter.get_position().get_y()][current_fighter.get_position().get_x()] = current_fighter.get_classification()
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # print
        self.add_enemies_on_map(enemies)
        self.print_map()

    # In range current with list enemies and walls
    def print_range_enemies_with_walls(self):
        """
        Print the in range example
        """
        print("In range :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # get available case
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        # print
        self.add_range_enemies_on_map(in_range)
        self.add_enemies_on_map(enemies)
        self.print_map()

    # Reachable current with list enemies reachable
    def print_reachable_enemies_with_walls(self):
        """
        Print the reachable example
        """
        print("Reachable :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # get the available case beside enemies
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        # get the reachable enemies that are not blocking by fighter or wall
        reachable = self.get_reachable_enemies(current_fighter, in_range)
        # print
        self.add_current_fighter_on_map(current_fighter)
        self.add_enemies_on_map(enemies)
        self.add_reachable_enemies_on_map(reachable)
        self.print_map()

    # Nearest for each dot put the number of case to reach enemy
    def print_nearest_enemies_reachable(self):
        """
        Print the nearest example
        """
        print("Nearest :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # get the available case beside enemies
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        # get the reachable enemies that are not blocking by fighter or wall
        reachables = self.get_reachable_enemies(current_fighter, in_range)
        # get the nearest available case beside enemies
        nearest = self.get_nearest_enemies(current_fighter, reachables)
        # print
        self.add_current_fighter_on_map(current_fighter)
        self.add_enemies_on_map(enemies)
        self.add_nearest_enemies_on_map(nearest)
        self.print_map()

    # Chosen return the coordonate to attack
    def print_chosen_enemy_reachable(self):
        """
        Print the chosen example
        """
        print("Chosen :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # get the available case beside enemies
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        # get the reachable enemies that are not blocking by fighter or wall
        reachables = self.get_reachable_enemies(current_fighter, in_range)
        # get the nearest available case beside enemies
        nearest = self.get_nearest_enemies(current_fighter, reachables)
        # chose the nearest case sorted by y and x coordonate
        chosen = nearest[0]
        # print
        self.add_current_fighter_on_map(current_fighter)
        self.add_enemies_on_map(enemies)
        self.add_chosen_enemy_on_map(chosen)
        self.print_map()

    # Move_to_chosen move to the chosen using priority of x and y
    def print_step(self):
        """
        Print the step example
        """
        print("Move :")
        # choose the first fighter
        current_fighter = self.fighters[0]
        # choose his enemies
        enemies = self.get_enemies(current_fighter)
        # get the available case beside enemies
        in_range = self.get_range_from_enemies(current_fighter, enemies)
        # get the reachable enemies that are not blocking by fighter or wall
        reachables = self.get_reachable_enemies(current_fighter, in_range)
        # case we can't move
        if len(reachables) != 0:
            # get the nearest available case beside enemies
            nearest = self.get_nearest_enemies(current_fighter, reachables)
            # chose the nearest case sorted by y and x coordonate
            chosen = nearest[0]
            # get the adjacent case distance to the chosen'+'
            # TODO Improve shortest way
            adjacent_case_to_move = self.get_adjacent_case_to_move(current_fighter, chosen)
            # move the current fighter
            current_fighter.move_to(*adjacent_case_to_move)
        # print
        self.add_current_fighter_on_map(current_fighter)
        self.add_enemies_on_map(enemies)
        #self.add_chosen_enemy_on_map(chosen)
        self.print_map()

    def print_order_fighter_on_map(self):
        """
        Print ordered fighter example
        """
        for index, fighter in enumerate(self.fighters):
            self.map[fighter.get_position().get_y()][fighter.get_position().get_x()] = str(index+1)
        self.print_map()

    def print_map(self):
        """
        print the map
        """
        from copy import deepcopy
        map_with_fighter = deepcopy(self.map)
        self.add_fighters_on_map(map_with_fighter)
        str_map = ""
        for line in map_with_fighter:
            str_map += "".join(line) + "\n"
        print(str_map)


class ObjectBuilder:
    """
    Builder to instanciate objects from the input
    """
    def __init__(self, lines):
        """
        Build the fighters and the map from the input
        :param lines: the lines of the input file
        """
        self.lines = lines
        self.fighters = self.build_fighters()
        self.map = self.build_map()

    def find_all_fighter(self, line, y, classification):
        """
        Find all the fighter from the input file
        :param line: the line to analyse
        :param y: the number of line to analyse
        :param classification: the fighter classification as 'E' for elve or 'G' for gobelin
        :return: the list of tuple of specific classification fighter
        """
        x = 0
        # find every specific classification fighter
        while line.find(classification, x) != -1:
            x = line.find(classification, x)
            if x == -1:
                break
            finder = y, x, classification
            # return the corresponding tuple on a list efficiently
            yield tuple(finder)
            x += 1

    def build_map(self):
        """
        Create the map containing walls and dots while removing the fighter
        """
        # get the map from the input file
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
        """
        Create the list of fighter objects using input file
        """
        # return a list of carts as (x, y, direction of cart)
        fighters = []
        fighters_object = []
        y = 0
        # browse each line of the input file
        for line in self.lines:
            # case elve
            elves = self.find_all_fighter(line, y, "E")
            if elves != 0:
                fighters += [e for e in self.find_all_fighter(line, y, "E")]
            # case gobelin
            gobelins = self.find_all_fighter(line, y, "G")
            if gobelins != 0:
                fighters += [g for g in self.find_all_fighter(line, y, "G")]
            y += 1
        # sort the fighters by their coordonate y and x
        fighters = sorted(fighters)
        # browse on list of tuple
        for fighter in fighters:
            # create each fighter object
            fighters_object.append(Fighter(Position(fighter[0], fighter[1]), fighter[2]))
        return fighters_object

    def remove_fighters_from_map(self, fighter_objects):
        """
        Remove the fighters from the map
        :param fighter_objects: list of the fighter objects
        """
        for fighter in fighter_objects:
            self.map[fighter.get_position().get_y()][fighter.get_position().get_x()] = "."

    def get_fighters(self):
        """
        Give us the fighters on a list
        :return: list of fighters object
        """
        return self.fighters

    def get_map(self):
        """
        Give us the map on a matrix
        :return: the list of elements of map
        """
        return self.map


def data_retrieve(lines):
    """
    Retrieve the data from the file
    :param lines: lines of input file
    :return: the new lines traited
    """
    return lines


def day_15_part_1(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    object_builder = ObjectBuilder(data)
    #object_builder.print_order_fighter_on_map()
    # data modelisation
    beverate_bandit_manager = BeverageBanditsManager(object_builder.get_fighters(), object_builder.get_map())
    #beverate_bandit_manager.print_first_fighter_target()
    #beverate_bandit_manager.print_range_enemies_with_walls()
    #beverate_bandit_manager.print_reachable_enemies_with_walls()
    #beverate_bandit_manager.print_nearest_enemies_reachable()
    #beverate_bandit_manager.print_chosen_enemy_reachable()
    #beverate_bandit_manager.print_step()
    # data analyse
    beverate_bandit_manager.execute(True)
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
