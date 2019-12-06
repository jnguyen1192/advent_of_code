import unittest
from parse import parse


def input_file():
    # return the input file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res

class TestDay6part1(unittest.TestCase):

    def test_day_6_part_2(self):
        text = input_file()
        #res = output_file()
        #pred = day_2_part_1(text)
        rules = []
        for line in sorted(text.split("\n")):
            couple = line.split(")")
            rules.append((couple[0], couple[1]))
        #print(rules)
        total = 0
        d = 1
        old_orbit_san = ["SAN"]
        new_orbit_san = []
        old_orbit_you = ["YOU"]
        new_orbit_you = []
        you = 0
        father_you = []
        father_san = []
        san = 0
        inter = False
        #print(rules)
        while len(old_orbit_you) != 0:
            for oy in old_orbit_you:
                #print("Orbit of", o)
                for r in rules:
                    if r[1] == oy:
                        total += d
                        new_orbit_you.append(r[0])
                        father_you.append((r[0], you))
                        you += 1
            old_orbit_you = new_orbit_you
            new_orbit_you = []

        while not inter or len(old_orbit_san) != 0:
            for os in old_orbit_san:
                #print("Orbit of", o)
                for r in rules:
                    if r[1] == os:
                        total += d
                        new_orbit_san.append(r[0])
                        father_san.append((r[0], san))
                        for i in father_you:
                            #print("test", i[0], r[1])
                            if i[0] == r[0]:
                                print(i[1] + san)
                                inter = True
                                break
                        san += 1
                    if inter:
                        break
                if inter:
                    break
            old_orbit_san = new_orbit_san
            new_orbit_san = []
            #print(old_orbit, len(rules), total, rules)
            d += 1


if __name__ == '__main__':
    unittest.main()
