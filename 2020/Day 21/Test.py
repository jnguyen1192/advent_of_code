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

def get_nb_any_allegens(lines):
    """
    mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
    trh fvjkl sbzzf mxmxvkd (contains dairy)
    sqjhc fvjkl (contains soy)
    sqjhc mxmxvkd sbzzf (contains fish)
    """
    allergens_dict_1 = {}
    for line in lines:
        ingredients_raw, allergens_raw = line.split(" (contains ")
        ingredients = ingredients_raw.split()
        allergens = allergens_raw[:-1].split(", ")
        for allergen in allergens:
            if allergen in allergens_dict_1:
                allergens_dict_1[allergen] = allergens_dict_1[allergen].intersection(set(ingredients))
            else:
                allergens_dict_1[allergen] = set(ingredients)
            #print(allergen, allergens_dict_1[allergen])
    allergens_set = set()
    for key in allergens_dict_1:
        for elmt in allergens_dict_1[key]:
            allergens_set.add(elmt)
    count = 0
    for line in lines:
        ingredients_raw, allergens_raw = line.split(" (contains ")
        ingredients = ingredients_raw.split()
        for ingredient in ingredients:
            if ingredient not in allergens_set:
                count += 1 # part 1
    #allergens_dict_2 = {}
    #for allergen_key in allergens_dict_1:
    #    allergens_dict_2[allergen_key] = allergens_dict_1[allergen_key]
    #print(allergens_dict_1)
    #print(allergens_set)
    # get allergen list
    found_list = []
    while len(found_list) < len(allergens_dict_1):
        for allergen in allergens_dict_1:
            if len(allergens_dict_1[allergen]) == 1:
                if allergens_dict_1[allergen] not in found_list:
                    found_list.append(allergens_dict_1[allergen])
                #print(allergens_dict_1[allergen])
                for others in allergens_dict_1:
                    if others != allergen:
                        allergens_dict_1[others] = allergens_dict_1[others] - allergens_dict_1[allergen]

    canonical = ''
    print(allergens_dict_1.items())
    for x in sorted(allergens_dict_1.items()):
        canonical = canonical + x[1].pop() + ','

    print(canonical[:-1])
        #print(key, allergens_dict_1[key])
    print("allergens_dict_1", allergens_dict_1)
    # from RedTwinkleToes (https://www.reddit.com/r/adventofcode/comments/khaiyk/2020_day_21_solutions/) https://topaz.github.io/paste/#XQAAAQD6BQAAAAAAAAA5CAOiE5B6KET+KAuGk3kMvKJWOOCbZym/soQHahm7r/YkUrIsS9wIo5Wd9VqWk+ZDzRDtp7TIZO4NbW6V9dez6sxhNWQuGsSfjfvNxdhVkNvCkOEyFnI239OwvKC0AWje+QFsSdGpQ1FUXXAq8cts2WEBVFHj11b86JepoqbM2Cw5KdVDAqfm55wmIZ4jKgtYTG/NhX5Dpy7JjNxX4k3IZIo/mkhNzHSmIPlbyzA120+Z4ndUavExz1hZVugcZquUFAsy0DFnarPY+1grHf9oqpWoJzp3CXqVneXzIgQpO8xypDLZWhKwZQPQKlFDW8NUjDTQoztT/gGfYq9NkjAMMP4LrxaNGJsb5yWJohWDSGu2pWNn9O9cYJV7nhTKmW/37l19qmq2CcrIqODMOfWTrAATmWJjZ9wnO1yr3vk3Pd1kM4STrQpqWVG/buib4Fo3vHqNN7sRNIOZtXLcNtuEhbPE94lwdYKtPJsO4wnt5LXpSXeMoawWmKp/gkhKhXL4/C5eHX4iZbtzt6Ny80Z+vtthpwpHPOQ+3Caz9+8uJjVAdOv/t406+IvuKC02TvGPLde3Orlkd2/lIsjgoQ7LinVRsYlaT+VOBpCwVnO+RjkT/pByqhNul5oaxrX258Ql2IMWZ+TjVEympSf+KLNS0ITYPytZNhySBQT5q8dl3KXbqc7FUsG37AXIk75UtLATuo9WC8Phi9CpBEZ6eNkZQ//7o2si
    return canonical[:-1]  # get nb cubes


class Test(unittest.TestCase):

    def test_part_1(self):
        lines = input_file("day")  # get input_test
        lines = input_file("test")  # get input_test
        res = output_file("test_1")  # get output_1
        res = output_file("1")  # get output_1
        pred = get_nb_any_allegens(lines)  # process
        print(pred)  # print
        assert(str(pred) == res[0])  # check

    def test_part_2(self):
        lines = input_file("test")  # get input_test
        lines = input_file("day")  # get input_test
        res = output_file("test_2")  # get output_1
        #res = output_file("2")  # get output_1
        pred = get_nb_any_allegens(lines)  # process
        print(pred) # https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/ popodiloco
        assert(str(pred) == res[0])


if __name__ == '__main__':
    unittest.main()
