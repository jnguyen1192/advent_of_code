import unittest
from datetime import datetime
from parse import parse


def input_file():
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


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
        self.max_sleep = 0
        self.day = [0] * 60

    def addDateFalls(self, date):
        self.current_date = date

    def addDateWakes(self, date):
        self.time += int(abs(self.current_date - date).total_seconds() / 60.0)
        if int(abs(self.current_date - date).total_seconds() / 60.0) > self.max_sleep:
            self.max_sleep = int(abs(self.current_date - date).total_seconds() / 60.0)
        for i in range(self.current_date.minute, date.minute):
            self.day[i] += 1
        self.current_date = date

    def get_best_minute(self):
        max_value = 0
        max_index = 0
        for index, value in enumerate(self.day):
            if value > max_value:
                max_value = value
                max_index = index
        return max_index

    def get_best_value(self):
        max_value = 0
        for index, value in enumerate(self.day):
            if value > max_value:
                max_value = value
        return max_value


def check_guard_exist(curr_guard_id, gardes):
    for g in gardes:
        if g.id == curr_guard_id:
            return True
    return False


def get_current_garde(curr_garde_id, gardes):
    for i in range(len(gardes)):
        if curr_garde_id == gardes[i].id:
            return i


def day_4_part_2(text):
    gardes = []
    falls = 0
    id_shift_most_recently = []
    # sort list
    raw_events = sorted(tuple(parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", l)) for l in text.split('\n')) # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py
    # a chaque fois que t'as un nouveau garde tu l'ajoute a la liste avec sa duree
    for raw in raw_events:
        date = datetime.strptime(str(raw[0])+"/"+str(raw[1])+"/"+str(raw[2])+"-"+str(raw[3]) + ":" + str(raw[4]), '%Y/%m/%d-%H:%M')
        # case id_guard
        if str(raw[5])[:5] == "Guard":
            curr_garde_id = parse('Guard #{:d} begins shift', raw[5])[0]
            # verifie si  le guard n existe pas
            if check_guard_exist(curr_garde_id, gardes):
                # case garde existe
                # stack la pile
                id_shift_most_recently.insert(0, curr_garde_id)
            else:
                # ajoute un nouveau garde dans la liste de gardes
                gardes.append(Garde(curr_garde_id, date))
                id_shift_most_recently.insert(0, curr_garde_id)

        if str(raw[5])[:5] == "falls":
            # case falls
            gardes[get_current_garde(id_shift_most_recently[falls], gardes)].addDateFalls(date)
            falls -= 1
        if str(raw[5])[:5] == "wakes":
            # case wakes
            falls += 1
            gardes[get_current_garde(id_shift_most_recently[falls], gardes)].addDateWakes(date)

    # check best constant garde
    best_id = 0
    best_minute = 0
    best_value = 0
    for g in gardes:
        if g.get_best_value() > best_value:
            best_id = g.id
            best_value = g.get_best_value()
            best_minute = g.get_best_minute()
    return best_id * best_minute


class TestDay4part2(unittest.TestCase):

    def test_day_4_part_2(self):
        lines = input_file()
        #res = output_file()
        pred = day_4_part_2(lines)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
