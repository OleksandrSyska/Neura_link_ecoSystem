import pygame as g

import value_control.settings as SET
from classes.Back_Ground import BG
FPS = 60
fl_running = True
g.init()
sc = g.display.set_mode((SET.SCW, SET.SCH)) # init. display
tiles = [
    g.image.load(f'src\\bg\\grass\\grass1.png'),
    g.image.load(f'src\\bg\\grass\\grass2.png'),
    g.image.load(f'src\\bg\\grass\\grass3.png'),
    g.image.load(f'src\\bg\\grass\\grass4.png')
]
trees = [
    g.image.load(f'src\\bg\\tree\\Btree1.png').convert_alpha(),
    g.image.load(f'src\\bg\\tree\\Btree2.png').convert_alpha(),
    g.image.load(f'src\\bg\\tree\\Btree3.png').convert_alpha(),
    g.image.load(f'src\\bg\\tree\\Btree4.png').convert_alpha()
]

water = [
    g.image.load(f'src\\bg\\water\\water1.png').convert_alpha(),
    g.image.load(f'src\\bg\\water\\water2.png').convert_alpha(),
    g.image.load(f'src\\bg\\water\\water3.png').convert_alpha(),
    g.image.load(f'src\\bg\\water\\water4.png').convert_alpha()
]

bg = BG(tiles,[trees,water],SET.SCW,SET.SCH)
clock = g.time.Clock()
while fl_running:
    for event in g.event.get():
        if event.type == g.KEYDOWN:
            if event.key == g.K_ESCAPE:
                fl_running = False
    bg.draw(sc)
    g.display.update()
    clock.tick(FPS)
exit()