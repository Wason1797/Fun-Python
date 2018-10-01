import pygame
import sys
from pygame.locals import *
import tensorflow as tf
import random as rd

window = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Linear Regression')
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


m = tf.Variable(rd.random(), dtype='float32')
b = tf.Variable(rd.random(), dtype='float32')
x_tens = tf.placeholder(dtype='float32')
y_tens = tf.placeholder(dtype='float32')

linear_model = m*x_tens + b


predict = m*(tf.constant([0, 1], dtype='float32'))+b


square_error = tf.square(linear_model-y_tens)
loss = tf.reduce_sum(square_error)

optimizer_function = tf.train.GradientDescentOptimizer(0.05)
train = optimizer_function.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
# Main Draw Loop

points_x = []
points_y = []
line = [0, 1]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sess.close()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            maped_x = translate(pos[0], 0, _with, 0, 1)
            maped_y = translate(pos[1], 0, _height, 1, 0)
            points_x.append(maped_x)
            points_y.append(maped_y)
            for i in range(550):
                sess.run(train, {x_tens: points_x, y_tens: points_y})
            line = sess.run(predict)
            print(sess.run(loss, {x_tens: points_x, y_tens: points_y}))
    for i in range(len(points_x)):
        maped_x = translate(points_x[i], 0, 1, 0, _with)
        maped_y = translate(points_y[i], 0, 1, _height, 0)
        draw_circle((int(maped_x), int(maped_y)), 4, WHITE)
    line_y1 = translate(line[0], 0, 1, _height, 0)
    line_y2 = translate(line[1], 0, 1, _height, 0)
    draw_line((0, line_y1), (_height, line_y2), 3, GREEN)
    pygame.display.update()
    pygame.time.wait(40)
    window.fill(BLACK)
