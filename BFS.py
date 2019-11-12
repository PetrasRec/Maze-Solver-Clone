from maze import Maze
import queue
import sys
class BreadthFirstSearch:

    def __init__(self, maze):
        self.maze = maze

    def search(self):
        # return the path to the endNode
        start = self.maze.start
        end = self.maze.end
        q = [start]
        start.visited = True
        start.dist = 0

        while len(q) > 0:
            current = q.pop(0)
            
            for child in self.maze.get_children(current):
                # if it is a wall, ignore this child
                if child.wall:
                    continue

                if not(child.visited):
                    child.visited = True
                    child.dist = current.dist + 1
                    q.append(child)
                    # if this child is the end, then quit the search for speed bonus
                    # TODO: quit the search
                else:
                    # TODO: change dist if greater
                    pass

        print("GETTING PATH")
        return self.get_path()


    def get_path(self):
        path = [self.maze.end]

        while not(path[len(path) - 1].x == self.maze.start.x and path[len(path) - 1].y == self.maze.start.y):
                current = path[len(path) - 1]
                bestDist = sys.maxsize
                bestNode = None
                for child in self.maze.get_children(current):
                    if child.dist < bestDist and child.visited:
                        bestDist = child.dist
                        bestNode = child

                if bestNode == None:
                    # path couldn't be found
                    break
                path.append(bestNode)     
                
        return path[::-1]
