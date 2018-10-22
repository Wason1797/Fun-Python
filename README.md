
# Fun Python

This library is a fun little project; most of the programs are my take on The Coding Train's
coding challenges

## Some of the projects i made

- **Python Basics**
  - Simple syntax and operations in python [first_app.py](Fundamentals/first_app.py)
  - A test file, it's not super important, contains a simple matrix class [test_file.py](Fundamentals/test_file.py)
  - Introduction to turtle graphics, recursive spiral exercise [recursive_spiral.py](Fractal_Trees/recursive_spiral.py)
- **Fractal Trees**
  - Recursive approach to draw fractal trees (i took the code from an internet example) [app.py](Fractal_Trees/app.py")
  - Object oriented approach [object_fractal_trees.py](Fractal_Trees/object_fractal_trees.py)
  - L-System approach [fractal_l_system.py](Fractal_Trees/fractal_l_system.py)
- **3D graphics and shapes with pygame**
  - 3D cube render with rotation (using matrix operations) [3D_render.py](3D_Graphics_Shapes/3D_render.py)
  - 3D Lorentz Attractor, also with the same approach as before [lorentz..py](3D_Graphics_Shapes/lorentz.py)
  - Lemniscata, this drawing looks as the infinity symbol (this one is 2D) [lemniscata.py](3D_Graphics_Shapes/lemniscata.py)
- **Snake Game**
  - Simple snake game, _this one was taken from a popular YouTube video_ [sanake.py](Games/snake.py)
- **Traveling Salesperson problem**
  - Lexicographic order approach -> this one is like brute forcing into the solution, not  super fast [LexSalesperson.py](Traveling_Salesperson/LexSalesperson.py)
  - Genetic algorithm approach -> this one is more fun, i implemented this one with cross-over and mutation, also I select my population in a random way without repetition, it may need some improvements tho [genSalesperson.py](Traveling_Salesperson/genSalesperson.py)
- **Tensorflow**
  - Linear Regression with gradient descent but no interactivity [tsExample.py](Tensor%20Flow/tsExample.py")
  - Linear Regression with gradient descent optimizer and interactivity, this script allows you to provide the points on a canvas, so the computer will adjust a line and show it to you [tsLinearRegression.py](Tensor%20Flow/tsLinearRegression.py)
  - Polynomial Regression, quadratic approach with interactivity (same as the linear one) [tsPolyRegression.py](Tensor%20Flow/tsPolyRegression.py)

## Resources

Coding Train's YouTube channel and all de documentation on the tools i used.
_I will provide the concrete resources (links to videos and such) I used on another time, I need to gather them all again_

## Tools

- pygame
- numpy
- tensorflow
- turtle
