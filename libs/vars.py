import pygame as pg
pg.display.init()

# Store the display size once so the board can scale correctly on any screen.
scr = pg.display.Info()
scrW = scr.current_w
scrH = scr.current_h
resolution = (scrW, scrH)

print("width:", scrW)
print("height:", scrH)


def ux(percentage):
    return int(scrW * percentage / 1000)


def uy(percentage):
    return int(scrH * percentage / 1000)


# Core game state used throughout the app.
dt = 0
fps = 240
isGameRunning = True
numRows = 12
maxTurns = numRows * numRows
numTurns = 0
idPlayer = 1
idWinner = 2
wins = [0, 0]

# Asset references loaded when the game starts.
xImage = None
oImage = None
xImage_white = None
oImage_white = None
rectBoard = None

# Board sizing is computed from the screen size to keep the layout responsive.
scale_board = uy(600)
scale_gap = max(1, (scale_board // numRows) // 10)
scale_cell = (scale_board - (scale_gap * (numRows + 1))) // numRows
scale_text_ = None


coords_board = (ux(500) - (scale_board // 2),
                uy(500) - (scale_board // 2))

dictCells = {"rect": {}, "value": {}}
