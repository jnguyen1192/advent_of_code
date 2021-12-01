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


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        res = output_file("1")  # get output_1
        def solve(card_public_key, door_public_key):
            MOD = 20201227
            def find_loop_size(subject, card_public_key):
                for i in range(MOD):
                    if pow(subject, i, MOD) == card_public_key:
                        return i
                return -1
            return pow(door_public_key, find_loop_size(7, card_public_key), MOD)

            #print(f"Part 1: {pow(door_public_key, card_loop_size, 20201227)}")


        card_public_key, door_public_key = [int(line) for line in lines]
        pred = solve(card_public_key, door_public_key)
        print(pred)  # https://www.reddit.com/user/gidso/ https://www.reddit.com/r/adventofcode/comments/kjtg7y/2020_day_25_solutions/
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("day")  # get input_test
        dirs = {
            "e": (1, 0),
            "w": (-1, 0),
            "ne": (1, -1),
            "nw": (0, -1),
            "se": (0, 1),
            "sw": (-1, 1)
        }

        def get_coords(line):
            index = 0
            x, y = 0, 0
            while index < len(line):
                if index < len(line) - 1 and line[index:index + 2] in dirs:
                    chars = line[index:index + 2]
                    index += 2

                elif line[index] in dirs:
                    chars = line[index]
                    index += 1

                # print(chars, end=" ")
                changes = dirs[chars]

                x += changes[0]
                y += changes[1]

            return x, y

        def count_neighbors(coords):
            total = 0
            for neighbor_coords in get_neighbors(coords):
                if neighbor_coords in black:
                    total += 1

            return total

        def get_neighbors(coords):
            # Return a list of neighboring coords
            result = []
            for direction in dirs:
                changes = dirs[direction]
                neighbor_coords = (coords[0] + changes[0], coords[1] + changes[1])
                result.append(neighbor_coords)

            return result

        def iterate():
            stack = set()
            visited = set()
            new_black = black.copy()

            for tile in black:
                stack.add(tile)
                stack.update(get_neighbors(tile))

            while len(stack) > 0:
                coords = stack.pop()
                if coords in visited:
                    continue

                visited.add(coords)

                neighbor_count = count_neighbors(coords)
                if coords in black and (neighbor_count == 0 or neighbor_count > 2):
                    new_black.remove(coords)

                elif coords not in black and (neighbor_count == 2):
                    new_black.add(coords)

            return new_black

        # Do the initial flips
        black = set()
        for line in lines:
            coords = get_coords(line)
            if coords in black:
                black.remove(coords)
            else:
                black.add(coords)

        for _ in range(100):
            black = iterate()

        print(len(black))

        assert(0 == 0)


if __name__ == '__main__':
    unittest.main()
