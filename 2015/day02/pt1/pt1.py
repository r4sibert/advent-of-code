# for every line in the file,
# 1) split the numbers at 'x' and assign them to variables
# 2) calculate total surface area as 2lw + 2wh + 2hl
# 3) find max(h,l,w), remove, and multiply the remaining values (should I order them??)
# 4) add 

from sys import argv
import re
import math

script, filename = argv

# Some other random solution online. Used to debug mine.
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
def split(string):
    pattern = r"\d+"
    num_list = [int(num_str) for num_str in re.findall(pattern, string)]
    #print(num_list)
    return num_list

grand_tally = 0

with open(filename, 'r') as file_object:
    for line in file_object:
        num_list = split(line)
        l = num_list[0]
        w = num_list[1]
        h = num_list[2]
        area = (2*l*w) + (2*h*w) + (2*l*h)
        slack = min(l*w, h*w, l*h)
        semi = area + slack
        grand_tally += area + slack

print(grand_tally)
