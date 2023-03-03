from settings import *
from sprites import *
import pygame
from random import shuffle
firstCard = None
secondCard = None
screen = pygame.display.set_mode((WIDTH, HEIGHT))
def make_board():
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
            board[row][col] = Card(x, y, shape, color)
            index += 1
    
def draw():
    screen.fill(BGCOLOR)
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            card = board[row][col]
            card.draw(screen)
    pygame.display.flip()
    
def on_mouse_down(pos):
    global firstCard, secondCard
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH):
            card = board[y][x]
            if card.rect.collidepoint(pos) and card != firstCard:
                card.turnedUp = True
                if firstCard == None:
                    firstCard = card
                else:
                    secondCard = card
                    if (firstCard.shape != secondCard.shape or
                        firstCard.color != secondCard.color):
                        firstCard.timer = 60
                        secondCard.timer = 60
                    else:
                        firstCard.matched = True
                        secondCard.matched = True
                    firstCard = None
                    secondCard = None
                    
def on_mouse_move(pos):
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH):
            card = board[y][x]
            if card.rect.collidepoint(pos):
                card.highlighted = True
            else:
                card.highlighted = False
def update():
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH):
            card = board[y][x]
            if card.timer > 0:
                card.timer -= 1
            elif not card.matched and not card == firstCard:
                card.turnedUp = False
            
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
                    on_mouse_move(event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    on_mouse_down(event.pos)
            clock.tick(FPS)
            
board = makeList(BOARDHEIGHT, BOARDWIDTH)
make_board()
pygame.init()
mainloop()




