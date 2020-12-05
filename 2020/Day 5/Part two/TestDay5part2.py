import unittest


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


def get_highest_seat_ID(lines):
    def get_seat_ID(line):  # get the seat ID
        rules = {"R": "+",  # upper half
                 "L": "-",  # lower half
                 "F": "-",  # lower half
                 "B": "+"}  # upper half

        def step_x(chars, x):  # for each step
            lower_row, upper_row = (0, 0) # intialize variables
            if x == 1:  # case Front and Back
                lower_row, upper_row = (0, 127)
            if x == 2: # case Left and Right
                lower_row, upper_row = (0, 7)
            for i, char in enumerate(chars[:len(chars)-1]):  # navigate before the end
                if rules[char] == "+":  # case we need to add on lower value
                    lower_row = lower_row + 2**(len(chars)-1 - i)
                if rules[char] == "-": # case we need to substract on upper value
                    upper_row = upper_row - 2**(len(chars)-1 - i)
            if rules[chars[-1]] == "+":  # case last char F or L we take the upper row
                return upper_row
            if rules[chars[-1]] == "-":  # case last char B or R we take the lower row
                return lower_row
            return 0

        # apply step 1
        row = step_x(line[:7], 1)  # case with F and B
        # apply step 2
        column = step_x(line[-3:], 2)  # case with B and R
        return row * 8 + column  # the final calcul

    IDS = []  # part 2 add a new array
    max = 0  # initialize max value
    for line in lines:  # for each lines
        ID = get_seat_ID(line)  # get the seat ID
        IDS.append(ID)  # part 2 fufill the new array
        if max < ID:  # check if it is the new max value
            max = ID  # assign the new max value
    # part 2
    IDS.sort()  # sort the array
    my_seat = 0  # initialize my seat value
    for i, ID in enumerate(IDS):  # for each IDS
        if ID + 1 != IDS[i + 1]:  # check if it miss an ID
            my_seat = ID + 1  # the ID missing is my seat !
            break
    return my_seat  # return nb of valid password


class TestDay5part2(unittest.TestCase):

    def test_day_5_part_2(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_highest_seat_ID(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
