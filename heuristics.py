import copy
import math
from hashing import HashTable
from sorted_list import OrderedList

def h1(smap, goals, cfg):
    box_goal_matches = []

    boxes = list(cfg.boxes)
    remaining_goals = list(goals)
    nearest_box = None
    nearest_box_dist = 0

    dist_sum = 0

    for box in cfg.boxes:
        i = 0
        nearest_idx = -1

        for goal in remaining_goals:
            if nearest_idx == -1 or goal.dist2(box) < remaining_goals[nearest_idx].dist2(box):
                nearest_idx = i
            i += 1

        dist = box.dist1(cfg.player)

        if not nearest_box or (box.dist1(remaining_goals[nearest_idx]) > 0 and dist < nearest_box_dist):
            nearest_box_dist = dist
            nearest_box = box

        box_goal_matches.append((box, remaining_goals[nearest_idx]))
        dist_sum += box.dist1(remaining_goals[nearest_idx])
        remaining_goals.pop(nearest_idx)

    return cfg.player.dist1(nearest_box) + dist_sum

def h2(smap, goals, cfg):
    goals_l = list(goals)
    boxes_l = list(cfg.boxes)

    goals_map = {}

    boxes_pending = [i for i in range(0, len(boxes_l))]

    while boxes_pending:

        box_idx = boxes_pending.pop(0)
        box = boxes_l[box_idx]

        def cp(g1, g2):
            return box.dist2(goals_l[g1]) - box.dist2(goals_l[g2])

        ordered_goals_l = OrderedList(cp)

        for goal_idx in range(0, len(goals_l)):
            ordered_goals_l.add(goal_idx)

        assigned_goal = False

        while ordered_goals_l.length() > 0 and not assigned_goal:

            goal_idx = ordered_goals_l.pop()

            d = goals_l[goal_idx].dist1(box)
            
            if goal_idx in goals_map:
                (gbox_idx, gd) = goals_map[goal_idx]

                if d < gd:
                    boxes_pending.append(gbox_idx)
                    goals_map[goal_idx] = (box_idx, d)
                    assigned_goal = True
                
            else:
                goals_map[goal_idx] = (box_idx, d)
                assigned_goal = True

    goals_matches = []

    bg_sum = 0
    nearest_box_dist = -1

    for k, v in goals_map.items():
        (box_idx, d) = v

        bg_sum += d

        box = boxes_l[box_idx]

        dist = cfg.player.dist1(box)

        if nearest_box_dist < 0 or dist < nearest_box_dist:
            nearest_box_dist = dist

        goals_matches.append((goals_l[k], box))

    return bg_sum + nearest_box_dist

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