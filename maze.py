import random

width = 5
height = 5

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

start_pos = Vector2(0, 0)

def generate_maze(position):
    stack.append(position)
    path.append(position)
    if len(path) == (width*height):
        return 
    else:
        options = [ ]
        for dirs in directions:
            result = Vector2(0, 0)
            result = position + dirs
            if result.x < 0 or result.x > width or result.y < 0 or \
                result.y > height:
                pass
            else:
                options.append(result)
        for option in options:
            if option in path:
                options.remove(option)
        if len(options) == 0:
            stack.pop()
            generate_maze(stack[-1])
        else:
            new_pos = random.choice(options)
            generate_maze(new_pos)

generate_maze(start_pos)
# for vector in path:
#     print(vector)
for pos in stack:
    print(pos)
print(len(stack))
print(len(path))