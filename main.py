import pygame as pg
from libs.config import dt, fps, isGameRunning, numRows, dictCells, resolution,ux,uy,drawBoard

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
    drawBoard(screen)

    pg.display.flip()
    dt = clock.tick(240) / 1000

pg.quit()