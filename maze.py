from node import Node

class Maze:

    def __init__(self, image):

        self.width = image.size[0]
        self.height = image.size[1]
        data = list(image.getdata(0))

        self.start = None
        self.end = None
        self.grid = []
        for y in range(self.height):
            row = []

            for x in range(self.width):
                index = self.convertToIndex(x, y)                
                node = Node(x, y, False if data[index] > 0 else True)
                if y == 0 and not(node.wall):
                    self.start = node
                elif y == self.height - 1 and not(node.wall):
                    self.end = node
                row.append(node)
            self.grid.append(row)

        
           
    def get_children(self, node):
        children = []

        for y in range(-1, 2):
            for x in range(-1, 2):
                if x == 0 or y == 0:
                    if x == 0 and y == 0:
                        continue
                   
                    new_x = x + node.x
                    new_y = y + node.y
                    if new_x < 0 or new_y < 0 or new_x > self.width - 1 or new_y > self.height - 1:
                        continue
                    children.append(self.grid[new_y][new_x])

        return children


    def convertToIndex(self, x, y):
        return y * self.width + x

    def convertToCoordinates(self, index):
        # index = y * width + x
        # x = y * width - index
        row = index // self.height
        col = row * self.width - index
        return (col, row)

