import bfs, dfs, iddfs, ggs, astar, idastar

from heuristics import heuristics

def choose_heuristic():
    # prompt for algorithm

    heu_selected = False

    while not heu_selected or not (heu_chosen >= 1 and heu_chosen <= len(heuristics)):
        if (heu_selected):
            error()
        else:
            heu_selected = True
        print("All heuristics:")
        heu_idx = 0
        for heu in heuristics:
            heu_idx += 1
            print("%d - %s" % (heu_idx, heu["name"]) )

        try:
            heu_chosen = int(input("Please select an algorithm: "))
        except ValueError:
            heu_chosen = -1
        
    heu_chosen -= 1

    return heuristics[heu_chosen]

def BFS(level, testall):
    return bfs.bfs(level, testall)

def DFS(level, testall):
    return dfs.dfs(level, testall)

def IDDFS(level, testall):
    # prompt for n

    if(testall):
        for n in [1, 2, 3, 5, 10, 20]:
            iddfs.iddfs(level, n, testall)
    else:
        n_selected = False

        while not n_selected:
            if (n_selected):
                error()
            else:
                n_selected = True
            try:
                n_chosen = int(input("Please define N depth for IDDFS: "))
            except ValueError:
                n_chosen = -1

        iddfs.iddfs(level, n_chosen, testall)
    return 1

def GGS(level, testall):
    if(testall):
        for h in heuristics:
            ggs.ggs(level, h, testall)
    else:   
        heuristic = choose_heuristic()
        ggs.ggs(level, heuristic, testall)
    return 1
    
def AStar(level, testall):
    if(testall):
        for h in heuristics:
            astar.astar(level, h, testall)
    else:   
        heuristic = choose_heuristic()
        astar.astar(level, heuristic, testall)
    return 1

def IDAStar(level, testall):
    if(testall):
        for h in heuristics:
            idastar.idastar(level, h, testall)
    else:   
        heuristic = choose_heuristic()
        idastar.idastar(level, heuristic, testall)
    return 1

algorithms = [
    {
        "name": bfs.ALGORITHM_NAME,
        "func": BFS,
    },
    {
        "name": dfs.ALGORITHM_NAME,
        "func": DFS,
    },
    {
        "name": iddfs.ALGORITHM_NAME,
        "func": IDDFS,
    },
    {
        "name": ggs.ALGORITHM_NAME,
        "func": GGS,
    },
    {
        "name": astar.ALGORITHM_NAME,
        "func": AStar,
    },
    {
        "name": idastar.ALGORITHM_NAME,
        "func": IDAStar,
    },
    {
        "name": "Test all",
        "funcs": [BFS, DFS, IDDFS, GGS, AStar, IDAStar],
    },
]