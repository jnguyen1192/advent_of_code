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


def get_ticket_snning_eror_rate(lines):
    class TicketScanning:
        """
        class: 1-3 or 5-7
        row: 6-11 or 33-44
        seat: 13-40 or 45-50

        your ticket:
        7,1,14

        nearby tickets:
        7,3,47
        40,4,50
        55,2,20
        38,6,12
        """
        def __init__(self, lines):
            # init game
            self.rules, self.your_ticket, self.nearby_ticket = self.scane_ticket(lines)
            self.wrong_numbers, self.max = self.get_wrong_numbers()
            #self.class_, self.row_, self.seat_, self.your_ticket, self.nearby_tickets = self.scane_ticket(lines)

        def get_max(self):
            max_ = 0
            for couple in self.rules:
                #print(couple)
                if couple[2] > max_:
                    max_ = couple[2]
                if couple[4] > max_:
                    max_ = couple[4]
            return max_

        def get_wrong_numbers(self):
            min = 0
            max = self.get_max()
            #print("MAX", max)
            numbers = {i: 1 for i in range(min, max+1)}  # init with 1
            for _, min_1, max_1, min_2, max_2 in self.rules:
                for i in range(min_1, max_1 + 1):
                    numbers[i] += 1
                for i in range(min_2, max_2 + 1):
                    numbers[i] += 1
            #print("wn", [number for number in numbers if numbers[number] == 1])
            return [number for number in numbers if numbers[number] == 1], max

        def scane_ticket(self, lines):
            def get_numbers_from_string(line):
                import re
                return list(map(int, re.findall(r'\d+', line)))

            final_array = [[], [], []]
            i = 0
            first = False
            for line in lines:
                if line == "":
                    i += 1
                    continue
                # rules
                if i == 0:
                    tmp = get_numbers_from_string(line)
                    #print(line.split(":")[0])
                    final_array[i].append((line.split(":")[0], tmp[0], tmp[1], tmp[2], tmp[3]))
                if i == 1:
                    if line != "your ticket:":
                        final_array[i] = [int(number) for number in line.split(",")]
                if i == 2:
                    if not first:
                        first = True
                        continue
                    final_array[i].append([int(number) for number in line.split(",")])
                # your ticket
                #    continue
                # nearby ticket
            final_array[0].sort()
            #print(final_array)
            return final_array

        def get_ticket_scanning_error_rate(self):
            wrong_numbers = []
            list_to_delete = []
            for i, nt in enumerate(self.nearby_ticket):
                for number in nt:
                    if number > self.max:
                        wrong_numbers.append(number)
                        list_to_delete.append(i)
                        # remove current nearby ticket
                        break
                    elif number in self.wrong_numbers:
                        wrong_numbers.append(number)
                        list_to_delete.append(i)
                        break
            for i in list_to_delete[::-1]:
                self.nearby_ticket.pop(i)
            #print("wrong_numbers", len(wrong_numbers), wrong_numbers)
            return sum(wrong_numbers)

        def get_order_fields(self):
            #print("range(len(self.your_ticket))", range(len(self.your_ticket)))
            order_fields = []
            for j in range(len(self.your_ticket)):  # for each field
                for i, rule in enumerate(self.rules):  # for each rules
                    field, min_1, max_1, min_2, max_2 = rule
                    is_rule = True
                    for nt in self.nearby_ticket:  # for each nearby ticket
                        #print("number", number)
                        if not(min_1 <= nt[j] <= max_1 or min_2 <= nt[j] <= max_2) or field in order_fields:  # test min max
                            is_rule = False  # go to next rule
                            #print('false go to next rule')
                            break
                    if is_rule:
                        order_fields.append(field)  # case it is the rule
                        break
                    #print(rule)
            #print(order_fields)
            return order_fields

        def get_fields_start_with(self, start_with="departure"):
            fields = []
            for rule in self.rules:
                if start_with in rule[0]:
                    fields.append(rule[0])
            return fields

    ts = TicketScanning(lines)
    ts.get_ticket_scanning_error_rate()
    print("get_order_fields", len(ts.get_order_fields()), ts.get_order_fields())
    ticket_fields_positions = []
    for i, field in enumerate(ts.get_order_fields()):
        for field_to_match in ts.get_fields_start_with():
            if field == field_to_match:
                ticket_fields_positions.append(i)
                break
    #print(ticket_fields_positions)
    #print([ts.your_ticket[i] for i in ticket_fields_positions])
    def multiply(list):
        prod = 1
        for elmt in list:
            prod *= elmt
        return prod
    print("ticket_fields_positions", ticket_fields_positions)
    print([ts.your_ticket[i] for i in ticket_fields_positions])
    print(len([ts.your_ticket[i] for i in ticket_fields_positions]))
    print(len(ts.your_ticket))
    #ts.get_fields_start_with()
    return multiply([ts.your_ticket[i] for i in ticket_fields_positions])


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        #lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        #res = output_file("test_1")  # get output_1
        pred = get_ticket_snning_eror_rate(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_1")  # get output_1
        pred = get_ticket_snning_eror_rate(lines)  # process
        import functools

        sections = open('input_day').read().split('\n\n')

        def make_range(expr):
            (l, h) = [int(n) for n in expr.split('-')]
            return range(l, h + 1)

        property_map = {}
        rules = []
        for r in [[i.strip() for i in r.split(':')] for r in sections[0].split('\n')]:
            ranges = r[1].replace('or', '').replace('  ', ' ').split(' ')
            rules.append([r[0], make_range(ranges[0]), make_range(ranges[1])])

        tickets = [[int(n) for n in s.split(',')] for s in sections[2].split('\n')[1:]]
        valid_tickets = list(
            filter(lambda t: all([any([num in r[1] or num in r[2] for r in rules]) for num in t]), tickets))

        my_card = [int(num) for num in sections[1].split('\n')[1].split(',')]

        i = 0
        s = 1
        matching = {}
        while (len(property_map.keys()) < len(rules)):
            pi = [t[i] for t in valid_tickets]
            if matching.get(i) is None:
                matching[i] = list(filter(lambda rule: all([(p in rule[1] or p in rule[2]) for p in pi]), rules))
            matching[i] = list(filter(lambda m: m[0] not in property_map.keys(), matching[i]))
            if len(matching[i]) == 1:
                name = matching[i][0][0]
                property_map[name] = i
                if name.startswith('departure'):
                    print("dep", my_card[i])
                    s *= my_card[i]
            i = (i + 1) % len(valid_tickets[0])
        print(s)
        print(pred)
        assert(str(pred) == res[0])  # check https://github.com/busdriverbuddha/aoc2020_solutions/blob/main/day13.py

if __name__ == '__main__':
    unittest.main()
