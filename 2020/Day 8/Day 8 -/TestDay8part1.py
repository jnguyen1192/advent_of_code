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

    class game_console:
        def __init__(self):
            self.accumulator = 0  # initialize accumlator
            self.instructions = []  # initialize instructions
            self.history = {"i": []}  # initialize history

        def prepare_instructions(self, lines):
            for line in lines:  # for each linse
                instr, number_raw = line.split(" ")  # extract the instruction and value
                self.instructions.append((instr, int(number_raw[1:]) if number_raw[0] == "+" else -int(
                    number_raw[1:])))  # add them into instruction list

        def compiler(self, i, instr, value, accumulator):  # analyser if each instructions
            if instr == "nop":  # case nop
                return i + 1, accumulator  # go to next instruction
            if instr == "acc":  # case acc
                accumulator += value  # increase accumulator value
                return i + 1, accumulator  # go to next instruction
            if instr == "jmp":
                return i + value, accumulator  # go to +value instruction
            return "error"

        def run(self):
            i = 0  # initialize line number in instruction list
            while True:
                self.history["i"].append(i)  # add line number in history line number
                i, self.accumulator = self.compiler(i, self.instructions[i][0], self.instructions[i][1], self.accumulator)
                if i in self.history["i"]:  # case line instruction was already travelled
                    break  # end the program

    g_c = game_console()  # create game console
    g_c.prepare_instructions(lines)  # insert instructions in game console
    g_c.run()  # start game console

    return g_c.accumulator  # return accumlator in game console


class TestDay8part1(unittest.TestCase):

    def test_day_8_part_1(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_accumulator(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
