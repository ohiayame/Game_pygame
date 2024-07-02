import pygame
import random

# 게임 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 630, 900  # 화면 크기 변경
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("숫자 야구 게임")

# 색상 설정
WHITE = (242, 230, 255)
BLACK = (100, 112, 125)
BLUE = (255, 255, 255)
RED = (255, 142, 165)
PURPLE = (66, 181, 255)

# 폰트 설정 (시스템에 설치된 폰트 사용)
font = pygame.font.Font(None, 40)  # None 대신에 폰트 파일 경로를 지정할 수 있습니다.

# 공 이미지 로드
ball_size = 100  # 공 크기 설정
ball_image = pygame.image.load("야구게임\s_ball.png")
ball_image = pygame.transform.scale(ball_image, (ball_size, ball_size))

# glove 이미지 로드
glove_size = 100
glove_image = pygame.image.load("야구게임\glove.png")
glove_image = pygame.transform.scale(glove_image, (glove_size,glove_size))

# 난수 생성
cp_li = []
while len(cp_li) < 3:
    cp_num = random.randint(0, 9)
    if cp_num not in cp_li:
        cp_li.append(cp_num)

# 게임 변수
game_out = 0
game_count = 0
player_input = []
result_text = ""
game_over = False
attempts = []
game_over_text = ""  # 게임 오버 텍스트 초기화

# 숫자 버튼 생성
button_size = 70
buttons = []
button_color = BLUE  # 버튼 색상 변경
for i in range(10):
    x = (i % 5) * (button_size + 20) + 90
    y = (i // 5) * (button_size + 20) + 400
    buttons.append(pygame.Rect(x, y, button_size, button_size))
game_strike = 0

# 게임 루프
running = True
while running:
    screen.fill(WHITE)

    # 버튼 그리기
    if not game_over:
        for i, rect in enumerate(buttons):
            pygame.draw.rect(screen, button_color, rect)  # 버튼 색상 적용
            text = font.render(str(i), True, PURPLE)
            screen.blit(text, (rect.x + (button_size - text.get_width()) // 2, rect.y + (button_size - text.get_height()) // 2))  # 버튼 중앙에 텍스트 표시

        # 게임 상태 표시
        status_text = f"{game_count + 1} play : Please input {' '.join(map(str, player_input))}"
        status = font.render(status_text, True, BLACK)
        screen.blit(status, (screen_width // 2 - status.get_width() // 2, 20))  # 화면 상단 중앙에 표시

    # 이전 입력 및 결과 표시
    y_offset = 100
    for attempt in attempts:
        attempt_text = f"{attempt['count']} ) input: {attempt['input']}  {attempt['result']}"
        attempt_display = font.render(attempt_text, True, BLACK)
        screen.blit(attempt_display, (20, y_offset))
        y_offset += 40

    # 결과 텍스트 표시
    result_display = font.render(result_text, True, RED)
    screen.blit(result_display, (20, 70))
    
    # 스트라이크 수에 따른 공 이미지 표시
    for i in range(game_strike):
        x = screen_width // 2 - ball_image.get_width() // 2 - (game_strike - 1) * (ball_image.get_width() // 2)
        y = screen_height // 2 - ball_image.get_height() // 2 + 200
        screen.blit(ball_image, (x + i * ball_image.get_width(), y))
    # out수에 따른 glove이미지 표시
    if game_out > 0:
        for i in range(game_out):
            x = screen_width // 2 - glove_image.get_width() // 2 - (game_out - 1) * (glove_image.get_width() // 2)
            y = screen_height // 2 - glove_image.get_height() // 2 + 350
            screen.blit(glove_image, (x + i * glove_image.get_width()+ 2, y))
        
    # 정답 텍스트 표시
    if game_over:
        answer_text = f"answer : {' '.join(map(str, cp_li))}"
        answer_display = font.render(answer_text, True, BLACK)
        screen.blit(answer_display, (screen_width // 2 - answer_display.get_width() // 2, screen_height // 2 - answer_display.get_height() // 2))
        
        game_over_display = font.render(game_over_text, True, BLACK)
        screen.blit(game_over_display, (screen_width // 2 - game_over_display.get_width() // 2, (screen_height // 2 - game_over_display.get_height() // 2) - 40))
        
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = event.pos
            for i, rect in enumerate(buttons):
                if rect.collidepoint(mouse_pos) and len(player_input) < 3:
                    player_input.append(i)
                    if len(player_input) == 3:
                        game_count += 1
                        game_strike = 0
                        game_ball = 0
                        for idx in range(3):
                            if cp_li[idx] == player_input[idx]:
                                game_strike += 1
                            elif player_input[idx] in cp_li:
                                game_ball += 1
                        if game_strike == 0 and game_ball == 0:
                            game_out += 1
                        
                        result_text = f"result: {game_strike} Strike, {game_ball} Ball" + (f", {game_out} Out" if game_out > 0 else "")
                        
                        attempts.append({
                            'count': game_count,
                            'input': ' '.join(map(str, player_input)),
                            'result': result_text
                        })
                        if game_strike == 3:
                            game_over_text = "The game is over! your win!!"
                            game_over = True
                        elif game_count >= 5 or game_out >= 2:
                            game_over_text = "The game is over! your lose" + (" (5play over)" if game_count == 5 else " (2out)")
                            game_over = True
                        player_input = []

    # 화면 업데이트
    pygame.display.flip()

# 게임 종료 대기
pygame.time.wait(10)

pygame.quit()