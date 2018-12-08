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
    # a worker is define by his time to work and his job letter
    def __init__(self, id, time_to_work=0):
        self.id = id
        self.time_to_work = time_to_work
        self.letter = "."

    def get_id(self):
        # return the id of a worker
        return self.id

    def add_job(self, job):
        # add a time to work
        self.time_to_work = job.get_time_to_do()
        self.letter = job.get_letter_job()

    def is_available_worker(self):
        # return True if the worker has nothing to do
        return self.time_to_work <= 0

    def step(self):
        # each step it works one second
        if self.time_to_work > 0:
            self.time_to_work = self.time_to_work - 1
        else:
            self.letter = '.'


class Job:
    # a job is define by the time and the job needs to do it
    def __init__(self, letter, time_to_do, prerequite_jobs):
        self.letter = letter
        self.time_to_do = time_to_do
        self.prerequite_jobs_letters = prerequite_jobs

        self.time_current_time = time_to_do
        self.number_current_workers = 0

    def get_letter_job(self):
        # return the letter of the job
        return self.letter

    def get_time_to_do(self):
        # return the time to do the job
        return self.time_to_do

    def add_worker(self):
        # add a worker on the job
        self.number_current_workers += 1

    def is_job_done(self):
        # if the job is done return True and free the worker
        return self.time_current_time == 0

    def is_job_available(self, jobs_done):
        # if the prerequite jobs are done and there was no worker on the job return True
        # case there was a worker on the job or job is end
        if self.number_current_workers != 0 or self.time_current_time == 0:
            return False
        # case prerequite done
        if set(self.prerequite_jobs_letters).issubset([job.get_letter_job() for job in jobs_done])and self.time_current_time != 0:
            return True
        return False

    def step(self):
        # only step if there was something to do and a worker is here
        if self.time_current_time > 0 and self.number_current_workers != 0:
            # each step are calculate by the number of workers affected on the job
            self.time_current_time -= self.number_current_workers
        # remove the worker if the job is ended
        if self.time_current_time == 0:
            self.number_current_workers = 0


class Workflow:
    # class to create the environment containing workers, jobs and timeline
    def __init__(self, correct_order, time_step=60, number_worker=5, timer=0):
        self.correct_order = correct_order
        self.time_step = time_step
        self.timer = timer
        self.number_worker = number_worker

        self.workers = []
        self.jobs = []
        self.jobs_done = []

    def get_time_by_letter(self, letter):
        # return the time a worker need to end
        time_by_letter = string.ascii_uppercase
        time_letter = self.time_step + time_by_letter.find(letter) + 1
        return time_letter

    def get_timer(self):
        # return the number of seconds past
        return self.timer

    def is_all_job_done(self):
        # return True if all jobs are done
        for job in self.jobs:
            if not job.is_job_done():
                return False
        return True

    def get_job_by_letter(self, letter):
        # return the job using the letter
        correct_order_string = self.correct_order.get_correct_order_string()
        for i in range(len(correct_order_string)):
            if letter == correct_order_string[i]:
                return self.jobs[i]

    def get_worker_by_id(self, id):
        # return the job using the letter
        for id_current in range(len(self.workers)):
            if id == id_current:
                return self.workers[id_current]

    def get_jobs_letters_done(self):
        # return the jobs done
        jobs_letters_done = []
        for job in self.jobs_done:
            jobs_letters_done.append(job.get_letter_job())
        return jobs_letters_done

    def get_ids_available_workers(self):
        # return the ids of available workers
        ids_available_workers = []
        for worker in self.workers:
            if worker.is_available_worker():
                ids_available_workers.append(worker.get_id())
        return ids_available_workers

    def get_letters_available_jobs(self):
        # return the ids of available workers
        letters_available_jobs = []
        for job in self.jobs:
            # add a job if the prerequite are done
            if job.is_job_available(self.jobs_done):
                letters_available_jobs.append(job.get_letter_job())
        return letters_available_jobs

    def update_jobs_done(self):
        # return the jobs done
        self.jobs_done = []
        for job in self.jobs:
            if job.is_job_done():
                self.jobs_done.append(job)

    def get_jobs_done(self):
        # return the list of jobs done
        return self.jobs_done

    def init_workers(self):
        # create the workers with nothing to do
        for i in range(self.number_worker):
            # add a worker
            self.add_worker(Worker(i, 0))

    def init_jobs(self, correct_order_string):
        # create the jobs to do by their needs
        for letter in correct_order_string:
            # get time to do by job letter
            time_to_do = self.get_time_by_letter(letter)
            # get prerequite jobs a job need by letter
            prerequite_letters = self.correct_order.get_prerequite_letters(letter)
            # add a job
            self.add_job(Job(letter, time_to_do, prerequite_letters))

    def add_worker(self, worker):
        # add a worker on the list of workers
        self.workers.append(worker)

    def add_job(self, job):
        # add a job on the list of jobs
        self.jobs.append(job)

    def assign_worker_on_job(self, id, job):
        # assign a worker using id on a specific job
        worker = self.get_worker_by_id(id)
        worker.add_job(job)
        job.add_worker()

    def step_time(self):
        # step all the worker
        for worker in self.workers:
            worker.step()
        # step all the jobs
        for job in self.jobs:
            job.step()
        # update the list of job done
        self.update_jobs_done()
        self.timer += 1

    def print_exec(self):
        # print the workflow
        worker_str = ""
        for work in self.workers:
            worker_str += str(work.letter) + "\t"
        print(self.timer, "\t", worker_str, "".join([job.get_letter_job() for job in self.jobs_done]))

    def exec(self, debug=False):
        # get the result from part 1
        correct_order_string = self.correct_order.get_correct_order_string()
        # create the workers
        self.init_workers()
        # create the jobs
        self.init_jobs(correct_order_string)
        # launch the step machine with an infinite loop
        # is_all_job_done_stop_step
        while not self.is_all_job_done():
            # get jobs done
            jobs_done = self.get_jobs_done()
            if debug:
                self.print_exec()
            # case first iteration for get available jobs
            if self.timer == 0:
                raw_nodes = self.correct_order.raw_nodes
                letters = set([raw[0] for raw in raw_nodes] + [raw[1] for raw in raw_nodes])
                letters_available_jobs = get_first_letters(letters, self.correct_order.raw_nodes)
            else:
                letters_available_jobs = self.get_letters_available_jobs()
            # assign worker on each available job or wait if not worker are available
            for letter in letters_available_jobs:
                job_available = self.get_job_by_letter(letter)
                # case the job is available
                if job_available.is_job_available(jobs_done):
                    # add an worker on it
                    # search for available worker
                    ids_available_workers = self.get_ids_available_workers()
                    # verify if a worker can have a job
                    # case worker available
                    if len(ids_available_workers) != 0:
                        # assign the worker on this job
                        self.assign_worker_on_job(ids_available_workers[0], job_available)
                else:
                    continue
                    # wait if nothing to  do
            self.step_time()


def day_7_part_2(text):
    # data retrieve
    correct_order = part_1(text)
    # data transformation
    worktime = Workflow(correct_order)
    # data modelisation
    worktime.exec(True)
    # data visualisation
    time_in_seconds = worktime.get_timer()
    return str(time_in_seconds)


class TestDay7part2(unittest.TestCase):

    def test_day_7_part_2(self):
        text = input_file()
        #res = output_file()
        pred = day_7_part_2(text)
        print(pred)
        #assert(pred == res[0])

    def test_code(self):
        a = ['D']
        b = ['A', 'D']
        if set(a).issubset(b):
            print("Condition ok")


if __name__ == '__main__':
    unittest.main()
