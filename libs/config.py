import pygame as pg
from libs.colors import *
from libs.vars import *


def coordCell(index):
    board_padding = (scale.board - (scale.cell * setting.rows +
                     scale.gap * (setting.rows - 1))) // 2
    return board_padding + (scale.cell + scale.gap) * index


def load_assets():
    # load images
    asset.xImage = pg.image.load('images/X.png').convert_alpha()
    asset.oImage = pg.image.load('images/O.png').convert_alpha()

    # transform images
    asset.xImage = pg.transform.scale(
        asset.xImage, (scale.mark, scale.mark))
    asset.oImage = pg.transform.scale(
        asset.oImage, (scale.mark, scale.mark))

    # initialize overlay images
    asset.xImage_white = asset.xImage.copy()
    asset.oImage_white = asset.oImage.copy()

    # white fill to overlay images
    asset.xImage_white.fill((255, 255, 255), special_flags=pg.BLEND_RGB_MAX)
    asset.oImage_white.fill((255, 255, 255), special_flags=pg.BLEND_RGB_MAX)

    # roboto_surface
    asset.roboto_surface = font.scaled.roboto.regular.render(
        "TIC TAC TOE", True, color_cell)

    # width of title text
    asset.roboto_w = asset.roboto_surface.get_width()

    # i dont know whats happening here, I forgot
    asset.roboto_txt_rect = asset.roboto_surface.get_rect()


def initBoard():
    asset.rectBoard = pg.Rect(
        coord.board.x,
        coord.board.y,
        scale.board,
        scale.board,
    )

    for h in range(setting.rows):
        for w in range(setting.rows):
            key = (h, w)

            cell_offset_x = coordCell(w)
            cell_offset_y = coordCell(h)

            x = int(coord.board.x + cell_offset_x)
            y = int(coord.board.y + cell_offset_y)

            dictCells["rect"][key] = pg.Rect(x, y, scale.cell, scale.cell)
            dictCells["value"][key] = 0


def drawHover(screen, rect):
    pg.draw.rect(screen, color_cell_hover, rect, border_radius=(scale.gap // 2))

    position = (rect.x + scale.gap // 2, rect.y + scale.gap // 2)
    hover_image = (
        asset.xImage_white if setting.player == 1 else asset.oImage_white
    )
    hover_image.set_alpha(25)
    screen.blit(hover_image, position)


def drawCell(screen, rect, key, mouse_position):
    is_hovered = rect.collidepoint(mouse_position)
    cell_color = color_cell_hover if is_hovered else color_cell
    pg.draw.rect(screen, cell_color, rect, border_radius=(scale.gap // 2))

    position = (rect.x + scale.gap // 2, rect.y + scale.gap // 2)
    value = dictCells["value"][key]
    if value == 0:
        if is_hovered:
            drawHover(screen, rect)
        return

    image = asset.xImage if value == 1 else asset.oImage
    screen.blit(image, position)


def drawTitle(screen):
    title_rect = pg.Rect(
        0,
        0,
        asset.roboto_w + scale.cell,
        scale.cell + scale.cell // 5,
    )
    title_rect.bottomleft = (
        asset.rectBoard.left,
        asset.rectBoard.top - scale.gap,
    )
    pg.draw.rect(screen, color_board, title_rect, border_radius=scale.gap)

    if asset.roboto_surface is not None:
        asset.roboto_txt_rect = asset.roboto_surface.get_rect(
            center=title_rect.center
        )
        screen.blit(asset.roboto_surface, asset.roboto_txt_rect)


def draw(screen):
    mouse_position = pg.mouse.get_pos()
    pg.draw.rect(
        screen,
        color_board,
        asset.rectBoard,
        border_radius=scale.gap,
    )
    for key, rect in dictCells["rect"].items():
        drawCell(screen, rect, key, mouse_position)
    drawTitle(screen)


def changePlayer():
    setting.player = -1 if setting.player == 1 else 1


def mark(key):
    if dictCells["value"][key] != 0:
        return

    dictCells["value"][key] = setting.player
    print(key)
    changePlayer()
