import pygame
import random

pygame.init()
# 화면 설정
screen_width, screen_height = 630, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BINGO GAME")
# 색, font
PURPLE = (242, 230, 255)
GLAY = (100, 112, 125)
WHITE = (255, 255, 255)
PINK = (255, 142, 165)
BLUE = (66, 181, 255)
RED = (255, 0, 0)

font = pygame.font.Font(None, 40)
# button크기와 색등 
button_size = 70
buttons = []
button_color = WHITE
selected_color = PINK
# random 25숫자
numbers = list(range(1, 26))
random.shuffle(numbers)
selected = [False] * 25

clock = pygame.time.Clock()
# 숫자의 색
number_texts = [font.render(str(number), True, BLUE) for number in numbers]
# 버튼 위치
for i in range(25):
    x = (i % 5) * (button_size + 20) + 90
    y = (i // 5) * (button_size + 20) + 100
    buttons.append(pygame.Rect(x, y, button_size, button_size))

# random으로 숫자를 뽑는 버튼
next_button_rect = pygame.Rect(210, 650, 200, 90)
next_button_text = font.render("Next Number", True, WHITE)

bingo_text = None
message_start_time = None

running = True
game_count = 0
bingo_count = 0
game_over = False
# 빙고 알고리즘 함수
def check_bingo(selected):
    bingo_count = 0
    for i in range(5):
        if all(selected[i*5:(i+1)*5]):
            bingo_count += 1
        if all([selected[i + j*5] for j in range(5)]):
            bingo_count += 1
    if all([selected[i*5 + i] for i in range(5)]):
        bingo_count += 1
    if all([selected[i*5 + (4-i)] for i in range(5)]):
        bingo_count += 1
    return bingo_count

while running:
    # 화면
    screen.fill(PURPLE)
    for i, rect in enumerate(buttons):
        color = selected_color if selected[i] else button_color
        pygame.draw.rect(screen, color, rect)
        screen.blit(number_texts[i], (rect.x + (button_size - number_texts[i].get_width()) // 2,
                                      rect.y + (button_size - number_texts[i].get_height()) // 2))
    
    pygame.draw.rect(screen, BLUE, next_button_rect)
    screen.blit(next_button_text, (next_button_rect.x + (next_button_rect.width - next_button_text.get_width()) // 2,
                                   next_button_rect.y + (next_button_rect.height - next_button_text.get_height()) // 2))
    # 빙고 미시지를 표시
    if bingo_text:
        screen.blit(bingo_text, (90, 50))
    # 3번이상 빙고가 있을 경우 종료
    if game_over:
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False
    # 화면 갱신
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스로 버튼을 누르면
            if next_button_rect.collidepoint(event.pos):
                # 숫자를 랜덤으로 선택후 BOOL리스트의 그 숫자의 인덱스 값의 원소가 fOLSE면 실행
                while True:
                    next_number = random.choice(numbers)
                    index = numbers.index(next_number)
                    if not selected[index]:
                        selected[index] = True
                        game_count += 1
                        new_bingo_count = check_bingo(selected)
                        
                        # 실행하기 전 빙고의 개수보다 증가하면 메시지를 지정
                        if new_bingo_count > bingo_count:
                            bingo_count = new_bingo_count
                            if bingo_count >= 3:
                                bingo_game_over = font.render(f"{new_bingo_count} BINGOS! Game Over in {game_count} moves.", True, PINK)
                                game_over = True
                                bingo_text = bingo_game_over
                            else:
                                bingo_text = font.render("BINGO!", True, PINK)
                        break
    clock.tick(60)
        
pygame.quit()
