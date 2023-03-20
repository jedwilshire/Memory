from settings import *
from sprites import *
import pygame
from random import shuffle
# Global variables
cards_selected = [None, None]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set window caption
pygame.display.set_caption('MEMORY')

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
            board[row][col] = make_card(x, y, shape, color)
            index += 1
    
def draw():
    screen.fill(BGCOLOR)
    for row in range(BOARDHEIGHT):
        for col in range(BOARDWIDTH):
            card = board[row][col]
            if card.turnedUp == False:
                if not card.highlighted:
                    pygame.draw.rect(screen, BOXCOLOR, card.rect)
                else:
                    pygame.draw.rect(screen, HIGHLIGHTCOLOR, card.rect)
            else:
                screen.blit(card.back, card.rect)
    pygame.display.flip()
    
def on_mouse_down(pos):
    for y in range(BOARDHEIGHT):
        for x in range(BOARDWIDTH):
            card = board[y][x]
            if card.rect.collidepoint(pos) and card != cards_selected[0]:
                card.turnedUp = True
                if cards_selected[0] == None:
                    cards_selected[0]  = card
                else:
                    cards_selected[1]  = card
                    firstCard, secondCard = cards_selected[0], cards_selected[1] # syntatic sugar
                    if (firstCard.shape != secondCard.shape or
                        firstCard.color != secondCard.color):
                        firstCard.timer = 60
                        secondCard.timer = 60
                    else:
                        firstCard.matched = True
                        secondCard.matched = True
                    cards_selected[0] = None
                    cards_selected[1] = None
                    
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
            elif not card.matched and not card == cards_selected[0]: # turn face down if not selected and not first card selected
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

def make_card(x, y, shape, color):
    card = pygame.sprite.Sprite()
    card.shape = shape
    card.color = color
    card.turnedUp = False
    card.rect = pygame.Rect(x, y, BOXSIZE, BOXSIZE)
    card.highlighted = False
    card.timer = 0
    card.matched = False
    card.back = pygame.Surface((BOXSIZE, BOXSIZE))
    card.back.fill(LIGHTBGCOLOR)
    if shape == DONUT:
        cx = BOXSIZE // 2
        cy = BOXSIZE // 2
        pygame.draw.circle(card.back, color, (cx, cy), BOXSIZE * .40)
        pygame.draw.circle(card.back, LIGHTBGCOLOR, (cx, cy), BOXSIZE * .20)
    elif shape == SQUARE:
        rect = Rect(BOXSIZE * .2, BOXSIZE * .2, BOXSIZE * .6, BOXSIZE * .6)
        pygame.draw.rect(card.back, color, rect)
    elif shape == CROSS:
        pygame.draw.line(card.back, color, (0, BOXSIZE // 2),
                         (BOXSIZE, BOXSIZE // 2))
        pygame.draw.line(card.back, color, (BOXSIZE // 2, 0),
                         (BOXSIZE // 2, BOXSIZE))
    elif shape == LINES:
        numLines = 10
        gap = BOXSIZE // numLines
        for i in range(1, numLines, 1):
            pygame.draw.line(card.back, color, (gap * i, 0),
                             (gap * i, BOXSIZE))
    elif shape == DIAMOND:
        pygame.draw.line(card.back, color, (BOXSIZE // 2, 0),
                         (BOXSIZE, BOXSIZE // 2))
        pygame.draw.line(card.back, color, (BOXSIZE, BOXSIZE // 2),
                         (BOXSIZE // 2, BOXSIZE))
        pygame.draw.line(card.back, color, (BOXSIZE // 2, BOXSIZE),
                         (0, BOXSIZE // 2))
        pygame.draw.line(card.back, color, (0, BOXSIZE // 2),
                         (BOXSIZE // 2, 0))
    return card

board = makeList(BOARDHEIGHT, BOARDWIDTH)
make_board()
pygame.init()
mainloop()




