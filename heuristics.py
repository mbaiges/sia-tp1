import copy
import math

from hashing import HashTable
from sorted_list import OrderedList

def h1(smap, goals, cfg):

    nearest_box = None
    nearest_box_dist = 0

    for box in cfg.boxes:

        dist = box.dist1(cfg.player)

        if not nearest_box or dist < nearest_box_dist:
            nearest_box_dist = dist
            nearest_box = box

    nearest_goal_from_box = None
    nearest_goal_from_box_dist = 0

    for goal in goals:
        dist = nearest_box.dist1(goal)

        if not nearest_goal_from_box or dist < nearest_goal_from_box_dist:
            nearest_goal_from_box_dist = dist
            nearest_goal_from_box = goal

    return nearest_box_dist + nearest_goal_from_box_dist

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

    return len(cfg.boxes.difference(goals))
    
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