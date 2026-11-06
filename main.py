import pygame as g

import value_control.settings as SET
FPS = 60
g.init()
sc = g.display.set_mode((SET.SCW, SET.SCH)) # init. display

clock = g.time.Clock()
while 1:
    for event in g.event.get():
        if event.type == g.KEYDOWN:
            if event.key == g.K_ESCAPE:
                exit()
    g.display.update()
    clock.tick(FPS)