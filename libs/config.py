from pygame import display
display.init()

scr = display.Info()
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
#scaleRects["cell"] = 0

scales = {"rect" : {}, "value" : {}}

