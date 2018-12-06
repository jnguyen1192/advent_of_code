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


def get_nearest_point(x, y, areas):
    # return the nearest point from a position if there are equals we put a 0 as a dot
    d_min = np.inf
    # each distances to case dot
    distances = []
    nearest_to_other_points = []
    for index, area in enumerate(areas):
        d = area.get_manhattan_distance(x, y)
        # if it is the same point return the point
        if d == 0.0:
            return index
        distances.append(d)
        if d <= d_min:
            d_min = d
            nearest_to_other_points.append(index)
    # case dot
    distances.sort()
    if distances[0] == distances[1]:
        return 52
    # case different point return the minimum point
    return nearest_to_other_points[-1]


def pretty_print(areas, grid):
    # for a pretty print
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
             "w", "x", "y", "z", "aa", "bb", "cc", "dd", "ee", "ff",
             "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo",
             "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx",
             "yy", "zz", "."]
    # grid alpha
    grid_char = np.chararray(grid.shape, unicode=True)
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            grid_char[y][x] = alpha[int(grid[y][x])] #alpha[int(grid[y][x])]

    # points on grid
    for index, area in enumerate(areas):
        grid_char[area.y][area.x] = alpha[index].upper()
    print(grid_char)


def normalize_areas(maxx, maxy, factor_to_finite, areas):
    for area in areas:
        area.x = area.x + int((maxx*factor_to_finite)/2)
        area.y = area.y + int((maxy*factor_to_finite)/2)
    return areas


def get_all_borders_areas(grid):
    # return all the areas on the borders
    left_bound_areas = list(set(grid[:, 1]))
    left_bound_areas.remove(52)
    top_bound_areas = list(set(grid[:, 1]))
    top_bound_areas.remove(52)
    bot_bound_areas = list(set(grid[grid.shape[0]-1, ]))  # shape[1] line
    bot_bound_areas.remove(52)
    right_bound_areas = list(set(grid[:, grid.shape[1]-1]))  # shape[1] line
    right_bound_areas.remove(52)
    return list(set(left_bound_areas+top_bound_areas+bot_bound_areas+right_bound_areas))


def set_nearest_point(grid, areas):
    # pour chaque cellule qui valent 0 faire un calcul pour definir quel chiffre est le plus proche
    # s il y a egalite mettre un point soit 0
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            # get nearest point and put the good point or dot
            grid[y][x] = get_nearest_point(x, y, areas)
    return grid


def get_num_probably_finite_areas(all_bound_areas, areas):
    # return the number of the probably finite areas because there was some exceptions
    return list(set(list(range(len(areas)))) - set(all_bound_areas))


def count_number_of_n_in_grid(n, grid):
    # return the size of area
    return len(np.where(grid == n)[0])


def get_best_area_size(num_probably_finite_areas, grid, maxx, maxy):
    best_area_size = 0
    for num_finite_area in num_probably_finite_areas:
        finite_area_size = count_number_of_n_in_grid(num_finite_area, grid)
        # the area is fixed on the previous try which was 9674
        if best_area_size < finite_area_size < 9674:
            best_area_size = finite_area_size
    return best_area_size


def get_distance_coordonate_area(x, y, area):
    return


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
    """
    # transform the grid with nearest point
    grid = set_nearest_point(grid, areas)
    # get all probably infinite areas on the grid borders
    all_probably_finite_areas_on_borders = get_all_borders_areas(grid)
    num_probably_finite_areas = get_num_probably_finite_areas(all_probably_finite_areas_on_borders, areas)
    best_area_size = get_best_area_size(num_probably_finite_areas, grid, maxx, maxy)
    """
    # total_distance_of_all_given_coordonate
    # less than 10000
    less_than = 10000
    # goal : create region with distance inferior 10000

    # first we will test with 32 and the little input
    # for each point on grid without margin for beginning
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            sum = 0
            bool_sum = True
            # parcours chaque areas
            for area in areas:
                # area.get_manhattan_distance(x, y, area)
                sum += area.get_manhattan_distance(x, y)
                # sum_all_coordonate_distance()
                if sum >= less_than:
                    bool_sum = False
                    break
            # set the grid
            grid[y][x] = bool_sum
    np.savetxt("test.txt", grid, delimiter=" ", fmt='%i')
    print(len(np.where(grid == 1)[0]))

    # if sum_all_coordonate < 100000 return True else False

    # print the boolean grid


    return ""


class TestDay5part1(unittest.TestCase):

    def test_day_6_part_2(self):
        text = input_file()
        #res = output_file()
        pred = day_6_part_2(text)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
