import unittest


def input_file():
    # return the input_test file in a text
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    # read line of output_1 file
    file = open('output', 'r')
    res = file.read()
    file.close()
    return res


class Cart:
    """
    A cart is represented by his coordonate and his direction,
    its moves are specific during an intersection.
    """
    def __init__(self, y, x, direction, map, per_intersection_memory=0):
        """

        :param y: the coordonate y from 0 to n to the down
        :param x: the coordonate x from 0 to n to the right
        :param direction: the direction representing as a pick of an arrow
        """
        self.y = y
        self.x = x
        self.direction = direction
        self.map = map
        self.per_intersection_memory = per_intersection_memory

    def get_direction(self):
        """
        This function is useful to get that attribute
        :return: direction of the cart to know where it will go
        """
        return self.direction

    def get_per_intersection_memory(self):
        # get the current intersection memory
        return self.per_intersection_memory

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
            self.direction_south()
        elif current_direction == "^":
            self.direction_east()
        elif current_direction == "<":
            self.direction_north()
        else:
            self.direction_west()

    def go_straight(self):
        # nothing to change
        pass

    def go_left(self):
        current_direction = self.get_direction()
        if current_direction == ">":
            self.direction_north()
        elif current_direction == "^":
            self.direction_west()
        elif current_direction == "<":
            self.direction_south()
        else:
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
    Builder to instanciate objects from the input_test
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
        # browse on list of tuple
        for cart in carts:
            # create each cart object
            carts_object.append(Cart(cart[0], cart[1], cart[2], self.map))
        # remove the carts from the map
        self.remove_carts_from_map(carts_object)
        return carts_object

    def remove_carts_from_map(self, carts_object):
        for cart in carts_object:
            self.map[cart.get_position_yx()[0]][cart.get_position_yx()[1]] = " "

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

        :param collision_position: coordonate of the first collision
        :param last_position: coordonate of the last position of cart

        :param collision: True if there was a collision
        :param is_last_cart: True if there was only one cart alive
        """
        self.carts = carts
        self.map = map
        self.collision_position = (0, 0)
        self.last_position = (0, 0)
        self.collision = False
        self.is_last_cart = False

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

    def the_last_cart_position(self, cart):
        """
        The collision between two carts happened
        """
        self.last_position = cart.get_position_yx

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
            next_position = curr_position[0] + 1, curr_position[1]
        return next_position

    def are_they_on_collision(self, cart):
        """
        We know if it will be a collision between the current cart and an other
        :param cart: the current cart
        :return: True if there was a cart with the current cart position
        """
        # get the next position of current cart
        #next_position = self.get_next_position_cart(cart)
        current_position = cart.get_position_yx()
        two_cars = 0
        # browse in carts
        for cart in self.carts:
            # if there was a cart here return True
            if current_position == cart.get_position_yx():
                two_cars += 1
        if two_cars == 2:
            self.collision_position = current_position
            return True
        return False

    def sort_carts(self):
        """
        update the carts order by horizontally then vertically
        """
        carts_to_sorted = []
        for cart in self.carts:
            carts_to_sorted.append(tuple((cart.get_position_yx()[0], cart.get_position_yx()[1], cart.get_direction(), cart.get_per_intersection_memory())))
        carts_to_sorted = sorted(carts_to_sorted)
        self.carts = []
        # browse on list of tuple
        for cart in carts_to_sorted:
            # create each cart object
            self.carts.append(Cart(cart[0], cart[1], cart[2], self.map, cart[3]))

    def remove_carts_on_collision(self, cart):
        """
        Remove the two carts on collision from the list of carts
        :param cart: the cart to test for the collision
        """
        #next_position = self.get_next_position_cart(cart)
        current_position = cart.get_position_yx()
        two_cars = 0
        # browse in carts
        for cart in self.carts:
            # if there was a cart here return True
            if current_position == cart.get_position_yx():
                two_cars += 1
        # use the position to the collision to remove carts
        if two_cars == 2:
            carts_alive = []
            for cart in self.carts:
                if cart.get_position_yx() != current_position:
                    carts_alive.append(cart)
            self.carts = carts_alive

    def run(self):
        # launch the execution of cart on the map only if there was no collision
        while not self.is_last_cart:
            # browse in each carts
            # refresh order
            # sort carts
            self.sort_carts()
            for cart in self.carts:
                cart.move()
                # determine if it will be a collision between the current cart and another
                if self.are_they_on_collision(cart):
                    # set the final parameter and leave the loop
                    self.there_was_a_collision()
                    # remove all carts on collision
                    self.remove_carts_on_collision(cart)
            # get the last position
            if len(self.carts) == 1:
                self.last_position = self.carts[0].get_position_yx()
                self.is_last_cart = True
                break

    def print_map_with_carts(self, pos_x=(-1, -1)):
        from copy import deepcopy
        map_with_carts = deepcopy(self.map)

        for cart in self.carts:
            y, x = cart.get_position_yx()
            map_with_carts[y][x] = cart.get_direction()
        y, x = pos_x
        if y != -1:
            map_with_carts[y][x] = "X"
        string_map = ""
        for line in map_with_carts:
            string_map += "".join(line) + "\n"
        print(string_map)

    def visualize(self):
        return self.last_position[1], self.last_position[0]

    def print_map(self):
        # print the map using the matrix map
        for index, values in enumerate(self.map):
            print(index, "\t\t\t", values)


def data_retrieve(lines):
    # return the new lines traited
    # count nb cart
    return lines


def data_preparation(lines):
    # return the value of input_test
    return lines


def day_13_part_2(lines):
    # data retrieve
    lines = data_retrieve(lines)
    # data preparation
    object_builder = ObjectBuilder(lines)
    # data modelisation
    mine_cart_madness = MineCartMadnessManager(object_builder.get_carts(), object_builder.get_map())
    # data analyse
    mine_cart_madness.run()
    # data visualize
    last_postion = mine_cart_madness.visualize()
    return str(last_postion[0]) + "," + str(last_postion[1])


class TestDay13part2(unittest.TestCase):

    def test_day_13_part_2(self):
        lines = input_file()
        res = output_file()
        pred = day_13_part_2(lines)
        assert(pred == res)


if __name__ == '__main__':
    unittest.main()
