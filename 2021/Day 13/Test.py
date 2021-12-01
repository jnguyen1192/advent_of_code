import unittest


def input_file(suffix):
    file = open('input_' + suffix, 'r')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    return lines


def output_file(number):
    file = open('output_'+str(number), 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


def get_differences(lines):
    adapters = []
    for line in lines:
        adapters.append(int(line))
    adapters.sort()
    #print(adapters)
    differences = {1: 1,
                   2: 1,
                   3: 1}
    for index, adapter in enumerate(adapters[:-1]):  # count difference
        #print(adapter, adapters[index + 1], abs(adapter - adapters[index + 1]))
        differences[abs(adapter - adapters[index + 1])] += 1
    return differences[1],  differences[3]


def get_ID_earliest_bus(lines):
    ID_current_bus = int(lines[0])
    IDs_bus = [int(str_ID_bus) for str_ID_bus in lines[1].replace(",x", ",-1").split(",")]
    ID_next_bus = -1
    min_wait = 1000000
    for ID_bus in IDs_bus:
        if ID_bus == -1:
            continue
        wait = int(ID_current_bus / ID_bus) * ID_bus + ID_bus - ID_current_bus
        if wait < min_wait:
            min_wait = wait
            ID_next_bus = ID_bus
    return min_wait * ID_next_bus# "OK"


def get_time_stamp_ID_earliest_bus_part_2(test_timestamp, IDs_bus):
    ID_next_bus = -1
    min_wait = 1000000
    for ID_bus in IDs_bus:
        if ID_bus == -1:
            continue
        wait = int(test_timestamp / ID_bus) * ID_bus + ID_bus - test_timestamp
        if wait < min_wait:
            min_wait = wait
            ID_next_bus = ID_bus
    return min_wait, ID_next_bus# "OK"


def get_earliest_timestamp_matching_list(lines):
    ID_current_bus = int(lines[0])
    IDs_bus_to_match = [int(str_ID_bus) for str_ID_bus in lines[1].replace(",x", ",-1").split(",")]
    test_print = 1
    timestamp = 0
    while True:
        test_IDs_bus_to_match = []
        test_timestamp = timestamp
        #print(timestamp)
        for index, ID_bus in enumerate(IDs_bus_to_match[:int(len(IDs_bus_to_match)/2)]):
            if test_timestamp % IDs_bus_to_match[index] == 0:  # first
                test_IDs_bus_to_match.insert(index, IDs_bus_to_match[index])
                if timestamp == 702007178 or timestamp == 1202161486:
                    print(len(test_IDs_bus_to_match))
                    print("Insert", index, IDs_bus_to_match[index])
                    print(test_IDs_bus_to_match)
            else:
                test_IDs_bus_to_match.insert(index, -1)

            if timestamp == 702007178 or timestamp == 1202161486:
                print("Before bug", timestamp, test_timestamp + len(IDs_bus_to_match) - index - 1, IDs_bus_to_match[len(IDs_bus_to_match) - index - 1])

            if (test_timestamp + len(IDs_bus_to_match) - index - 1) % IDs_bus_to_match[len(IDs_bus_to_match) - index - 1] == 0:  # first
                test_IDs_bus_to_match.insert(index + 1, IDs_bus_to_match[len(IDs_bus_to_match) - index - 1])
                if timestamp == 702007178 or timestamp == 1202161486:
                    print(len(test_IDs_bus_to_match))
                    print("Insert", index + 1, IDs_bus_to_match[len(IDs_bus_to_match) - index - 1])
                    print(test_IDs_bus_to_match)
            else:
                test_IDs_bus_to_match.insert(index + 1, -1)

            if timestamp == 1202161486:
                print(timestamp, test_timestamp, test_IDs_bus_to_match)
            if not(IDs_bus_to_match[index] == test_IDs_bus_to_match[index] and
            IDs_bus_to_match[len(IDs_bus_to_match) - index - 1] == test_IDs_bus_to_match[index + 1]):
                # TODO is in list fist and last then first + 1 and last - 1
                result = 1
                for x in test_IDs_bus_to_match:
                    result = result * x
                #print("Optimize")
                timestamp += abs(result)
                break
            test_timestamp += 1
        #print(timestamp)
        if ((timestamp+1)/10**test_print) > 1:
            test_print += 1
            print(timestamp, test_IDs_bus_to_match)
        if IDs_bus_to_match == test_IDs_bus_to_match:
            print("Final", IDs_bus_to_match, "=", test_IDs_bus_to_match)
            return timestamp

        #print(timestamp)
        timestamp += IDs_bus_to_match[0] #  TODO optimize
        #print(timestamp, IDs_bus_to_match[0])


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        #res = output_file("test_1")  # get output_1
        pred = get_ID_earliest_bus(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        departure_ids = [
            (int(v), (int(v) - i) % int(v))
            for i, v in enumerate(lines[1].split(","))
            if v != "x"
        ]

        i = 0
        k = departure_ids[i][0]
        increment = k
        while True:
            div, mod = departure_ids[i + 1]
            if k % div == mod:
                if i == len(departure_ids) - 2:
                    print(k)
                    break
                increment *= div
                i += 1
            k += increment
        #pred = get_earliest_timestamp_matching_list(lines)  # process
        #print(pred)  # print 1033238510395
        assert(str(0) == res[0])  # check https://github.com/busdriverbuddha/aoc2020_solutions/blob/main/day13.py
        """
        10002435027
        195492481379
        1033238510395
        """


if __name__ == '__main__':
    unittest.main()
