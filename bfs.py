from common import finished, next_configs

def unordered_positions_equal(list1, list2):
    still_equal = True
    for (i, j) in list1:
        still_equal = False
        for (k, l) in list2:
            if (i == k and j == l):
                still_equal = True
        if not still_equal:
            return False

    return True
        
def config_was_used(config, processed):
    for cfg in processed:
        if cfg['player'][0] == config['player'][0] and cfg['player'][1] == config['player'][1] and unordered_positions_equal(cfg['boxes'], config['boxes']):
            return True
    return False

def build_path(node):
    path = []

    n = node.copy()

    while n['father'] != None:
        path.insert(0, n['pos'])
        n = n['father']

    path.insert(0, n['pos'])

    return path
            
def bfs(level):
    smap = level['smap']

    first_node = {
        'father': None,
        'pos': {},
        'children': []
    }

    first_node['pos'] = level['start']

    queue = []

    #metemos al nodo inicial en la cola

    queue.append(first_node)
    processed = []

    # mientras que la cola tenga elementos y no gane

    won = False

    while queue and not won:
        
        # saco el primer nodo de la cola
        node = queue.pop(0)
        # agrego este nodo a los nodos procesados
        processed.append(node["pos"])

        # primero me fijo si gane
        if(finished(node["pos"]["boxes"], level)):
            # si gane listo
            print("found solution")
            won = True
            
        else:
            # si no gane pido mis movimientos legales
            possible_configs = next_configs(node["pos"], level["smap"])
            # print("Possible configs: ", possible_configs)

            children = node["children"]
            
            #por cada movimiento legal me fijo si ya tube esta config antes y si no la apendeo a la cola
            
            for config in possible_configs:
                if not config_was_used(config, processed):
                    new_node = {
                        'father': node,
                        'pos': config.copy(),
                        'children': []
                    }
                    children.append(new_node)
                    queue.append(new_node)

            # print("Used configs: ", processed)
            # print("Queue is: ", queue)

    if won:
        path = build_path(node)

        return {
            'msg': 'Ganaste pibe, bien ahi',
            'path': path
        }
    else:
        return {
            'msg': 'No Ganaste pibe, mal ahi',
            'path': None
        }

