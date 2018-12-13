import unittest


def input_file():
    # return the input file in a text
    file = open('input', 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file():
    # read line of output file
    file = open('output', 'r')
    res = file.read()
    file.close()
    return res


class GenerationPlant:
    # class that represent the rules for each generation of plants
    def __init__(self, input_line, constraints, number_of_generation=20):
        """

        :param input_line: the plant that will have generation
        :param constraints: the constraints for each generation
        """
        self.input_line = input_line
        self.generation = []
        self.constraints = constraints
        self.number_of_generation = number_of_generation
        self.beginning = 0  # to the border

    def sum_number_pot_containing__plants(self):
        # return number of plant of the current generation
        # the iterator for each rules applied
        ind_beg = self.generation[-1].find("#")
        generation = self.generation[-1][ind_beg:]
        # reverse generation
        rev_generation = generation[::-1]
        ind_beg = rev_generation.find("#")
        generation = rev_generation[ind_beg:]
        # rebuild generation
        generation = generation[::-1]
        sum_pots = 0
        for key, pot in enumerate(generation):
            if pot == "#":
                sum_pots += key + self.beginning  # because first pot is -2
        return sum_pots

    def next_generation(self):
        # build the next generation and add it on the list of generation
        current_generation = self.generation[-1]
        # apply rule
        self.apply_rule(current_generation)

    def rebuild_generation(self, generation):
        # the iterator for each rules applied
        ind_beg = generation.find("#")
        generation = "...." + generation[ind_beg:]
        # reverse generation
        rev_generation = generation[::-1]
        ind_beg = rev_generation.find("#")
        generation = "...." + rev_generation[ind_beg:]
        # rebuild generation
        return generation[::-1]

    def apply_rule(self, generation):
        # apply rules to the generation
        generation = self.rebuild_generation(generation)
        generation_list = []
        # begin at the right pot and end at the right pot
        for i in range(3, len(generation)+1):
            match_find = False
            for key, value in self.constraints.items():
                #print("key ", key)
                #print("generation ", generation[i-3:i+2])
                if key == generation[i-3:i+2]:
                    # transform the pot
                    generation_list.append(value)
                    # increment the iterator
                    match_find = True
                    # interrupt the matcher
                    break
            if not match_find:
                generation_list.append(".")
        generation_after = "".join(generation_list)
        if generation_after.find("#") < 2:
            self.beginning -= 1
        if generation_after.find("#") > 2:
            self.beginning += 1
        # add on list generation the current generation
        self.generation.append(generation_after)

    def execute(self):
        # process on plants
        # init the generation list
        self.generation.append(self.input_line)
        # process with number of generation
        for i in range(self.number_of_generation):
            self.next_generation()

    def visualize(self):
        # return the result
        return self.sum_number_pot_containing__plants()


def find_all_orientation(line, y, orientation):
    obj = set()
    x = 0
    # orientation
    # first iteration
    while line.find(orientation, x) != -1:
        x = line.find(orientation, x)
        if x == -1:
            break
        obj.add((x, y, orientation))
        x += 1
    if len(obj) == 0:
        return 0
    return obj


class ObjectBuilder:
    # class that permits to create all object
    def __init__(self, lines):
        self.carts = []
        self.lines = lines

    def build_carts(self):
        # return a list of carts as (x, y, orientation of cart)
        carts = []
        y = 0
        for line in self.lines:
            right_orientation = find_all_orientation(line, y, ">")
            if right_orientation != 0:
                carts.append(find_all_orientation(line, y, ">"))
            left_orientation = find_all_orientation(line, y, "<")
            if left_orientation != 0:
                carts.append(find_all_orientation(line, y, "<"))
            up_orientation = find_all_orientation(line, y, "^")
            if up_orientation != 0:
                carts.append(find_all_orientation(line, y, "^"))
            down_orientation = find_all_orientation(line, y, "v")
            if down_orientation != 0:
                carts.append(find_all_orientation(line, y, "v"))
            y += 1
        return carts

    def build_curves(self):
        curves_up_left, curves_up_right = ([], [])
        y = 0
        for line in self.lines:
            curves_up_left.append(find_all_orientation(line, y, "/"))
            curves_up_right.append(find_all_orientation(line, y, '\\'))
            y += 1
        print(len(curves_up_left))
        print(len(curves_up_right))
        print(curves_up_left)
        print(curves_up_right)
        prob = (len(curves_up_left) + len(curves_up_right))
        print("probably ", int((prob/4)), " curves")
        # TODO build the curves
        #print(len(curves_up_left), " ", len(curves_up_right))

    def draw_new_curves(self):
        # TODO draw new curves using carts and collision only


    def build_intersec_path(self):
        pass



def data_retrieve(lines):
    # return the new lines traited
    ob = ObjectBuilder(lines)
    # cart(x, y, orientation)
    carts = ob.build_carts()
    print(carts)
    ob.build_curves()
    # count nb cart
    return lines


def data_preparation(lines):
    # return the value of input
    return lines


def day_13_part_1(lines):
    # data retrieve
    lines = data_retrieve(lines)
    # data preparation
    lines= data_preparation(lines)
    # data modelisation
    #plants_life_being = GenerationPlant(input_line, constraints)
    # data analyse
    #plants_life_being.execute()
    # data visualize
    #sum_number_of_plants_last_generation = plants_life_being.visualize()
    return str(0)


class TestDay13part1(unittest.TestCase):

    def test_day_13_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_13_part_1(lines)
        print(pred)
        #assert(pred == res)


if __name__ == '__main__':
    unittest.main()
