from builtins import print
import pygame
import sys
from pygame.locals import *
import random as rd
import math as mt

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((700, 500), 0, 32)
pygame.display.set_caption('Traveling Salesperson')
_with, _height = window.get_size()


num_cities = 9
completed = 1
total_paths = mt.factorial(num_cities)
cities = []
order = list(range(num_cities))
lowest_distance = 0
best_path = order.copy()


def swap(arr, index_a, index_b):
    arr[index_a], arr[index_b] = arr[index_b], arr[index_a]


def lex_order():
    lar_i = -1
    lar_j = -1
    for index in range(len(order)-1):
        if order[index] < order[index+1]:
            lar_i = index
    if lar_i == -1:
        print("finished")
        return True
    for index in range(len(order)):
        if order[lar_i] < order[index]:
            lar_j = index
    swap(order, lar_i, lar_j)
    end_arr = order[lar_i+1::]
    del order[lar_i+1::]
    end_arr.reverse()
    order.extend(end_arr)
    return None


def translate(_coord):
    return _coord[0]+_with//2, _coord[1]+_height//2


def draw_circle(start, radius, _color):
    pygame.draw.circle(window, _color, start, radius)


def draw_line(start, end, _stroke, _color):
    pygame.draw.line(window, _color, start, end, _stroke)


def text_to_screen(text, x, y, size, _color=(200, 000, 000), font_type='Arial'):
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, _color)
        window.blit(text, (x, y))


def setup():
    for counter in range(num_cities):
        cities.append((rd.randint(5, _with-10), rd.randint(5, _height-10)))


def calculate_distance(point_a, point_b):
    return pow((point_a[0] - point_b[0]), 2) + pow((point_a[1] - point_b[1]), 2)


def calculate_path_distance(points, _order):
    total_distance = 0
    for j in range(len(_order)-1):
        total_distance += calculate_distance(points[_order[j]],
                                             points[_order[j+1]])
    return total_distance


if __name__ == '__main__':
    setup()
    stop_draw = None
    lowest_distance = calculate_path_distance(cities, best_path)
    current_distance = 0
    range_search = range(len(order)-1)
    range_best = range(len(best_path)-1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if stop_draw is None:
            for city in cities:
                draw_circle(city, 7, RED)
            for i in range_search:
                draw_line(cities[order[i]], cities[order[i+1]], 1, WHITE)
            for i in range_best:
                draw_line(cities[best_path[i]], cities[best_path[i+1]], 4, GREEN)
            if lex_order() is True:
                stop_draw = True
            current_distance = calculate_path_distance(cities, order)
            if current_distance < lowest_distance:
                lowest_distance = current_distance
                best_path = order.copy()
            completed += 1
            percent_finished = (completed/total_paths) * 100
            text_to_screen(str(round(percent_finished, 3))+" %", 10, _height - 20, 20, WHITE)
            pygame.display.update()
            pygame.time.wait(1)
            window.fill(BLACK)

