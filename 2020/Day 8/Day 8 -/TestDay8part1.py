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


def get_accumulator(lines):
    accumulator = 0  # initialize accumlator
    instructions = []  # initialize instructions

    def compiler(i, instr, value, accumulator):  # analyser if each instructions
        if instr == "nop":  # case nop
            return i + 1, accumulator  # go to next instruction
        if instr == "acc":  # case acc
            accumulator += value  # increase accumulator value
            return i + 1, accumulator  # go to next instruction
        if instr == "jmp":
            return i + value, accumulator  # go to +value instruction
        return "error"

    for line in lines:  # for each linse
        instr, number_raw = line.split(" ")  # extract the instruction and value
        instructions.append((instr, int(number_raw[1:]) if number_raw[0]=="+" else -int(number_raw[1:])))  # add them into instruction list
    #print(instructions)

    history = {"i": []}  # initialize history
    i = 0  # initialize line number in instruction list
    while True:
        history["i"].append(i)  # add line number in history line number
        i, accumulator = compiler(i, instructions[i][0], instructions[i][1], accumulator)
        if i in history["i"]:  # case line instruction was already travelled
            break  # end the program

    return accumulator  # return nb of valid password


class TestDay8part1(unittest.TestCase):

    def test_day_8_part_1(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_accumulator(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
