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

dt = 0 #delta time
fps = 240 #fps
isGameRunning = True #game state
numRows = 6 #number of rows
maxTurns = numRows * numRows #maxturns allowed
board =  uy(600) #only for scaleRects["board"]
gap = (board // numRows) // 10 #only for scaleRects["gap"]
currentTurnCount = 0 #turnscount
idPlayer = 1 #id current player
idWinner = 2 #id winner
wins = [0,0] #wins , 0 is for O and 1 is for X
dictCells = {"rect" : {}, "value" : {}} #dictionary to store rects and the values

#dictCells["rect"][key]
#dictCells["value"][key]
#scaleRects["cell"] = 0

#for key in dictCells["rect"]:
#        rect_value = dictGrid["rect"][key]
#        state_value = dictGrid["value"][key]


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

xImage = None
oImage = None


def load_assets():
    global xImage, oImage
    xImage = pg.image.load('images/X.png').convert_alpha()
    oImage = pg.image.load('images/O.png').convert_alpha()
    xImage = pg.transform.scale(xImage, (scaleRects["cell"] - scaleRects["gap"], scaleRects["cell"] - scaleRects["gap"]))
    oImage = pg.transform.scale(oImage, (scaleRects["cell"] - scaleRects["gap"], scaleRects["cell"] - scaleRects["gap"]))


# --- 1. INITIALIZATION (Run this ONCE before your game loop) ---
def initBoard():
    for h in range(numRows):
        for w in range(numRows):
            key = f"{h}{w}"
            
            # Unpack offsets directly from your lambda function
            cell_offset_x, cell_offset_y = coords["cell"](w, h)
            
            x = int(coords["board"][0] + cell_offset_x)
            y = int(coords["board"][1] + cell_offset_y)
            width = scaleRects["cell"]
            height = scaleRects["cell"]
            
            # Create and store the Pygame Rect object
            dictCells["rect"][key] = pg.Rect(x, y, width, height)
            
            # Initialize the game state (1 for X, -1 for O, and 0 for nothing)
            dictCells["value"][key] = 0

# --- 2. RENDERING (Run this EVERY FRAME inside your game loop) ---
def drawBoard(screen):
    # Draw the main green board background
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
    
    # Iterate through the grid and draw the pre-calculated Rects
    for h in range(numRows):
        for w in range(numRows):
            key = f"{h}{w}"
            
            # Draw each white cell using the saved Rect
            pg.draw.rect(screen, "white", dictCells["rect"][key])

def mark(key):
    global idPlayer

    if key not in dictCells["value"] or dictCells["value"][key] != 0: #breaks the func if key doesnt exist or value is not 0
        return

    dictCells["value"][key] = idPlayer
    print(key)
    idPlayer = -1 if idPlayer == 1 else 1

def drawMarks(screen):
    for key, value in dictCells["value"].items():
        if value == 0:
            continue

        rect = dictCells["rect"][key]
        x = rect.x + scaleRects["gap"] // 2
        y = rect.y + scaleRects["gap"] // 2

        if value == 1:
            screen.blit(xImage, (x, y))
        elif value == -1:
            screen.blit(oImage, (x, y))
