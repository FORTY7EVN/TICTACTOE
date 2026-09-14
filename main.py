import pygame as pg
from libs.vars import (
    resolution, fps,
    dictCells,
    isGameRunning,
)
from libs.colors import *
from libs.config import (initBoard, draw, mark, load_assets)

# Start the game window and prepare all image assets before drawing.
screen = pg.display.set_mode(resolution, pg.FULLSCREEN)
load_assets()

clock = pg.time.Clock()
initBoard()

# Main game loop: process input, update board state, and render every frame.
while isGameRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isGameRunning = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                isGameRunning = False

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # Use the click position from the event to avoid stale mouse data
            # when the game is running in fullscreen mode.
            posMouse = event.pos
            for key, rect in dictCells["rect"].items():
                if rect.collidepoint(posMouse):
                    mark(key)
                    break

    screen.fill(color_background)
    draw(screen)
    pg.display.flip()
    clock.tick(fps)

pg.quit()
