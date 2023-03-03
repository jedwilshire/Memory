import pgzrun
from settings import *
from random import shuffle
board = []
selected = [-1, -1]
def make_board():
    for shape in ALLSHAPES:
        for color in ALLCOLORS:
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
                elif shape == CROSS:
                    screen.draw.line((x, y + BOXSIZE // 2),
                                     (x + BOXSIZE, y + BOXSIZE // 2), color)
                    screen.draw.line((x + BOXSIZE // 2, y),
                                     (x + BOXSIZE // 2, y + BOXSIZE), color)
                elif shape == LINES:
                    numLines = 10
                    gap = BOXSIZE // numLines
                    for i in range(1, numLines, 1):
                        screen.draw.line((x + gap * i, y),
                                         (x + gap * i, y + BOXSIZE), color)
                elif shape == DIAMOND:
                    screen.draw.line((x + BOXSIZE // 2, y),
                                     (x + BOXSIZE, y + BOXSIZE // 2),
                                     color)
                    screen.draw.line((x + BOXSIZE, y + BOXSIZE // 2),
                                     (x + BOXSIZE // 2, y + BOXSIZE),
                                     color)
                    screen.draw.line((x + BOXSIZE // 2, y + BOXSIZE),
                                     (x, y + BOXSIZE // 2),
                                     color)
                    screen.draw.line((x, y + BOXSIZE // 2),
                                     (x + BOXSIZE // 2, y),
                                     color)
            x += BOXSIZE + GAPSIZE
            index += 1
        y += BOXSIZE + GAPSIZE
        x = GAPSIZE
       
def update():
    pass
def on_mouse_down(pos):
    x = (pos[0] - GAPSIZE) // (BOXSIZE + GAPSIZE)
    y = (pos[1] - GAPSIZE) // (BOXSIZE + GAPSIZE)
    if (x >= 0 and y >= 0 and selected[0] == -1):
        board[y * BOARDWIDTH + x][2] = True 
        selected[0] = x
        selected[1] = y
    elif (x >= 0 and y >= 0):
        board[y * BOARDWIDTH + x][2] = True
        previous_shape = board[selected[1] * BOARDWIDTH + selected[0]][0]
        previous_color = board[selected[1] * BOARDWIDTH + selected[0]][1]
        shape = board[y * BOARDWIDTH + x][0]
        color = board[y * BOARDWIDTH + x][1]
        if previous_shape != shape or previous_color != color:
            #add animation
            
            board[y * BOARDWIDTH + x][2] = False
            board[selected[1] * BOARDWIDTH + selected[0]][2] = False
        selected[0] = -1
        selected[1] = -1
            
            
make_board()
pgzrun.go()




