import math

def h1(smap, goals, cfg):
    box_goal_matches = []

    boxes = list(cfg.boxes)
    remaining_goals = list(goals)
    nearest_box = None

    dist_sum = 0

    for box in cfg.boxes:
        i = 0
        nearest_idx = -1

        for goal in remaining_goals:
            if nearest_idx == -1 or goal.dist2(box) < remaining_goals[nearest_idx].dist2(box):
                nearest_idx = i
            i += 1

        if not nearest_box or (box.dist1(remaining_goals[nearest_idx]) > 0 and box.dist1(cfg.player) < nearest_box.dist1(cfg.player)):
            nearest_box = box

        box_goal_matches.append((box, remaining_goals[nearest_idx]))
        dist_sum += box.dist1(remaining_goals[nearest_idx])
        remaining_goals.pop(nearest_idx)

    return cfg.player.dist1(nearest_box) + dist_sum

def h2(smap, goals, cfg):
    return "H2"

def h3(smap, goals, cfg):
    return "H3"
    
heuristics = [
    {
        "name": "Heuristic #1",
        "func": h1,
    },
    {
        "name": "Heuristic #2",
        "func": h2,
    },
    {
        "name": "Heuristic #3",
        "func": h3,
    },
]