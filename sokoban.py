# import libraries

import numpy as np
from datetime import datetime
from os import listdir
from os.path import isfile, join

# own libraries

import constants
from algorithms import algorithms
import level_parser

# definitions

levels_folder = 'levels'

def solve(level, alg):
    return alg(level)
    
def error():
	print('Not a valid entry. Please try again')

def add_finish_boxes(level):
    finish_pos = []

    smap = level["smap"]

    for i in range(0, len(smap)):
        for j in range(0, len(smap[0])):
            if (smap[i][j] == constants.GOAL):
                finish_pos.append([i, j])

    level["goals"] = finish_pos

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
            print("%d - %s" % (lvl_idx, level["name"]) )

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

    # call solve(level, algorithm)

    print("All settled! Starting solving level '%s' with algorithm '%s'" % (levels[lvl_chosen]["name"], algorithms[alg_chosen]["name"]))

    # TODO: chequear si deberiamos empezar a contar el tiempo despues de armar las estructuras
    initial_time = datetime.now()
    lvl = levels[lvl_chosen]

    add_finish_boxes(levels[lvl_chosen])

    results = solve(levels[lvl_chosen], algorithms[alg_chosen]["func"])
    finish_time = datetime.now()

    print("Time: ", finish_time - initial_time)

    # prompt answer and stats

start_game()


#tomamos la función asociada a la variable y la invocamos

