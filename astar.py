import copy
from datetime import datetime

from common import finished, next_configs, process_results, build_path
from utils import *
from sorted_list import OrderedList
from hashing import HashTable

ALGORITHM_NAME = "A*"
            
def astar(level, h, testall):
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

    nodes_list.add(first_node)

    #known_cfgs = set()
    known_nodes = HashTable()

    #known_cfgs.add(first_node.config)
    known_nodes.put(first_node.config, first_node)

    nodes_processed = 0

    won = False

    while nodes_list.length() > 0 and not won:
        
        node = nodes_list.pop()

        if(finished(node.config.boxes, level)):
            won = True
        else:
            nodes_processed += 1

            possible_configs = next_configs(node.config, level.smap)

            children = node.children
            
            for config in possible_configs:

                proc_node = known_nodes.get(config)
                new_node = Node(copy.copy(config), node, [], node.depth + 1, {'g': node.depth + 1, 'h': h(smap, level.goals, config)})  

                if proc_node:
                    new_node_f = new_node.meta['g']+new_node.meta['h']
                    proc_node_f = proc_node.meta['g']+proc_node.meta['h']

                    if(new_node_f >= proc_node_f):
                        continue

                # if config in known_cfgs:
                #     continue

                #known_cfgs.add(config)
                known_nodes.put(config, new_node)  

                children.append(new_node)
                nodes_list.add(new_node)


    finish_time = datetime.now()

    elapsed_time = finish_time - initial_time

    if won:
        path = build_path(node)
        return process_results(won, testall, elapsed_time, smap, node, path, ALGORITHM_NAME, nodes_processed - 1, nodes_list.length())
    else:
        return process_results(won, testall, elapsed_time, smap, None, [], ALGORITHM_NAME, nodes_processed - 1, nodes_list.length())

