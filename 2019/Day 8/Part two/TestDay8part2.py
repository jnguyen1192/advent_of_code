import unittest
from parse import parse
import PIL
import numpy as np

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


class TestDay8part2(unittest.TestCase):

    def test_day_8_part_2(self):
        text = input_file()
        # res = output_file()
        # pred = day_2_part_1(text)
        width, height = (25, 6)#(2, 2)
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
                    #c_zero = count_zero_digits(layer)
                    layers.append(layer)
                    layer = []
                    i_layer = 1
            return layers
        def first_pixel_found(sum):
            #print(sum)
            for i in sum:
                if i == "0":
                    return "0"
                if i == "1":
                    return "1"
            return "2"
        # final with all sum of color for each position
        final_img = []
        layers = load_layers(text)
        for i in range(limit):
            sum = []
            for layer in layers:
                sum.append(layer[i])
            final_img.append(first_pixel_found(sum))

        # final create img
        img = np.zeros(shape=(height, width, 3),
                              dtype=np.uint8)
        for j in range(height):
            for i in range(width):
                if final_img[j * width + i] == "1":
                    img[j][i] = [255, 255, 255]
                if final_img[j * width + i] == "0":
                    img[j][i] = [0, 0, 0]
        from PIL import Image  # https://deptinfo-ensip.univ-poitiers.fr/ENS/doku/doku.php/stu:python_gui:tuto_images
        imgpil = Image.fromarray(img)  # Transformation du tableau en image PIL
        imgpil.save("resultat.jpg")


if __name__ == '__main__':
    unittest.main()
