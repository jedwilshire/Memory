# from pygame import Rect, Surface
# import pygame
# from settings import *
# class Card:
#     def __init__(self, x, y, shape, color):
#         self.shape = shape
#         self.color = color
#         self.turnedUp = False
#         self.rect = Rect(x, y, BOXSIZE, BOXSIZE)
#         self.highlighted = False
#         self.timer = 0
#         self.matched = False
#         self.back = self.makeBack()
#         
#     def makeBack(self):
#         back = Surface((BOXSIZE, BOXSIZE))
#         back.fill(LIGHTBGCOLOR)
#         shape = self.shape
#         color = self.color
#         x = 0
#         y = 0
#         if shape == DONUT:
#             cx = x + BOXSIZE // 2
#             cy = y + BOXSIZE // 2
#             pygame.draw.circle(back, color, (cx, cy), BOXSIZE * .40)
#             pygame.draw.circle(back, LIGHTBGCOLOR, (cx, cy), BOXSIZE * .20)
#         elif shape == SQUARE:
#             rect = Rect(x + BOXSIZE * .2, y + BOXSIZE * .2, BOXSIZE * .6, BOXSIZE * .6)
#             pygame.draw.rect(back, color, rect)
#         elif shape == CROSS:
#             pygame.draw.line(back, color, (x, y + BOXSIZE // 2),
#                              (x + BOXSIZE, y + BOXSIZE // 2))
#             pygame.draw.line(back, color, (x + BOXSIZE // 2, y),
#                              (x + BOXSIZE // 2, y + BOXSIZE))
#         elif shape == LINES:
#             numLines = 10
#             gap = BOXSIZE // numLines
#             for i in range(1, numLines, 1):
#                 pygame.draw.line(back, color, (x + gap * i, y),
#                                  (x + gap * i, y + BOXSIZE))
#         elif shape == DIAMOND:
#             pygame.draw.line(back, color, (x + BOXSIZE // 2, y),
#                              (x + BOXSIZE, y + BOXSIZE // 2))
#             pygame.draw.line(back, color, (x + BOXSIZE, y + BOXSIZE // 2),
#                              (x + BOXSIZE // 2, y + BOXSIZE))
#             pygame.draw.line(back, color, (x + BOXSIZE // 2, y + BOXSIZE),
#                              (x, y + BOXSIZE // 2))
#             pygame.draw.line(back, color, (x, y + BOXSIZE // 2),
#                              (x + BOXSIZE // 2, y))
#         return back
#     
#     def draw(self, screen):
#         if self.turnedUp == False:
#             if not self.highlighted:
#                 pygame.draw.rect(screen, BOXCOLOR, self.rect)
#             else:
#                 pygame.draw.rect(screen, HIGHLIGHTCOLOR, self.rect)
#         else:
#             screen.blit(self.back, self.rect)
#             