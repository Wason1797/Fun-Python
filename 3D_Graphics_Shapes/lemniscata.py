import numpy as np
import math as mt
import pygame
import sys
import random
from pygame.locals import *


pygame.init()
window = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Lorentz Atractor')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

_with, _height = window.get_size()


def translate(_coord):
    return _coord[0]+_with//2, _coord[1]+_height//2


points = []
a = 100
t = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    d = (1 + pow(mt.sin(t), 2))
    x = (a * mt.cos(t)) / d
    y = (a * mt.sin(t) * mt.cos(t)) / d
    points.append((x, y))
    pygame.draw.circle(window, RED, translate((int(x), int(y))), 1)
    pygame.display.update()
    t = 0 if t > 360 else t + mt.radians(0.5)
    # rotate += mt.radians(1)
    pygame.time.wait(15)
    # window.fill(BLACK)
