from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global cur_x, cur_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cur_x, cur_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
facing_right = True
facing_left = False
cur_x, cur_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if cur_x - 3 <= x <= cur_x + 3 and cur_y - 3 <= y <= cur_y + 3 and facing_right:
        x = cur_x
        y = cur_y
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif cur_x - 3.5 <= x <= cur_x + 3 and cur_y - 3 <= y <= cur_y + 3 and facing_left:
        x = cur_x
        y = cur_y
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif cur_x - x >= 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif cur_x - x < 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    hand_arrow.draw(cur_x, cur_y)
    update_canvas()

    frame = (frame + 1) % 8
    handle_events()

    if cur_x - x > 0:
        facing_right = True
        facing_left = False
        x += 3
    elif cur_x - x < 0:
        facing_right = False
        facing_left = True
        x -= 3

    if cur_y - y > 0:
        y += 3
    elif cur_y - y < 0:
        y -= 3
close_canvas()
