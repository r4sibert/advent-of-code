# Advent of Code 2015, Day 6
# using conda activate lpthw_env

from sys import argv
import numpy as np
import re

script, filename = argv

# Three possibilities for light states:
# 1) on
# 2) off
# 3) toggle (on to off or vice versa)

# Regex needed for on, off, toggle and two sets
# of coordinates

def parse(st):
    # Dictionary of regex
    switch = {
            'on': r"on",
            'off': r"off",
            'tog': r"toggle",
            }
    # Look for instructions in the string.
    for key in switch:
        if re.search(switch[key], st) is not None:
            state = re.search(switch[key], st) 

    # Look for coordinates
    numbers = re.findall(r"\d+,\d+", st)
    first, second = numbers
    start = [int(i) for i in first.split(',')]
    end = [int(i) for i in second.split(',')]

    # Return coordinates and instructions to main
    parsed = [start, end, state[0]]
    return parsed


def d6_1(fname):
    lights = np.zeros((1000,1000))
    
    # Parse lines into variables, slice the matrix,
    # apply operations. on = 1, off = 0, 
    # toggle = 1 - <state>
    for i in open(fname):
        start, end, state = parse(i)
        if state == "on":
            lights[start[0]:end[0]+1, start[1]:end[1]+1] = 1
        elif state == "off":
            lights[start[0]:end[0]+1, start[1]:end[1]+1] = 0 
        else:
            sublight = lights[start[0]:end[0]+1, start[1]:end[1]+1]
            sublight[:] = 1 - sublight 
    print(np.count_nonzero(lights).item())
    return


def d6_2(fname):
    lights = np.zeros((1000,1000))
    
    for i in open(fname):
        start, end, state = parse(i)
        sublight = lights[start[0]:end[0]+1, start[1]:end[1]+1]
        if state == "on":
            sublight += 1
        elif state == "off":
            sublight -= 1
        elif state == "toggle":
            sublight += 2
        lights[lights < 0] = 0

    print(int(np.sum(lights)))
    return   



d6_2(filename)


