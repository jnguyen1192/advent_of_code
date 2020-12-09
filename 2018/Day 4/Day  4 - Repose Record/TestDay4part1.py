import unittest
from datetime import datetime
from parse import parse


def input_file():
    # return the input_test file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # return the output_1 file in a string
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res


class Guard:
    # The guard with his timers
    def __init__(self, id, current_date):
        self.id = id
        self.current_date = current_date
        self.time = 0
        # init each minute by zero between midnight and one hour
        self.day = [0] * 60

    def set_current_date(self, date):
        # set the date for sleeping
        self.current_date = date

    def awake_process(self, date):
        # add to the timer for sleeping
        self.time += int(abs(self.current_date - date).total_seconds() / 60.0)
        self.increment_minutes(self.current_date.minute, date.minute)
        self.set_current_date(date)

    def get_best_minute(self):
        # get the minute which the guard will probably sleep
        max_value = 0
        max_index = 0
        for index, value in enumerate(self.day):
            if value > max_value:
                max_value = value
                max_index = index
        return max_index

    def increment_minutes(self, start_minute, end_minute):
        # increment minutes on our list
        for i in range(start_minute, end_minute):
            self.day[i] += 1

    def get_super_id(self):
        return self.id * self.get_best_minute()


def check_guard_exist(curr_guard_id, guards):
    # return true if the guard was found on the list of guards
    for g in guards:
        if g.id == curr_guard_id:
            return True
    return False


def get_current_guard(curr_guard_id, guards):
    # return the guard in the list using id
    for i in range(len(guards)):
        if curr_guard_id == guards[i].id:
            return i


def get_best_sleeping_guard(guards):
    # return best sleeping guard
    best_time = 0
    best_guard = 0
    for g in guards:
        if g.time > best_time:
            best_time = g.time
            best_guard = g
    return best_guard


def create_guards(raw_events):
    # init
    guards = []
    falls = 0
    id_shift_most_recently = []
    for raw in raw_events:
        date = datetime.strptime(str(raw[0])+"/"+str(raw[1])+"/"+str(raw[2])+"-"+str(raw[3]) + ":" + str(raw[4]), '%Y/%m/%d-%H:%M')
        # case id_guard
        if str(raw[5])[:5] == "Guard":
            curr_garde_id = parse('Guard #{:d} begins shift', raw[5])[0]
            # verifie si  le guard n existe pas
            if check_guard_exist(curr_garde_id, guards):
                # case garde existe
                # stack la pile
                id_shift_most_recently.insert(0, curr_garde_id)
            else:
                # ajoute un nouveau garde dans la liste de gardes
                guards.append(Guard(curr_garde_id, date))
                # stack la pile
                id_shift_most_recently.insert(0, curr_garde_id)

        if str(raw[5])[:5] == "falls":
            # case falls
            guards[get_current_guard(id_shift_most_recently[falls], guards)].set_current_date(date)
            # destack la pile
            falls -= 1
        if str(raw[5])[:5] == "wakes":
            # case wakes
            # stack la pile
            falls += 1
            guards[get_current_guard(id_shift_most_recently[falls], guards)].awake_process(date)
    return guards


def day_4_part_1(text):
    # sort list
    raw_events = sorted(tuple(parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", l)) for l in text.split('\n'))  # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py
    # a chaque fois que t'as un nouveau garde tu l'ajoute a la liste avec sa duree
    guards = create_guards(raw_events)
    # check best current garde
    best_guard_sleeping = get_best_sleeping_guard(guards)
    # multiply to obtain the result
    best_guard_id_by_minute = best_guard_sleeping.get_super_id()
    return str(best_guard_id_by_minute)


class TestDay4part1(unittest.TestCase):
    def test_day_4_part_1(self):
        text = input_file()
        res = output_file()
        pred = day_4_part_1(text)
        assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
