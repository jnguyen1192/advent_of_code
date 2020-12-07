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
        first_part, second_part = line.split("contain ")
        # rule
        if "other bag" not in second_part:
            rules.append((" ".join(first_part.split(" ")[0:2]), [(sp.split(" ")[0], " ".join(sp.split(" ")[1:3])) for sp in second_part.split(", ")]))
    from pprint import pprint

    def get_all_bag_color_that_can_be_contain(bag, all_bag_color=set()):
        childs_bag = [rule[1] for rule in rules if rule[0] == bag]
        #print(childs_bag)
        #print("get_all_bag_color_that_can_be_contain", childs_bag, all_bag_color)
        if len(childs_bag) == 0:
            #print(bag)
            return all_bag_color
        [all_bag_color.add(elmt) for elmt in childs_bag[0]]
        for child_bag in childs_bag[0]:
            [all_bag_color.add(elmt) for elmt in get_all_bag_color_that_can_be_contain(child_bag, all_bag_color)]
                #print("in", all_bag_color)
        return all_bag_color

    def get_value(bag, final_value=1):
        for rule in rules:
            if rule[0] == bag:
                print("rule[1]", rule[1])
                print("for child in rule[1]", [child for child in rule[1]])
                [print(int(child[0]), "*", get_value(child[1], final_value)) for child in rule[1]]
                final_value = sum([int(child[0]) * get_value(child[1], final_value) for child in rule[1]])
        return final_value

    # apply rules
    apply_rules = []
    final_value = get_value("shiny gold", 1)




    # get result

    #pprint(rules)
    return final_value  # return nb of valid password


class TestDay6part1(unittest.TestCase):

    def test_day_6_part_1(self):
        lines = input_file()  # get input
        res = output_file()  # get output
        pred = get_nb_bag_colors_one_shiny_gold_bag(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
