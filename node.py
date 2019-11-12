import sys
class Node:
    def __init__(self, x, y, wall):
        self.x = x
        self.y = y
        self.wall = wall
        self.visited = False
        self.dist = sys.maxsize