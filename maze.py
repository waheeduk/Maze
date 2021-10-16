import random

maze_width = 4
maze_height = 4

path = [ ]
stack = [ ]

class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
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

filled = 1
start_pos = Vector2(0, 0)

def generate_maze(position, width, height, filled):
    if position not in stack:
        stack.append(position)
    path.append(position)
    if filled == 25:
        return 
    else:
        options = [ ]
        for dirs in directions:
            result = Vector2(0, 0)
            result = position + dirs
            if result.x < 0 or result.x > width or result.y < 0 or \
                result.y > height:
                pass
            elif result in path:
                pass
            else:
                options.append(result)
        if len(options) == 0:
            if len(stack) != 1:
                stack.pop()
                print(f"stack popped new gen maze with pos of {stack[-1]}")
                return generate_maze(stack[-1], width, height, filled)
            else:
                return generate_maze(stack[-1], width, height, filled)
        else:
            new_pos = random.choice(options)
            filled += 1
            return generate_maze(new_pos, width, height, filled)

generate_maze(start_pos, maze_width, maze_height, filled)
