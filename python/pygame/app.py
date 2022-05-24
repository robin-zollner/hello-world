from cmath import sqrt
from re import T
import sys, pygame
from turtle import st

class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
x1, y1 = 200, 25
x2, y2 = 180 , 55
x3, y3 = 220, 55

def side_len(x1, y1, x2, y2):
    xdif2 = (x2 - x1)**2
    ydif2 = (y2 - y1)**2
    ln = sqrt(xdif2 + ydif2)
    return ln.real

def get30(x1=0, y1=0, len=1):
          

def toStr(arr):
    for a in arr:
        a = str(a)
    return arr
sidelen = [side1len, side2len, side3len] = [side_len(x1, y1, x2, y2), side_len(x1, y1, x3, y3), side_len(x2, y2, x3, y3)]

sidelenSTR = toStr(sidelen)

print(sidelen, side1len, side2len, side3len, sep='*\n', end='**\n\n')

font = pygame.font.SysFont(None, 20)
img1 = font.render(str(side1len), True, Colors.MAGENTA)

run = True

while run:
    textloc = textloc1, textloc2, textloc3 = (tx1, ty1), (tx2, ty2), (tx3, ty3) = (width/2, height-150), (width/2, height-100),(width/2, height-50) 
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            screen.fill(Colors.BLACK)
            pygame.draw.rect(screen, Colors.GREEN, pygame.Rect(30, 30, 60, 60))
            pygame.draw.circle(screen, Colors.CYAN, [width/2, height/2], 20)
            pygame.draw.polygon(screen, Colors.RED, points=[(x1, y1), (x2, y2), (x3, y3)])
            screen.blit(img1, textloc1)
    pygame.display.flip()