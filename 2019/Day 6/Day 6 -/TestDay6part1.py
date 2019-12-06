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

    def test_day_6_part_1(self):
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
        old_orbit = ["COM"]
        new_orbit = []
        while len(old_orbit) != 0:
            for o in old_orbit:
                #print("Orbit of", o)
                for r in rules:
                    if r[0] == o:
                        total += d
                        new_orbit.append(r[1])
                        #print('new_orbit element', r[1])
                        #print(r)
                        #rules.remove(r)
                #print("new_orbit", new_orbit)
            old_orbit = new_orbit
            new_orbit = []
            #print(old_orbit, len(rules), total, rules)
            d += 1
        print(total)


if __name__ == '__main__':
    unittest.main()
