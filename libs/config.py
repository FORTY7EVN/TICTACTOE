import pygame as pg
from libs.colors import *
from libs.vars import (
    numRows, idPlayer, xImage, oImage,
    dictCells,
    scale_board, scale_gap, scale_cell,
    coords_board,
    xImage_white, oImage_white)


# Convert a logical cell index into screen-space coordinates while centering
# the leftover spacing around the whole grid instead of biasing it to the top/left.
def coordCell(index):
    board_padding = (scale_board - (scale_cell * numRows +
                     scale_gap * (numRows - 1))) // 2
    return board_padding + (scale_cell + scale_gap) * index

# Load and resize the X/O images once so they can be reused in drawing.


def load_assets():
    global xImage, oImage, xImage_white, oImage_white
    xImage = pg.image.load('images/X.png').convert_alpha()
    oImage = pg.image.load('images/O.png').convert_alpha()
    xImage = pg.transform.scale(
        xImage, (scale_cell - scale_gap, scale_cell - scale_gap))
    oImage = pg.transform.scale(
        oImage, (scale_cell - scale_gap, scale_cell - scale_gap))
    xImage_white = xImage.copy()
    xImage_white.fill((255, 255, 255), special_flags=pg.BLEND_RGB_MAX)
    oImage_white = oImage.copy()
    oImage_white.fill((255, 255, 255), special_flags=pg.BLEND_RGB_MAX)


# Create the board rectangles and default cell values before gameplay starts.
def initBoard():
    for h in range(numRows):
        for w in range(numRows):
            key = (h, w)

            cell_offset_x = coordCell(w)
            cell_offset_y = coordCell(h)

            x = int(coords_board[0] + cell_offset_x)
            y = int(coords_board[1] + cell_offset_y)

            dictCells["rect"][key] = pg.Rect(x, y, scale_cell, scale_cell)
            dictCells["value"][key] = 0


# Draw the board, hover effects, and the placed symbols for each cell.
def draw(screen):
    mouse_position = pg.mouse.get_pos()

    pg.draw.rect(
        screen,
        color_board,
        (
            int(coords_board[0]),
            int(coords_board[1]),
            scale_board,
            scale_board,
        ),
    )
    for key, rect in dictCells["rect"].items():
        cell_color = (
            color_cell_hover
            if rect.collidepoint(mouse_position)
            else color_cell
        )
        pg.draw.rect(screen, cell_color, rect, border_radius=(scale_gap//2))

        position = (rect.x + scale_gap // 2, rect.y + scale_gap // 2)
        value = dictCells["value"][key]
        if value == 0:
            if rect.collidepoint(mouse_position):
                hover_image = (xImage_white if idPlayer ==
                               1 else oImage_white)
                hover_image.set_alpha(25)
                screen.blit(hover_image, position)
            continue

        image = xImage if value == 1 else oImage
        screen.blit(image, position)


# Place a mark only if the target cell is empty and switch turns.
def mark(key):
    global idPlayer

    if dictCells["value"][key] != 0:
        return

    dictCells["value"][key] = idPlayer
    print(key)
    idPlayer = -1 if idPlayer == 1 else 1
