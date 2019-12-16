import unittest
from parse import parse
import copy
from pprint import pprint


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


def update_using_nm_e_ne(tmp_map, element, new_element):
    """
    Update the map using the new element that will block visibility of other asteroids
    :param tmp_map: the tempory map
    :param element: the element as (x, y)
    :param new_element: the new element as (x, y)
    """
    height = len(tmp_map)
    width = len(tmp_map[0])
    e_x, e_y = element
    ne_x, ne_y = new_element
    diff_x = ne_x - e_x
    diff_y = ne_y - e_y

    def is_in_map(test_element):
        x, y = test_element
        if x < 0 or y < 0 or x > width - 1 or y > height - 1:
            return False
        return True

    def is_line(x, y):
        # case line
        if x == 0 or y == 0:
            return True
        # case diagonal
        if abs(x) - abs(y) == 0:
            return True
        # case horse movement
        return False

    #if element == (3, 4):
    #    print("New element" , new_element)
    # case it is a line
    if is_line(diff_x, diff_y):
        i_x, i_y = new_element
        beg = True
        while is_in_map(new_element):
            if not beg:
                """if (i_x, i_y) == (11, 13):
                    print("WTF line", new_element)
                """
                tmp_map[i_y][i_x] = "X"
            else:
                beg = False
            if diff_y < 0:
                i_y += -1
            if diff_y > 0:
                i_y += 1
            if diff_x < 0:
                i_x += -1
            if diff_x > 0:
                i_x += 1
            new_element = (i_x, i_y)
    # case it will be like a horse movement in chess
    else:
        prime = False
        p_x, p_y = (0, 0)
        # case prime number
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for prime_number in prime_numbers:
            if diff_x % prime_number == 0 and diff_y % prime_number == 0:
                p_x = int(diff_x / prime_number)
                p_y = int(diff_y / prime_number)
                prime = True
                break
        i_x, i_y = new_element
        old_element = new_element
        beg = True
        while is_in_map(new_element):
            # first iteration to keep #
            if not beg:
                """
                if (i_x, i_y) == (11, 13):
                    print("WTF horse", element, new_element, diff_x, diff_y, i_x, i_y)
                    # tmp_map[y][x] = "O"
                    str_print = ""
                    for i_l, l in enumerate(tmp_map):
                        for i_el, el in enumerate(l):
                            str_print += tmp_map[i_l][i_el]
                        str_print += "\n"
                    print(str_print)
                """
                tmp_map[i_y][i_x] = "X"
            else:
                beg = False
            if prime:
                i_x += p_x
                i_y += p_y
            else:

                #print(diff_y, diff_x)
                i_y += diff_y
                i_x += diff_x
            new_element = (i_x, i_y)


def get_around_visible_asteroids(tmp_map, element, the_range):
    #print("The current range", the_range)
    #print("The current element", element)
    # TODO test min max y
    around_visible_asteroids = []
    height = len(tmp_map)
    width = len(tmp_map[0])
    top, right, bot, left = (True, True, True, True)
    # Get min x
    x, y = element
    # case left line not exist
    if x < the_range:
        left = False
        #print("left line not exist")
    if x + the_range > width - 1:
        right = False
        #print("right line not exist")
    #if element == (4, 4):
        #print("Top test ", y, the_range, y - the_range)
    if y < the_range:
        top = False
        #print("top line not exist")
    if y + the_range > height - 1:
        bot = False
        #print("bottom line not exist")
    if not left and not right and not top and not bot:
        return []

    # init limits
    if x < the_range:
        min_width_range = 0
    else:
        min_width_range = x - the_range

    if x + the_range > width - 1:
        max_width_range = width - 1
    else:
        max_width_range = x + the_range
    if y - the_range < 0:
        min_height_range = 0
    else:
        min_height_range = y - the_range
    if y + the_range > height - 1:
        max_height_range = height - 1
    else:
        max_height_range = y + the_range
    # top case
    if top:
        # TODO specify the correct range using width
        #if element == (4, 4):
        #    print("Top case", min_width_range, max_width_range)
        for i in range(min_width_range, max_width_range + 1):
            #if element == (4, 4):
            #    print("Test top case", (i, y - the_range))
            if tmp_map[y - the_range][i] == "#":
                # add this coord on an array
                new_element = (i, y - the_range)
                #if element == (4, 4):
                #    print("new_element top", new_element)
                around_visible_asteroids.append(new_element)
                # update the tmp_map with the blocked visibility
                update_using_nm_e_ne(tmp_map, element, new_element)
    # right case
    if right:
        # TODO specify the correct range using height
        #if element == (4, 4):
        #    print("Right case", min_height_range, max_height_range, the_range)
        for i in range(min_height_range, max_height_range + 1):
            if tmp_map[i][x + the_range] == "#":
                # add this coord on an array
                new_element = (x + the_range, i)
                #if element == (4, 4):
                #    print("new_element", new_element)
                around_visible_asteroids.append(new_element)
                # update the tmp_map with the blocked visibility
                update_using_nm_e_ne(tmp_map, element, new_element)
    # bot case
    if bot:
        # TODO specify the correct range using width
        #print("Bot case from", (min_width_range, y + the_range), "to", (max_width_range, y + the_range) , "with range",the_range, "on", element)
        for i in range(min_width_range, max_width_range + 1):
            #print((i, y + the_range), the_range)
            #print(i, y+the_range, min_width_range, max_width_range)
            if tmp_map[y + the_range][i] == "#":
                # add this coord on an array
                new_element = (i, y + the_range)
                #if element == (4, 4):
                #    print("new_element", new_element)
                around_visible_asteroids.append(new_element)
                # update the tmp_map with the blocked visibility
                update_using_nm_e_ne(tmp_map, element, new_element)
    # left case
    if left:
        # TODO specify the correct range using height
        for i in range(min_height_range, max_height_range + 1):
            if tmp_map[i][x - the_range] == "#":
                # add this coord on an array
                new_element = (x - the_range, i)
                #if element == (4, 4):
                #    print("new_element left", new_element)
                around_visible_asteroids.append(new_element)
                # update the tmp_map with the blocked visibility
                update_using_nm_e_ne(tmp_map, element, new_element)

    return list(set(around_visible_asteroids))


def get_nb_asteroids(tmp_map, element):
    """
    Get the number of asteroids visible
    :param map: the map
    :param element: the element as (x, y)
    :return: the number of asteroids visible + 1
    """
    #print("Before visibles", element)
    asteroids_visible = []
    height = len(tmp_map)
    width = len(tmp_map[0])
    x, y = element
    top_max = y
    right_max = width - 1 - x
    bot_max = height - 1 - y
    left_max = x
    range_max = max([top_max, right_max, bot_max, left_max])
    #print("Before")
    #pprint(tmp_map)
    # get all asteroids visible around range 1
    for i in range(1, range_max + 1):
        asteroids_visible += get_around_visible_asteroids(tmp_map, element, i)
    """
    if element == (0, 0):
        print(range_max)
        #tmp_map[y][x] = "O"
        str_print = ""
        for i_l, l in enumerate(tmp_map):
            for i_el, el in enumerate(l):
                str_print += tmp_map[i_l][i_el]
            str_print += "\n"
        print(str_print)
    """
    #print("After")

    # count #
    #i = 0
    #for i_l, l in enumerate(tmp_map):
        #    for i_el, el in enumerate(l):
        #        if tmp_map[i_l][i_el] == "#":
    #            i += 1
    #print("visibles", element, i-1, len(set(asteroids_visible)))

    return len(set(asteroids_visible))

def print_map(map, element):
    x, y = element
    str_print = ""
    for i_l, l in enumerate(map):
        for i_el, el in enumerate(l):
            if element == (i_el, i_l):
                str_print += "X"
            else:
                str_print += map[i_l][i_el]
        str_print += "\n"
    print(str_print)


class TestDay10part1(unittest.TestCase):

    def test_day_10_part_1(self):
        text = input_file()
        # res = output_file()
        # pred = day_2_part_1(text)
        # declare elements and map
        asteroids = []
        map = []

        lines = [val for val in text.split("\n")]
        for i_line, line in enumerate(lines):
            line_map = []
            for i_element, element in enumerate(line):
                line_map.append(element)
                if element == "#":
                    asteroids.append((i_element, i_line))
            map.append(line_map)
        #print(asteroids)
        #pprint(map)
        max = 0
        final_asteroid = ""
        nb_asteroid = 0
        # for each asteroids get the number of asteroid visible
        for asteroid in asteroids:
            #print("Original map")
            #pprint(map)
            tmp_map = copy.deepcopy(map)
            nb_asteroid = get_nb_asteroids(tmp_map, asteroid)

            if nb_asteroid > max:
                max = nb_asteroid
                final_asteroid = asteroid
        #print(max, final_asteroid)
        print_map(map, final_asteroid)

        def get_next_asteroid_using_map_and_laser_position(tmp_map, station, laser_position=False):
            height = len(tmp_map)
            width = len(tmp_map[0])
            x_station, y_station = station
            if not laser_position:
                # TODO get the first asteroid
                for y in range(y_station - 1, 0 - 1, -1):
                    print(y)
                    if tmp_map[y][x_station] == "#":
                        print("Boom", (x_station, y))
                        return (x_station, y)
            next_asteroid = (0, 0)
            # TODO changement de coordonnees
            old_x_laser, old_y_laser = laser_position
            x_laser = old_x_laser - x_station
            y_laser = old_y_laser - y_station
            # TODO la station est à (0, 0)
            #print(y_laser, x_laser)
            # case top-right
            if y_laser < 0 and abs(y_laser) > abs(x_laser) and x_laser >= 0:
                if x_laser == 0:
                    print("++boom")
                    x_laser += 1
                print("Top right")
                for x in range(x_laser, width - x_station):
                    for y in range(-y_station, 0, 1):
                        # and not on diag

                        #print("range", -y_station, y_laser + 1)
                        #print((x + x_station, y + y_station))
                        # print((x, y))
                        if tmp_map[y + y_station][x + x_station] == "#" and abs(x) != abs(y) and abs(y) > abs(x):
                            return (x + x_station, y + y_station)
            # case diag top-right
            for i in range(1, y_station - 1):
                #print(i + y_station, i + x_station)
                if tmp_map[y_station - i][i + x_station] == "#":
                    #if (i + x_station, y_station - i) == (8, 3):
                    #    print("WHY")
                    return (i + x_station, y_station - i)
            # case right-top
            # TODO get list asteroids
            # TODO use laser_position

            # TODO The order is up, right, down and left
            # TODO It means -y to +x to +y to -x then loop
            return next_asteroid

        def update_using_laser_position(tmp_map, laser_position, i):
            x, y = laser_position
            tmp_map[y][x] = str(i)

        station = final_asteroid
        tmp_map = copy.deepcopy(map)
        laser_position = False
        for i in range(1, len(asteroids) + 1):
            # get the next position of the laser
            laser_position = get_next_asteroid_using_map_and_laser_position(tmp_map, station, laser_position)
            #print("Before first", laser_position)
            print_map(tmp_map, station)
            # remove the asteroid on the current map
            update_using_laser_position(tmp_map, laser_position, i)
            print("After ", laser_position)
            print_map(tmp_map, station)
            if i == 6:
                break
            if i == 200:
                x, y = laser_position
                print(x*100 + y)
        if len(asteroids) < 200:
            print(laser_position)


        #coordinate_220th = (8, 2)
        #x, y =coordinate_220th
        #print(x*100 + y)
        #


if __name__ == '__main__':
    unittest.main()
