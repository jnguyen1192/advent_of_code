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


def parttwo(lines):
    numbers = [int(line) for line in lines]
    # the result
    first_frequency = 0
    # the list of frequencies
    frequencies = [0]
    # the current frequency
    current_frequency = 0
    # boolean to find the frequency
    twice = False
    # repeat the process in a circle
    while True:
        # browse in numbers
        for nb in numbers:
            # add the frequency
            current_frequency += nb
            # compare if the frequency exist
            if current_frequency in frequencies:
                # get the first frequency
                first_frequency = current_frequency
                # exit the infinite loop
                twice = True
                break
            # add the frequency to the frequencies
            frequencies.append(current_frequency)
        if twice:
            break
    return str(first_frequency)


class TestDay1part2(unittest.TestCase):

    def test_day_1_part_2(self):
        lines = input_file()
        res = output_file()
        assert(parttwo(lines) == res[0])


if __name__ == '__main__':
    unittest.main()
