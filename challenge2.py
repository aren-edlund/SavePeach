#!/usr/bin/python

"""
:Author: Aren Edlund
:March 03, 2014
"""

import sys

def my_find(target, board):
    """
    Find some target in the ascii board

    :param `target`: The target char to search for
    :type target: String type
    :param `board`: The board to search
    :type board: List of list of strings
    """
    for index, line in enumerate(board):
        if target in line:
            return (index, line.index(target))

def gen_neighbors(point):
    """
    Generate the neighbors of a node

    :param `point`: The point to generate neighbors for
    :type point: Tuple type
    """
    return [(point[0] + 1, point[1]),
            (point[0] - 1, point[1]),
            (point[0], point[1] - 1),
            (point[0], point[1] + 1)]

def get_path(came_from, current):
    """
    Recursively get the path from the mapping dictionary

    :param `came_from`: The mapping of steps
    :type came_from: Dictonary type
    :param `current`: The current node you are on
    :type current: Tuple type
    """
    if current in came_from:
        p = get_path(came_from, came_from[current])
        p.append(current)
        return p
    else:
        return [current]

def A_star(star, end):
    """
    The A* searhc algorithm as implemented from Wikipedia pseudocode

    :param `start`: The starting location on the board
    :type start: Tuple representing the cartesian coordinates
    :param `end`: The goal location to end at
    :type end: Tuple represeting the cartesian coordinates
    """
    visited = []
    open_dirs = [start]
    came_from = {}
    g_score = {start : 0}
    f_score = {start : g_score[start] + (abs(start[0] - end[0]) + abs(start[1] - end[1]))}
    while open_dirs:
        current = 1000
        for score in f_score:
            if f_score[score] < current and score in open_dirs:
                current = f_score[score]
                node = score
        if node == end:
            p = get_path(came_from, node)
            return p
        open_dirs.remove(node)
        visited.append(node)
        for neighbor in gen_neighbors(node):
            if neighbor not in visited:
                tentative = g_score[node] + 1

                if neighbor not in open_dirs:
                    came_from[neighbor] = node
                    g_score[neighbor] = tentative
                    f_score[neighbor] = g_score[neighbor] + (abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1]))
                    open_dirs.append(neighbor)

if __name__ == "__main__":
    """
    The main loop of the program
    """
    #get the board dimension from the user
    limit = int(raw_input())
    #sys.stderr.write(str(limit) + "\n")
    position = str(raw_input())
    position = set(map(int, position.split()))
    board = []
    #Wait until the dimensions have been filled
    while len(board) < limit:
        board.append(str(raw_input()))

    #sys.stderr.write(str(board))

    start = my_find("m", board)
    princess = my_find("p", board)

    #Search the board using A*
    path = A_star(start, princess)
    path.reverse()
    #Convert the steps based on the coordiantes returne
    for index, step in enumerate(path):
        if index < limit - 1:
            if step[0] > path[index + 1][0]:
                sys.stdout.write("DOWN\n")
                sys.exit()
            elif step[0] < path[index + 1][0]:
                sys.stdout.write("UP\n")
                sys.exit()
            elif step[1] < path[index + 1][1]:
                sys.stdout.write("LEFT\n")
                sys.exit()
            else:
                sys.stdout.write("RIGHT\n")
                sys.exit()
