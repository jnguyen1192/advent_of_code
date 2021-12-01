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


def get_3_dimension_nb_cubes(lines):
    actives = set()  # https://topaz.github.io/paste/#XQAAAQAQBAAAAAAAAAA2GkofDKPu58xc5+iCM9F3N3GOUCplqA4MZtKB3vCK1x165V5x7dMJ3yOj9Vu0spGRLEk0t/FNjbZavmTUViRYLlmwbrC9/Q2cS5AteR1Z0ULxPhZzw4DVcpTKK10BZxDd1TDUghc6+kfDF5PRek1WcsDdEjTtmFbTUfO9DtdyeWc330cIbCUDPiG1FWFwdOPio2yjhoiz37RsFvrl29I9JON6BbkX7zKvjHn+BRu2J9RfPudEbFMiPqP4zN5XrZLhWP9pD7kskuj8gBWJXiMH4YUmwJjhyVrWxzto6N3Qf1F/uH1eZXV7sJFHveL/2yulJbUjCww6QP9ZLjSJ2c4vsvvmq36lqKrrR33qwemhfwKWBns6ifR3W98hwslf5k0Z1X4PXz/Fh9c5okZNrNqpvr29yx1PilwCD/PalhICdNeyvzags+cvrAHDivkqiAsYQJSuQbbSYxaJleQwEQuLlxxoAQ/PSpai0dznxRUZGpTQtCa0xw7KO9EhZegFJun2mkUvvuR8mU5JyWb1Rlb/1UZwJQ==
    y = 0
    z = 0
    for line in lines:
        x = 0
        for char in line:
            if char == '#':
                actives.add((x, y, z))
            x += 1
        y += 1

    for cycle in range(6):
        new_actives = set()

        zs = [z for (x, y, z) in actives]
        ys = [y for (x, y, z) in actives]
        xs = [x for (x, y, z) in actives]

        for z in range(min(zs) - 1, max(zs) + 2):
            for y in range(min(ys) - 1, max(ys) + 2):
                for x in range(min(xs) - 1, max(xs) + 2):
                    is_active = (x, y, z) in actives
                    active_neighbours = 0

                    for z2 in range(z - 1, z + 2):
                        for y2 in range(y - 1, y + 2):
                            for x2 in range(x - 1, x + 2):
                                if (x, y, z) == (x2, y2, z2):
                                    continue

                                if (x2, y2, z2) in actives:
                                    active_neighbours += 1

                    #print(cycle, x, y, z, "Active neighbours", active_neighbours)

                    if is_active and 2 <= active_neighbours <= 3:
                        new_actives.add((x, y, z))

                    if not is_active and active_neighbours == 3:
                        new_actives.add((x, y, z))

        actives = new_actives

    return len(actives)  # get nb cubes

def get_4_dimension_nb_cubes(lines):
    actives = set()
    y = 0
    z = 0
    w = 0
    for line in lines:
        x = 0
        for char in line:
            if char == '#':
                actives.add((x, y, z, w))
            x += 1
        y += 1

    for cycle in range(6):
        new_actives = set()

        ws = [w for (x, y, z, w) in actives]
        zs = [z for (x, y, z, w) in actives]
        ys = [y for (x, y, z, w) in actives]
        xs = [x for (x, y, z, w) in actives]

        for w in range(min(ws) - 1, max(ws) + 2):
            for z in range(min(zs) - 1, max(zs) + 2):
                for y in range(min(ys) - 1, max(ys) + 2):
                    for x in range(min(xs) - 1, max(xs) + 2):

                        is_active = (x, y, z, w) in actives
                        active_neighbours = 0

                        for w2 in range(w - 1, w + 2):
                            for z2 in range(z - 1, z + 2):
                                for y2 in range(y - 1, y + 2):
                                    for x2 in range(x - 1, x + 2):
                                        if (x, y, z, w) == (x2, y2, z2, w2):
                                            continue

                                        if (x2, y2, z2, w2) in actives:
                                            active_neighbours += 1

                        #print(cycle, x, y, z, w, "Active neighbours", active_neighbours)

                        if is_active and 2 <= active_neighbours <= 3:
                            new_actives.add((x, y, z, w))

                        if not is_active and active_neighbours == 3:
                            new_actives.add((x, y, z, w))

        actives = new_actives

    return len(actives)


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        res = output_file("1")  # get output_1
        pred = get_3_dimension_nb_cubes(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        res = output_file("2")  # get output_1
        pred = get_4_dimension_nb_cubes(lines)  # process
        print(pred) # https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/ popodiloco
        assert(str(pred) == res[0])


if __name__ == '__main__':
    unittest.main()
