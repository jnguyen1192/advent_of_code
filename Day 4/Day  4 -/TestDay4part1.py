import unittest
from datetime import datetime


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


class Garde:
    def __init__(self, id, current_date):
        self.id = id
        self.current_date = current_date
        self.time = 0

    def addDateFalls(self, date):
        self.time += int(abs(self.current_date - date).total_seconds() / 60.0)
        print(self.id, " ", self.time)
        self.current_date = date

    def addDateWakes(self, date):
        self.current_date = date


def check_guard_exist(curr_guard_id, gardes):
    for g in gardes:
        if g.id == curr_guard_id:
            return True
    return False


def get_current_garde(curr_garde_id, gardes):
    for i in range(len(gardes)):
        if curr_garde_id == gardes[i].id:
            return i


def day_4_part_1(lines):
    gardes = []
    falls = 0
    id_shift_most_recently = []
    # a chaque fois que t'as un nouveau garde tu l'ajoute a la liste avec sa duree
    for line in lines:
        date = datetime.strptime(line.split(']')[0][1:], '%Y-%m-%d %H:%M')
        # case id_guard
        if line.split(' ')[2][:5] == "Guard":
            curr_garde_id = int(line.split(' ')[3][1:])
            # verifie si  le guard n existe pas
            if check_guard_exist(curr_garde_id, gardes):
                # case garde existe
                # recupere l objet concerne
                num_garde_list = get_current_garde(curr_garde_id, gardes)
                # change sa date courante avec add wake
                gardes[num_garde_list].addDateWakes(date)
                id_shift_most_recently.insert(0, curr_garde_id)
            else:
                # ajoute un nouveau garde dans la liste de gardes
                gardes.append(Garde(curr_garde_id, date))
                id_shift_most_recently.insert(0, curr_garde_id)
        #print(line.split(' ')[2][:5])
        if line.split(' ')[2][:5] == "falls":
            # case falls
            gardes[get_current_garde(id_shift_most_recently[falls], gardes)].addDateFalls(date)
            falls += 1
        if line.split(' ')[2][:5] == "wakes":
            # case wakes
            falls -= 1
            print(falls)
            print(id_shift_most_recently)
            gardes[get_current_garde(id_shift_most_recently[falls], gardes)].addDateWakes(date)
    # check best current garde
    best_id = 0
    best_time = 0
    for g in gardes:
        if g.time > best_time:
            best_id = g.id
            best_time = g.time
    # sum for each id the time guard not asleep
    return best_id * best_time


class TestDay4part1(unittest.TestCase):

    def test_day_4_part_1(self):
        lines = input_file()
        #res = output_file()
        pred = day_4_part_1(lines)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
