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
pygame.display.set_caption('Traveling Salesperson Genetic Approach')
_with, _height = window.get_size()

cities = []
# cities = [(385, 121), (109, 259), (381, 213), (188, 454), (308, 322), (274, 454), (176, 106), (563, 206)]
num_cities = 10
population = []
p_size = 600     # p_size mus not be greater than factorial(num_cities)
max_generations = 25
fitness = []
min_distance = 0
best_path = []


def swap(arr, index_a, index_b):
    arr[index_a], arr[index_b] = arr[index_b], arr[index_a]


def text_to_screen(text, x, y, size, _color=(200, 000, 000), font_type='Arial'):
    text = str(text)
    font = pygame.font.SysFont(font_type, size)
    text = font.render(text, True, _color)
    window.blit(text, (x, y))


def draw_circle(start, radius, _color):
    pygame.draw.circle(window, _color, start, radius)


def draw_line(start, end, _stroke, _color):
    pygame.draw.line(window, _color, start, end, _stroke)


def calculate_distance(point_a, point_b):
    return pow((point_a[0] - point_b[0]), 2) + pow((point_a[1] - point_b[1]), 2)


def calculate_path_distance(points, _order):
    total_distance = 0
    for j in range(len(_order)-1):
        total_distance += calculate_distance(points[_order[j]],
                                             points[_order[j+1]])
    return total_distance


def setup():
    for counter in range(num_cities):
        cities.append((rd.randint(5, _with-10), rd.randint(5, _height-10)))
    first_order = list(range(num_cities))
    shuffle(first_order, num_cities//2)
    population.append(first_order)
    for counter in range(p_size-1):
        while first_order in population:
            next_order = first_order.copy()
            shuffle(next_order, num_cities//2)
            first_order = next_order.copy()
        population.append(first_order)


def calculate_population_fitness():
    min_distance_local = mt.inf
    best_path_local = []
    for ind in population:
        _distance = calculate_path_distance(cities, ind)
        if _distance < min_distance_local:
            min_distance_local = _distance
            best_path_local = ind.copy()
        fitness.append(1/(_distance+1))
    return best_path_local, min_distance_local


def normalize_fitness():
    fit_sum = 0
    for fit in fitness:
        fit_sum += fit
    for index in range(len(fitness)):
        fitness[index] = fitness[index]/fit_sum


def shuffle(arr, times):
    for counter in range(times):
        index_a = rd.randint(0, len(arr)-1)
        index_b = rd.randint(0, len(arr)-1)
        swap(arr, index_a, index_b)


def pick_fitness_based(pop_arr, fit_arr):
    index = 0
    r = rd.random()
    while r > 0:
        r = r - fit_arr[index]
        index += 1
    index -= 1
    return pop_arr[index].copy()


def mutate(_parent, _rate):
    for counter in range(num_cities):
        if rd.random() < _rate:
            index = rd.randint(0, len(_parent)-2)
            swap(_parent, index, index+1)


def cross_over_b(order_a, order_b):
    new_order = []
    index = 0
    while index < len(order_a)-1:
        dist_a = calculate_distance(cities[order_a[index]], cities[order_a[index+1]])
        dist_b = calculate_distance(cities[order_b[index]], cities[order_b[index+1]])
        if dist_a < dist_b:
            new_order.append(order_a[index])
            new_order.append(order_a[index+1])
        else:
            new_order.append(order_b[index])
            new_order.append(order_b[index + 1])
        index += 2
    return new_order


def cross_over(order_a, order_b):
    start = rd.randint(0, (len(order_a)-1))
    if start == (len(order_a)-1):
        start -= 1
    end = rd.randint(start+1, (len(order_a)-1))
    new_order = order_a[start:end]
    for item in order_b:
        if item not in new_order:
            new_order.append(item)
    return new_order


def next_generation():
    new_population = []
    for j in range(len(population)):
        order_a = pick_fitness_based(population, fitness)
        order_b = pick_fitness_based(population, fitness)
        order = cross_over(order_a, order_b)
        mutate(order, 0.4)
        new_population.append(order)
    return new_population


if __name__ == '__main__':
    generation_count = 0
    new_min_distance = 1
    setup()
    best_path, min_distance = calculate_population_fitness()
    normalize_fitness()
    stop_draw = None
    range_search = range(len(population[0])-1)
    range_best = range(len(best_path)-1)
    print(cities)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if stop_draw is None:
            for path in population:
                for city in cities:
                    draw_circle(city, 7, RED)
                for i in range_search:
                    draw_line(cities[path[i]], cities[path[i+1]], 1, WHITE)
                for i in range_best:
                    draw_line(cities[best_path[i]], cities[best_path[i+1]], 4, GREEN)
                text_to_screen("Generation: " + str(generation_count) + " Distance: " +
                               str(min_distance), 10, _height-21, 20, WHITE)
                pygame.display.update()
                pygame.time.wait(1)
                window.fill(BLACK)
            stop_draw = True
        elif generation_count < max_generations:
            population = next_generation()
            fitness.clear()
            new_best_path, new_min_distance = calculate_population_fitness()
            if new_min_distance < min_distance:
                min_distance = new_min_distance
                best_path = new_best_path
                print(generation_count)
                print(best_path)
                print(min_distance)
            normalize_fitness()
            generation_count += 1
            stop_draw = None
            print(new_min_distance)
            print(min_distance / new_min_distance)
        elif min_distance/new_min_distance < 0.999999:
            print(new_min_distance)
            print(min_distance / new_min_distance)
            population = next_generation()
            fitness.clear()
            new_best_path, new_min_distance = calculate_population_fitness()
            if new_min_distance < min_distance:
                min_distance = new_min_distance
                best_path = new_best_path
                print(generation_count)
                print(best_path)
                print(min_distance)
            normalize_fitness()
            generation_count += 1
            stop_draw = None
