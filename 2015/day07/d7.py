# Advent of Code 2015, Day 07
#           |                      
#   __,   __|        _   _  _  _|_ 
#  /  |  /  |  |  |_|/  / |/ |  |  
#  \_/|_/\_/|_/ \/  |__/  |  |_/|_/
#               _  
#              | | 
#          __  | | 
#         /  \_|/  
#         \__/ |__/
#              |\  
#              |/  
#                  |      
#      __   __   __|   _  
#     /    /  \_/  |  |/  
#     \___/\__/ \_/|_/|__/
#     
# ------------------------------------------------------------                                                               

# Build circuits using 16-bit binary conversions of base 10 numbers
# Need to build a 16-bit binary calculator.

from sys import argv

script, filename = argv

def initialize(untang):
    # Function returns a dict containing circuit starting conditions
    # e.g., ['2', '->', 'b']

    starter_map = {}

    for i in untang:
        if len(i) == 3: # initial values exist only in array of length 3
            try:
                starter_map[i[-1]] = int(i[0]) # Add to wire-value dictionary if first value is a number 
            except ValueError:
                continue # ignore if not

    return starter_map 


def sorter(tangled):
    # Returns a list of arrays, ordered first by number
    # and then alphabetically. 

    disentangled = [] # Clean array of values split on spaces
    untangled = [] # Ordered version of disentangled
    
    for i in open(tangled):
        stripped = i.strip() # strip \n etc. from lines
        disentangled.append(stripped.split(' ')) # split line on spaces and store as array value
    untangled = sorted(disentangled, key=lambda word: (len(word), word)) # sort by len and alpha

    return untangled


def printmap(wmap):
    for i in wmap:
        print(i, '=>', wmap[i])


def sandbox(fname):
    instructions = sorter(fname)
    wiremap = initialize(instructions) # wiremap initialized with starter values

    while len(wiremap) < len(instructions):
    
        for step in instructions:
            # catalog signal destination 
            out_wire =step[-1]

            # LENGTH 3
            if len(step) == 3: # Intial values set in wiremap. 
                #print("len3", step)
                if step[0] in wiremap: # if the wire has a signal, then connect new wire. 
                    wiremap[out_wire] = int(wiremap[step[0]])
                else:
                    continue

            # LENGTH 4
            elif len(step) == 4: # Every one begins with NOT
                # GATE always a 'NOT' bitwise, 16-bit
                GATE = step[0]
                IN1 = step[1]
                
                try:
                    wiremap[out_wire] = ~int(IN1) & 0xFFFF # If a number, perform GATE and assign it to wiremap
                except ValueError:
                    if IN1 in wiremap: # If input is a wire with signal, do operation and assign to wiremap.
                        wiremap[out_wire] = ~int(wiremap[IN1]) & 0xFFFF # bitwise NOT 16 bits
                    else:
                        continue

            #LENGTH 5
            elif len(step) == 5: # None have NOT
                # Check input 1, GATE, and input 2
                IN1 = step[0]
                GATE = step[1]
                IN2 = step[2]

                if IN1 in wiremap and IN2 in wiremap: # Gate will not be rshift or lshift if both in dict.
                    num1 = int(wiremap[IN1])
                    num2 = int(wiremap[IN2])
                    if GATE == 'AND':
                        wiremap[out_wire] = num1 & num2
                    elif GATE == 'OR':
                        wiremap[out_wire] = num1 | num2
                
                elif IN1 in wiremap: # IN2 will always be a number
                    if GATE == 'RSHIFT':
                        num1 = int(wiremap[IN1])
                        num2 = int(IN2) 
                        wiremap[out_wire] = num1 >> num2 
                    elif GATE == 'LSHIFT':
                        num1 = int(wiremap[IN1])
                        num2 = int(IN2) 
                        wiremap[out_wire] = num1 << num2 

                elif IN2 in wiremap: # All lines that start with a number use 'AND' 
                    try:
                        wiremap[out_wire] = int(IN1) & int(wiremap[IN2])
                    except:
                        continue
    printmap(wiremap)
    return


sandbox(filename)



