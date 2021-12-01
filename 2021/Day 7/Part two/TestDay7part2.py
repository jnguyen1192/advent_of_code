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
    rules = []
    # get rules
    for line in lines:
        first_part, second_part = line.split("contain ")
        # rule
        if "other bag" not in second_part:
            rules.append((" ".join(first_part.split(" ")[0:2]), [(sp.split(" ")[0], " ".join(sp.split(" ")[1:3])) for sp in second_part.split(", ")]))

    def get_value(bag):
        for rule in rules:
            if rule[0] == bag:  # when the rule bag is found
                return sum([int(child[0]) + int(child[0]) * get_value(child[1]) for child in rule[1]])  # get the value of each bags subcontainer add it and product it
        return 0  # case contains no other bags

    final_value = get_value("shiny gold")




    # get result

    #pprint(rules)
    return final_value  # return nb of valid password


class TestDay7part2(unittest.TestCase):

    def test_day_7_part_2(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_nb_bag_colors_one_shiny_gold_bag(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
