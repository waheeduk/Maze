import pygame
import sys
from maze import *

maze_tile_size = 20
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
screen=pygame.display.set_mode((maze_width*maze_tile_size, maze_height*maze_tile_size))
pygame.display.set_caption('Maze')
screen.fill((50,255,255))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #exit
            pygame.quit()
            sys.exit()
    pygame.display.update() #UPDATE DRAW FUNCTION
    #draws tiles in path
    for i in range(len(path)):
        pygame.draw.rect(screen, white, pygame.Rect(path[i].x*maze_tile_size, path[i].y*maze_tile_size, maze_tile_size, maze_tile_size), 0)
    # pygame.draw.rect(screen, white, pygame.Rect(0, 0, maze_tile_size, maze_tile_size), 0)