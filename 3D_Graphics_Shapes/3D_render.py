import numpy as np
import math as mt
import pygame
import sys
from pygame.locals import *

pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Cube Rotation')

# Set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

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


points = [np.array([-50, -50, -50]),
          np.array([50, -50, -50]),
          np.array([50, 50, -50]),
          np.array([-50, 50, -50]),
          np.array([-50, -50, 50]),
          np.array([50, -50, 50]),
          np.array([50, 50, 50]),
          np.array([-50, 50, 50])]


def translate(_coord):
    _with, _height = windowSurface.get_size()
    return _coord[0]+_with//2, _coord[1]+_height//2


def connect_points(x1, y1, x2, y2, _stroke):
    pygame.draw.line(windowSurface, BLUE, translate(
        (int(x1), int(y1))), translate((int(x2), int(y2))), _stroke)


rotate = mt.radians(0)
projected_points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for vector in points:
        rotated_2d = np.matmul(rotation_matrix_x(rotate), vector)
        rotated_2d = np.matmul(rotation_matrix_y(rotate), rotated_2d)
        rotated_2d = np.matmul(rotation_matrix_z(rotate), rotated_2d)
        projected_2d = np.matmul(projection_matrix, rotated_2d)
        projected_points.append(projected_2d)
        pygame.draw.circle(windowSurface, RED, translate(
            (int(projected_2d[0]), int(projected_2d[1]))), 5)

    for j in range(4):
        start = projected_points[j]
        end = projected_points[(j + 1) % 4]
        connect_points(start[0], start[1], end[0], end[1], 1)
        start = projected_points[j + 4]
        end = projected_points[((j + 1) % 4) + 4]
        connect_points(start[0], start[1], end[0], end[1], 1)
        start = projected_points[j]
        end = projected_points[j + 4]
        connect_points(start[0], start[1], end[0], end[1], 1)

    pygame.display.update()
    projected_points.clear()
    rotate += mt.radians(1)
    pygame.time.wait(40)
    windowSurface.fill(BLACK)
