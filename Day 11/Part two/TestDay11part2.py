import unittest
import numpy as np
import re


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


class Cloud_point:
    # class that illustrate a node containing header, child nodes and metadata entries
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def step(self):
        # get the current velocity
        vx, vy = self.velocity.get_velocity()
        # move into the next position
        self.position.move(vx, vy)

    def back_step(self):
        # get the current velocity
        vx, vy = self.velocity.get_velocity()
        # move into the next position
        self.position.move(-vx, -vy)

    def get_position_x(self):
        # return the x position
        return self.position.get_x()

    def get_position_y(self):
        # return the y position
        return self.position.get_y()


class Cloud:
    # class that illustrate all the points of the cloud with the respectives velocities
    def __init__(self, cloud_points, velocities):
        self.cloud_points = cloud_points
        self.velocities = velocities
        self.max_y, self.max_x = self.get_dimension_max()
        self.cloud = np.full((self.max_y, self.max_x), False)
        self.string_cloud = ""

    def visualize(self):
        # return the final string
        return self.string_cloud

    def str_cloud(self, max_x, min_x, max_y, min_y):
        # return the cloud in a string from a little array
        self.cloud = np.full((max_y - min_y, max_x - min_x), False)
        # get number line of cloud
        number_line_cloud = self.cloud.shape[1]
        # get number column of cloud
        number_column_cloud = self.cloud.shape[0]
        # add cloud_points to cloud
        for cloud_point in self.cloud_points:
            self.cloud[cloud_point.get_position_y()-1-min_y][cloud_point.get_position_x()-1-min_x] = True
        # create the cloud
        string_cloud = ""
        for i in range(number_column_cloud):
            for j in range(number_line_cloud):
                if self.cloud[i][j]:
                    string_cloud += "#"
                else:
                    string_cloud += "."
            string_cloud += "\n"
        return string_cloud


    def exec(self):
        # execute the print cloud step by step
        i = 0
        while True:
            #print("step ", i)
            i += 1
            # get dimension shape
            break


def data_retrieve(lines):
    # return the new lines traited
    data = []
    for line in lines:
        data.append([int(d) for d in re.findall(r'-?\d+', line)])
    return data


def data_preparation(data):
    # return the cloud points and velocities associated
    for raw in data:
        raw[0] = raw[1]
    return raw


def day_11_part_2(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    cloud_points, velocities = data_preparation(data)
    # data modelisation
    cloud = Cloud(cloud_points, velocities)
    # data analyse
    cloud.exec()
    # data visualize
    str_cloud = cloud.visualize()
    return str_cloud


class TestDay11part2(unittest.TestCase):

    def test_day_11_part_2(self):
        lines = input_file()
        res = output_file()
        pred = day_11_part_2(lines)
        assert(pred == res)


if __name__ == '__main__':
    unittest.main()
