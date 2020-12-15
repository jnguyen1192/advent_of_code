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


def get_2020th_memory_game(lines, limit=2020):
    class MemoryGame:
        def __init__(self, lines):
            # init game
            self.numbers_spoken = self.first_numbers_spoken(lines)
            self.current_i = len(self.numbers_spoken) + 1
            self.last_number_spoken = self.numbers_spoken[self.current_i - 1]

        def first_numbers_spoken(self, lines):

            return {index+1: int(number) for index, number in enumerate(lines[0].split(","))}

        def get_difference_last_spoken_numbers_turn(self, current_i):
            numbers = []
            #print(self.numbers_spoken)
            for i in range(current_i, 0, -1):
                if self.numbers_spoken[i-1] == self.last_number_spoken:
                    numbers.append(i)
                if len(numbers) > 1:
                    break
            print(self.current_i, numbers[0] - numbers[1], "=", numbers[0], "-", numbers[1])
            return numbers[0] - numbers[1]

        def next_turn(self):
            #print(len([1 for number_spoken in list(self.numbers_spoken.values()) if self.last_number_spoken==number_spoken])>1, len([1 for number_spoken in list(self.numbers_spoken.values()) if self.last_number_spoken==number_spoken]))
            if not(len([1 for number_spoken in list(self.numbers_spoken.values()) if self.last_number_spoken==number_spoken]) > 1):  # If that was the first time the number has been spoken
                self.numbers_spoken[self.current_i] = 0  # the current player says 0.
            else:  # Otherwise the number had been spoken before;
                self.numbers_spoken[self.current_i] = self.get_difference_last_spoken_numbers_turn(self.current_i)  # how many turns apart the number is from when it was previously spoken
            self.last_number_spoken = self.numbers_spoken[self.current_i]
            self.current_i += 1



    mg = MemoryGame(lines)
    #print(mg.numbers_spoken)
    #print(mg.last_number_spoken)
    i = 0
    while i < limit:
        mg.next_turn()
        i += 1
    return mg.numbers_spoken[2020]


def get_30000000th_memory_game(lines, limit=30000000):
    class MemoryGame:
        def __init__(self, lines):
            # init game
            self.numbers_spoken = self.first_numbers_spoken(lines)
            self.current_i = len(self.numbers_spoken) + 1
            self.last_number_spoken = int(lines[0].split(",")[-1])

        def first_numbers_spoken(self, lines):
            return {int(number): [index+1] for index, number in enumerate(lines[0].split(","))}

        def next_turn(self):
            #print(len([1 for number_spoken in list(self.numbers_spoken.values()) if self.last_number_spoken==number_spoken])>1, len([1 for number_spoken in list(self.numbers_spoken.values()) if self.last_number_spoken==number_spoken]))
            # TODO part 2 inverse dict
            #print(self.last_number_spoken, self.numbers_spoken)
            #print(self.numbers_spoken[self.last_number_spoken])
            if len(self.numbers_spoken[self.last_number_spoken]) < 2:
            #if not(len([1 for number_spoken in list(self.numbers_spoken.values()) if ==number_spoken]) > 1):  # If that was the first time the number has been spoken
                if self.numbers_spoken.get(0, 0) == 0:
                    self.numbers_spoken[0] = []
                else:
                    self.numbers_spoken[0].append(self.current_i)  # the current player says 0.
                if len(self.numbers_spoken[0]) > 2:
                    self.numbers_spoken[0] = self.numbers_spoken[0][-2:]
                self.last_number_spoken = 0
            else:  # Otherwise the number had been spoken before;
                tmp = self.current_i - 1 - self.numbers_spoken[self.last_number_spoken][0]
                #print(self.numbers_spoken[self.last_number_spoken], self.last_number_spoken )
                #print(self.current_i, tmp, "=", self.current_i - 1, "-", self.numbers_spoken[self.last_number_spoken][-2])
                if self.numbers_spoken.get(tmp, 0) == 0:
                    self.numbers_spoken[tmp] = [self.current_i]
                else:
                    self.numbers_spoken[tmp].append(self.current_i)   # how many turns apart the number is from when it was previously spoken
                    if len(self.numbers_spoken[tmp]) > 2:
                        self.numbers_spoken[tmp] = self.numbers_spoken[tmp][-2:]
                self.last_number_spoken = tmp
            #print(self.current_i, self.last_number_spoken)
            self.current_i += 1



    mg = MemoryGame(lines)
    #print(mg.numbers_spoken)
    #print(mg.last_number_spoken)
    timeout = len(mg.numbers_spoken)
    i = 0
    while i < limit - timeout:
        mg.next_turn()
        #print(mg.last_number_spoken)
        if i % 10000000 == 0:
            print(i)
        i += 1

    print(mg.last_number_spoken)
    return mg.numbers_spoken[30000000]


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        #res = output_file("test_1")  # get output_1
        pred = get_2020th_memory_game(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test_2")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        pred = get_30000000th_memory_game(lines)  # process
        print(pred)
        assert(str(pred) == res[0])  # check https://github.com/busdriverbuddha/aoc2020_solutions/blob/main/day13.py

if __name__ == '__main__':
    unittest.main()
