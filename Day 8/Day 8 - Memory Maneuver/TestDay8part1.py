import unittest
from parse import parse


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
    def __init__(self, num_node, child_nodes, metadata_entries, metadata):
        self.num_node = num_node
        self.child_nodes = child_nodes
        self.metadata_entries = metadata_entries
        self.metadata = metadata

    def get_metadata(self):
        return self.metadata

    def get_child_nodes(self):
        return self.child_nodes

    def get_metadata_entries(self):
        return self.metadata_entries


class MetadataSearcher:
    # class to transform a line into nodes using an iterator to browse the numbers
    def __init__(self, numbers):
        # convert string list into int list
        self.numbers = list(map(int, numbers))
        self.nodes = []
        self.num_node = 0
        self.iterator = 0
        self.child_iterator = len(numbers) - 1

    def get_next_num_node(self):
        # return the n+1 num of node
        self.num_node += 1
        return self.num_node

    def next_iterator(self):
        # increment the iterator by one
        self.iterator += 1

    def get_iterator(self):
        # return the current iterator
        return self.iterator

    def next_child_iterator(self):
        # increment the iterator by one
        self.child_iterator -= 1

    def get_child_iterator(self):
        # return the current iterator
        return self.child_iterator

    def add_node(self, node):
        # add the node in the node list
        self.nodes.append(node)

    def child_equals_zero(self, metadata_entries):
        # create the node directly
        num_node = self.get_next_num_node()
        # add metadata on node
        metadata = []
        # browse in numbers to find next metadata entries
        for i in range(metadata_entries):
            metadata.append(self.numbers[self.get_iterator()])
            self.next_iterator()
        # create the associate node
        node = Node(num_node, 0, metadata_entries, metadata)
        # add it on the list of node
        self.add_node(node)

    def child_different_zero(self, nb_child, metadata_entries):
        # create the node directly
        num_node = self.get_next_num_node()
        # add metadata on node
        metadata = []
        # browse in numbers to find next metadata entries
        for i in range(metadata_entries):
            #print(self.get_child_iterator())
            metadata.append(self.numbers[self.get_child_iterator()])
            self.next_child_iterator()
        # create the associate node
        node = Node(num_node, nb_child, metadata_entries, metadata)
        # add it on the list of node
        self.add_node(node)

    def get_next_header(self):
        # return the header composed by the couple (nb_child, metadata_entries)
        nb_child = self.numbers[self.iterator]
        self.next_iterator()
        metadata_entries = self.numbers[self.iterator]
        print(nb_child, " ", metadata_entries)
        self.next_iterator()
        return nb_child, metadata_entries

    def nb_child_zero_or_different(self, nb_child, metadata_entries):
        # proceed the two case
        if nb_child == 0:
            self.child_equals_zero(metadata_entries)
        else:
            self.child_different_zero(nb_child, metadata_entries)

    def get_end_iterator(self):
        # return the index of the last iterator using nodes nb_child and metadata_entries
        reverse_end_iterator = 0
        for node in self.nodes:
            if node.get_child_nodes() != 0:
                reverse_end_iterator += node.get_metadata_entries()
        print('self.iterator ', self.iterator)
        return len(self.numbers) - reverse_end_iterator

    def get_sum_metadata_entries(self):
        # return the sum of all metadata entries
        sum_metadata = 0
        for node in self.nodes:
            sum_metadata += sum(node.get_metadata())
        return sum_metadata

    def exec(self):
        # browse until the end of the searcher
        while self.get_iterator() != self.get_end_iterator():
            # get the current header
            nb_child, metadata_entries = self.get_next_header()
            # proceed the right case
            self.nb_child_zero_or_different(nb_child, metadata_entries)


def day_8_part_1(lines):
    # data retrieve
    numbers = lines[0].split(' ')
    # data preparation
    metadata_searcher = MetadataSearcher(numbers)
    # data modelisation
    metadata_searcher.exec()
    # data analyse
    sum_metadata_entries = metadata_searcher.get_sum_metadata_entries()
    return str(sum_metadata_entries)


class TestDay5part1(unittest.TestCase):

    def test_day_8_part_1(self):
        lines = input_file()
        #res = output_file()
        pred = day_8_part_1(lines)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
