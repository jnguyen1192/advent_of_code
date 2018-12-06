import unittest
import numpy as np
from pprint import pprint


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

    def get_size_area_from_other_points(self, areas):
        # calcul the size area from other points
        return 0

    def get_manhattan_distance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)


def get_nearest_point(x, y, areas):
    d_min = np.inf
    # each distances to case dot
    distances = []
    nearest_to_other_points = []
    #alpha = "abcdefghijklmnopqrstuvwxyz."
    for index, area in enumerate(areas):
        d = area.get_manhattan_distance(x, y)
        #print(alpha[index].upper(), " ", d)
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
    #np.savetxt("test.out", grid.astype(int), fmt='%i', delimiter=' ')


def day_6_part_1(lines):
    areas = []
    maxx, maxy = (0, 0)
    for line in lines:
        x, y = ([int(l) for l in line.split(',')])
        areas.append(Area(x, y))
        if maxx < x:
            maxx = x
        if maxy < y:
            maxy = y

    # print with the letter
    grid = np.zeros((maxy + 2, maxx + 2), dtype=int)
    # pour chaque cellule qui valent 0 faire un calcul pour definir quel chiffre est le plus proche
    # s il y a egalite mettre un point soit 0
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            # get nearest point and put the good point or dot
            grid[y][x] = get_nearest_point(x, y, areas)

    # all_bound_areas = get_all_bound_areas()
    left_bound_areas = list(set(grid[:, 1]))
    left_bound_areas.remove(52)
    top_bound_areas = list(set(grid[:, 1]))
    top_bound_areas.remove(52)
    bot_bound_areas = list(set(grid[grid.shape[0]-1, ]))  # shape[1] line
    bot_bound_areas.remove(52)
    right_bound_areas = list(set(grid[:, grid.shape[1]-1]))  # shape[1] line
    right_bound_areas.remove(52)
    all_bound_areas = list(set(left_bound_areas+top_bound_areas+bot_bound_areas+right_bound_areas))
    print("all_bound_areas ", all_bound_areas)
    # finite_areas = get_finite_areas()
    finite_areas = list(set(list(range(len(areas)))) - set(all_bound_areas))
    print("finite_areas ", finite_areas)
    # count in matrice
    count = len(np.where(grid == 2)[0])
    # best_area_size = get_best_area_size(finite_areas)
    #for finite_area in finite_areas:

    print()
    #pretty_print(areas, grid)
    return ""


class TestDay6part1(unittest.TestCase):

    def test_day_6_part_1(self):
        lines = input_file()
        lines.sort()
        #res = output_file()
        pred = day_6_part_1(lines)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
