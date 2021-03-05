from bfs import bfs

def BFS(level):
    print('BFS')
    return bfs(level)

def DFS(level):
	print('DFS')

def IDDFS(level):
	print('IDDFS')

def GGS(level):
	print('GGS')

def AStar(level):
	print('AStar')

def IDAStar(level):
	print('IDAStar')

algorithms = [
    {
        "name": "Breadth First Search (BFS)",
        "func": BFS,
    },
    {
        "name": "Depth First Search (DFS)",
        "func": DFS,
    },
    {
        "name": "Iterative Deepening Depth First Search (IDDFS)",
        "func": IDDFS,
    },
    {
        "name": "GGS",
        "func": GGS,
    },
    {
        "name": "AStar",
        "func": AStar,
    },
    {
        "name": "IDAStar",
        "func": IDAStar,
    },
]