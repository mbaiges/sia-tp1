import constants

def finished(boxes, level):
    for box in boxes:
        if not box in level["goals"]:
            return False
    return True

def box_becomes_immovable(box, smap):

    cornering_directions = [
        [
            [-1, 0],
            [0, -1]
        ],
        [
            [-1, 0],
            [0, 1]
        ],
        [
            [1, 0],
            [0, -1]
        ],
        [
            [1, 0],
            [0, 1]
        ],
    ]

    for ((i, j), (k, l)) in cornering_directions:
        pos1 = [box[0] + i, box[1] + j]
        pos2 = [box[0] + k, box[1] + l]

        if(smap[pos1[0]][pos1[1]] == constants.WALL and smap[pos2[0]][pos2[1]] == constants.WALL):
            return True

    return False

def next_configs(positions, smap):
    player = positions["player"]
    boxes = positions["boxes"].copy()

    smap_wb = smap.copy()

    for i in range(0, len(smap_wb)):
        smap_wb[i] = smap_wb[i].copy()

    #create an auxiliar map with box information for faster checks
    for (i, j) in boxes:
        smap_wb[i][j] = constants.BOX

    configs = []

    directions = [
        [-1, 0],
        [0, -1],
        [1, 0],
        [0, 1]
    ]

    #por cada una de las 4 direcciones
    for (i, j) in directions:
        #si tengo pared no puedo
        new_pos = [player[0] + i, player[1] + j]
        
        if smap_wb[new_pos[0]][new_pos[1]] != constants.WALL:
            #si hay una caja
            if smap_wb[new_pos[0]][new_pos[1]] == constants.BOX:
                #tengo que fijarme si una mas en la misma direccion hay o una pared o una caja
                if smap_wb[player[0] + 2*i][player[1] + 2*j] != constants.WALL and smap_wb[player[0] + 2*i][player[1] + 2*j] != constants.BOX and (not box_becomes_immovable([player[0] + 2*i, player[1] + 2*j], smap) or smap_wb[player[0] + 2*i][player[1] + 2*j] == constants.GOAL):
                    # me fijo si la caja que movi quedo en una posicion inganable, de ser asi no se mete el caso
                    new_boxes = boxes.copy()
                    for i in range(0, len(new_boxes)):
                        nbox = new_boxes[i].copy()
                        if nbox[0] == new_pos[0] and nbox[1] == new_pos[1]:
                            nbox[0] = player[0] + 2*i
                            nbox[1] = player[1] + 2*j
                        new_boxes[i] = nbox
                    # me muevo a mi y a la caja
                    configs.append({
                        "player": new_pos,
                        "boxes": new_boxes
                    })                    
            #no hay una caja (hay un espacio vacio)
            else:
                configs.append({
                    "player": new_pos,
                    "boxes": boxes.copy()
                })

    return configs

                 
