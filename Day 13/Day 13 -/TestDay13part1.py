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
    def __init__(self, y, x, direction):
        """

        :param y: the coordonate y from 0 to n to the down
        :param x: the coordonate x from 0 to n to the right
        :param direction: the direction representing as a pick of an arrow
        """
        self.y = y
        self.x = x
        self.direction = direction

    def get_direction(self):
        """
        This function is useful to get that attribute
        :return: direction of the cart to know where it will go
        """
        return self.direction

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

    def move(self):
        """
        This function calculate the next position of the cart
        :return: the next position y x of a cart
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
    # class that permits to create all object
    def __init__(self, lines):
        self.carts = []
        self.lines = lines
        self.carts = self.build_carts()
        self.map = self.build_map()

    def print_map(self):
        # print the map using the matrix map
        for index, values in enumerate(self.map):
            print(index, "\t\t\t", values)

    def print_carts(self):
        # print the map using the matrix map
        print(self.carts)

    def build_carts(self):
        # return a list of carts as (x, y, direction of cart)
        carts = []
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
        return sorted(carts)

    def build_map(self):
        # return the matrix of the map
        map = []
        for line in self.lines:
            line_list = []
            for i in line:
                line_list.append(i)
            map.append(line_list)
        return map


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
    object_builder.print_map()
    object_builder.print_carts()
    print("First carts ", object_builder.map[15][25])
    #plants_life_being = GenerationPlant(input_line, constraints)
    # data analyse
    #plants_life_being.execute()
    # data visualize
    #sum_number_of_plants_last_generation = plants_life_being.visualize()
    return str(0)


class TestDay13part1(unittest.TestCase):

    def test_day_13_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_13_part_1(lines)
        print(pred)
        #assert(pred == res)


if __name__ == '__main__':
    unittest.main()
