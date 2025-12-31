# Advent of Code 2015 day 5

# Objective: Find the nice strings (one per line)
# Rules (All three must be true):
#   1) the string must contain three vowels
#   2) the string contains a double letter
#   3) it does not contain 'ab', 'cd', 'pq', or 'xy'

from sys import argv

script, filename = argv
limits = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

# -------------------------------------------------------------------
# Pt1
# -------------------------------------------------------------------
def offlimits(st):
    for i in limits:
        if i in st:
            return False
    return True


def vowel_check(st):
    count = 0
    for char in st:
        if char in vowels:
            count += 1
        if count >=3:
            return True
    return False


def double(st):
    letter = ''
    for char in st:
        if char == letter:
            return True
        else:
            letter = char
    return False


def d5_1(fname):
    counter = 0
    for line in open(fname):
        if offlimits(line) and vowel_check(line) and double(line):
            counter += 1
    return


# -------------------------------------------------------------------
# Pt2
# -------------------------------------------------------------------
def bytwo(st):
    adj = ''
    letters = []
    for i in range(0, len(st.strip()) - 1, 1):
        window = st[i:i+2]
        if window == adj:
            adj = ''
            break
        elif window in letters:
            return True
        else:
            adj = window
            letters.append(window)
    return False


def skipletter(st):
    buffer = len(st.strip()) - 2
    for i in range(0, len(st.strip()), 1): 
        if i < buffer: 
            if st[i] == st[i+2]:
                return True
        else:
            return False


def d5_2(fname):
    counter = 0
    for line in open(fname):
        print(line)
        if bytwo(line) and skipletter(line):
            counter += 1
    print(counter)    
    return

# ---------------------------------------------------------------------

d5_2(filename)

