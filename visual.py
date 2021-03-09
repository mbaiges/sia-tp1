import pygame, sys, random
from pygame.locals import *

BOARDWIDTH = 4  # number of columns in the board
BOARDHEIGHT = 4 # number of rows in the board

TILESIZE = 80

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

FPS = 30

BLANK = None

class GameObject:
    def __init__(self, image, x, y):
        self.image = image
        self.pos = image.get_rect().move(x, y)

def play(smap, path):
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    player_img = pygame.image.load('images/player.bmp').convert()
    box_img = pygame.image.load('images/box.bmp').convert()
    goal_img = pygame.image.load('images/goal.bmp').convert()
    background_img = pygame.image.load('images/background.bmp').convert()

    box_objects = []
    player_object = None

    for pos in path:
        for box in path.boxes:
            box_object = GameObject(box_img, box.x, box.y)
            box_objects.append(box_object)
        
        player = pos['player']
        player_object = GameObject(player_img, player.x, player.y)
        
        
