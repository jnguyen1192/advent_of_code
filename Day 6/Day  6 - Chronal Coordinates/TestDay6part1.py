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
    nearest_to_other_points = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for index, area in enumerate(areas):
        d = area.get_manhattan_distance(x, y)
        print(alpha[index].upper(), " ", d)
        if d <= d_min:
            d_min = d
            nearest_to_other_points.append(index)
    return nearest_to_other_points


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
    """
    d_min = np.inf
    longest_distance_other_points = []
    for index, area in enumerate(areas):
        d = area.get_distance_from_other_points(areas)
        if d < d_min:
            d_min = d
            nearest_other_points.append(index)
    print(longest_distance_other_points)
    """
    grid = np.zeros((maxy+1, maxx+1))
    # grille a completer pour avoir les areas
    for index, obj in enumerate(areas):
        #print(obj.y, " ", obj.x, " ", index)
        grid[obj.y][obj.x] = (index + 1) * 100
    pprint(grid)
    get_nearest_point(0, 5, areas)
    # pour chaque cellule qui valent 0 faire un calcul pour definir quel chiffre est le plus proche
    # s il y a egalite mettre un point soit 0
    """
    for y in grid.shape[0]:
        for x in grid.shape[1]:
            # get nearest point
    """
    return ""


class TestDay6part1(unittest.TestCase):

    def test_day_6_part_1(self):
        lines = input_file()
        #res = output_file()
        pred = day_6_part_1(lines)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
