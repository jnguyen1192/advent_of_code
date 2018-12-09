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
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class Node:
    # class that illustrate a node containing header, child nodes and metadata entries
    def __init__(self, num_node):
        self.num_node = num_node


class MetadataSearcher:
    # class to transform a line into nodes using an iterator to browse the numbers
    def __init__(self, numbers):
        # convert string list into int list
        self.numbers = list(map(int, numbers))

    def exec(self):
        # create the root node
        root_node = Node(*self.create_root())
        # add it on the list of node
        self.add_node(root_node)
        # call the recursive function for the first time using root_node
        self.find_children(root_node.get_child_nodes())


def day_10_part_1(lines):
    # data retrieve
    numbers = lines[0].split(' ')
    # data preparation
    metadata_searcher = MetadataSearcher(numbers)
    # data modelisation
    metadata_searcher.exec()
    # data analyse
    sum_metadata_entries = metadata_searcher.get_sum_metadata_entries()
    # data visualize
    #metadata_searcher.print_node()
    return str(sum_metadata_entries)


class TestDay10part1(unittest.TestCase):

    def test_day_10_part_1(self):
        lines = input_file()
        res = output_file()
        pred = day_10_part_1(lines)
        assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
