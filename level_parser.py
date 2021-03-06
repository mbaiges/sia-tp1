import numpy as np

import constants
from utils import *

def process_file(txt_file):
    f = open(txt_file, "r")
    
    level_name = txt_file.split('.')[0].split('/')[1]

    smap = []

    l = f.readline()

    # # paredes, o goal, x caja, ^ jugador, % caja con goal, $ jugador con goal

    players_found = 0
    boxes_found = 0
    goals_found = 0
    boxes = set()

    i = 0
    while l:
        row = []
        j = 0
        for char in l:
            if char == ' ':
                row.append(constants.EMPTY)
            elif char == '#':
                row.append(constants.WALL)
            elif char == '.':
                goals_found += 1
                row.append(constants.GOAL)
            elif char == '$':
                boxes_found += 1
                boxes.add(Position(i, j))
                row.append(constants.EMPTY)
            elif char == '@':
                players_found += 1
                player = Position(i, j)
                row.append(constants.EMPTY)
            elif char == '*':
                boxes_found += 1
                boxes.add(Position(i, j))
                goals_found += 1
                row.append(constants.GOAL)
            elif char == '+':
                players_found += 1
                player = Position(i, j)
                goals_found += 1
                row.append(constants.GOAL)
            elif char != '\n':
                print(level_name)
                #raise "Unexpected char '%s' - file '%s'" % (char, txt_file)
            j += 1

        smap.append(row)

        l = f.readline()
        i += 1

    if players_found != 1:
        raise "Maps must have only one player - file '%s'" % txt_file


    if boxes_found == 0:
        raise "Maps must have at least one box - file '%s'" % txt_file
    elif boxes_found != goals_found:
        raise "Maps must have the same amount of boxes and goals - file '%s'" % txt_file

    max_len = max(map(len, smap))

    for line in smap:
        for i in range(len(line), max_len):
            line.append(constants.EMPTY)

    new_level = Level(level_name, Config(player, set(boxes)), np.matrix(smap), set())
    
    return new_level