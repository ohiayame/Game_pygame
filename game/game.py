import pygame
import random
import time

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
# 色
PURPLE = (205, 176, 255)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
# パドルサイズ
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 30
# ボールサイズ
BALL_SIZE = 40
# パドル速度
PADDLE_SPEED = 15
# ボール速度
BALL_SPEED_X = 5
BALL_SPEED_Y = -5

# 画面作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("壁打ちアイスホッケー")

# パドルの初期位置
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT -5

# ボールの初期位置と速度
ball_x = WIDTH // 2    # 左上の座標
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# スコア
score = 0
font = pygame.font.SysFont(None,50)

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # マウスの位置を取得
    # mouse_x, mouse_y = pygame.mouse.get_pos()

    # # パドルの位置をマウスの位置に合わせて更新
    # paddle_x = mouse_x - PADDLE_WIDTH / 2
    
    # パドルの移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle_x += PADDLE_SPEED

    # パドルが画面外に出ないようにする
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > WIDTH - PADDLE_WIDTH:
        paddle_x = WIDTH - PADDLE_WIDTH

    # ボールの移動
    ball_x += ball_dx
    ball_y += ball_dy

    # ボールが壁にぶつかったら反射
    if ball_x <= 0 or ball_x >= WIDTH - BALL_SIZE:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1
    # ボールが画面下部に落ちたらゲーム終了
    if ball_y >= HEIGHT - 60:
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (400, 300))
       
        running = False

    # ボールがパドルに当たったら反射
    if (ball_y + BALL_SIZE >= paddle_y ) and ( ball_x + BALL_SIZE >= paddle_x ) and ( ball_x <= paddle_x + PADDLE_WIDTH) :
        score += 1
        ball_dy *= -1
     # スコアが5の倍数のときにボールの速度を上げる
    if score % 5 == 0 and score != 0:
        if ball_dx > 0:
            ball_dx += 0.03
        else:
            ball_dx -= 0.
        if ball_dy > 0:
            ball_dy += 0.03
        else:
            ball_dy -= 0.03    

    # 画面クリア
    screen.fill(BLACK)

    # パドル描画 (paddle_x, paddle_y) の位置(左上)から始まる PADDLE_WIDTH、PADDLE_HEIGHT の紫色の四角形が画面に描画
    pygame.draw.rect(screen, PURPLE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # スコア表示
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    
    
    # ボール描画
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # 画面更新
    pygame.display.flip()

    # フレームレート設定
    pygame.time.Clock().tick(60)
    
    
final_score_text = font.render("Final Score: " + str(score), True, WHITE)
text_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(final_score_text, text_rect)

# 画面更新
pygame.display.flip()

# 2秒待機
time.sleep(2)    

pygame.quit()