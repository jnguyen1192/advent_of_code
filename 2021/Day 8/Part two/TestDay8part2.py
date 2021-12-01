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
            self.history = {"i": [],
                            "wrong_instr": [],
                            "correct_value": False}  # initialize history

        def prepare_instructions(self, lines):
            for line in lines:  # for each linse
                instr, number_raw = line.split(" ")  # extract the instruction and value
                self.instructions.append((instr, int(number_raw[1:]) if number_raw[0] == "+" else -int(
                    number_raw[1:])))  # add them into instruction list

        def compiler(self, i, instr, value, accumulator):  # analyser if each instructions
            if instr == "nop":  # case nop
                if i not in self.history["wrong_instr"] and not self.history["correct_value"]:  # case correct nop instruction
                    self.history["wrong_instr"].append(i)  # add line correct instruction into history
                    self.history["correct_value"] = True  # exit corrected mode
                    return i + value, accumulator, self.history  # go to +value instruction
                return i + 1, accumulator, self.history  # go to next instruction
            if instr == "acc":  # case acc
                accumulator += value  # increase accumulator value
                return i + 1, accumulator, self.history  # go to next instruction
            if instr == "jmp":
                if i not in self.history["wrong_instr"] and not self.history["correct_value"]:  # case correct jmp instruction
                    self.history["wrong_instr"].append(i)  # add line correct instruction into history
                    self.history["correct_value"] = True  # exit corrected mode
                    return i + 1, accumulator, self.history  # go to next instruction
                return i + value, accumulator, self.history  # go to +value instruction
            return "error"

        def run(self):
            i = 0  # initialize line number in instruction list
            while True:
                self.history["i"].append(i)  # add line number in history line number
                i, self.accumulator, self.history = self.compiler(i, self.instructions[i][0],
                                                                  self.instructions[i][1],
                                                                  self.accumulator)

                if i in self.history["i"]:  # case line instruction was already travelled
                    # infinite loop
                    i = 0  # restart the program
                    self.history["i"] = []
                    self.history["correct_value"] = False  # correct next nop or jmp instruction
                    self.accumulator = 0  # restart accumulator
                    # print("Infinite loop")
                if i == len(self.instructions):
                    # print("Correct end")
                    break

    g_c = game_console()  # create game console
    g_c.prepare_instructions(lines)  # insert instructions in game console
    g_c.run()  # start game console

    return g_c.accumulator  # return accumulator in game console



class TestDay8part1(unittest.TestCase):

    def test_day_8_part_2(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_accumulator(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
