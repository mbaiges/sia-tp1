import copy
from datetime import datetime

from common import finished, next_configs, process_results, build_path
from utils import *
from hashing import HashTable

ALGORITHM_NAME = "Iterative Deepening Depth First Search (IDDFS)"

def build_path(node):
    path = []

    n = copy.copy(node)

    while n.father != None:
        path.insert(0, n.config)
        n = n.father

    path.insert(0, n.config)

    return path
            
def iddfs(level, n, testall):
    initial_time = datetime.now()

    smap = level.smap

    first_node = Node(level.start, None, [], 0)

    deque = []

    #metemos al nodo inicial en la cola
    deque.append(first_node)
    known_nodes = HashTable()

    known_nodes.put(first_node.config, first_node)

    nodes_processed = 0
    n = 2

    # curr_n = n

    # mientras que la cola tenga elementos y no gane
    won = False

    limit_nodes_per_n = []
    limit_nodes_per_n_size = 0

    while deque and not won:
        
        # saco el primer nodo del stack
        node = deque.pop()
        
        # if node in processed:
        #     l = list(processed)
        #     idx = l.index(node)

        #     if idx >= 0 and idx < len(l):
        #         proc_node = l[idx]
        #         if node.depth >= proc_node.depth:
        #             pase = True
        #             continue
        #     else:
        #         continue

        # primero me fijo si gane
        if(finished(node.config.boxes, level)):
            # si gane listo
            won = True
        else:
            nodes_processed += 1

            # si no gane pido mis movimientos legales
            possible_configs = next_configs(node.config, level.smap)
            children = node.children

            if (node.depth + 1) % n == 0:
                children_at_limit = True
            else:
                children_at_limit = False
            
            for config in possible_configs:
                proc_node = known_nodes.get(config)

                if proc_node and node.depth + 1 >= proc_node.depth:
                    continue

                new_node = Node(copy.copy(config), node, [], node.depth + 1)

                known_nodes.put(config, new_node)  

                children.append(new_node)

                if children_at_limit:
                    limit_idx = int(new_node.depth / n) - 1
                    if len(limit_nodes_per_n) < limit_idx + 1:
                        limit_nodes_per_n.append(0)
                    limit_nodes_per_n[limit_idx] += 1

                    deque.insert(0, new_node)  
                else:
                    deque.append(new_node)    

                
                
                # print("Added move: ", new_node.config)

            # print("Used configs: ", processed)
            # print("deque is: ", deque)

    finish_time = datetime.now()

    elapsed_time = finish_time - initial_time

    #print(limit_nodes_per_n)

    if won:
        path = build_path(node)
        return process_results(won, testall, elapsed_time, smap, node, path, ALGORITHM_NAME, nodes_processed - 1, len(deque))
    else:
        return process_results(won, testall, elapsed_time, smap, None, [], ALGORITHM_NAME, nodes_processed - 1, len(deque))

