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


def get_100_moves(lines):
    class Crab_cups:
        def __init__(self, lines):
            self.circle_labeled = list(lines[0])
            self.current_cup = 0
            self.pick_up = []
            self.destination_cup = ""

        def get_circle_labeled(self):
            return self.circle_labeled

        def move(self):
            # The crab picks up the three cups that are immediately clockwise of the current cup.
            # normal case
            if self.current_cup+4 > len(self.circle_labeled):
                self.pick_up = self.circle_labeled[self.current_cup+1:] + self.circle_labeled[: (self.current_cup+4)%len(self.circle_labeled)]
            else:
                self.pick_up = self.circle_labeled[(self.current_cup+1) % len(self.circle_labeled):self.current_cup+4]

            def get_next_destination_cup(destination_cup):
                if destination_cup == 0:
                    destination_cup = len(self.circle_labeled)
                if str(destination_cup) not in self.pick_up:
                    return destination_cup
                return get_next_destination_cup(destination_cup - 1)

            self.destination_cup = get_next_destination_cup((int(self.circle_labeled[self.current_cup]) - 1) % len(self.circle_labeled))
            #print("cups:", " ".join(self.circle_labeled[:self.current_cup]) + ' (' + self.circle_labeled[self.current_cup] + ') ' + " ".join(self.circle_labeled[self.current_cup + 1:]))
            for elmt in self.pick_up:
                self.circle_labeled.remove(elmt)
            #print("pick up:", ", ".join(self.pick_up))
            #print("destination:", self.destination_cup)
            insert_index = (self.circle_labeled.index(str(self.destination_cup)) + 1)
            #print(insert_index)
            if self.current_cup + 1 > len(self.circle_labeled):
                current_cup_value = self.circle_labeled[-1]
            else:
                current_cup_value = self.circle_labeled[self.current_cup]
            for i, elmt in enumerate(self.pick_up):
                self.circle_labeled.insert(i + insert_index, elmt) # TODO optimize

            while current_cup_value != self.circle_labeled[self.current_cup]:
                self.circle_labeled = self.circle_labeled[-1:] + self.circle_labeled[:-1]

            self.current_cup = (self.current_cup + 1) % len(self.circle_labeled)

        def get_labels_on_cup_after_one(self):
            index = self.circle_labeled.index('1')
            if index == 0:
                labels_on_cup_after_one = self.circle_labeled[index+1:]
            else:
                labels_on_cup_after_one = self.circle_labeled[index+1:] + self.circle_labeled[:index]
            return "".join(labels_on_cup_after_one)
    cc = Crab_cups(lines)
    power = 0
    #for i in range(100): # part1
    for i in range(10000000): # part2
        if i % 10**power == 0:
            print("-- move", i+1, "--")
            power += 1
        cc.move()
    #print(cc.get_labels_on_cup_after_one())
    return cc.get_labels_on_cup_after_one()


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        lines = input_file("test")  # get input_test
        res = output_file("test_2")  # get output_1
        #res = output_file("1")  # get output_1
        pred = get_100_moves(lines)  # process
        print(pred)  # print 33570 too high
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        #res = output_file("2")  # get output_1
        def solve(n):
            s = '284573961'
            cups = [int(x) for x in s]
            ext = [x for x in range(10, n + 1)]
            cups += ext

            d = {}
            for i in range(len(cups)):
                if i == len(cups) - 1:
                    d[cups[i]] = cups[0]
                else:
                    d[cups[i]] = cups[i + 1]

            start = int(s[0])
            for i in range((n * 10) + 1):
                a = d[start]
                b = d[a]
                c = d[b]
                d[start] = d[c]
                put = start - 1
                if put in [a, b, c] or put < 1:
                    while put in [a, b, c] or put < 1:
                        put -= 1
                        if put < 1:
                            put = n
                d[c] = d[put]
                d[put] = a
                start = d[start]

            return d[1] * d[d[1]]

        print(solve(1000000))

        assert(0 == res[0])


if __name__ == '__main__':
    unittest.main()
