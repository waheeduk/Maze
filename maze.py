import random

#size of the maze
maze_width = 20
maze_height = 20

#holds all tiles we visit as we go across
path = [ ]
#holds the latest tiles we've visited in order
stack = [ ]

#class to hold vector2 coordinates with added cosntructors
class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        return False
    def __str__(self):
        return f"({self.x}, {self.y})"

directions = [ ]
up = Vector2(0, -1)
down = Vector2(0, 1)
left = Vector2(-1, 0)
right = Vector2(1, 0)
directions.append(up)
directions.append(down)
directions.append(left)
directions.append(right)

#variable to count number of total tiles we've visited
filled = 1
#starts at top left
start_pos = Vector2(0, 0)

def generate_maze(position, width, height, filled):
    """function that generates recursively generates a maze that visits 
    every tile in a grid"""
    if position not in stack:
        stack.append(position)
    path.append(position)
    if filled == (maze_width+1)*(maze_height+1):
        return 
    else:
        #holds possible routes for maze to travel
        options = [ ]
        for dirs in directions:
            #generates directions in four cardinals
            result = Vector2(0, 0)
            result = position + dirs
            #checks out of bounds
            if result.x < 0 or result.x > width or result.y < 0 or \
                result.y > height:
                pass
            #prevents doubling back
            elif result in path:
                pass
            else:
                options.append(result)
        #checks if we've backed into a corner, in which case, we go backtrack
        if len(options) == 0:
            if len(stack) != 1:
                stack.pop()
                return generate_maze(stack[-1], width, height, filled)
            else:
                return generate_maze(stack[-1], width, height, filled)
        #saves a viable route
        else:
            new_pos = random.choice(options)
            filled += 1
            return generate_maze(new_pos, width, height, filled)

generate_maze(start_pos, maze_width, maze_height, filled)