import tensorflow as tf
import random as rd

m = tf.Variable(rd.random(), dtype='float32')
b = tf.Variable(rd.random(), dtype='float32')
x_tens = tf.placeholder(dtype='float32')
y_tens = tf.placeholder(dtype='float32')

linear_model = m*x_tens + b
square_error = tf.square(linear_model-y_tens)
loss = tf.reduce_sum(square_error)

optimizer_function = tf.train.GradientDescentOptimizer(0.01)
train = optimizer_function.minimize(loss)

points_x = [1, 2, 3, 4]
points_y = [2, 5, 6, 9]

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
sess.run(train, {x_tens: points_x, y_tens: points_y})
print(sess.run(loss, {x_tens: points_x, y_tens: points_y}))
sess.close()
