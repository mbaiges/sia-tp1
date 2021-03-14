# import libraries
import numpy as np
from os import listdir
from os.path import isfile, join

# own libraries
import constants
from algorithms import algorithms
import level_parser
from utils import *

# definitions

levels_folder = 'levels'

def solve(level, alg):
    return alg(level)
    
def error():
	print('Not a valid entry. Please try again')

def add_finish_boxes(level):
    smap = level.smap
    print(smap)
    for i in range(0, smap.shape[0]):
        for j in range(0, smap.shape[1]):
            if (smap[i,j] == constants.GOAL):
                level.goals.add(Position(i,j))

def start_game():
    level_files = [f for f in listdir(levels_folder) if isfile(join(levels_folder, f))]
    levels = []

    for f in listdir(levels_folder):
        if isfile(join(levels_folder, f)):
            levels.append(level_parser.process_file(levels_folder + '/' + f))

    # prompt for level selection

    lvl_selected = False

    while not lvl_selected or not (lvl_chosen >= 1 and lvl_chosen <= len(levels)):
        if (lvl_selected):
            error()
        else:
            lvl_selected = True
        print("All levels:")
        lvl_idx = 0
        for level in levels:
            lvl_idx += 1
            print("%s - %s" % (f'{lvl_idx:03}', level.name) )

        try:
            lvl_chosen = int(input("Please select a level: "))
        except ValueError:
            lvl_chosen = -1
    
    # determine level
    lvl_chosen -= 1

    # prompt for algorithm

    alg_selected = False

    while not alg_selected or not (alg_chosen >= 1 and alg_chosen <= len(algorithms)):
        if (alg_selected):
            error()
        else:
            alg_selected = True
        print("All algorithms:")
        alg_idx = 0
        for alg in algorithms:
            alg_idx += 1
            print("%d - %s" % (alg_idx, alg["name"]) )

        try:
            alg_chosen = int(input("Please select an algorithm: "))
        except ValueError:
            alg_chosen = -1
        
    alg_chosen -= 1

    print("All settled! Starting solving level '%s' with algorithm '%s'" % (levels[lvl_chosen].name, algorithms[alg_chosen]["name"]))

    lvl = levels[lvl_chosen]

    add_finish_boxes(levels[lvl_chosen])

    solve(levels[lvl_chosen], algorithms[alg_chosen]["func"])


start_game()


#tomamos la función asociada a la variable y la invocamos

