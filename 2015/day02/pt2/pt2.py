# for every line in the file,
# 1) split the numbers at 'x' and assign them to variables
# 2) calculate total surface area as 2lw + 2wh + 2hl
# 3) find max(h,l,w), remove, and multiply the remaining values (should I order them??)
# 4) add 

from sys import argv
import re

script, filename = argv

# Some other random solution online. Used to debug mine.
# A better, cleaner solution.
def day2_1(fname):
    total = 0
    lin_num = 0
    for line in open(fname):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        total += area + slack
        lin_num += 1
    print(total)

# My code starts here.
# ----------------------------------------------------------------------
def d2_1(fname):
    grand_tally = 0
    pattern = r"\d+"
    for line in open(fname):
        num_list = [int(num_str) for num_str in re.findall(pattern, line)]
        l = num_list[0]
        w = num_list[1]
        h = num_list[2]
        area = 2*((l*w) + (h*w) + (l*h))
        slack = min(l*w, h*w, l*h)
        grand_tally += area + slack
    print(grand_tally)


def d2_2(fname):
    grand_tally = 0
    for line in open(fname):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        min1, min2, min3 = min(l, w), min(w, h), min(l, h)
        short = min(min1, min2, min3)
        long = max(min1, min2, min3)
        short_perim = 2*(short + long)
        bow = l*h*w
        total = short_perim + bow
        grand_tally += total
    print(f"Grand tally is {grand_tally}")


d2_2(filename)
