from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 599
        self.image1 = load_image('ball21x21.png')   # small ball
        self.image2 = load_image('ball41x41.png')   # big ball
        self.velocity = random.randint(100, 1000)    # random velocity
        self.IsSmall = random.randint(0, 1)
        if not self.IsSmall:
            self.dist = 800 - 73
        else:
            self.dist = 800 - 63



    def update(self):
        if self.y >= 73 and not self.IsSmall:
            self.y -= self.dist / self.velocity
        elif self.y >= 63 and self.IsSmall:
            self.y -= self.dist / self.velocity

    def draw(self):
        if self.IsSmall:
            self.image1.draw(self.x, self.y)
        else:
            self.image2.draw(self.x, self.y)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 8)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()

grass = Grass()
team = [Boy() for i in range(1, 11 + 1)]
balls = [Ball() for i in range(1, 20 + 1)]  # generate balls

running = True
# game main loop code
while running:
    handle_events()

    # game logic
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    # game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()