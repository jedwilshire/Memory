from settings import *
import pygame
from random import shuffle

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set window caption
pygame.display.set_caption('MEMORY')

def makeBoard():
    board_maker = []
    for shape in ALLSHAPES:
        for color in ALLCOLORS:
            board_maker.append([shape, color])
            board_maker.append([shape, color])
    shuffle(board_maker)
    index = 0
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            x = GAP + col * (GAP + BOXSIZE)
            y = GAP + row * (GAP + BOXSIZE)
            shape = board_maker[index][0]
            color = board_maker[index][1]
            board[row][col] = makeCard(x, y, shape, color)
            index += 1
    
def draw():
    screen.fill(BGCOLOR)
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            card = board[row][col]
            if card.turnedUp == False:
                pygame.draw.rect(screen, BOXCOLOR, card.rect)
            else:
                screen.blit(card.back, card.rect)
    pygame.display.flip()
    
def onMouseDown(x, y):
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            if board[row][col].rect.collidepoint((x, y)):
                board[row][col].turnedUp = not board[row][col].turnedUp

 
def onMouseMove(x, y):
    pass
def update():
    pass
            
def makeList(row, col):
    board = []
    for i in range(row):
        board.append([])
        for k in range(col):
            board[i].append(None)
    return board

def mainloop():
    running = True
    clock = pygame.time.Clock()
    while running:
        # event loop
        update()
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                onMouseMove(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                onMouseDown(event.pos[0], event.pos[1])
        clock.tick(FPS)

def makeCard(x, y, shape, color):
    card = pygame.sprite.Sprite()
    card.shape = shape
    card.color = color
    card.turnedUp = False
    card.rect = pygame.Rect(x, y, BOXSIZE, BOXSIZE)
    card.back = pygame.Surface((BOXSIZE, BOXSIZE))
    card.back.fill(LIGHTBGCOLOR)
    if shape == DONUT:
        pygame.draw.circle(card.back, color, (BOXSIZE // 2, BOXSIZE // 2), BOXSIZE//2, width = 10)
    elif shape == SQUARE:
        rect = pygame.Rect(BOXSIZE * .2, BOXSIZE * .2, BOXSIZE * .6, BOXSIZE * .6)
        pygame.draw.rect(card.back, color, rect)
    elif shape == CROSS:
        pygame.draw.line(card.back, color, (0, BOXSIZE // 2),
                         (BOXSIZE, BOXSIZE // 2), width = 2)
        pygame.draw.line(card.back, color, (BOXSIZE // 2, 0),
                         (BOXSIZE // 2, BOXSIZE), width = 4)
    elif shape == LINES:
        numLines = 10
        gap = BOXSIZE // numLines
        for i in range(1, numLines, 1):
            pygame.draw.line(card.back, color, (gap * i, 0),
                             (gap * i, BOXSIZE), width = 2)
    elif shape == DIAMOND:
        pygame.draw.line(card.back, color, (BOXSIZE // 2, 0),
                         (BOXSIZE, BOXSIZE // 2), width = 3)
        pygame.draw.line(card.back, color, (BOXSIZE, BOXSIZE // 2),
                         (BOXSIZE // 2, BOXSIZE), width = 3)
        pygame.draw.line(card.back, color, (BOXSIZE // 2, BOXSIZE),
                         (0, BOXSIZE // 2), width = 3)
        pygame.draw.line(card.back, color, (0, BOXSIZE // 2),
                         (BOXSIZE // 2, 0), width = 3)
    return card

board = makeList(BOARDHEIGHT, BOARDWIDTH)
makeBoard()
pygame.init()
mainloop()




