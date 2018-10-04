import pygame
import sys
from pygame.locals import *
import tensorflow as tf
import random as rd
import numpy as np

window = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Polynomial Regression')
_with, _height = window.get_size()

# Set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


def translate(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


def draw_circle(start, radius, _color):
    pygame.draw.circle(window, _color, start, radius)


def draw_line(_start, _end, _stroke, _color):
    pygame.draw.line(window, _color, _start, _end, _stroke)


a = tf.Variable(rd.randrange(-1, 1), dtype='float32')
b = tf.Variable(rd.randrange(-1, 1), dtype='float32')
c = tf.Variable(rd.randrange(-1, 1), dtype='float32')
x_tens = tf.placeholder(dtype='float32')
y_tens = tf.placeholder(dtype='float32')
x_predict = tf.placeholder(dtype='float32')

poly_model = a*(tf.square(x_tens))+b*x_tens+c

predict = a*(tf.square(x_predict))+b*x_predict+c

square_error = tf.square(poly_model-y_tens)
loss = tf.reduce_sum(square_error)

optimizer_function = tf.train.GradientDescentOptimizer(0.05)
train = optimizer_function.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
# Main Draw Loop

points_x = []
points_y = []
curve_y = []
curve_x = np.arange(-1, 1, 0.07).tolist()
simulated = None

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sess.close()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            maped_x = translate(pos[0], 0, _with, -1, 1)
            maped_y = translate(pos[1], 0, _height, 1, -1)
            points_x.append(maped_x)
            points_y.append(maped_y)
            for i in range(550):
                sess.run(train, {x_tens: points_x, y_tens: points_y})
            curve_y = sess.run(predict, {x_predict: curve_x})
            print(sess.run(loss, {x_tens: points_x, y_tens: points_y}))
            simulated = True
    for i in range(len(points_x)):
        maped_x = translate(points_x[i], -1, 1, 0, _with)
        maped_y = translate(points_y[i], -1, 1, _height, 0)
        draw_circle((int(maped_x), int(maped_y)), 4, WHITE)
    if simulated is True:
        for i in range(len(curve_x)-1):
            x_value = translate(curve_x[i], -1, 1, 0, _with)
            y_value = translate(curve_y[i], -1, 1, _height, 0)
            x_next = translate(curve_x[i+1], -1, 1, 0, _with)
            y_next = translate(curve_y[i+1], -1, 1, _height, 0)
            if y_value < _height:
                draw_line((x_value, y_value), (x_next, y_next), 3, GREEN)
    pygame.display.update()
    pygame.time.wait(40)
    window.fill(BLACK)
