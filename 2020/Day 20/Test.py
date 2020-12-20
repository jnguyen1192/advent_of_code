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


def get_multiply_ids_borders_tile():
    suffix = "day"
    file = open('input_' + suffix, 'r')
    tiles_raw = file.read().split("\n\n")
    tiles_raw[-1] = tiles_raw[-1]
    file.close()
    # create dict
    tiles = {}
    for tile_raw in tiles_raw:
        id_value_tile = tile_raw.split(":\n")
        # TODO flatten the square into borders
        """
        000     { 000 011 122 230 }
        3 1  =>       or
        221     { 000 110 221 032 }
        """
        square = id_value_tile[1].split("\n")
        top_border = list(square[0])
        right_border = [row[-1] for row in square]
        bot_border = list(square[-1][::-1])
        left_border = [row[0] for row in square][::-1]
        tiles[id_value_tile[0].split()[1]] = [[top_border, right_border, bot_border, left_border], 0, 1]
    h = int((len(tiles) ** (1/2)))
    w = int((len(tiles) ** (1/2)))
    #print(h, w, ((h - 2) * 2 + (w - 2) * 2), (h - 1) * (w - 1))
    final_nb_adj = 4 * 2 + 3 * ((h - 2) * 2 + (w - 2) * 2) + 4 * ((h - 2) * (w - 2))
    print(final_nb_adj, tiles)
# 2 3 2
# 3 4 3
# 2 3 2
# 3 * 3 <=> 24 = 4 * 2 + 4 * 3 + 1*4
# 2 3 3 2
# 3 4 4 3
# 2 3 3 2
# 3 * 4 <=> 34 = 4*2 + 6*3 + 2*4
# 2 3 3 2
# 3 4 4 3
# 3 4 4 3
# 2 3 3 2
# 3 * 4 <=> 34 = 4*2 + 3 * ((h-2) * 2 + (w-2) * 2) + 4*(h-1) * (w-1)
    def count_nb_adj(tile, tile_to_test):
        nb_adj = 0
        #if tile == '2473':
        #    print(tile, tile_to_test)
        for test_border in [t[::tiles[tile][2]] for t in tiles[tile][0]]:
            # check borders
            #if tile == '2473':
            #    print(test_border in [t[::tiles[tile_to_test][2]*-1] for t in tiles[tile_to_test][0]], test_border, [t[::tiles[tile_to_test][2]*-1] for t in tiles[tile_to_test][0]])
            if test_border in [t[::tiles[tile_to_test][2]*-1] for t in tiles[tile_to_test][0]]:
                nb_adj += 1
        return nb_adj
    final_nb_adj_test = 0
    # try each combination
    # there was 2 ** len(tiles) - 1 combinations in the example
    all_combination = []
    for i in range(2 ** len(tiles)):
        all_combination.append(
            [-1] * (len(tiles) - len(list("{0:b}".format(i)))) + [1 if j == '1' else -1 for j in list("{0:b}".format(i))])
    print("Combination", all_combination)
    dict_keys = list(tiles.keys())
    #print(list(dict_keys))
    i = 0
    while final_nb_adj_test != final_nb_adj:
        for index, combination in enumerate(all_combination[i]):
            tiles[dict_keys[index]][2] = combination
        i += 1
        final_nb_adj_test = 0
        for tile in tiles:
            # get nb adj
            nb_adj = 0
            max_tile_nb_adj = 0
            for tile_to_test in tiles:
                if tile != tile_to_test:
                    nb_adj += count_nb_adj(tile, tile_to_test)
                    if max_tile_nb_adj < nb_adj:
                        max_tile_nb_adj = nb_adj
            # add on dict
            tiles[tile][1] = max_tile_nb_adj
            final_nb_adj_test += max_tile_nb_adj
            #print(tile, tiles[tile])

        #print(final_nb_adj_test, [tiles[tile][1] for tile in tiles], [tiles[tile][2] for tile in tiles])
    prod = 1
    for tile in tiles:
        if tiles[tile][1] == 2:
            #print(tile)
            prod *= int(tile)

    #print(prod)
    return prod  #len([*filter(r.fullmatch, ms.split())])  # get nb cubes


import math

def readTiles(inpath="input_day"):
    tiles = {}
    with open(inpath, "r") as infile:
        for rawTile in infile.read().split("\n\n"):
            name, *lines = rawTile.splitlines()
            num = int(name[5:-1])
            lines = [list(l) for l in lines]
            tiles[num] = lines
        return tiles


def getBorders(tile):
    return (tile[0], [l[-1] for l in tile], tile[-1], [l[0] for l in tile])


def getFlips(tile):
    return [tile, tile[::-1], [l[::-1] for l in tile], [l[::-1] for l in tile][::-1]]


def getRots(tile):
    rots = [tile]
    last = tile
    for _ in range(3):
        tile = [l[:] for l in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x])-y-1][x]
        last = tile
        rots.append(tile)
    return rots


def getTransforms(tile):
    possible = []
    for flip in getFlips(tile):
        possible.extend(getRots(flip))
    output = []
    for pos in possible:
        if pos not in output:
            output.append(pos)
    return output


def recTile(tiled, tileOpts, dimension, x=0, y=0, seen=set()):
    if y == dimension:
        return tiled
    nextX = x + 1
    nextY = y
    if nextX == dimension:
        nextX = 0
        nextY += 1
    for id, tiles in tileOpts.items():
        if id in seen:
            continue
        seen.add(id)
        for transId, border in tiles.items():
            top, _, _, left = border

            if x > 0:
                neighborId, neighborTrans = tiled[x-1][y]
                _, neighborRight, _, _ = tileOpts[neighborId][neighborTrans]
                if neighborRight != left:
                    continue
            if y > 0:
                neighborId, neighborTrans = tiled[x][y-1]
                _, _, neighborBottom, _ = tileOpts[neighborId][neighborTrans]
                if neighborBottom != top:
                    continue
            tiled[x][y] = (id, transId)
            ans = recTile(tiled, tileOpts, dimension,
                          x=nextX, y=nextY, seen=seen)
            if ans is not None:
                return ans
        seen.remove(id)
    tiled[x][y] = None
    return None


def getTiled(tiles):
    tileOpts = {id: getTransforms(tile) for id, tile in tiles.items()}
    tileBorderOpts = {}
    for id, tiles in tileOpts.items():
        for idx, tile in enumerate(tiles):
            if id not in tileBorderOpts.keys():
                tileBorderOpts[id] = {}
            tileBorderOpts[id][idx] = getBorders(tile)
    dimension = math.isqrt(len(tileOpts))
    tiled = [[None] * dimension for _ in range(dimension)]
    return tileOpts, recTile(tiled, tileBorderOpts, dimension)


def part1(tiled):
    return tiled[0][0][0] * tiled[0][-1][0] * tiled[-1][0][0] * tiled[-1][-1][0]


def removeGuides(tileOpts, tiled):
    out = []
    for row in tiled:
        tiles = []
        for num, transId in row:
            tile = tileOpts[num][transId]
            tiles.append([l[1:-1] for l in tile[1:-1]])
        for y in range(len(tiles[0][0])):
            newRow = []
            for id in range(len(tiles)):
                newRow.extend(tiles[id][x][y] for x in range(len(tiles[id])))
            out.append(newRow)
    return out


MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def parseMonster():
    monsterLocs = []
    maxX, maxY = 0, 0
    for y2, line in enumerate(MONSTER.splitlines()):
        for x2, char in enumerate(line):
            if char == "#":
                monsterLocs.append((x2, y2))
                maxX = max(x2, maxX)
                maxY = max(y2, maxY)
    return monsterLocs, maxX, maxY


def checkMonsters(grid):
    monsterLocs, maxX, maxY = parseMonster()

    monsterSpots = set()
    for y in range(len(grid)):
        if y + maxY >= len(grid):
            break
        for x in range(len(grid[y])):
            if x + maxX >= len(grid[y]):
                break
            isMonster = True
            for xOff, yOff in monsterLocs:
                if grid[y+yOff][x+xOff] != "#":
                    isMonster = False
                    break
            if isMonster:
                for dx, dy in monsterLocs:
                    monsterSpots.add((x+dx, y+dy))
    if len(monsterSpots) == 0:
        return None
    allFilled = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                allFilled.add((x, y))
    return len(allFilled - monsterSpots)


def part2(tileOpts, tiled):
    grid = removeGuides(tileOpts, tiled)

    gridOpts = getTransforms(grid)

    for opt in gridOpts:
        ans = checkMonsters(opt)
        if ans is not None:
            return ans

class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        #res = output_file("1")  # get output_1
        #pred = get_multiply_ids_borders_tile()  # process
        #print(pred)  # print
        tiles = readTiles()
        tileOpts, tiled = getTiled(tiles)
        print(f"Part 1: {part1(tiled)}\nPart 2: {part2(tileOpts, tiled)}") # Thanks to https://github.com/AidanGlickman/Advent-2020/blob/master/day20/solution.py
        assert(0 == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        res = output_file("2")  # get output_1
        pred = get_sum_resulting_values_part_2(lines)  # process
        print(pred) # https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/ popodiloco
        assert(str(pred) == res[0])


if __name__ == '__main__':
    unittest.main()
