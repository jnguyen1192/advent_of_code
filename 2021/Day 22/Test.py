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

def get_sum_prod_winner():
    suffix = "day"
    file = open('input_' + suffix, 'r')
    #print([line.rstrip('\n\n\n') for line in file])
    player_1_raw, player_2_raw = file.read().split("\n\n")
    file.close()
    p1 = [int(i) for i in player_1_raw.split(":")[1].split()]
    p2 = [int(i) for i in player_2_raw.split(":")[1].split()]
    while len(p1) != 0 and len(p2) != 0:
        if p1[0] < p2[0]:
            p2.append(p2[0])
            p2.append(p1[0])
            p1.pop(0)
            p2.pop(0)
        else:
            p1.append(p1[0])
            p1.append(p2[0])
            p1.pop(0)
            p2.pop(0)
    if len(p1) == 0:
        w = p2
    else:
        w = p1
    return sum([value * (len(w) - index) for index, value in enumerate(w)])


def get_sum_prod_recursive_game():
    suffix = "day"
    file = open('input_' + suffix, 'r')
    #print([line.rstrip('\n\n\n') for line in file])
    player_1_raw, player_2_raw = file.read().split("\n\n")
    file.close()
    d1 = [int(i) for i in player_1_raw.split(":")[1].split()]
    d2 = [int(i) for i in player_2_raw.split(":")[1].split()]
    #d1, d2 = ([], [])

    def recursive_game(d1, d2):
        rounds = set()
        d1 = d1.copy()
        d2 = d2.copy()
        while len(d1) != 0 and len(d2) != 0:
            ##print("d1", d1[0], d1)
            ##print("d2", d2[0], d2)
            if (tuple(d1), tuple(d2)) in rounds:
                # d1 win game
                return True, d1
            rounds.add((tuple(d1), tuple(d2)))
            c_1 = d1[0]
            c_2 = d2[0]
            d1.pop(0)
            d2.pop(0)
            #print(len(d1) < c_1 or len(d2) < c_2)
            if len(d1) < c_1 or len(d2) < c_2:
                winner = c_2 < c_1
                #print(winner)
            else:
                # new game recursive combat
                winner, _ = recursive_game(d1[:c_1], d2[:c_2])
            if winner:
                d1.append(c_1)
                d1.append(c_2)
            else:
                d2.append(c_2)
                d2.append(c_1)
        if len(d1) > 0:
            return True, d1
        else:
            return False, d2
    _, w = recursive_game(d1, d2)
    print(_, w)
    return sum([value * (len(w) - index) for index, value in enumerate(w)])

class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        res = output_file("1")  # get output_1
        pred = get_sum_prod_winner()  # process
        print(pred)  # print 33570 too high
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        #res = output_file("2")  # get output_1
        pred = get_sum_prod_recursive_game()  # oxyphilat reddit https://www.reddit.com/r/adventofcode/comments/khyjgv/2020_day_22_solutions/
        print(pred) # https://topaz.github.io/paste/#XQAAAQBIBwAAAAAAAAAzHIoib6qfHSKVYph9lQLay1GBckscbQAWF5tFBlefiPDt+BX0Fc4oGy9ZjlmyaNP4MtrB1KcV17um0tGFOwHK0oZC9YuQy+Gx2YPiJ7gu6LX7GbA/bK00Ny0r8tpKHgfnLwaKcdg6PBcC4cQ4LhFtmsbUTvqt6tFSR1/ES6nOSXvkb9Z6uih9KNwvl1e32cH8WL2CrJTBD1mqZjc0BMddWxnofHaJ/6I0sFidIIHk2iB8cuSwP66dW2QDf1EPxr0RTWRrTsCHR4AYtBHJy5NhiGmcHe8k2bokAF2sZWwK2tdrRoXuVLO5H2UHof/GPJTohe/ggBK6QnP0HOWup4m/U6B67SctO/WPiJJB3isx10z25xbSWEd57zarjN6iiJbqPiElvcM6DuUNxtcCe7OtJkDXvuCPEDDDa8tThRU1XS+jj41R623eu6kZD4I12CNimR9b+y5Oayfg8NMEutI77/RRA5YnIrMpsVt4LhPfl30uhpXTWADhktlLj7ta62MPrZnV/BOTAQedzq/pLTjkb0eVgo375+XtlqZdjB/K5bpA3O09Bypd1kxyqcqWGNPr7Avv08paRqlKnzSoluCJQKdc2NhPWMc4gKbXtBl75H8rNZGzead/+jVXoOttoGh1lULbMdOvQGD9iKNFNLrveKHp9Y6l8WoG5KQLSm9QGF93kFDAKiEk1D2VvRJv1oVsb51ns05RAqXcu8GvPL/5dz+PZ5t83SwZ64oM4sDAFQUIDHqtPTwtkt7bPFCFkeZOJ2DWXUrysFpnmAd74cv1i9yZbc1A6+NRoA8vifCXnBjtMV0amNbZIr35gzNQqE74tNv/nGZFeQ==
        assert(str(pred) == res[0])


if __name__ == '__main__':
    unittest.main()
