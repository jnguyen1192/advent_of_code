import unittest
import numpy as np
import re

def input_file():
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
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

def read_input(lines):
    # init input
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


def day_3_part_1(lines):
    left_edge, top_edge, width, tall = read_input(lines)
    # build claims
    area = build_claim(left_edge, top_edge, width, tall)
    # count claim >= 2
    overlap_count = (area == 1).sum()
    #print("overlap_count ", overlap_count)
    return overlap_count


class TestDay3part1(unittest.TestCase):

    def test_day_3_part_1(self):
        lines = input_file()
        pred = day_3_part_1(lines)
        print("overlap count ", pred)

    def test_build_claim(self):
        print(build_claim(0, 1, 3, 2))


if __name__ == '__main__':
    unittest.main()
