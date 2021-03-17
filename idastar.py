import copy
from datetime import datetime

from common import finished, next_configs, process_results, build_path
from utils import *
from hashing import HashTable
from sorted_list import OrderedList

ALGORITHM_NAME = "Iterative Deepening A* (IDA*)"
            
def idastar(level, h, testall):
    initial_time = datetime.now()

    smap = level.smap

    first_node = Node(level.start, None, [], 0, {'g': 0, 'h': h(smap, level.goals, level.start)})

    lim = first_node.meta['g'] + first_node.meta['h'] # f(n0)

    min_exceeded_lim = -1

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

    q1 = []
    q2 = []

    out_of_frontier = OrderedList(cp)

    q1.append(first_node)
    known_nodes = HashTable()

    known_nodes.put(first_node.config, first_node)

    nodes_processed = 0

    won = False

    first_found = False

    while (q1 or q2) and not won:

        if not q1:
            q1 = q2
            q2 = []
            lim = min_exceeded_lim
            min_exceeded_lim = -1

        node = q1.pop()

        f = node.meta['g'] + node.meta['h']

        if f > lim:
            q2.append(node)
            continue

        if(finished(node.config.boxes, level)):
            won = True
        else:
            nodes_processed += 1
            possible_configs = next_configs(node.config, level.smap)

            children = node.children
            
            for config in possible_configs:

                proc_node = known_nodes.get(config)

                if proc_node and node.depth + 1 >= proc_node.depth:
                    continue

                new_node = Node(copy.copy(config), node, [], node.depth + 1, {'g': node.depth + 1, 'h': h(smap, level.goals, config)})

                known_nodes.put(config, new_node)  

                children.append(new_node)

                f = new_node.meta['g'] + new_node.meta['h']

                if f > lim:
                    q2.append(new_node) 
                    if min_exceeded_lim == -1 or f < min_exceeded_lim:
                        min_exceeded_lim = f
                else:
                    q1.append(new_node)     
                

    finish_time = datetime.now()

    elapsed_time = finish_time - initial_time

    if won:
        path = build_path(node)
        return process_results(won, testall, elapsed_time, smap, node, path, ALGORITHM_NAME, nodes_processed - 1, len(q1) + len(q2))
    else:
        return process_results(won, testall, elapsed_time, smap, None, [], ALGORITHM_NAME, nodes_processed - 1, len(q1) + len(q2))

