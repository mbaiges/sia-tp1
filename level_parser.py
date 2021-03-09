import constants

def process_file(txt_file):
    f = open(txt_file, "r")
    
    level_name = f.readline().replace('\n', '')

    data = {}

    data['name'] = level_name

    smap = []

    l = f.readline()

    # # paredes, o goal, x caja, ^ jugador, % caja con goal, $ jugador con goal

    players_found = 0
    boxes_found = 0
    goals_found = 0
    boxes = []

    i = 0
    while l:
        row = []
        j = 0
        for char in l:
            if char == ' ':
                row.append(constants.EMPTY)
            if char == '#':
                row.append(constants.WALL)
            if char == 'o':
                goals_found += 1
                row.append(constants.GOAL)
            if char == 'x' or char == 'X':
                boxes_found += 1
                boxes.append([i, j])
                row.append(constants.EMPTY)
            if char == '^':
                players_found += 1
                player = [i, j]
                row.append(constants.EMPTY)
            if char == '%':
                boxes_found += 1
                boxes.append([i, j])
                goals_found += 1
                row.append(constants.GOAL)
            if char == '$':
                players_found += 1
                player = [i, j]
                goals_found += 1
                row.append(constants.GOAL)
            # elif char != '\n':
                # raise "Unexpected char '%s' - file '%s'" % (char, txt_file)
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

    data['start'] = {
        'player': player,
        'boxes': boxes
    }

    data['smap'] = smap

    print(level_name)
    print(smap)
    
    return data