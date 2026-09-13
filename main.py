import pygame as pg
from libs.config import (
    dt, fps, isGameRunning, numRows, dictCells, resolution,
    mark, ux, uy, drawBoard, initBoard, drawMarks, load_assets
)

screen = pg.display.set_mode(resolution, pg.FULLSCREEN)
load_assets()

clock = pg.time.Clock()
initBoard()
while isGameRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameRunning = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isGameRunning = False

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            posMouse = pg.mouse.get_pos()
            for key, rect in dictCells["rect"].items():
                if key != "board" and rect.collidepoint(posMouse):
                    mark(key)
                    break

    screen.fill('black')
    drawBoard(screen)
    drawMarks(screen)
    pg.display.flip()
    dt = clock.tick(240) / 1000

pg.quit()