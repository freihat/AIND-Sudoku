# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from utils import *

def reduce(values):
    try:
        solved_values = [box for box in values.keys() if len(values[box]) == 1]
    except AttributeError: 
        return print('irreducable')
    a1 = len([i for i in values.values() if len(i)==1])
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    a2 = len([i for i in values.values() if len(i)==1])
    if a2 > a1: reduce(values)
    return values

def naked_twins(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 2]
    a1 = len([i for i in values.values() if len(i)==2])
    for box in solved_values:
        peers_dict = {k:values[k] for k in tuple(peers[box]) if k in values}
        if values[box] in peers_dict.values():
        #if sum( x == values[box] for x in values.values() )
            for peer in peers[box]:
                if len(values[peer])>=3:
                    for digit in values[box]:
                        if digit in values[peer]:
                            values[peer] = values[peer].replace(digit,'')  
    return values

def reduce_puzzle(values):
    import copy
    X = True
    while X:
        values = reduce(values)
        values_t = copy.deepcopy(values)
        values_t = naked_twins(values)
        if values_t == values:
            X = False
        else:
            values = values_t
    return values
first_time = 1   
layer = 1           
puzzle_dict = {}
puzzle = {}
s = {}
def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    
    # Choose one of the unfilled squares with the fewest possibilities
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!

    # If you're stuck, see the solution.py tab!
    ########################################
    
    # reduce the puzzle and copy unreduced version of the puzzle in case the puzzle is wrong and irreducable
    
    global puzzle_dict, puzzle, x, p, s, layer, first_time
    import copy
    
    if first_time == 0:
        values = reduce_puzzle(values)
        first_time = 1
                
    # check if the puzzle is solved
    minimum_keys = [key for key in values.keys() if len(values[key])==1]
    if (len(minimum_keys)==81):
        print('solved')
        display(values)
        return
    
    # knowing the puzzle is not solved find the boxes with most constraints
    i=1
    minimum_keys = []
    while minimum_keys == []:
        i+=1
        minimum_keys = [key for key in values.keys() if len(values[key])==i]
        #print('number of keys with', i, 'constraints is:', len(minimum_keys))
    
    search_key = minimum_keys[0]
    
    for itr in values[search_key]:
        s[layer] = copy.deepcopy(values)
        values[search_key] = itr
        values = reduce_puzzle(values)
        print(search_key, ':', values[search_key])
        display(values)
        puzzle_length=''
        for string in s[layer].values(): puzzle_length+=string
        
        if '' in values.values():
            values = copy.deepcopy(s[layer])
        elif len(puzzle_length) == 81:
            print ('success')
            display(s[layer])
            return
        else:
            #print(layer)
            layer+=1
            search(values)
    
    layer = layer - 1
    return s[layer]



import sys
sys.setrecursionlimit(1000)

#grid2 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = grid_values(grid2)
search(values)