import pygame
import sys
from maze import *

#variables to hold information about rendered game
maze_tile_size = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
screen_width = (int(maze_tile_size * 1.5) * maze_width)
screen_height = (int(maze_tile_size * 1.5) * maze_height)

pygame.init()
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Maze')
screen.fill(BLACK)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #exit
            pygame.quit()
            sys.exit()
    pygame.display.update() #UPDATE DRAW FUNCTION
    #draws tiles in path
    for i in range(len(path)):
        tile_pos = Vector2((path[i].x*maze_tile_size)+ ((maze_tile_size/2)*path[i].x), (path[i].y*maze_tile_size)+((maze_tile_size/2)*path[i].y))
        if i == 0:
            pygame.draw.rect(screen, BLUE, pygame.Rect(tile_pos.x, tile_pos.y, maze_tile_size , maze_tile_size), 0)
        else:
            pygame.draw.rect(screen, WHITE, pygame.Rect(tile_pos.x, tile_pos.y, maze_tile_size , maze_tile_size), 0)
        #draws walls or lack thereof between tiles
        if i <= len(path)-2:
            j = path[i+1]-path[i]
            if j == up:
                wall_pos = tile_pos - Vector2(0, maze_tile_size/2)
                pygame.draw.rect(screen, WHITE, pygame.Rect(wall_pos.x, wall_pos.y, maze_tile_size, maze_tile_size/2), 0)
            if j == down:
                wall_pos = tile_pos + Vector2(0, maze_tile_size)
                pygame.draw.rect(screen, WHITE, pygame.Rect(wall_pos.x, wall_pos.y, maze_tile_size, maze_tile_size/2), 0)
            if j == left:
                wall_pos = tile_pos - Vector2(maze_tile_size/2, 0)
                pygame.draw.rect(screen, WHITE, pygame.Rect(wall_pos.x, wall_pos.y, maze_tile_size/2, maze_tile_size), 0)
            if j == right:
                wall_pos = tile_pos + Vector2(maze_tile_size, 0)
                pygame.draw.rect(screen, WHITE, pygame.Rect(wall_pos.x, wall_pos.y, maze_tile_size/2, maze_tile_size), 0)
    pygame.image.save(screen, "media/maze_example.png")
            