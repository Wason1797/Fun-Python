# we need to install windows-curses with this command
# pip install windows-curses

import random
import curses


def main(wind):
    curses.noecho()  # we init the screen, a console screen
    curses.cbreak()
    curses.curs_set(0)  # we set the cursor on zero, so is not shown
    wind.timeout(100)
    wind.keypad(True)
    s_height, s_with = wind.getmaxyx()  # get the with and height of the window
    # we init the console screen

    snake_x = (s_with // 4)
    snake_y = (s_height // 2)

    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    food = [(s_height // 2), (s_with // 2)]
    wind.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:

        next_key = wind.getch()
        key = key if next_key == -1 else next_key
        if snake[0][0] in [0, s_height] or snake[0][1] in [0, s_with] or snake[0] in snake[1:]:
            curses.endwin()
            quit()
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                n_food = [
                    random.randint(1, s_height - 1),
                    random.randint(1, s_with - 1)
                ]
                food = n_food if n_food not in snake else None
            wind.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            wind.addch(tail[0], tail[1], ' ')
        wind.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        # .refresh()


curses.wrapper(main)




