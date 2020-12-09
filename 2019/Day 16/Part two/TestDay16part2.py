import unittest
from parse import parse
import copy
from pprint import pprint


def input_file():
    # return the input_test file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output_1 file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class TestDay16part2(unittest.TestCase):

    def test_day_16_part_2(self):
        text = input_file()

        signal = [int(i) for i in text.split("\n")[0]]
        #print(signal)
        def FFT(signal, nb_phase=1):
            # skip the first element
            # repeat once for the first element
            def process_element(signal_, repeat=0):
                base_pattern = [0, 1, 0, -1]
                current_pattern = []
                for i in base_pattern:
                    current_pattern += [i] * repeat
                #print(current_pattern, repeat)
                sum = 0
                current_pos_pattern = 1
                str_calc = ""
                #print(len(signal_))
                for s in signal_:
                    #str_calc += str(s) + " * " + str(current_pattern[current_pos_pattern%len(current_pattern)]) + " + "
                    if current_pattern[current_pos_pattern % len(current_pattern)] != 0 or s != 0:
                        sum += current_pattern[current_pos_pattern % len(current_pattern)] * s

                    current_pos_pattern += 1
                # TODO sum de tous les -1
                # TODO sum de tous les +1
                #
                print(sum)
                #str_calc += " = " + str(sum)
                #print(str_calc)
                #print(abs(sum)%10)
                return abs(sum) % 10

            def new_signal(signal_):
                new_list = []
                #print("signal_", signal_)
                #print(len(signal_))
                for i in range(1, len(signal_) + 1):
                    print(i)
                    new_list.append(process_element(signal_, i))
                return new_list
            # TODO real signal = 10000 * signal
            #current_signal = signal
            current_signal = [s for s in signal] * 100000
            # TODO get the first 7th number
            first_seventh = int("".join([str(i) for i in current_signal[:7]]))
            # TODO skip [first_seventh:first_seventh+8]
            for i in range(nb_phase):
                #print(i)
                current_signal = new_signal(current_signal)
                print("After phase", i + 1, current_signal[:8])
            #return current_signal[:8]#
            return current_signal[first_seventh:first_seventh+8]

        print("".join([str(i) for i in FFT(signal, 100)]))










if __name__ == '__main__':
    unittest.main()
