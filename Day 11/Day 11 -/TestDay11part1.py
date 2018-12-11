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
    def __init__(self, input=5093, n=300, f_n=3):
        """

        :param n: size of grid N
        :param f_n: size of filter
        """
        self.input = input
        self.n = n
        self.f_n = f_n
        self.grid = np.zeros((n, n))
        self.grid_power_level = np.zeros((n, n))
        self.grid_filter_power_level = np.zeros((n, n))
        self.max_x, self.max_y, self.max_power_level = (0, 0, 0)

    def get_filter_power_level(self, x, y):
        # return the power level of each filter
        sum_power_level = 0
        for y_ in range(y, y + 3):
            for x_ in range(x, x + 3):
                sum_power_level += self.grid_power_level[y_][x_]
        return sum_power_level

    def get_power_level(self, x, y):
        # return the power level of each case
        # from 1 to 300
        x += 1
        y += 1
        rack_id = (((x + 10)*y) + self.input) * (x + 10)
        #print("hundred of digit ", rack_id)
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

    def execute(self):
        # process on grid
        # fill power level grid
        for y in range(self.n):
            for x in range(self.n):
                self.grid_power_level[y][x] = self.get_power_level(x, y)
        # fill power filter level grid
        for y in range(self.n - self.f_n):
            for x in range(self.n - self.f_n):
                self.grid_filter_power_level[y][x] = self.get_filter_power_level(x, y)
                # keep the max value
                if self.grid_filter_power_level[y][x] > self.max_power_level:
                    self.max_power_level = self.grid_filter_power_level[y][x]
                    self.max_y = y
                    self.max_x = x

    def visualize(self):
        # return the result
        return self.max_x+1, self.max_y+1


def data_retrieve(lines):
    # return the new lines traited
    return lines


def data_preparation(data):
    # return the value of input
    return int(data[0])


def day_11_part_1(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    grid_serial_number = data_preparation(data)
    # data modelisation
    fuel = Fuel(grid_serial_number)
    # data analyse
    fuel.execute()
    # data visualize
    x, y = fuel.visualize()
    return str(x) + "," + str(y)


class TestDay10part1(unittest.TestCase):

    def test_day_11_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_11_part_1(lines)
        print(pred)
        #assert(pred == res)


if __name__ == '__main__':
    unittest.main()
