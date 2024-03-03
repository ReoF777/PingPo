import pygame
from pygame.locals import *
from consts import *
class Paddle:
    """
    パドルのクラスです。パドルの位置データを保持します。
    """
    def __init__(self, Pos, surface): # コンストラクタ(初期位置を設定します。)
        self.x = Pos[0]
        self.y = Pos[1]
        self.serface = surface

    def setPos(self, x, y):   # 位置設定メソッド
        self.x = x
        self.y = y
    
    def moveRight(self):
        self.x = self.x + 1.5
    
    def moveLeft(self):
        self.x = self.x - 1.5
    
    def getPos(self):
        return (self.x, self.y)
    
    def drawSelf(self):
        rect = Rect(self.x, self.y, PADDLE_SIZE[0], PADDLE_SIZE[1])
        rect.center = (self.x, self.y)
        pygame.draw.rect(self.serface, (0,150,150), rect, 0)