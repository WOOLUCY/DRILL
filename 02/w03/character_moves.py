from pico2d import *
from math import * 

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

square_move = True
circle_move = False
x = 0
y = 0

while True:
    while square_move:
        while x < 800:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x += 2
            delay(0.001)

        while y + 90 + 45 < 600:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(800, y + 90)
            y += 2
            delay(0.001)

        while x > 0:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 600 - 45)
            x -= 2
            delay(0.001)

        while y > 0:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0, y + 90)
            y -= 2
            delay(0.001)

        while x < 400:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x += 2
            delay(0.001)

        circle_move = True
        square_move = False

    while circle_move:
        x = 400
        y = 90
        r = 10

        radian = 0.0
        degree = 1
        pi = 3.141592

        while degree <= 360:
            clear_canvas_now()  
            grass.draw_now(400, 30)
            character.draw_now(x, y)

            radian = (degree * pi / 180) + 29.85
            x = 400 + cos(radian) * 210
            y = 300 + sin(radian) * 210

            degree += 1
            delay(0.01) 
            
        circle_move = False
        square_move = True
            

close_canvas()
