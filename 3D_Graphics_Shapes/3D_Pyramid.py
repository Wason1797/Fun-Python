import numpy as np
import math as mt
import pygame
import sys
from pygame.locals import *


pygame.init()

window_surface = pygame.display.set_mode((500, 500), 0, 32)

pygame.display.set_caption('Pyramid Rotation')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

projection_mt = np.array(
    [[1, 0, 0],
     [0, 1, 0]]
)


def rotation_mt_z(_angle):
    return np.array(
        [
            [mt.cos(_angle), -mt.sin(_angle), 0],
            [mt.sin(_angle), mt.cos(_angle), 0],
            [0, 0, 1]
        ]
    )


def rotation_mt_y(_angle):
    return np.array(
        [
            [mt.cos(_angle), 0, mt.sin(_angle)],
            [0, 1, 0],
            [-mt.sin(_angle), 0, mt.cos(_angle)]
        ]
    )


def rotation_mt_x(_angle):
    return np.array(
        [
            [1, 0, 0],
            [0, mt.sin(_angle), mt.cos(_angle)],
            [0, mt.cos(_angle), -mt.sin(_angle)]

        ]
    )


pyramid = [
    np.array([-1/2, 0, -1/2]),
    np.array([-1/2, 0, 1/2]),
    np.array([1/2, 0, 1/2]),
    np.array([1/2, 0, -1/2]),
    np.array([0, -1, 0])
]


def translate_coord(_coord):
    _width, _height = window_surface.get_size()
    return _coord[0]+_width//2, _coord[1]+_height//2


def connect_points(x1, y1, x2, y2, _stroke, _color):
    pygame.draw.line(window_surface, _color, translate_coord(
        (int(x1), int(y1))), translate_coord((int(x2), int(y2))), _stroke)


def draw_point(x, y, _color, _stroke):
    pygame.draw.circle(window_surface, _color,
                       translate_coord((int(x), int(y))), _stroke)


theta = mt.radians(0)
projected_pyramid = []
scale = 200


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for point in pyramid:
        rotated = np.matmul(rotation_mt_x(theta), np.multiply(point, scale))
        rotated = np.matmul(rotation_mt_y(theta), rotated)
        rotated = np.matmul(rotation_mt_z(theta), rotated)

        projected = np.matmul(projection_mt, rotated)
        projected_pyramid.append(projected)
        draw_point(projected[0], projected[1], BLUE, 6)

    for i in range(4):
        point = projected_pyramid[i]
        corner = projected_pyramid[4]
        end = projected_pyramid[(i+1)%4]
        connect_points(point[0], point[1], corner[0], corner[1], 3, RED)
        connect_points(point[0], point[1], end[0], end[1], 3, RED)

        

    pygame.display.update()
    projected_pyramid.clear()
    theta+=mt.radians(1)
    pygame.time.wait(40)
    window_surface.fill(BLACK)
