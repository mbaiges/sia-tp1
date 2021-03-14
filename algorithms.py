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

    return heuristics[heu_chosen]["func"]

def BFS(level):
    return bfs.bfs(level)

def DFS(level):
    return dfs.dfs(level)

def IDDFS(level):
    # prompt for n

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

    return iddfs.iddfs(level, n_chosen)

def GGS(level):
    heuristic = choose_heuristic()
    return ggs.ggs(level, heuristic)

def AStar(level):
    heuristic = choose_heuristic()
    return astar.astar(level, heuristic)

def IDAStar(level):
    heuristic = choose_heuristic()
    return idastar.idastar(level, heuristic)

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
]