import unittest
from parse import parse
import copy
from pprint import pprint

import time

def input_file():
    # return the input_test file in a text
    file = open('input', 'r')
    text = file.read()
    file.close()
    return text


def output_file():
    # read line of output_1 file
    file = open('output', 'r')
    res = [line.rstrip('\n') for line in file]
    file.close()
    return res

class TestDay12part3(unittest.TestCase):

    def test_day_12_part_3(self):
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
            return [x_vel, y_vel, z_vel]

        def get_new_position_using_velocity(moon, velocity):
            x, y, z = moon
            x_vel, y_vel, z_vel = velocity
            return [x + x_vel, y + y_vel, z + z_vel]

        def get_new_moons_velocity(moons, moons_velocity):
            new_moons_velocity = []
            for i_m, moon in enumerate(moons):
                x_vel, y_vel, z_vel = moons_velocity[i_m]
                new_x_vel, new_y_vel, new_z_vel = get_current_velocity(moon, moons)
                new_moons_velocity.append((x_vel + new_x_vel, y_vel + new_y_vel, z_vel + new_z_vel))
            return new_moons_velocity

        def set_new_moons_velocity(moons, moons_velocity):
            for i_m, moon in enumerate(moons):
                x_vel, y_vel, z_vel = moons_velocity[i_m]
                new_x_vel, new_y_vel, new_z_vel = get_current_velocity(moon, moons)
                moons_velocity[i_m] = [x_vel + new_x_vel, y_vel + new_y_vel, z_vel + new_z_vel]

        def get_new_moons_position(moons, moons_velocity):
            new_moons_position = []
            for i_m, moon in enumerate(moons):
                new_moons_position.append(get_new_position_using_velocity(moon, moons_velocity[i_m]))
            return new_moons_position

        def set_new_moons_position(moons, moons_velocity):
            for i_m, moon in enumerate(moons):
                moons[i_m] = get_new_position_using_velocity(moons[i_m], moons_velocity[i_m])

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


        def is_beg(moons_velocity):
            for moon_velocity in moons_velocity:
                x, y, z = moon_velocity
                if abs(x) + abs(y) + abs(z) != 0:
                    return False
            return True

        lines = text.split("\n")
        moons = []
        moons_velocity = []
        # step 0
        for line in lines:
            r, x, y, z = line.split("=")
            x = int(x.split(",")[0])
            y = int(y.split(",")[0])
            z = int(z.split(">")[0])
            moons.append([x, y, z])
            moons_velocity.append([0, 0, 0])
        #print("Step 0")
        #for i_m, moon in enumerate(moons):
        #    print(moons[i_m], moons_velocity[i_m])
        moons_velocity = get_new_moons_velocity(moons, moons_velocity)
        i = 0
        nb_steps = 1000000000000
        start = time.time()
        while i < nb_steps:
            # step 1
            # update moons
            set_new_moons_position(moons, moons_velocity)
            # update velocities
            #if i % 100000 == 0:
            #print("Step", i)
            #for i_m, moon in enumerate(moons):
            #    print(moons[i_m], moons_velocity[i_m])
            #print(get_total_energy(moons, moons_velocity))
            i += 1
            if is_beg(moons_velocity):
                break
            if i < nb_steps:
                set_new_moons_velocity(moons, moons_velocity)
            if i % 1000000 == 0:
                done = time.time()
                elapsed = done - start
                print(i, elapsed)
        print(i*2)

        #print(get_total_energy(moons, moons_velocity))



if __name__ == '__main__':
    unittest.main()
