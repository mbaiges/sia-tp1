import copy
from datetime import datetime

from common import finished, next_configs, process_results, build_path
from utils import *
from sorted_list import OrderedList

ALGORITHM_NAME = "A*"
            
def astar(level, h):
    initial_time = datetime.now()

    smap = level.smap

    first_node = Node(level.start, None, [], 0, {'g': 0, 'h': h(smap, level.goals, level.start)})

    def cp(e1, e2):
        g1 = e1.meta['g']
        g2 = e2.meta['g']
        h1 = e1.meta['h']
        h2 = e2.meta['h']

        f1 = g1 + h1
        f2 = g2 + h2
        
        if f1 == f2:
            return h1 - h2
        else:
            return f1 - f2

    nodes_list = OrderedList(cp)

    #metemos al nodo inicial en la cola ( ͡° ͜ʖ ͡°)

    nodes_list.add(first_node)
    known_cfgs = set()

    known_cfgs.add(first_node.config)

    nodes_processed = 0

    # mientras que la cola tenga elementos y no gane

    won = False

    while nodes_list.length() > 0 and not won:
        
        # saco el primer nodo del nodes_list
        node = nodes_list.pop()
        # print('ITERATION: ', nodes_processed, ' --------------------------------------------------------------')

        # print("Current node: ", node.config)
    
        # primero me fijo si gane
        if(finished(node.config.boxes, level)):
            # si gane listo
            # print("Found solution!")
            won = True
        else:
            nodes_processed += 1

            # si no gane pido mis movimientos legales
            possible_configs = next_configs(node.config, level.smap)
            # print("Possible configs: ", possible_configs)

            children = node.children
            
            #por cada movimiento legal me fijo si ya tube esta config antes y si no la apendeo a la cola
            # print("Procesed: ===>", processed)
            for config in possible_configs:

                if config in known_cfgs:
                    continue

                known_cfgs.add(config)

                new_node = Node(copy.copy(config), node, [], node.depth + 1, {'g': node.depth + 1, 'h': h(smap, level.goals, config)})
                children.append(new_node)
                nodes_list.add(new_node)
                # print("Added move: ", new_node.config)

            # print("Used configs: ", processed)
            # print("Stack is: ", stack)

    finish_time = datetime.now()

    elapsed_time = finish_time - initial_time

    if won:
        path = build_path(node)
        return process_results(won, elapsed_time, smap, node, path, ALGORITHM_NAME, nodes_processed - 1, nodes_list.length())
    else:
        return process_results(won, elapsed_time, smap, None, [], ALGORITHM_NAME, nodes_processed - 1, nodes_list.length())

