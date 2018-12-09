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
    def __init__(self, num_node, child_nodes, metadata_entries, parent_num_node, metadata=[]):
        self.num_node = num_node
        self.child_nodes = child_nodes
        self.metadata_entries = metadata_entries
        self.metadata = metadata
        self.parent_num_node = parent_num_node
        self.children_num_node = []

    def is_parent(self):
        # return true if the node is a parent
        if len(self.children_num_node) > 0:
            return True
        return False

    def add_new_children(self, new_children_num_node):
        # add a new children on the list
        self.children_num_node.append(new_children_num_node)

    def get_num_node(self):
        # return the num of node
        return self.num_node

    def get_metadata(self):
        # return the list of metadata
        return self.metadata

    def set_metadata(self, metadata):
        # set the metadata list
        self.metadata = metadata

    def get_child_nodes(self):
        # return the number of children
        return self.child_nodes

    def get_metadata_entries(self):
        # return the number of metadata entries
        return self.metadata_entries

    def get_children_num_node(self):
        # return the children num node
        return self.children_num_node

    def get_parent_num_node(self):
        return self.parent_num_node


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
        self.recursivity_memory_ = []

    def get_nodes(self):
        # return the list of nodes
        return self.nodes

    def print_node(self):
        sum_lengh_metadata = 0
        for node in self.nodes:
            if len(self.nodes) < len(string.ascii_uppercase):
                print(string.ascii_uppercase[node.num_node-1], " ", node.child_nodes, " ", node.metadata_entries, " ", node.metadata)
                print("Children ", [string.ascii_uppercase[c-1] for c in node.children_num_node])
            else:
                print(node.num_node-1, " ", node.child_nodes, " ", node.metadata_entries, " ", node.metadata)
                print("Children ", node.children_num_node)
            sum_lengh_metadata += len(node.metadata)
        print("self.recursivity_memory ", self.recursivity_memory)
        print("-------------------------------")

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

    def child_with_metadata(self, metadata_entries, parent_num_node):
        # create the node directly
        num_node = self.get_next_num_node()
        # add metadata on node
        metadata = self.metadata_retrieve(metadata_entries)
        # create the associate node
        node = Node(num_node, 0, metadata_entries, parent_num_node, metadata)
        # add it on the list of node
        self.add_node(node)

    def child_without_metadata(self, nb_child, metadata_entries, parent_num_node):
        # create the node directly
        num_node = self.get_next_num_node()
        # get the metadata later
        # create the associate node
        node = Node(num_node, nb_child, metadata_entries, parent_num_node)
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
        # remove the num node on memory
        self.recursivity_memory.pop()

    def alloc_memory_recurivity_(self, child_num_node):
        # add the next num node on memory
        self.recursivity_memory_.append(child_num_node)

    def free_memory_recurivity_(self):
        # add the num node on memory
        self.recursivity_memory_.pop()

    def nb_child_zero_or_different(self, nb_child, metadata_entries):
        # proceed by two case
        if nb_child == 0:
            # create the child with his metadata
            self.child_with_metadata(metadata_entries, self.get_num_node())
        else:
            # alloc memory for recursivity
            self.alloc_memory_recurivity()
            #self.print_node()
            # create the child without metadata
            self.child_without_metadata(nb_child, metadata_entries, self.get_num_node())
            # recursive to find the child of the current child
            self.find_children(self.get_num_node(), nb_child)
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
        return root_num_node, root_child_nodes, root_metadata_entries, root_num_node - 1, root_metadata

    def find_children(self, num_node, child_nodes, root=False):
        # recursive loop to find children of a child
        for i in range(child_nodes):
            # get the parent node
            parent_node = self.get_nodes()[num_node-1]
            # add children on parent node
            parent_node.add_new_children(self.get_num_node()+1)
            # get the current header
            nb_child, metadata_entries = self.get_next_header()
            # proceed the right case
            self.nb_child_zero_or_different(nb_child, metadata_entries)

    def is_child_num_node_parent(self, child_num_node):
        # return true if the child is a parent too
        for node in self.nodes:
            # get children
            children = node.get_children_num_node()
            for child in children:
                if child.get_num_node() == child_num_node:
                    return True
            # if children equals child_num_node
            # return True
        return False

    def get_child_num_node_by_index(self, node, index):
        # return the child of node using index to pick it
        children_num_node = node.get_children_num_node()
        # index - 1 : Pour A[1, 1, 2] si index vaut 1,
        # ça veut dire que nous choisissons le premier enfant de A,
        # dans notre cas B qui vaut 2 dans notre liste de noeuds
        print(node.get_num_node())
        print("index ", index)
        print("children_num_node ", children_num_node)
        return children_num_node[index - 1]
        # step 1 : get_children_num_node() = > Pour A, B devient 1 et C devient 2

    def find_value(self, child_num_node):
        # find the value of the child node indexed
        # get the node using num node
        print("child_num_node ", child_num_node)
        print("self.get_node_using_num_node(self.nodes[child_num_node].get_parent())", self.get_node_using_num_node(self.nodes[child_num_node].get_parent_num_node()))
        # we want to get the node give
        # the node is 1 for the first example
        child_node = self.get_node_using_num_node(self.get_child_num_node_by_index(self.get_node_using_num_node(self.nodes[child_num_node].get_parent_num_node()), child_num_node))
        print("not child_node.is_parent() ", not child_node.is_parent())
        # case with no child
        if not child_node.is_parent():
            # it is the case of B [10 , 11, 12] = 33
            # get the sum of children using num node
            print("B num = ", child_num_node)
            print("B = ", sum(child_node.get_metadata()))
            return sum(child_node.get_metadata())
        # case with parent
        else:
            # get children)
            # it is the case of C which we get his metadata
            children_metadata_entries = child_node.get_metadata()
            print("children_metadata_entries ", children_metadata_entries)
            sum_value = 0
            # browse using in child using index
            for children_metadata_entrie in children_metadata_entries:
                # case index is wrong
                if children_metadata_entrie <= child_node.get_child_nodes():
                    #child_num_node_ = self.get_child_num_node_by_index(child_node, children_metadata_entrie)
                    print("child_num_node_ ", children_metadata_entrie, " ", child_node.get_child_nodes())
                    sum_value += self.find_value(children_metadata_entrie)  # correspond a 2 soit C

            print("C num = ", child_num_node)
            print("C = ", sum_value)
            return sum_value
            """
            # alloc memory for recursivity
            self.alloc_memory_recurivity()
            #self.print_node()
            # create the child without metadata
            self.child_without_metadata(nb_child, metadata_entries)
            # recursive to find the child of the current child
            self.find_children(self.get_num_node(), nb_child)
            # add metadata on node created before
            metadata = self.metadata_retrieve(metadata_entries)
            # update the associate node using memory for recursivity
            node_before_recursivity = self.get_node_using_num_node(self.recursivity_memory[-1])
            # free memory after recusivity
            self.free_memory_recurivity()
            # set the metadata
            node_before_recursivity.set_metadata(metadata)
            """

    def exec(self):
        # create the root node
        root_node = Node(*self.create_root())
        # add it on the list of node
        self.add_node(root_node)
        # call the recursive function for the first time using root_node
        self.find_children(root_node.get_num_node(), root_node.get_child_nodes(), True)

    def get_sum_metadata_entries_only_child_root(self, root_num_node):
        # return the sum of children values of root
        sum_metadata_entries = 0
        # we know the root is the number one
        # we get the metadata entries
        root_node = self.get_node_using_num_node(root_num_node)
        # we get the metadata entries of root
        root_metadata_entries = root_node.get_metadata()
        # root_metadata_entries represent [1, 1, 2] which were [B, B, C]
        for root_metadata_entrie in root_metadata_entries:
            print("root_metadata_entrie ", root_metadata_entrie)
            oldval = sum_metadata_entries
            if root_metadata_entrie < root_node.get_child_nodes() and root_metadata_entries != 0:
                sum_metadata_entries += self.find_value(root_metadata_entrie) # root_metadata_entrie correspond a l'index 1 soit B
            print(sum_metadata_entries - oldval)
        return sum_metadata_entries


def day_8_part_2(lines):
    # data retrieve
    numbers = lines[0].split(' ')
    # data preparation
    metadata_searcher = MetadataSearcher(numbers)
    # data modelisation
    metadata_searcher.exec()
    # data analyse
    # sum_metadata_entries_only_child_root
    root_num_node = 1
    sum_values_root = metadata_searcher.get_sum_metadata_entries_only_child_root(root_num_node)
    # data visualize
    #metadata_searcher.print_node()
    return str(sum_values_root)


class TestDay8part1(unittest.TestCase):

    def test_day_8_part_2(self):
        lines = input_file()
        #res = output_file()
        pred = day_8_part_2(lines)
        print("pred ", pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
