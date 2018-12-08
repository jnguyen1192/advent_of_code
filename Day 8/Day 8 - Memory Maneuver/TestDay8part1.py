import unittest
import string


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


class RootNode:
    # the first node of numbers
    def __init__(self, numbers):
        # convert string list into int list
        self.numbers = list(map(int, numbers))

    def get_child_nodes(self):
        #return the fist number
        return self.numbers[0]

    def get_metadata_entries(self):
        #return the second number
        return self.numbers[1]

    def get_metadata(self):
        # return the metadata at the end of numbers
        return self.numbers[-self.get_metadata_entries():]


class Node:
    # class that illustrate a node containing header, child nodes and metadata entries
    def __init__(self, num_node, child_nodes, metadata_entries, metadata=[]):
        self.num_node = num_node
        self.child_nodes = child_nodes
        self.metadata_entries = metadata_entries
        self.metadata = metadata

    def get_num_node(self):
        # return the num of node
        return self.num_node

    def get_metadata(self):
        # return the list of metadata
        return self.metadata

    def set_metadata(self, metadata):
        self.metadata = metadata

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
        self.is_visit = [False] * len(numbers)
        self.num_node = 0
        self.iterator = 0
        self.child_iterator = len(numbers) - 1
        self.recursivity_memory = []

    def get_node_using_num_node(self, num_node):
        # return the node with the num node given as parameter
        for node in self.nodes:
            if node.get_num_node() == num_node:
                return node

    def get_num_node(self):
        # return the num of node
        return self.num_node

    def get_next_num_node(self):
        # return the n+1 num of node
        self.num_node += 1
        return self.num_node

    def previous_num_node(self):
        # get the previous node for recusivity
        self.num_node -= 1

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

    def metadata_retrieve(self, metadata_entries):
        # return the metadata of current position increment the iterator
        metadata = []
        # browse in numbers to find next metadata entries
        for i in range(metadata_entries):
            metadata.append(self.numbers[self.get_iterator()])
            self.next_iterator()
        return metadata

    def child_with_metadata(self, metadata_entries):
        # create the node directly
        num_node = self.get_next_num_node()
        # add metadata on node
        metadata = self.metadata_retrieve(metadata_entries)
        # create the associate node
        node = Node(num_node, 0, metadata_entries, metadata)
        # add it on the list of node
        self.add_node(node)

    def child_without_metadata(self, nb_child, metadata_entries):
        # create the node directly
        num_node = self.get_next_num_node()
        # get the metadata later
        # create the associate node
        node = Node(num_node, nb_child, metadata_entries)
        # add it on the list of node
        self.add_node(node)

    def get_next_header(self):
        # return the header composed by the couple (nb_child, metadata_entries)
        nb_child = self.numbers[self.iterator]
        # increment the iterator
        self.next_iterator()
        metadata_entries = self.numbers[self.iterator]
        # increment the iterator
        self.next_iterator()
        return nb_child, metadata_entries

    def alloc_memory_recurivity(self):
        # add the next num node on memory
        self.recursivity_memory.append(self.num_node + 1)

    def free_memory_recurivity(self):
        # add the num node on memory
        self.recursivity_memory.pop()

    def nb_child_zero_or_different(self, nb_child, metadata_entries):
        # proceed by two case
        if nb_child == 0:
            # create the child with his metadata
            self.child_with_metadata(metadata_entries)
        else:
            # alloc memory for recursivity
            self.alloc_memory_recurivity()
            # create the child without metadata
            self.child_without_metadata(nb_child, metadata_entries)
            # recursive to find the child of the current child
            self.find_children(nb_child)
            # add metadata on node created before
            metadata = self.metadata_retrieve(metadata_entries)
            # update the associate node using memory for recursivity
            node_before_recursivity = self.get_node_using_num_node(self.recursivity_memory[-1])
            # free memory after recusivity
            self.free_memory_recurivity()
            # set the metadata
            node_before_recursivity.set_metadata(metadata)

    def get_sum_metadata_entries(self):
        # return the sum of all metadata entries
        sum_metadata = 0
        for node in self.nodes:
            sum_metadata += sum(node.get_metadata())
        return sum_metadata

    def print_node(self):
        sum_lengh_metadata = 0
        for node in self.nodes:
            print(string.ascii_uppercase[node.num_node-1], " ", node.child_nodes, " ", node.metadata_entries, " ", node.metadata)
            sum_lengh_metadata += len(node.metadata)
        print("self.recursivity_memory ", self.recursivity_memory)
        print("-------------------------------")

    def create_root(self):
        # return parameters to create a node root
        root_node = RootNode(self.numbers)
        # create the node directly
        root_num_node = self.get_next_num_node()
        # get the number of children of root
        root_child_nodes = root_node.get_child_nodes()
        # increment the iterator
        self.next_iterator()
        # get the number of metadata entries of root
        root_metadata_entries = root_node.get_metadata_entries()
        # increment the iterator
        self.next_iterator()
        # get the metadata of root
        root_metadata = root_node.get_metadata()
        return root_num_node, root_child_nodes, root_metadata_entries, root_metadata

    def find_children(self, child_nodes):
        # recusive loop to find children of a child
        for i in range(child_nodes):
            # get the current header
            nb_child, metadata_entries = self.get_next_header()
            # proceed the right case
            self.nb_child_zero_or_different(nb_child, metadata_entries)

    def exec(self):
        # create the root node
        root_node = Node(*self.create_root())
        # add it on the list of node
        self.add_node(root_node)
        # call the recursive function for the first time using root_node
        self.find_children(root_node.get_child_nodes())


def day_8_part_1(lines):
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


class TestDay5part1(unittest.TestCase):

    def test_day_8_part_1(self):
        lines = input_file()
        #res = output_file()
        pred = day_8_part_1(lines)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
