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


class Cart:
    """
    A cart is represented by his coordonate and his direction,
    its moves are specific during an intersection.
    """
    def __init__(self, y, x, direction, map):
        """

        :param y: the coordonate y from 0 to n to the down
        :param x: the coordonate x from 0 to n to the right
        :param direction: the direction representing as a pick of an arrow
        """
        self.y = y
        self.x = x
        self.direction = direction
        self.map = map
        self.per_intersection_memory = 0

    def get_direction(self):
        """
        This function is useful to get that attribute
        :return: direction of the cart to know where it will go
        """
        return self.direction

    def get_position_yx(self):
        """
        Get the position of the cart
        :return: the position y x of the current cart
        """
        return self.y, self.x

    def go_east(self):
        """
        This function permit us to the move the at the right
        """
        self.x += 1

    def go_north(self):
        """
        This function permit us to move the cart up
        """
        self.y -= 1

    def go_west(self):
        """
        This function permit us to the move the at the left
        """
        self.x -= 1

    def go_south(self):
        """
        This function permit us to move the cart down
        """
        self.y += 1

    def direction_south(self):
        self.direction = "v"

    def direction_east(self):
        self.direction = ">"

    def direction_north(self):
        self.direction = "^"

    def direction_west(self):
        self.direction = "<"

    def go_right(self):
        current_direction = self.get_direction()
        if current_direction == ">":
            #self.go_south()
            self.direction_south()
        elif current_direction == "^":
            #self.go_east()
            self.direction_east()
        elif current_direction == "<":
            #self.go_north()
            self.direction_north()
        else:
            #self.go_west()
            self.direction_west()

    def go_straight(self):
        current_direction = self.get_direction()
        if current_direction == ">":
            #self.go_east()
            self.direction_east()
        elif current_direction == "^":
            #self.go_north()
            self.direction_north()
        elif current_direction == "<":
            #self.go_west()
            self.direction_west()
        else:
            #self.go_south()
            self.direction_south()

    def go_left(self):
        current_direction = self.get_direction()
        if current_direction == ">":
            #self.go_north()
            self.direction_north()
        elif current_direction == "^":
            #self.go_west()
            self.direction_west()
        elif current_direction == "<":
            #self.go_south()
            self.direction_south()
        else:
            #self.go_east()
            self.direction_east()

    def incr_per_intersection_memory(self):
        self.per_intersection_memory = (self.per_intersection_memory + 1) % 3

    def update_direction(self):
        """
        This function permits to update the direction using the current case
        """
        next_case_coord = self.y, self.x
        next_case = self.map[next_case_coord[0]][next_case_coord[1]]
        direction = self.get_direction()
        if next_case == "+":
            if self.per_intersection_memory == 0:
                self.go_left()
            elif self.per_intersection_memory == 1:
                self.go_straight()
            else:
                self.go_right()
            self.incr_per_intersection_memory()
        elif next_case == "/":
            if direction == ">":
                self.direction_north()
            elif direction == "^":
                self.direction_east()
            elif direction == "<":
                self.direction_south()
            else:
                self.direction_west()
        elif next_case == "\\":
            if direction == ">":
                self.direction_south()
            elif direction == "^":
                self.direction_west()
            elif direction == "<":
                self.direction_north()
            else:
                self.direction_east()
        #print(self.get_direction())

    def move(self):
        """
        This function calculate the next position of the cart and move it
        """
        current_direction = self.get_direction()
        if current_direction == ">":
            self.go_east()
        elif current_direction == "^":
            self.go_north()
        elif current_direction == "<":
            self.go_west()
        else:
            self.go_south()
        self.update_direction()


def find_all_direction(line, y, direction):
    finder = False
    x = 0
    # direction
    # first iteration
    while line.find(direction, x) != -1:
        x = line.find(direction, x)
        if x == -1:
            break
        finder = y, x, direction
        x += 1
    if not finder:
        return 0
    return tuple(finder)


class ObjectBuilder:
    """
    Builder to instanciate objects from the input
    """
    def __init__(self, lines):
        self.carts = []
        self.lines = lines
        self.map = self.build_map()
        self.carts = self.build_carts()

    def print_carts(self):
        # print the map using the matrix map
        print(self.carts)

    def build_carts(self):
        # return a list of carts as (x, y, direction of cart)
        carts = []
        carts_object = []
        y = 0
        for line in self.lines:
            right_direction = find_all_direction(line, y, ">")
            if right_direction != 0:
                carts.append(find_all_direction(line, y, ">"))
            left_direction = find_all_direction(line, y, "<")
            if left_direction != 0:
                carts.append(find_all_direction(line, y, "<"))
            up_direction = find_all_direction(line, y, "^")
            if up_direction != 0:
                carts.append(find_all_direction(line, y, "^"))
            down_direction = find_all_direction(line, y, "v")
            if down_direction != 0:
                carts.append(find_all_direction(line, y, "v"))
            y += 1
        carts = sorted(carts)
        print(carts)
        # browse on list of tuple
        for cart in carts:
            # create each cart object
            carts_object.append(Cart(cart[0], cart[1], cart[2], self.map))
        return carts_object

    def build_map(self):
        # return the matrix of the map
        map = []
        for line in self.lines:
            line_list = []
            for i in line:
                line_list.append(i)
            map.append(line_list)
        return map

    def get_carts(self):
        """
        Give us the carts on a list
        :return: carts[]
        """
        return self.carts

    def get_map(self):
        """
        Give us the map on a matrix
        :return: map[][]
        """
        return self.map


class MineCartMadnessManager:
    """
    A mine cart madness manager allow us to move carts on the map and find the collision
    """
    def __init__(self, carts, map):
        """

        :param carts: list of carts
        :param map: matrix of map containing turns and intersections
        """
        self.carts = carts
        self.map = map
        self.collision_position = (0, 0)
        self.collision = False

    def is_collision(self):
        """
        Determine if there was a collision between two carts
        :return: True if there was a collision
        """
        return self.collision

    def there_was_a_collision(self):
        """
        The collision between two carts happened
        """
        self.collision = True

    def get_next_position_cart(self, cart):
        """
        Get the next position of the current cart
        :param cart: the cart we want to evaluate
        :return: the next position of the cart
        """
        next_position = 0
        curr_direction = cart.get_direction()
        curr_position = cart.get_position_yx()
        if curr_direction == ">":
            next_position = curr_position[0], curr_position[1] + 1
        elif curr_direction == "^":
            next_position = curr_position[0] - 1, curr_position[1]
        elif curr_direction == "<":
            next_position = curr_position[0], curr_position[1] - 1
        elif curr_direction == "v":
            next_position = curr_position[0] + 1, curr_position[1] - 1
        return next_position

    def will_collision(self, cart):
        """
        We know if it will be a collision in the next move
        :param cart: the current cart
        :return: True if there was a cart in front of the current cart
        """

        # get the next position of current cart
        next_position = self.get_next_position_cart(cart)
        current_position = cart.get_position_yx()
        # browse in carts
        for cart in self.carts:
            # if there was a cart here return True
            # First case in the right position they enter on collision
            if next_position == cart.get_position_yx():
                return True
            # Second case at the same time they enter on collision
            if next_position == self.get_next_position_cart(cart) and current_position != cart.get_position_yx():
                print("boom")
                return True
        return False

    def run(self):
        # launch the execution of cart on the map only if there was no collision
        turn = 0
        while not self.is_collision():
            # browse in each carts
            #self.print_map()
            #print(turn)
            turn += 1
            for cart in self.carts:
                # determine if it will be a collision between the current cart and another
                if self.will_collision(cart):
                    # set the final parameter and leave the loop
                    self.collision_position = cart.get_position_yx()
                    self.there_was_a_collision()
                    self.print_map_with_carts(cart.get_position_yx())
                    break
                cart.move()
                #self.print_map_with_carts()

    def print_map_with_carts(self, pos_X):
        from copy import deepcopy
        map_with_carts = deepcopy(self.map)

        for cart in self.carts:
            y, x = cart.get_position_yx()
            map_with_carts[y][x] = cart.get_direction()
        y, x = pos_X
        map_with_carts[y][x] = "X"
        string_map = ""
        for line in map_with_carts:
            string_map += "".join(line) + "\n"
        print(string_map)

    def visualize(self):
        return self.collision_position[1], self.collision_position[0]

    def print_map(self):
        # print the map using the matrix map
        for index, values in enumerate(self.map):
            print(index, "\t\t\t", values)


def data_retrieve(lines):
    # return the new lines traited
    # count nb cart
    return lines


def data_preparation(lines):
    # return the value of input
    return lines


def day_13_part_1(lines):
    # data retrieve
    lines = data_retrieve(lines)
    # data preparation
    object_builder = ObjectBuilder(lines)
    # data modelisation
    mine_cart_madness = MineCartMadnessManager(object_builder.get_carts(), object_builder.get_map())
    # data analyse
    mine_cart_madness.run()
    # data visualize
    collision_position = mine_cart_madness.visualize()
    return str(collision_position[0]) + "," + str(collision_position[1])


class TestDay13part1(unittest.TestCase):

    def test_day_13_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_13_part_1(lines)
        print(pred)
        #assert(pred == res)


if __name__ == '__main__':
    unittest.main()
