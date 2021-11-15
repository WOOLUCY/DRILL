from pico2d import *

import game_framework
import game_world

# Bird  Speed
PIXEL_PER_METER = (100.0 / 3) # 100 pixel 300 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    spr = None

    def __init__(self, x, y, velocity = 0):
        self.x, self.y, self.velocity = x, y, velocity
        self.spr_w, self.spr_h = 100, 100
        self.frame = 0
        self.frame_amount = 14
        if Bird.spr == None:
            Bird.spr = load_image('bird100x100x14.png')
        self.velocity += RUN_SPEED_PPS
        self.dir = 1

    def update(self):
        if clamp(100, self.x, 1500) == 1500:
            self.velocity -= RUN_SPEED_PPS
        elif clamp(100, self.x, 1500) == 100:
            self.velocity += RUN_SPEED_PPS
        self.dir = clamp(-1, self.velocity, 1)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_amount
        self.x += self.velocity * game_framework.frame_time

    def draw(self):
        if self.dir == 1:
            self.spr.clip_draw(int(self.frame) * self.spr_w, 0, self.spr_w, self.spr_h, self.x, self.y)
        else:
            # self.spr.clip_draw(int(self.frame) * self.spr_w, 0, self.spr_w, self.spr_h, self.x, self.y)
            self.spr.clip_composite_draw(int(self.frame) * self.spr_w, 0, self.spr_w, self.spr_h, 0, 'h', self.x, self.y, self.spr_w, self.spr_h)
        debug_print('Velocity :' + str(self.velocity) + '   Dir :' + str(self.dir))

