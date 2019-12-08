import unittest
from parse import parse


def input_file():
    # return the input file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class TestDay8part1(unittest.TestCase):

    def test_day_8_part_1(self):
        text = input_file()
        # res = output_file()
        # pred = day_2_part_1(text)
        width = 25
        height = 6
        limit = width * height

        def count_zero_digits(layer):
            c = 0
            for l in layer:
                if l == "0":
                    c += 1
            return c

        def count_one_multiply_two_digits(layer):
            c_1 = 0
            c_2 = 0
            for l in layer:
                if l == "1":
                    c_1 += 1
                if l == "2":
                    c_2 += 1
            return c_1 * c_2

        # load layers
        def load_layers(text):
            i_layer = 1
            layer = []
            layers = []
            for t in text:
                layer.append(t)
                i_layer += 1
                if i_layer > limit:
                    c_zero = count_zero_digits(layer)
                    layers.append((c_zero, layer))
                    layer = []
                    i_layer = 1
            return layers

        layers = sorted(load_layers(text))
        print(len(layers))
        print(count_one_multiply_two_digits(layers[0][1]))


if __name__ == '__main__':
    unittest.main()
