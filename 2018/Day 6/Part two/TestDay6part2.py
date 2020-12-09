import unittest
import numpy as np


def input_file():
    # return the input_test file in a text
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    # read line of output_1 file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class Area:
    # define the area object containing coordinate and size
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_manhattan_distance(self, x, y):
        # return the manhattan distance between two points
        return abs(self.x - x) + abs(self.y - y)


def init_areas_with_bounds(lines):
    # create the areas with the dimension of grid
    areas = []
    maxx, maxy = (0, 0)
    for line in lines:
        x, y = ([int(l) for l in line.split(',')])
        areas.append(Area(x, y))
        if maxx < x:
            maxx = x
        if maxy < y:
            maxy = y
    return maxx, maxy, areas


def normalize_areas(maxx, maxy, factor_to_finite, areas):
    # change the area coordonate following the factor to finite area
    for area in areas:
        area.x = area.x + int((maxx*factor_to_finite)/2)
        area.y = area.y + int((maxy*factor_to_finite)/2)
    return areas


def count_number_of_n_in_grid(n, grid):
    # return the size of the region
    return len(np.where(grid == n)[0])


def set_grid_using_areas_with_inertie(grid, areas, inertie):
    # transform the grid into a boolean grid which true represent the region
    # for each point on grid with margin
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            # init for each step the variables
            sum = 0
            bool_sum = True
            # parcours chaque areas
            for area in areas:
                # sum of all coordonate distance()
                sum += area.get_manhattan_distance(x, y)
                # if sum_all_coordonate < 100000 return True else False
                if sum >= inertie:
                    bool_sum = False
                    break
            # set the grid
            grid[y][x] = bool_sum


def day_6_part_2(lines):
    # factor for the margin if our grid is 3*3 and
    # the factor is 2 we obtains 9*9 with the areas
    # on the middle of the grid
    factor_to_finite = 2
    # get_areas_and_dimension
    maxx, maxy, areas = init_areas_with_bounds(lines)
    # add area for a special grid using a factor for the margin
    grid = np.zeros((int(maxy*factor_to_finite), int(maxx*factor_to_finite)), dtype=int)
    # set areas coordonate before add them
    areas = normalize_areas(maxx, maxy, factor_to_finite, areas)
    # total_distance_of_all_given_coordonate
    # less than 10000
    inertie = 10000  # or 32 for the little input_test
    # goal : create region with distance inferior 10000
    # transform grid to a region using areas with a minimum inertie
    set_grid_using_areas_with_inertie(grid, areas, inertie)
    # count the number of true in the grid which represent the region
    total_distance_of_all_given_coordonate = count_number_of_n_in_grid(True, grid)
    return str(total_distance_of_all_given_coordonate)


class TestDay5part1(unittest.TestCase):

    def test_day_6_part_2(self):
        text = input_file()
        res = output_file()
        pred = day_6_part_2(text)
        assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
