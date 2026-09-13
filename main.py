import pygame as pg
from libs.config import dt, fps, isGameRunning, numRows, dictGrid, resolution,ux,uy

screen = pg.display.set_mode(resolution,pg.FULLSCREEN)

clock = pg.time.Clock()

while isGameRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameRunning = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isGameRunning = False
    screen.fill('black')
    pg.draw.rect(
                screen,
                "white",
                (ux(500),
                 uy(500),
                    50,50
                ))

    pg.display.flip()
    dt = clock.tick(240) / 1000

pg.quit()