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
    accumulator = 0
    instructions = []

    def compiler(i, instr, value, accumulator, history):
        if instr == "nop":
            if i not in history["wrong_instr"] and not history["correct_value"]:
                history["wrong_instr"].append(i)
                history["correct_value"] = True
                return i + value, accumulator, history
            return i + 1, accumulator, history
        if instr == "acc":
            accumulator += value
            return i + 1, accumulator, history
        if instr == "jmp":
            if i not in history["wrong_instr"] and not history["correct_value"]:
                history["wrong_instr"].append(i)
                history["correct_value"] = True
                return i + 1, accumulator, history
            return i + value, accumulator, history
        return "error"

    for line in lines:
        instr, number_raw = line.split(" ")
        instructions.append((instr, int(number_raw[1:]) if number_raw[0]=="+" else -int(number_raw[1:])))
    #print(instructions)
    history = {"i": [],
               "wrong_instr": [],
               "correct_value": False}
    i = 0

    while True:
        history["i"].append(i)
        i, accumulator, history = compiler(i, instructions[i][0], instructions[i][1], accumulator, history)
        #print(history["i"], history["wrong_instr"])
        if i in history["i"]:
            # infinite loop
            i = 0
            history["i"] = []
            history["correct_value"] = False
            accumulator = 0
            #print("Infinite loop")
        if i == len(instructions):
            #print("Correct end")
            break

    return accumulator  # return nb of valid password


class TestDay8part1(unittest.TestCase):

    def test_day_8_part_2(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_accumulator(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
