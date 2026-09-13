import pygame as pg
pg.display.init()

scr = pg.display.Info()
scrW = scr.current_w
scrH = scr.current_h
resolution = (scrW, scrH)
print("width:",scrW)
print("height:",scrH)

def ux(percentage):
    return int(scrW * percentage / 1000)

def uy(percentage):
    return int(scrH * percentage / 1000)

dt = 0
fps = 240
isGameRunning = True
numRows = 3
maxTurns = numRows * numRows

board =  uy(600)
gap = (board // numRows) // 10



currentTurnCount = 0

idPlayer = 1
idWinner = 2

wins = [0,0]

dictCells = {"rect" : {}, "value" : {}}

#dictCells["rect"][key]
#dictCells["value"][key]

#for key in dictCells["rect"]:
#        rect_value = dictGrid["rect"][key]
#        state_value = dictGrid["value"][key]d


scaleRects = {
    "board": board, # Single value for a perfect square
    "gap": gap, # Single value for a perfect square
    "cell": (board - (gap * (numRows + 1))) // numRows # Tuple (width, height) for a rectangle
}

def coordCell(var):
    return gap + (scaleRects["cell"] + gap) * var

coords = {
    "board": (ux(500) - (scaleRects["board"] / 2), uy(500) - (scaleRects["board"] / 2)), #
    "cell": lambda w, h: (coordCell(w), coordCell(h)),# lambda delays the calculation until you actually pass w and h to it
}

def drawBoard(screen):
    dictCells["rect"]["board"] = pg.draw.rect(
        screen,
        "green",
        (
            int(coords["board"][0]),
            int(coords["board"][1]),
            scaleRects["board"],
            scaleRects["board"],
        ),
    )
    for h in range(numRows):
        for w in range(numRows):
            key = f"{h}{w}"
            
            # 1. Unpack your X and Y offsets directly from your lambda function
            cell_offset_x, cell_offset_y = coords["cell"](w, h)
            
            # 2. Add them to the board's starting position
            dictCells["rect"][key] = pg.draw.rect(
                screen,
                "white",
                (
                    int(coords["board"][0] + cell_offset_x),
                    int(coords["board"][1] + cell_offset_y),
                    scaleRects["cell"],
                    scaleRects["cell"]
                )
            )



    
#scaleRects["cell"] = 0


