from pygame import Rect
from settings import *
class Card:
    def __init__(self, x, y, shape, color):
        self.shape = shape
        self.color = color
        self.turnedUp = False
        self.rect = Rect(x, y, BOXSIZE, BOXSIZE)
        self.highlighted = False
        self.timer = 0
        self.matched = False
        
    def draw(self, screen):
        if self.turnedUp == False:
            if not self.highlighted:
                screen.draw.filled_rect(self.rect, BOXCOLOR)
            else:
                screen.draw.filled_rect(self.rect, HIGHLIGHTCOLOR)
        else:
            screen.draw.filled_rect(self.rect, LIGHTBGCOLOR)
            shape = self.shape
            color = self.color
            x = self.rect.x
            y = self.rect.y
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