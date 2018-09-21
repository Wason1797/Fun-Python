import numpy as np
import math as mt
import pygame
import sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption('Lorentz Attractor')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

_with, _height = window.get_size()

projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0]])


def rotation_matrix_z(_angle):
    return np.array([
        [mt.cos(_angle), -mt.sin(_angle), 0],
        [mt.sin(_angle), mt.cos(_angle), 0],
        [0,                 0,           1]
    ])


def rotation_matrix_y(_angle):
    return np.array([
        [mt.cos(_angle), 0, mt.sin(_angle)],
        [0,              1,              0],
        [-mt.sin(_angle), 0, mt.cos(_angle)]

    ])


def rotation_matrix_x(_angle):
    return np.array([
        [1,             0,                0],
        [0, mt.cos(_angle), -mt.sin(_angle)],
        [0, mt.sin(_angle), mt.cos(_angle)]

    ])


def translate(_coord):
    return _coord[0]+_with//2, _coord[1]+_height//2


def connect_points(x1, y1, x2, y2, _stroke, _color):
    pygame.draw.line(window, _color, translate((int(x1), int(y1)))
                     , translate((int(x2), int(y2))), _stroke)


points = []
projected_points = []
_sigma = 10
_rho = 28
_betha = 8/3

x = 0.01
y = 0
z = 0
dt = 0.01
rotate = 0
COLOR = WHITE
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    dx = (_sigma*(y-x))*dt
    dy = (x*(_rho-z)-y)*dt
    dz = (x*y-_betha*z)*dt
    x += dx
    y += dy
    z += dz
    points.append([x, y, z])
    for vector in points:
        rotated_2d = np.matmul(rotation_matrix_x(rotate), vector)
        rotated_2d = np.matmul(rotation_matrix_y(rotate), rotated_2d)
        rotated_2d = np.matmul(rotation_matrix_z(rotate), rotated_2d)
        projected_2d = np.matmul(projection_matrix, rotated_2d)
        projected_2d = np.multiply(projected_2d, 4)
        projected_points.append(projected_2d)
        # pygame.draw.circle(window, COLOR, translate((int(projected_2d[0]), int(projected_2d[1]))), 1)

    for i in range(len(projected_points)-1):
        connect_points(projected_points[i][0], projected_points[i][1],
                       projected_points[i+1][0], projected_points[i+1][1], 1, COLOR)
    projected_points.clear()
    pygame.display.update()
    rotate = 0 if rotate > mt.radians(360) else rotate + mt.radians(1)
    pygame.time.wait(35)
    window.fill(BLACK)
