import unittest
import numpy as np


class digit_code:
    def __init__(self):
        self.digit_code_mat = self.init_matrice()
        self.list_combination = []

    def init_matrice(self):
        digit_code_matrice = np.empty((8, 7))
        digit_code_matrice[:] = np.nan
        # affect 1 2 3 to digit code matrice
        digit_code_matrice[2, 2:5] = range(1, 4)
        # affect 4 5 6 to digit code matrice
        digit_code_matrice[3, 2:5] = range(4, 7)
        # affect 7 8 9 to digit code matrice
        digit_code_matrice[4, 2:5] = range(7, 10)
        # affect   0   to digit code matrice
        digit_code_matrice[5][3] = 0
        return digit_code_matrice.astype(int)

    def available_move(self, digit_number):
        # init avaible list move
        available_move = []
        # get item index
        index_mat = np.where(self.digit_code_mat == digit_number)
        ind_line = index_mat[0][0]
        ind_column = index_mat[1][0]
        # init available coord
        available_xy = [-2, -1, 1, 2]
        # browse available coord
        for line in available_xy:
            for column in available_xy:
                # only available move like a horseman in digit code matrice
                if abs(line) != abs(column) and self.digit_code_mat[ind_line + line][ind_column + column] >= 0:
                    available_move.append(self.digit_code_mat[ind_line + line][ind_column + column])
        return available_move

    def exit_loop(self, length, combination):
        # condition to exit the infinite loop
        if length != 1:
            c = 0
            for sequence in combination:
                if sequence[-1] == -1:
                    c += 1
            if c == length:
                return True
        return False

    def clone_list_into_multiple_list(self, length, real_am, sequence, combination, count):
        # init a clone list
        clone_list = []
        # first case with digit_number except
        if length != 1:
            # multi list contains all cloned list
            for d in real_am:
                clone_list.append(sequence + [d])
        else:
            for d in real_am:
                clone_list.append([sequence] + [d])
        # remove the element which we clone before
        combination.pop(count)
        # insert multi list into list combination on the good index
        for m in clone_list :
            combination.insert(count, m)

    def next_move(self, length, sequence, count, combination):
        # first case with digit_number except
        if length != 1:
            # get available move on last digit number of a combination
            am = self.available_move(sequence[-1])
            # substract am by the current sequence to obtains the real available move
            real_am = (list(set(am) - set(sequence)))
        else:
            real_am = self.available_move(sequence)
        # test it is the end of the combination
        if len(real_am) == 0:
            sequence.append(-1)
        # test if there was only one real available value
        elif len(real_am) == 1:
            sequence.append(real_am[0])
        # else clone the list each time there was a new available move
        else:
            self.clone_list_into_multiple_list(length, real_am, sequence, combination, count)

    def clean_final_combination(self, combination):
        for count, sequence in enumerate(combination):
            combination[count] = sequence[:-1]

    def get_combination_by_digit_number(self, digit_number):
        # except if the digit number specified cannot do a horseman move
        if len(self.available_move(digit_number)) == 0:
            return []
        # init the first combination
        combination = [digit_number]
        # infinite loop
        while True:
            # test if each sequence are finished to -1
            length = len(combination)
            # condition to exit the infinite loop
            if self.exit_loop(length, combination):
                break
            # for each sequence on list combination
            for count, sequence in enumerate(combination):
                # case the list is end, we didn't do the process
                if length != 1:
                    if sequence[-1] == -1:
                        continue
                # we increment by a horseman move on each list
                self.next_move(length, sequence, count, combination)
                # cause we add multi list we need to manipulate the loop by hand
                # and
                # first case with digit_number except
                if count == length or length == 1:
                    break
        # clean final combination
        self.clean_final_combination(combination)
        return combination


class TestNicolasChallenge(unittest.TestCase):

    def setUp(self):
        self.dcm = digit_code()

    def test_create_numpy_matrice_digit_code_challenge(self):
        digit_code_mat = self.dcm.digit_code_mat
        mat = np.asarray([[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
                          [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
                          [np.nan, np.nan, 1., 2., 3., np.nan, np.nan],
                          [np.nan, np.nan, 4., 5., 6., np.nan, np.nan],
                          [np.nan, np.nan, 7., 8., 9., np.nan, np.nan],
                          [np.nan, np.nan, np.nan, 0., np.nan, np.nan, np.nan],
                          [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
                          [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]])
        assert(np.array_equal(digit_code_mat, mat.astype(int)))

    def test_get_combinaison_using_digit_0(self):
        test = [4, 6]
        digit_number = 0
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_1(self):
        test = [6, 8]
        digit_number = 1
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_2(self):
        test = [7, 9]
        digit_number = 2
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_3(self):
        test = [4, 8]
        digit_number = 3
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_4(self):
        test = [0, 3, 9]
        digit_number = 4
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_5(self):
        test = []
        digit_number = 5
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_6(self):
        test = [0, 1, 7]
        digit_number = 6
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_7(self):
        test = [2, 6]
        digit_number = 7
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_8(self):
        test = [1, 3]
        digit_number = 8
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_get_combinaison_using_digit_9(self):
        test = [2, 4]
        digit_number = 9
        dcm = self.dcm.available_move(digit_number)
        dcm.sort()
        assert(dcm == test)

    def test_clone_list(self):
        src = [1]
        dest = [6, 8]
        res = []
        for d in dest:
            res.append(src + [d])
        print(res)

    def test_get_the_second_combinaison(self):
        digit_number = 1
        multi_list = []
        # nous commencons par le chiffre 1
        # ajouter le digit
        self.dcm.list_combination.append(digit_number)
        print(self.dcm.list_combination)
        print(self.dcm.available_move(digit_number))
        # creer autant de liste qu il y a de move available
        for d in self.dcm.available_move(digit_number):
            multi_list.append(self.dcm.list_combination + [d])
        print(multi_list)
        # nous parcourons pour savoir quels sont les positions disponibles

    def test_each_number_in_list_combination(self):
        digit_number = 1
        self.dcm.list_combination.append(digit_number)
        # infinite loop
        while True:
            # test if each sequence are finished to -1
            length = len(self.dcm.list_combination)
            # first case with digit_number except
            if length != 1:
                c = 0
                for sequence in self.dcm.list_combination:
                    #print(sequence)
                    if sequence[-1] == -1:
                        c += 1
                if c == length:
                    break
            # for each sequence on list combination
            for count, sequence in enumerate(self.dcm.list_combination):
                # case the list is end, we didn't do the process
                if length != 1:
                    if sequence[-1] == -1:
                        continue
                # first case with digit_number except
                if length != 1:
                    am = self.dcm.available_move(sequence[-1])
                    # substract am by the current sequence to obtains the real available move
                    am = (list(set(am) - set(sequence)))
                else:
                    am = self.dcm.available_move(sequence)
                # test it is the end of the combination
                if len(am) == 0:
                    sequence.append(-1)
                # test if there was only one value
                elif len(am) == 1:
                    sequence.append(am[0])
                # else clone the list each time there was a new available move
                else:
                    multi_list = []
                    # first case with digit_number except
                    if length != 1:
                        # multi list contains all cloned list
                        for d in am:
                            multi_list.append(sequence + [d])
                    else:
                        for d in am:
                            multi_list.append([sequence] + [d])
                    # remove the element which we clone before
                    self.dcm.list_combination.pop(count)
                    # insert multi list into list combination on the good index
                    for m in multi_list:
                        self.dcm.list_combination.insert(count, m)
                # cause we add multi list we need to manipulate the loop by hand
                # first case with digit_number except
                if count == length or length == 1:
                    break
        print(self.dcm.list_combination)

    def test_substract_list_value(self):
        l1 = [4, 6]
        l2 = [1, 6, 0]
        print(list(set(l1) - set(l2)))

    def test_availble_move_on_five(self):
        print(self.dcm.available_move(5))

    def test_total_number_combination(self):
        nb_combinaison = 0
        for i in range(10):
            nb_combinaison += len(self.dcm.get_combination_by_digit_number(i))
            #print(i, " ", len(self.dcm.get_combination_by_digit_number(i)))
        print(nb_combinaison)
        #print(len(self.dcm.get_combination_by_digit_number(1)))

    def test_print_all_combination(self):
        for i in range(10):
            for sequence in self.dcm.get_combination_by_digit_number(i):
                print(sequence)


if __name__ == '__main__':
    unittest.main()
