#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 08:23:14 2020
Given a 2 dimensional array and a set of directions, navigat o the end of the 
maze!
      0 = Safe place to walk
      1 = Wall
      2 = Start Point
      3 = Finish Point
      Directons as N,S,E,W
@author: TjH
"""


def maze_runner(maze, directions):
    # Find the starting location of the maze
    start_index = []
    for row in maze:
        if 2 in row:
            for position, object in enumerate(row):
                if object == 2:
                    start_index.append(maze.index(row))
                    start_index.append(position)
                    break
    direction = {'N':(-1,0), 'S': (1,0), "E":(0,1), 'W':(0,-1)}
    #Start walking
    
    for move in directions:
        try:
            start_index[0] += direction[move][0]
            start_index[1] += direction[move][1]
            if maze[start_index[0]][start_index[1]] == 3:
                return 'Finish'
            # The edge case is when the coordinates are negative
            elif maze[start_index[0]][start_index[1]] ==  1:
                return 'Dead'
            elif maze[start_index[0]]<0 or maze[start_index[1]]<0:
                return 'Dead'
        except:
            return 'Dead'
    return "Lost"

maze = [[0, 0, 0, 2, 0, 0],
        [1, 0, 0, 3, 0, 0], 
        [1, 1, 0, 1, 0, 0], 
        [0, 1, 1, 0, 0, 1], 
        [0, 1, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0, 0]]

directions = ['N', 'E', 'W', 'E', 'N']