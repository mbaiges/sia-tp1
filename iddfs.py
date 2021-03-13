import copy

from common import finished, next_configs, process_results
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
            
def iddfs(level):
    smap = level.smap

    first_node = Node(level.start, None, [], 1)

    deque = []

    #metemos al nodo inicial en la cola

    deque.append(first_node)
    processed = HashTable()

    nodes_processed = 0

    n = 50
    # curr_n = n

    # mientras que la cola tenga elementos y no gane

    won = False

    is_on_limit = False


    # print("Entering While")

    while deque and not won:
        
        # saco el primer nodo del stack
        node = deque.pop()
        
        # print('ITERATION: ', nodes_processed, ' --------------------------------------------------------------')
        
        pase = False

        proc_node = processed.get(node.config)

        # if proc_node:
        if proc_node and node.depth >= proc_node.depth:
            continue


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
            
        
        if pase:
            print("Re locardo")

        # print("Current node: ", node)

        # agrego este nodo a los nodos procesados
        processed.put(node.config, node)  

        # print("Added node: ", processed.get(node.config))
    
        # print('checking node at depth: ', node.depth)

        # primero me fijo si gane
        if(finished(node.config.boxes, level)):

            #for nodeinque in deque:
               # if nodeinque.depth < node.depth:
                    #print("there were nodes at: ", nodeinque.depth)

            # si gane listo
            # print("Found solution!")
            won = True
        else:
            nodes_processed += 1
            
            if( node.depth % n == 0):
                is_on_limit = True
            else:
                is_on_limit = False

            # si no gane pido mis movimientos legales
            possible_configs = next_configs(node.config, level.smap)
            # print("Possible configs: ", possible_configs)

            children = node.children
            
            for config in possible_configs:
                new_node = Node(copy.copy(config), node, [], node.depth + 1)
                children.append(new_node)
                if is_on_limit:
                    deque.insert(0, new_node)  
                    #print('added node at begining', node.depth + 1)
                else:
                    deque.append(new_node)    
                    #print('added node at end', node.depth + 1 )

                
                
                # print("Added move: ", new_node.config)

            # print("Used configs: ", processed)
            # print("deque is: ", deque)

    if won:
        path = build_path(node)
        return process_results(won, smap, node, path, ALGORITHM_NAME, nodes_processed - 1, len(deque))
    else:
        return process_results(won, smap, None, [], ALGORITHM_NAME, nodes_processed - 1, len(deque))

