import math
import pygame
from consts import *

class Ball:
    """
    ボールのクラスです。ボールの位置データを保持します。
    """
    def __init__(self, Pos, surface): # コンストラクタ(初期位置を設定します。)
        self.x = Pos[0]
        self.y = Pos[1]
        self.vX = 0
        self.vY = 20
        self.surface = surface
    
    def movePos(self):        # 移動メソッド
        if self.x > WINDOW_SIZE[0] or self.x < 0:
            self.vX = self.vX * -1

        if self.y > WINDOW_SIZE[1] or self.y < 0:
            self.vY = self.vY * -1
        
        self.x = self.x + self.vX
        self.y = self.y + self.vY
    
    def getPos(self):             # 位置取得メソッド
        return (self.x, self.y)
    
    def PaddleCollisionProc(self, paddlePos): # ボールパドル衝突処理メソッド(ボールを衝突したパドルの位置に応じて弾き飛ばします)
        # パドルから見たボールの相対位置に応じて処理を実行
        if(self.vY <= 0):                                    # ｙ方向の速度が負の場合
            return
        elif(abs(paddlePos[0]-self.x)< PADDLE_SIZE[0]/8):     # パドルの真ん中付近に衝突した場合
            absSpeed = math.sqrt(self.vX**2 + self.vY**2)
            self.vX = absSpeed * math.cos(math.radians(90))
            self.vY = absSpeed * -math.sin(math.radians(90))
        elif(abs(paddlePos[0]-self.x)< PADDLE_SIZE[0]*5/8 and\
                paddlePos[0]>self.x):                        # パドルの真ん中よりも左側に衝突した場合
            absSpeed = math.sqrt(self.vX**2 + self.vY**2)
            self.vX = absSpeed * math.cos(math.radians(120))
            self.vY = absSpeed * -math.sin(math.radians(120))
        elif(abs(paddlePos[0]-self.x)< PADDLE_SIZE[0]*5/8 and\
              paddlePos[0]<self.x):                         # パドルの真ん中よりも右側に衝突した場合
            absSpeed = math.sqrt(self.vX**2 + self.vY**2)
            self.vX = absSpeed * math.cos(math.radians(60))
            self.vY = absSpeed * -math.sin(math.radians(60))
        elif(paddlePos[0]>self.x):                          # パドルの右端付近に衝突した場合
            absSpeed = math.sqrt(self.vX**2 + self.vY**2)
            self.vX = absSpeed * math.cos(math.radians(144))
            self.vY = absSpeed * -math.sin(math.radians(144))
        else:                                                # パドルの左端付近に衝突した場合
            self.vX = absSpeed * math.cos(math.radians(36))
            self.vY = absSpeed * -math.sin(math.radians(36))
    
    def blockColiderProc(self, blockPos):
        if(self.x > blockPos[0] and self.x <= blockPos[0]+blockPos[2] and \
            self.y > blockPos[1] and self.y < blockPos[1] + blockPos[3]):
            self.vY = self.vY * -1
            return True
        else:
            return False

    def drawSelf(self):      # ボール描画処理
        pygame.draw.circle(self.surface, (150,120,120), (self.x,self.y), 8)