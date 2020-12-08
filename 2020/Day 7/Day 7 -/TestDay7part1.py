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


def get_nb_bag_colors_one_shiny_gold_bag(lines):
    nb_bag_colors = 0
    rules = []
    # get rules
    for line in lines:
        first_part, second_part = line.split("contain ")  # split the line in two parts
        if "other bag" not in second_part:
            rules.append((" ".join(first_part.split(" ")[0:2]), [" ".join(sp.split(" ")[1:3]) for sp in second_part.split(", ")]))  # parse rules

    def get_all_bag_color_that_can_be_contain(bag, all_bag_color):
        childs_bag = [rule[1] for rule in rules if rule[0] == bag]  # get subbag of current bag
        if len(childs_bag) == 0:  # case there was not subbag
            return all_bag_color  # return all the bag color
        [all_bag_color.add(elmt) for elmt in childs_bag[0]]  # update bags color for each subbag
        [[all_bag_color.add(elmt) for elmt in get_all_bag_color_that_can_be_contain(child_bag, all_bag_color)] for child_bag in childs_bag[0]]  # get all subbag deeper
        return all_bag_color

    for rule in rules:  # for each rule
        all_bag_color = get_all_bag_color_that_can_be_contain(rule[0], set())  # get all colors
        if "shiny gold" in all_bag_color:  # case shiny gold in all rule color
            nb_bag_colors += 1  # increment

    return nb_bag_colors  # return nb of valid password


class TestDay7part1(unittest.TestCase):

    def test_day_7_part_1(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_bag_colors_one_shiny_gold_bag(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
