from PIL import Image
import time
import argparse
from maze import Maze

from BFS import BreadthFirstSearch

print ("Loading Image")
im = Image.open("Mazes/maze5.png")
print("Image loaded")
maze = Maze(im)
print("Maze generated")
path = BreadthFirstSearch(maze).search() 

impixels = im.load()



for node in path:
    impixels[node.x,node.y] = (255,0,0)
    pass

im.save("image.png")
print("End.")