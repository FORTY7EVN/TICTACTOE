import pygame as pg
from libs.colors import *
from libs.vars import *

# Convert a logical cell index into screen-space coordinates while centering
# the leftover spacing around the whole grid instead of biasing it to the top/left.


def coordCell(index):
    board_padding = (scale.board - (scale.cell * setting.rows +
                     scale.gap * (setting.rows - 1))) // 2
    return board_padding + (scale.cell + scale.gap) * index

# Load and resize the X/O images once so they can be reused in drawing.


def load_assets():
    asset.xImage = pg.image.load('images/X.png').convert_alpha()
    asset.oImage = pg.image.load('images/O.png').convert_alpha()
    asset.xImage = pg.transform.scale(
        asset.xImage, (scale.mark, scale.mark))
    asset.oImage = pg.transform.scale(
        asset.oImage, (scale.mark, scale.mark))
    asset.xImage_white = asset.xImage.copy()
    asset.xImage_white.fill((255, 255, 255), special_flags=pg.BLEND_RGB_MAX)
    asset.oImage_white = asset.oImage.copy()
    asset.oImage_white.fill((255, 255, 255), special_flags=pg.BLEND_RGB_MAX)

    asset.roboto_surface = font.scaled.roboto.regular.render(
        "TIC TAC TOE", True, color_cell)
    asset.roboto_w = asset.roboto_surface.get_width()
    asset.roboto_h = asset.roboto_surface.get_height()
    asset.roboto_txt_rect = asset.roboto_surface.get_rect()

# Create the board rectangles and default cell values before gameplay starts.


def initBoard():
    for h in range(setting.rows):
        for w in range(setting.rows):
            key = (h, w)

            cell_offset_x = coordCell(w)
            cell_offset_y = coordCell(h)

            x = int(coord.board.x + cell_offset_x)
            y = int(coord.board.y + cell_offset_y)

            dictCells["rect"][key] = pg.Rect(x, y, scale.cell, scale.cell)
            dictCells["value"][key] = 0

# Draw the board, hover effects, and the placed symbols for each cell.


def draw(screen):
    mouse_position = pg.mouse.get_pos()

    rect_board = pg.draw.rect(
        screen,
        color_board,
        (
            coord.board.x,
            coord.board.y,
            scale.board,
            scale.board,
        ),
        border_radius=scale.gap,
    )
    for key, rect in dictCells["rect"].items():
        cell_color = (
            color_cell_hover
            if rect.collidepoint(mouse_position)
            else color_cell
        )
        pg.draw.rect(screen, cell_color, rect, border_radius=(scale.gap // 2))

        position = (rect.x + scale.gap // 2, rect.y + scale.gap // 2)
        value = dictCells["value"][key]
        if value == 0:
            if rect.collidepoint(mouse_position):
                hover_image = (asset.xImage_white
                               if setting.player == 1 else asset.oImage_white)
                hover_image.set_alpha(25)
                screen.blit(hover_image, position)
            continue

        image = asset.xImage if value == 1 else asset.oImage
        screen.blit(image, position)
    title_rect = pg.Rect(
        0,
        0,
        asset.roboto_w + scale.cell,
        scale.cell + scale.cell//5,
    )
    title_rect.bottomleft = (rect_board.left, rect_board.top - scale.gap)
    pg.draw.rect(screen, color_board, title_rect, border_radius=scale.gap)

    if asset.roboto_surface is not None and asset.roboto_txt_rect is not None:
        asset.roboto_txt_rect = asset.roboto_surface.get_rect(
            center=title_rect.center)
        screen.blit(asset.roboto_surface, asset.roboto_txt_rect)


# Place a mark only if the target cell is empty and switch turns.
def mark(key):
    if dictCells["value"][key] != 0:
        return

    dictCells["value"][key] = setting.player
    print(key)
    setting.player = -1 if setting.player == 1 else 1
