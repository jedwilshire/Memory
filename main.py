import pgzrun
from settings import *
from random import shuffle
board = []

def make_board():
    for shape in ALLSHAPES:
        for color in ALLCOLORS:
            if shape == SQUARE:
                board.append([shape, color, True])
                board.append([shape, color, True])
            else:
                board.append([shape, color, False])
                board.append([shape, color, False])
    shuffle(board)
def draw():
    screen.fill(BGCOLOR)
    index = 0
    x = GAPSIZE
    y = GAPSIZE
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            if board[index][2] == False:
                rect = Rect(x, y, BOXSIZE, BOXSIZE)
                screen.draw.filled_rect(rect, BOXCOLOR)
            else:
                rect = Rect(x, y, BOXSIZE, BOXSIZE)
                screen.draw.filled_rect(rect, LIGHTBGCOLOR)
                shape = board[index][0]
                color = board[index][1]
                if shape == DONUT:
                    cx = x + BOXSIZE // 2
                    cy = y + BOXSIZE // 2
                    screen.draw.filled_circle((cx, cy), BOXSIZE * .40, color)
                    screen.draw.filled_circle((cx, cy), BOXSIZE * .20, LIGHTBGCOLOR)
                elif shape == SQUARE:
                    rect = Rect(x + BOXSIZE * .2, y + BOXSIZE * .2, BOXSIZE * .6, BOXSIZE * .6)
                    screen.draw.filled_rect(rect, color)
                
            x += BOXSIZE + GAPSIZE
            index += 1
        y += BOXSIZE + GAPSIZE
        x = GAPSIZE
       
def update():
    pass
make_board()
pgzrun.go()




