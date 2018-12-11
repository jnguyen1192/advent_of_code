import unittest
import numpy as np


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


class Fuel:
    # class that the grid 300*300 with iterator from 1 to 300
    def __init__(self, input=5093, n=300):
        """

        :param n: size of grid N
        """
        self.input = input
        self.n = n
        self.grid_power_level = self.fill_power_grid_level()
        self.grid = np.zeros((n, n))
        self.grid_filter_power_level = np.zeros((n, n))
        self.max_x, self.max_y, self.max_power_level = (0, 0, 0)

    def get_filter_power_level(self, x, y, f_n):
        # return the power level of each filter
        sum_power_level = 0
        for y_ in range(y, y + f_n):
            for x_ in range(x, x + f_n):
                sum_power_level += self.grid_power_level[y_][x_]
        return sum_power_level

    def get_power_level(self, x, y):
        # return the power level of each case
        # from 1 to 300
        x += 1
        y += 1
        rack_id = (((x + 10) * y) + self.input) * (x + 10)
        # print("hundred of digit ", rack_id)
        if rack_id > 99:
            rack_id = int(str(rack_id)[-3])
        else:
            rack_id = 0
        # TODO optimize
        """
        if self.input > 999:
            rack_id = int(str(rack_id)[-3:])
        if self.input > 
        """
        return rack_id - 5

    def fill_power_grid_level(self):
        # return the fill power level grid
        fill_power_level_grid = np.zeros((self.n, self.n))
        for y in range(self.n):
            for x in range(self.n):
                fill_power_level_grid[y][x] = self.get_power_level(x, y)
        return fill_power_level_grid

    def execute(self, f_n):
        # process on grid
        # fill power filter level grid
        for y in range(self.n - f_n):
            for x in range(self.n - f_n):
                self.grid_filter_power_level[y][x] = self.get_filter_power_level(x, y, f_n)
                # keep the max value
                if self.grid_filter_power_level[y][x] > self.max_power_level:
                    self.max_power_level = self.grid_filter_power_level[y][x]
                    self.max_y = y
                    self.max_x = x

    def visualize(self, f_n):
        # return the result
        return self.max_power_level, self.max_x + 1, self.max_y + 1, f_n


def part_2(grid_serial_number):
    # return the answer as x, y, f_n
    n = 300
    max_power_level, max_x, max_y, max_f_n = (0, 0, 0, 0)

    fuel = Fuel(grid_serial_number)  # f_n is the size of the filter
    # browse from one to 300 but in our case we know that size of less than 5 are useless to calculate
    for f_n in range(5, n + 1):
        fuel.execute(f_n)
        power_level, x, y, f_n = fuel.visualize(f_n)
        if power_level > max_power_level:
            print("power_level ", power_level)
            print("x ", x)
            print("y ", y)
            print("f_n ", f_n)
            max_power_level = power_level
            max_x = x
            max_y = y
            max_f_n = f_n
    return str(max_x) + "," + str(max_y) + "," + str(max_f_n)


def data_retrieve(lines):
    # return the new lines traited
    return lines


def data_preparation(data):
    # return the value of input
    return int(data[0])


def day_11_part_2(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    grid_serial_number = data_preparation(data)
    # data modelisation
    fuel = Fuel(grid_serial_number)
    # data analyse
    fuel.execute(3)
    # data visualize
    str_result = part_2(grid_serial_number)
    return str_result


class TestDay11part2(unittest.TestCase):
    def test_day_11_part_2(self):
        lines = input_file()
        res = output_file()
        pred = day_11_part_2(lines)
        print(pred)
        # assert(pred == res)


if __name__ == '__main__':
    unittest.main()
