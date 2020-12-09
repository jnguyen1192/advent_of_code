import unittest
import numpy as np
import re


def input_file():
    # read lines of input_test file
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


def build_claim(left_edge, top_edge, width, tall):
    # build 2000*2000 area
    area = np.zeros((2000, 2000))
    # add claim on it, if there was collision value > 1
    for i in range(len(left_edge)):
        area[top_edge[i]:top_edge[i]+tall[i], left_edge[i]:left_edge[i]+width[i]] += 1
    return area


def build_claim_u(left_edge, top_edge, width, tall):
    # build 2000*2000 area
    area = np.zeros((2000, 2000))
    # add one claim
    area[top_edge:top_edge+tall, left_edge:left_edge+width] += 1
    return area


def get_id_complete_claim(area, left_edge, top_edge, width, tall):
    id = 0
    # get the id of the complete claim
    for i in range(len(left_edge)):
        if is_claim_complete_u(area, left_edge[i], top_edge[i], width[i], tall[i]):
            # increment by one because it begins at 0
            id = i + 1
    return id


def is_claim_complete_u(area, left_edge, top_edge, width, tall):
    # check if a claim is complete
    return np.all(area[top_edge:top_edge+tall, left_edge:left_edge+width] == 1)


def read_input(lines):
    # init input_test
    left_edge = []
    top_edge = []
    width = []
    tall = []
    for line in lines:
        left_edge.append(int(re.findall(r"[\d]*", line)[5]))
        top_edge.append(int(re.findall(r"[\d]*", line)[7]))
        width.append(int(re.findall(r"[\d]*", line)[10]))
        tall.append(int(re.findall(r"[\d]*", line)[12]))
    return left_edge, top_edge, width, tall


def day_3_part_2(lines):
    left_edge, top_edge, width, tall = read_input(lines)
    # build claims
    area = build_claim(left_edge, top_edge, width, tall)
    # count claim >= 2
    overlap_count = (area == 1).sum()
    #print("overlap_count ", overlap_count)
    # count claim complete
    # we need to to the same process
    # but this time we verify that every values are equal to one to increment
    id = get_id_complete_claim(area, left_edge, top_edge, width, tall)
    return id


class TestDay3part2(unittest.TestCase):

    def test_day_3_part_2(self):
        lines = input_file()
        #res = output_file()
        pred = day_3_part_2(lines)
        print("id complete claim ", pred)
        #assert(pred == res[0])

    def test_build_claim(self):
        le = 0
        te = 1
        w = 3
        t = 2
        area = build_claim_u(le, te, w, t)
        print(area)
        b = is_claim_complete_u(area, le, te, w, t)
        print(b)


if __name__ == '__main__':
    unittest.main()
