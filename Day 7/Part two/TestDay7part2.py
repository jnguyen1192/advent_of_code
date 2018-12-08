import unittest
import string
from parse import parse


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


class CorrectOrder:
    # class to execute the correct order list
    def __init__(self, raw_nodes, first_letters):
        self.raw_nodes = raw_nodes
        self.available_letters = sorted(first_letters)
        self.correct_order_string = ""

    def get_available_letters(self):
        # return available letters
        return self.available_letters

    def add_available_letter(self, available_letter):
        # add an available letter in our list of letter sorted
        self.available_letters = list(sorted(set(self.available_letters + [available_letter])))

    def add_correct_order(self, letter):
        # add an available letter in our list of letter sorted
        self.correct_order_string = self.correct_order_string + str(letter)

    def get_prerequite_letters(self, letter):
        # return all prerequite letters
        prerequite_letters = []
        for raw in self.raw_nodes:
            if raw[1] == letter:
                prerequite_letters.append(raw[0])
        return prerequite_letters

    def is_all_prerequite(self, prerequite_letters):
        # constraint with all prerequite
        available_letters = self.get_available_letters()
        for letter in prerequite_letters:
            if letter in available_letters:
                return False
            elif letter not in self.get_correct_order_string():
                return False
        return True

    def get_available_letter_without_preprequite_letters(self):
        # return avaible letter respecting the constraint of prerequite letters
        available_letters = self.get_available_letters()
        for available_letter in available_letters:
            prerequite_letters = self.get_prerequite_letters(available_letter)
            if self.is_all_prerequite(prerequite_letters):
                return available_letter
        return available_letters[0]

    def get_available_letter(self):
        # return the available letter order by alpha
        available_letter = self.get_available_letter_without_preprequite_letters()
        # remove the letter
        self.available_letters.remove(available_letter)
        # add this letter to the correct order list
        self.add_correct_order(available_letter)
        return available_letter

    def next_step(self):
        # get_child of next available
        available_letter = self.get_available_letter()
        # add all child on available list
        for raw in self.raw_nodes:
            if raw[0] == available_letter:
                self.add_available_letter(raw[1])

    def exec(self):
        # execute the brute force
        while len(self.available_letters) != 0:
            self.next_step()

    def get_correct_order_string(self):
        # return the correct order string
        return self.correct_order_string


def get_first_letters(letters, raw_nodes):
    # return the first letters of the workflow
    first_letters = []
    # find all first value of the worflow
    for letter in letters:
        find_value = False
        for raw in raw_nodes:
            if letter == raw[1]:
                find_value = True
                break
        if not find_value:
            first_letters.append(letter)
    return first_letters


def part_1(text):
    # data retrieve
    raw_nodes = [tuple(parse("Step {} must be finished before step {} can begin.", l)) for l in text.split('\n')] # @source https://github.com/ngilles/adventofcode-2018/blob/master/day-04/day-04.py
    # data transformation
    letters = set([raw[0] for raw in raw_nodes] + [raw[1] for raw in raw_nodes])
    first_letters = get_first_letters(letters, raw_nodes)
    # data model
    correct_order = CorrectOrder(raw_nodes, first_letters)
    # data analysis
    correct_order.exec()
    # data visualize
    return correct_order


class Worker:
    # a worker is define by his time to work
    def __init__(self, time_to_work = 0):
        self.time_to_work = time_to_work

    def is_available_worker(self):
        return self.time_to_work <= 0

    def step(self):
        if self.time_to_work > 0:
            self.time_to_work = self.time_to_work - 1


class Job:
    # a job is define by the time and the worker needs to do it
    def __init__(self, time_to_do, number_workers_need):
        self.time_to_do = time_to_do
        self.time_current_time = time_to_do
        self.number_current_workers = 0
        self.number_workers_need = number_workers_need

    def is_full_of_workers(self):
        # return true if there was no place for another worker
        return self.number_current_workers == self.number_workers_need

    def add_worker(self):
        # add a worker on the job
        self.number_current_workers += 1

    def is_job_done(self):
        # if the job is done return True
        return self.time_current_time <= 0

    def step(self):
        if self.time_current_time > 0:
            # each step are calculate by the number of workers affected on the job
            self.time_current_time -= self.number_current_workers


class WorkTime:

    def __init__(self, correct_order, time_step=60, number_worker=5):
        self.correct_order = correct_order
        self.time_step = time_step
        self.number_worker = number_worker

    def get_time_by_letter(self, letter):
        # return the time a worker need to end
        time_by_letter = string.ascii_uppercase
        time_letter = self.time_step + time_by_letter.find(letter) + 1
        return time_letter

    def get_job_by_letter(self):
        # TODO
        return ""

    def get_time_step(self):
        # return the number of seconds past
        return self.time_step

    def is_all_job_done(self):
        # TODO
        return True

    def exec(self):
        # get the result from part 1
        correct_order_string = self.correct_order.get_correct_order_string()
        # create the workers with nothing to do
        workers = []
        for i in range(self.number_worker):
            workers.append(Worker(0))
        # create the jobs to do by their needs
        jobs = []
        # TODO create jobs

        # TODO launch the step machine with an infinite loop

        # TODO verify how many worker can have a job

        # TODO search for available worker

        # TODO is_all_job_done_stop_step
        #self.get_prerequite_letters(letter)

def day_7_part_2(text):
    # data retrieve
    correct_order = part_1(text)
    # data transformation
    worktime = WorkTime(correct_order)
    # data modelisation
    worktime.exec()
    # data visualisation
    time_in_seconds = worktime.get_time_step()
    return str(time_in_seconds)


class TestDay7part2(unittest.TestCase):

    def test_day_7_part_2(self):
        text = input_file()
        #res = output_file()
        pred = day_7_part_2(text)
        print(pred)
        #assert(pred == res[0])


if __name__ == '__main__':
    unittest.main()
