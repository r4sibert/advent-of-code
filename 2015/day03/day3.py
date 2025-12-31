# Advent of Code Day 3, P1

from sys import argv
script, filename = argv


def d3_p1(fname):
    location = [0, 0]
    houses = [[0, 0]]

    directions = {
            'N': 0,
            'S': 0,
            'E': 0,
            'W': 0,
    }

    moves = {
            '>': (1, 0, 'E'),
            '<': (-1, 0, 'W'),
            '^': (0, 1, 'N'),
            'v': (0, -1, 'S'),
    }

    with open(fname, 'r') as f:
        while True:
            char = f.read(1)
            if not char:
                break
            dx, dy, direct = moves[char]
            location[0] += dx
            location[1] += dy
            directions[direct] += 1
            if location not in houses:
                houses.append(list(location))

    print(len(houses))


def d3_p2(fname):
    santa_loc = [0, 0]
    robot_loc = [0, 0]
    houses = [[0, 0]]
    moves = {
            '>': (1, 0),
            '<': (-1, 0),
            '^': (0, 1),
            'v': (0, -1),
    }

    with open(fname, 'r') as f:
        counter = 1
        while True:
            char = f.read(1)
            if not char:
                break
            dx, dy, = moves[char]
            if counter % 2:
                robot_loc[0] += dx
                robot_loc[1] += dy
            else: 
                santa_loc[0] += dx
                santa_loc[1] += dy
            if santa_loc not in houses:
                houses.append(list(santa_loc))
            if robot_loc not in houses:
                houses.append(list(robot_loc))

            counter += 1

    print(len(houses))

    return


d3_p2(filename)
    
