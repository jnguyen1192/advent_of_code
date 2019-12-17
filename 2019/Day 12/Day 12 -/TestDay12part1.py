import unittest
from parse import parse
import copy
from pprint import pprint


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


class TestDay11part1(unittest.TestCase):

    def test_day_12_part_1(self):
        text = input_file()

        def get_current_velocity(current_moon, moons):
            x_vel, y_vel, z_vel = (0, 0, 0)
            for moon in moons:
                if current_moon != moon:
                    # velocity x
                    if current_moon[0] < moon[0]:
                        x_vel += 1
                    elif current_moon[0] > moon[0]:
                        x_vel -= 1
                    # velocity y
                    if current_moon[1] < moon[1]:
                        y_vel += 1
                    elif current_moon[1] > moon[1]:
                        y_vel -= 1
                    # velocity x
                    if current_moon[2] < moon[2]:
                        z_vel += 1
                    elif current_moon[2] > moon[2]:
                        z_vel -= 1
            return x_vel, y_vel, z_vel

        def get_new_position_using_velocity(moon, velocity):
            x, y, z = moon
            x_vel, y_vel, z_vel = velocity
            return x + x_vel, y + y_vel, z + z_vel

        def get_new_moons_velocity(moons, moons_velocity):
            new_moons_velocity = []
            for i_m, moon in enumerate(moons):
                x_vel, y_vel, z_vel = moons_velocity[i_m]
                new_x_vel, new_y_vel, new_z_vel = get_current_velocity(moon, moons)
                new_moons_velocity.append((x_vel + new_x_vel, y_vel + new_y_vel, z_vel + new_z_vel))
            return new_moons_velocity

        def get_new_moons_position(moons, moons_velocity):
            new_moons_position = []
            for i_m, moon in enumerate(moons):
                new_moons_position.append(get_new_position_using_velocity(moon, moons_velocity[i_m]))
            return new_moons_position

        def get_potential_or_kinetic_energy(object):
            x, y, z = object
            return abs(x) + abs(y) + abs(z)

        def get_energy(moon, moon_velocity):
            return get_potential_or_kinetic_energy(moon) * get_potential_or_kinetic_energy(moon_velocity)

        def get_total_energy(moons, moons_velocity):
            total = 0
            for i_m, moon in enumerate(moons):
                total += get_energy(moons[i_m], moons_velocity[i_m])
            return total

        lines = text.split("\n")
        moons = []
        moons_velocity = []
        # step 0
        for line in lines:
            r, x, y, z = line.split("=")
            x = int(x.split(",")[0])
            y = int(y.split(",")[0])
            z = int(z.split(">")[0])
            moons.append((x, y, z))
            moons_velocity.append((0, 0, 0))
        print("Step 0")
        for i_m, moon in enumerate(moons):
            print(moons[i_m], moons_velocity[i_m])
        moons_velocity = get_new_moons_velocity(moons, moons_velocity)
        i = 0
        nb_steps = 100000
        while i < nb_steps:
            # step 1
            # update moons
            moons = get_new_moons_position(moons, moons_velocity)
            # update velocities
            #print("Step", i+1)
            for i_m, moon in enumerate(moons):
                print(moons[i_m], moons_velocity[i_m])
            i += 1
            if i < nb_steps:
                moons_velocity = get_new_moons_velocity(moons, moons_velocity)
        #print(get_total_energy(moons, moons_velocity))



if __name__ == '__main__':
    unittest.main()
