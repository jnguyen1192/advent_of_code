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
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class Position:
    # class that illustrate a point
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        # return the current position
        return self.x, self.y

    def get_x(self):
        # return the current position
        return self.x

    def get_y(self):
        # return the current position
        return self.y

    def set_position(self, x, y):
        # set the current position
        self.x = x
        self.y = y

    def move(self, vx, vy):
        # move into the next position using
        self.x += vx
        self.y += vy


class Velocity:
    # class that illustrate a velocity
    def __init__(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def get_velocity(self):
        # return the velocity
        return self.vx, self.vy


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

    def step_cloud(self):
        # move all cloud by one step
        for i in range(len(self.cloud_points)):
            self.cloud_points[i].step()

    def back_step_cloud(self):
        # move all cloud by one step
        for i in range(len(self.cloud_points)):
            self.cloud_points[i].back_step()

    def get_dimension_max(self):
        # get the max x and y of the cloud
        max_x, max_y = (0, 0)
        for i in range(len(self.cloud_points)):
            if max_x < self.cloud_points[i].get_position_x():
                max_x = self.cloud_points[i].get_position_x()
            if max_y < self.cloud_points[i].get_position_y():
                max_y = self.cloud_points[i].get_position_y()
        return max_y, max_x

    def str_cloud(self, max_x, min_x, max_y, min_y):
        # print the cloud using array of points
        self.cloud = np.full((max_y - min_y, max_x - min_x), False)
        # get number line of cloud
        number_line_cloud = self.cloud.shape[1]
        # get number column of cloud
        number_column_cloud = self.cloud.shape[0]
        # add cloud_points to cloud
        for cloud_point in self.cloud_points:
            self.cloud[cloud_point.get_position_y()-1-min_y][cloud_point.get_position_x()-1-min_x] = True
        # print the cloud
        string_cloud = ""
        for i in range(number_column_cloud):
            for j in range(number_line_cloud):
                if self.cloud[i][j]:
                    string_cloud += "#"
                else:
                    string_cloud += "."
            string_cloud += "\n"
        return string_cloud

    def get_shape_cloud_dimension(self):
        # return the border min max of x y
        max_x, max_y = (0, 0)
        min_x, min_y = (10000000, 10000000)
        # get the border to know how positionning the points
        for cloud_point in self.cloud_points:
            if cloud_point.get_position_x() > max_x:
                max_x = cloud_point.get_position_x()
            if cloud_point.get_position_x() < min_x:
                min_x = cloud_point.get_position_x()
            if cloud_point.get_position_y() > max_y:
                max_y = cloud_point.get_position_y()
            if cloud_point.get_position_y() < min_y:
                min_y = cloud_point.get_position_y()
        return max_x - min_x, max_y - min_y

    def get_coordonate_cloud_dimension(self):
        # return the border min max of x y
        max_x, max_y = (0, 0)
        min_x, min_y = (10000000, 10000000)
        # get the border to know how positionning the points
        for cloud_point in self.cloud_points:
            if cloud_point.get_position_x() > max_x:
                max_x = cloud_point.get_position_x()
            if cloud_point.get_position_x() < min_x:
                min_x = cloud_point.get_position_x()
            if cloud_point.get_position_y() > max_y:
                max_y = cloud_point.get_position_y()
            if cloud_point.get_position_y() < min_y:
                min_y = cloud_point.get_position_y()
        return max_x, min_x-1, max_y, min_y-1

    def exec(self):
        # execute the print cloud step by step
        i = 0
        while True:
            print("step ", i)
            i += 1
            # get dimension shape
            old_x, old_y = self.get_shape_cloud_dimension()

            self.step_cloud()
            # thx nico
            curr_x, curr_y = self.get_shape_cloud_dimension()
            print("curr ", curr_x, " ", curr_y)
            if curr_x < old_x and curr_y < old_y:
                continue
            else:
                # print the cloud
                with open("Output.txt", "w") as text_file:
                    self.back_step_cloud()
                    max_x, min_x, max_y, min_y = self.get_coordonate_cloud_dimension()
                    old_str_cloud = self.str_cloud(max_x, min_x, max_y, min_y)
                    print(old_str_cloud, file=text_file)
                break


def data_retrieve(lines):
    # return the new lines traited
    data = []
    for line in lines:
        data.append([int(d) for d in re.findall(r'-?\d+', line)])
    return data


def get_border(data):
    # return the border min max of x y
    max_x, max_y = (0, 0)
    min_x, min_y = (10000000, 10000000)
    # get the border to know how positionning the points
    for raw in data:
        if raw[0] > max_x:
            max_x = raw[0]
        if raw[0] < min_x:
            min_x = raw[0]
        if raw[1] > max_y:
            max_y = raw[1]
        if raw[1] < min_y:
            min_y = raw[1]
    return max_x, min_x, max_y, min_y


def data_preparation(data):
    # return the cloud points and velocities associated
    cloud_points = []
    velocities = []
    # transform points to positions
    max_x, min_x, max_y, min_y = get_border(data)
    # using those borders, we get new points
    # we only have to add the opposite min to each x and y value
    # fufill the cloud points and velocities using input text
    for raw in data:
        cloud_points.append(Cloud_point(Position(raw[0]-min_x, raw[1]-min_y), Velocity(raw[2], raw[3])))
    return cloud_points, velocities


def day_10_part_1(lines):
    # data retrieve
    data = data_retrieve(lines)
    # data preparation
    cloud_points, velocities = data_preparation(data)
    # data modelisation
    cloud = Cloud(cloud_points, velocities)
    # data analyse
    cloud.exec()
    # data visualize
    #metadata_searcher.print_node()
    return str(0)


class TestDay10part1(unittest.TestCase):

    def test_day_10_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_10_part_1(lines)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
