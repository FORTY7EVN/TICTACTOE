from box import Box
import pygame as pg

pg.display.init()
pg.font.init()

# Store the display size once so the board can scale correctly on any screen.
scr = pg.display.Info()
display = Box({"scrW": scr.current_w, "scrH": scr.current_h})


# ===================================================================
rows = 12
max_turns = rows * rows
# ===================================================================

setting = Box(
    {
        "dt": 0, "fps": 240,
        "rows": rows, "max_turns": max_turns, "turns": 0,
        "player": 1, "winner": 2, "wins": [0, 0],
        "isGameRunning": True
    }
)


def ux(percentage):
    return int(display.scrW * percentage / 1000)


def uy(percentage):
    return int(display.scrH * percentage / 1000)


# ===================================================================
scale_board = uy(600)
scale_gap = max(1, (scale_board // setting.rows) // 10)
scale_cell = (scale_board - (scale_gap * (setting.rows + 1))) // setting.rows
# ===================================================================

asset = Box(
    {
        "xImage": None,
        "oImage": None,
        "xImage_white": None,
        "oImage_white": None,
        "rectBoard": None,
        "roboto_surface": None,
        "roboto_txt_rect": None,
        "roboto_w": None,
        "roboto_h": None,
    }
)
# Asset references loaded when the game starts.


scale = Box(
    {
        "board": uy(600),
        "gap": max(1, (scale_board // setting.rows) // 10),
        "cell": (scale_board - (scale_gap * (setting.rows + 1))) // setting.rows,
        "mark": scale_cell - scale_gap,
        "text": scale_cell - scale_gap
    })

coord = Box(
    {
        "board": {
            "x": ux(500) - (scale.board // 2),
            "y": uy(500) - (scale.board // 2)}
    })

path = Box(
    {
        "font": {
            "roboto": {
                "regular": "fonts/roboto/static/RobotoMono-Regular.ttf",
                "bold": "fonts/roboto/static/RobotoMono-Bold.ttf",
                "italic": "fonts/roboto/static/RobotoMono-Italic.ttf"
            }
        }
    }
)

font = Box(
    {
        "scaled": {
            "roboto": {
                "regular": pg.font.Font(path.font.roboto.regular, scale.text),
                "bold": pg.font.Font(path.font.roboto.bold, scale.text),
                "italic": pg.font.Font(path.font.roboto.italic, scale.text)
            }
        }
    }
)

# roboto_regular_scaled = pg.font.Font(font_regular_path, scale_text)
# roboto_bold_scaled = pg.font.Font(font_bold_path, scale_text)
# roboto_italic_scaled = pg.font.Font(font_italic_path, scale_text)

dictCells = {"rect": {}, "value": {}}
