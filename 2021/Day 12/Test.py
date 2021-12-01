import unittest


def input_file(suffix):
    file = open('input_' + suffix, 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file(number):
    file = open('output_'+str(number), 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def get_differences(lines):
    adapters = []
    for line in lines:
        adapters.append(int(line))
    adapters.sort()
    #print(adapters)
    differences = {1: 1,
                   2: 1,
                   3: 1}
    for index, adapter in enumerate(adapters[:-1]):  # count difference
        #print(adapter, adapters[index + 1], abs(adapter - adapters[index + 1]))
        differences[abs(adapter - adapters[index + 1])] += 1
    return differences[1],  differences[3]


def get_manhattan_distance_from_starting_point(lines):
    manhattan_distance_from_starting_point = 0
    """
    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.
    """
    class Ship:

        def __init__(self, lines, waypoint=(0, (10, -1)), pos=(0, 0), facing=0):
            self.lines = lines
            self.pos = pos
            self.waypoint = waypoint
            self.facing = facing
            self.move_rule = {"N": (3, (0, -1)),
                              "S": (1, (0, 1)),
                              "E": (0, (1, 0)),
                              "W": (2, (-1, 0)),
                              "L": -1,
                              "R": 1,
                              "F": None}

        def update_facing(self, code, number):
            if code in "NSEW":
                self.facing = self.move_rule[code][0]
            else:
                self.facing = int((self.facing + self.move_rule[code] * (number / 90)) % 4)

        def update_waypoint(self, code, number):
            if code in "NSEW":
                # TODO add on the correct direction
                self.facing = self.move_rule[code][0]
            else:
                self.facing = int((self.facing + self.move_rule[code] * (number / 90)) % 4)

        def move(self, line):
            code = line[0]
            number = int(line[1:])
            if code in "NSEW":
                self.pos = (self.pos[0] + (self.move_rule[code][1][0] * number),
                            self.pos[1] + (self.move_rule[code][1][1] * number))
                #self.update_facing(code, number)
            elif code in "F":
                self.pos = (self.pos[0] + (self.move_rule[self.facing][0] * number),
                            self.pos[1] + (self.move_rule[self.facing][1] * number))
            else:
                self.update_facing(code, number)
            print(line, self.facing, (self.pos[0]), (self.pos[1]))

        def run(self):
            for line in lines:
                self.move(line)

        def update_facing_part_2(self, code, number):
            # TODO use waypoint
            if code in "NSEW":
                self.facing = self.move_rule[code[1]]
            else:
                self.facing = int((self.facing + self.move_rule[code] * (number / 90)) % 4)

        def move_part_2(self, line):
            code = line[0]
            number = int(line[1:])
            if code in "NSEW":
                # update waypoint
                if code == "E":
                    self.waypoint = (self.waypoint[0], (self.waypoint[1][0] + number, self.waypoint[1][1]))
                elif code == "W":
                    self.waypoint = (self.waypoint[0], (self.waypoint[1][0] - number, self.waypoint[1][1]))
                elif code == "S":
                    self.waypoint = (self.waypoint[0], (self.waypoint[1][0], self.waypoint[1][1] + number))
                elif code == "N":
                    self.waypoint = (self.waypoint[0], (self.waypoint[1][0], self.waypoint[1][1] - number))
                #self.update_facing(code, number)
            elif code in "F":
                # use waypoint to move
                self.pos = (self.pos[0] + (number * self.waypoint[1][0]),
                            self.pos[1] + (number * self.waypoint[1][1]))

            else:
                before_waypoint = self.waypoint[0]
                self.waypoint = (int((self.waypoint[0] + self.move_rule[code] * (number / 90)) % 4), self.waypoint[1])  # use waypoint
                print(self.waypoint[0] - before_waypoint)
                test = (self.waypoint[0] - before_waypoint) % 4
                if test == 1:
                    self.waypoint = (self.waypoint[0],
                                     (-self.waypoint[1][1], self.waypoint[1][0]))  # use waypoint
                elif test == 2:
                    self.waypoint = (self.waypoint[0],
                                     (-self.waypoint[1][0], -self.waypoint[1][1]))  # use waypoint
                elif test == 3:
                    self.waypoint = (self.waypoint[0],
                                     (-self.waypoint[1][1], self.waypoint[1][0]))  # use waypoint
            print(line, self.waypoint, self.pos)

        def run_part_2(self):
            for line in lines:
                self.move_part_2(line)

        def get_manhattan_distance_from_starting_point(self):
            print(abs(self.pos[0]), abs(self.pos[1]))
            return abs(self.pos[0]) + abs(self.pos[1])

    s = Ship(lines)
    #s.run()
    s.run_part_2()

    return s.get_manhattan_distance_from_starting_point()  # "OK"


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        #res = output_file("test_1")  # get output_1
        pred = get_manhattan_distance_from_starting_point(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        sin = {0: 0, 90: 1, 180: 0, 270: -1}
        cos = {0: 1, 90: 0, 180: -1, 270: 0}

        x = y = dir = 0
        wx = 10
        wy = 1
        for op, val in [(x[:1], int(x[1:])) for x in lines]: # https://topaz.github.io/paste/#XQAAAQAOAwAAAAAAAAARiAinOloyihUu1b5x+73YwmpOl2G0L3PQlPHtFchCsp3Z7fUfQnunIDN8t+CJJX3YseRhG+W9EstmUaAJ3c8sTWSPKH/H6JKPyEXwJ8pTNI+0BhsSzgpK93UvN1JWllIh6QiaBJxla1SCg1epHogeNHQ8sMbtcaesPLvn3DKfBdk9MmMnQgof2ekO9FBH+15NMLrG6AFgivSo6FJXf9p8m2ksvr1xMAUTy9YXYAPJsHESdD+KLz0vdz3VtJeNYZNaNZJqIO8DxS/LhDLeyjSWXdxkxkqA3IrMtUoUo74s91uAsBgtevi51LXvS6ToW7/RDD9cCfMU5LnAT9rmFBF3An2PvI0a62WZ9dKqygvmpu1CZzlj8/BkrwExEZIDUmdOpp7z7fKB9dAuGYLylYimJGWH1yANdPtTpSQxeewYNHSAlYKmk0uz1Whgf8p8swByDRLupcuCn/+6V1Iv
            if op == 'N':
                wy += val
            elif op == 'S':
                wy -= val
            elif op == 'E':
                wx += val
            elif op == 'W':
                wx -= val
            elif op == 'R':
                nwx = wx * cos[-val % 360] - wy * sin[-val % 360]
                nwy = wx * sin[-val % 360] + wy * cos[-val % 360]
                wx, wy = nwx, nwy
            elif op == 'L':
                nwx = wx * cos[val % 360] - wy * sin[val % 360]
                nwy = wx * sin[val % 360] + wy * cos[val % 360]
                wx, wy = nwx, nwy
            else:
                x += val * wx
                y += val * wy
        #    print(wx, wy)

        print(abs(x) + abs(y))
        res = output_file("test_2")  # get output_1

        pred = get_manhattan_distance_from_starting_point(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
