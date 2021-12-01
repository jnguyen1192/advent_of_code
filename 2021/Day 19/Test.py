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

def get_nb_valid_line(lines):
    import re  # https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ 4HbQ
    rs, ms = open('input_day').read().split('\n\n')
    rs += '\n8: 42 | 42 8\n11: 42 31 | 42 11 31'  # part 2
    rs = dict([line.split(': ') for line in rs.split('\n')])

    def f(r='0', n=0):
        if n > 20: return ''
        if rs[r][0] == '"': return rs[r][1]
        return '(' + '|'.join([''.join([f(t, n + 1)
                                        for t in s.split()]) for s in rs[r].split('|')]) + ')'

    r = re.compile(f())
    print(len([*filter(r.fullmatch, ms.split())]))

    return len([*filter(r.fullmatch, ms.split())])  # get nb cubes


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        res = output_file("1")  # get output_1
        pred = get_nb_valid_line(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

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
