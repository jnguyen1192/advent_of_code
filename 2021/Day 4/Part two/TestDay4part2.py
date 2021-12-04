import unittest
from collections import Counter


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


def get_final_score(lines):
    bingo_numbers = [int(col_board_line) for col_board_line in lines[0].split(",") if col_board_line != ""]
    boards_finder = []
    boards = []
    i = 2
    while True:
        if i >= len(lines):
            break
        board_lines_raw = lines[i:i+5]

        board_lines = [[int(col_board_line) for col_board_line in board_line.split(" ") if col_board_line != ""] for board_line in board_lines_raw]
        board_columns = [[] for col in board_lines[0]]
        for board_line in board_lines:
            for i_col, col in enumerate(board_line):
                board_columns[i_col].append(col)
        board_raw = []
        for board_line in board_lines:
            for board_col in board_line:
                board_raw.append(board_col)
        boards.append(board_raw)
        #print(board_raw)
        boards_finder.append([[board_try, 0] for board_try in board_lines + board_columns])
        i += 6

    def get_win_board(bingo_numbers, boards_finder):
        win_board = 0
        for i_bingo_number, bingo_number in enumerate(bingo_numbers):
            for i_board, board in enumerate(boards_finder):
                for i_, _ in enumerate(board):
                    #print(_)
                    if bingo_number in _[0]:
                        boards_finder[i_board][i_][1] += 1
                        #print(boards_finder[i_board][i_])
                        if boards_finder[i_board][i_][1] == 5:
                            return i_board, i_bingo_number
                        #return sum(boards[i_board][i_][0]) * boards[i_board][i_][0][-1]

    for j in range(len(boards)):
        win_board, index_last_bingo_number = get_win_board(bingo_numbers, boards_finder)
        boards_finder.remove(boards_finder[win_board])
        boards.remove(boards[win_board])
        #print(boards_finder)
        # refresh counters
        #boards_finder = [[[_, 0] for _ in board_finder] for board_finder in boards_finder]
        boards_finder = [[[_[0], 0] for _ in board_finder] for board_finder in boards_finder]
        #print("hola", boards_finder)
        if len(boards_finder) == 1:
            #print(boards_finder)

            #print(boards_finder)
            win_board, index_last_bingo_number = get_win_board(bingo_numbers, boards_finder)
            #print(boards_finder)
            #print(bingo_numbers)
            for bingo_number in bingo_numbers[:index_last_bingo_number+1]:
                if bingo_number in boards[0]:
                   boards[0].remove(bingo_number)
            return sum(boards[0]) * bingo_numbers[index_last_bingo_number]

    #for bingo_number in bingo_numbers[:index_last_bingo_number+1]:
    #    if bingo_number in boards[win_board]:
    #        boards[win_board].remove(bingo_number)
    #print(boards_finder[0])
    #print(sum(boards[win_board]), bingo_numbers[index_last_bingo_number])
    return 0


class TestDay4part2(unittest.TestCase):

    def test_day_4_part_2(self):
        lines = input_file()  # get input_test
        res = output_file()  # get output_1
        pred = get_final_score(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check


if __name__ == '__main__':
    unittest.main()
