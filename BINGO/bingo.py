import pygame
import random

pygame.init()

screen_width, screen_height = 630, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BINGO GAME")

PURPLE = (242, 230, 255)
GLAY = (100, 112, 125)
WHITE = (255, 255, 255)
PINK = (255, 142, 165)
BLUE = (66, 181, 255)
RED = (255, 0, 0)

font = pygame.font.Font(None, 40)

button_size = 70
buttons = []
button_color = WHITE
selected_color = PINK
numbers = random.sample(range(1, 26), 25)  
selected = [False for _ in range(25)]

clock = pygame.time.Clock()
# 숫자의 색
number_texts = [font.render(str(number), True, BLUE) for number in numbers]
# 버튼의 위치
for i in range(25):
    # +90는 왼쪽의 여백, +400는 위의 여백
    x = (i % 5) * (button_size + 20) + 90
    y = (i // 5) * (button_size + 20) + 400
    buttons.append(pygame.Rect(x, y, button_size, button_size))
                    # pygame.Rect(left, top, width, height)
                    # left：矩形の左端の x 座標
                    # top：矩形の上端の y 座標
                    # width：矩形の幅
                    # height：矩形の高さ
running = True
game_count = 0
Bingo_count = 0

def check_bingo(selected):
    Bingo_count = 0
    # 세로 가로
    # all()는 안에 있는 원소들이 모두 True면 True, 한개라도 False가 있으면 False
    # selected는 [false] *25 -> 버튼을 누르면 True
    for i in range(5):
        # 0:5, 5:10, 10:15, 15:20, 20:25
        if all(selected[i*5:(i+1)*5]):
            Bingo_count += 1
            # i = 0-> 0,5,10,15,25 
        if all([selected[i + j*5] for j in range(5)]):
            Bingo_count += 1
    # 대각선
    if all([selected[i*5 + i] for i in range(5)]):
        Bingo_count += 1
    if all([selected[i*5 + (4-i)] for i in range(5)]):
        Bingo_count += 1
    return Bingo_count

# 初回描画
screen.fill(PURPLE)
for i, rect in enumerate(buttons):
    pygame.draw.rect(screen, button_color, rect)
    # pygame.draw.rect(surface, color, 버튼의 위치)
    # screen.blit()는 지정위치에 그리기
    screen.blit(number_texts[i], (rect.x + (button_size - number_texts[i].get_width()) // 2,
                                  rect.y + (button_size - number_texts[i].get_height()) // 2))
pygame.display.flip() # 화면의 갱신

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(buttons):
                # selected는 [false] *25 -> 버튼을 누르면 True
                # rect안에 event.pos(마우스)가 있는지 bool 
                if rect.collidepoint(event.pos) and not selected[i]:
                    selected[i] = True
                    game_count += 1
                    new_bingo_count = check_bingo(selected)
                    
                    if new_bingo_count > Bingo_count:
                        Bingo_count = new_bingo_count
                        screen.fill(PURPLE)  # 背景をリセットしてメッセージをクリア
                        
                        for j, rect in enumerate(buttons):
                            color = selected_color if selected[j] else button_color
                            pygame.draw.rect(screen, color, rect)
                            screen.blit(number_texts[j], (rect.x + (button_size - number_texts[j].get_width()) // 2, rect.y + (button_size - number_texts[j].get_height()) // 2))

                        if Bingo_count >= 3:
                            text = font.render(f"3 BINGOS! Game Over in {game_count} moves.", True, RED)
                            screen.blit(text, (90, 100))
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            running = False
                        elif Bingo_count == 1:
                            text = font.render("BINGO!", True, PINK)
                            screen.blit(text, (100, 100))
                            pygame.display.flip()
                            pygame.time.wait(500)  # 1秒の待機
                    else:
                        # ボタンの色を更新して再描画
                        pygame.draw.rect(screen, selected_color, rect)
                        screen.blit(number_texts[i], (rect.x + (button_size - number_texts[i].get_width()) // 2, rect.y + (button_size - number_texts[i].get_height()) // 2))
                        pygame.display.flip()
                    break
        
    clock.tick(60)

pygame.quit()
