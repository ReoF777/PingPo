import pygame
from pygame.locals import *
import sys
from ball import Ball
from paddle import Paddle
from consts import *

def isCollision(ballX, ballY, paddleX, paddleY):
    """
    衝突検知メソッド\n
    パドルとボールが衝突したと判断した時にはTrue、\n
    そうでない場合にはFalseを返す
    """
    if(ballX > paddleX - PADDLE_SIZE[0]/2 and ballX < paddleX + PADDLE_SIZE[0]/2) and \
        (ballY < paddleY + PADDLE_SIZE[1]*4 and ballY > paddleY - PADDLE_SIZE[1]*4):
        return True
    else:
        False

def main():
    pygame.init()
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(icon)
    SURFACE = pygame.display.set_mode(WINDOW_SIZE)
    pygame.key.set_repeat(5, 2)
    pygame.display.set_caption(WINDOW_TITLE)
    flag = True                                # 処理判定フラグ(プログラム終了、異常発生時にはFlase、それ以外にはTrue)
    fpsClock = pygame.time.Clock()
    sysFont = pygame.font.SysFont(None, 30)
    score = 0

    paddle = Paddle(PADDLE_START, SURFACE)     # パドルを作成
    ball = Ball(BALL_START, SURFACE)           # ボールを作成

    BlockPos = []                              # 各ブロックの座標(中心座標)を入れるリスト
    for i in range(BLOCK_ROW_NUM):
        for j in range(BLOCK_COLUMN_NUM):
            BlockPos.append(Rect((50+j*90, 10+i*60), (70, 30)))

    while flag:
        SURFACE.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:      # プログラム終了の場合
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:    # qキーが押されたときにプログラム終了
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_d:  # dキーが押された時には右へ移動
                    paddle.moveRight()
                elif event.key == pygame.K_a:  # aキーが押された時には左へ移動
                    paddle.moveLeft()
            else:
                pass
        
        # 衝突検出(ボールとパドル)
        ballPos = ball.getPos()
        paddlePos = paddle.getPos()
        isCrash = isCollision(ballPos[0], ballPos[1], paddlePos[0], paddlePos[1])
        if isCrash:
            ball.PaddleCollisionProc(paddlePos)

        # 衝突検出(ボールとブロック)
        removeBlock = []
        for i in range(len(BlockPos)):
            blockPos = BlockPos[i]
            isCrash = ball.blockColiderProc(blockPos)
            if(isCrash):
                removeBlock.append(blockPos)
        
        for i in range(len(removeBlock)):
            BlockPos.remove(removeBlock[i])
            score += 10

        # ボール移動処理
        ball.movePos()
        ballPos = ball.getPos()
        if(ballPos[1] > WINDOW_SIZE[1] - 10):
            score -= 10
        
        # パドル、ブロック、ボール描画
        paddle.drawSelf()
        ball.drawSelf()
        for i in range(len(BlockPos)):
            pygame.draw.rect(SURFACE, (50,80,50), BlockPos[i], 0)

        # 得点更新
        message = sysFont.render(f"Score: {score}", True, (0, 128, 200))
        messageRect = message.get_rect()
        messageRect.center = (WINDOW_SIZE[0]*0.9, WINDOW_SIZE[1]*0.35)
        SURFACE.blit(message, messageRect)
        
        pygame.display.update()
        fpsClock.tick(30)

if __name__ == "__main__":
    main()