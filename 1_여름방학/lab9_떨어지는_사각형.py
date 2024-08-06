import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Falling Squares Example')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

square_size = 50
falling_speed = 200
falling_squeares = []  # 떨어지는 사각형을 저장

# 사용자 정의 이벤트 설정 (  매 1초마다 SPAWN_SQUARE 이벤트 발생 )
SPAWN_SQUARE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_SQUARE, 1000) # 1초마다 사각형 생성

# FPS제어를 위한 clock 객체 생성
clock = pygame.time.Clock()

def spawn_square():
    # 랜덤한 x 위치에 새로운 사각형 생성
    x_position = random.randint(0, screen_width - square_size)
    new_square = pygame.Rect(x_position, 0, square_size, square_size)
    falling_squeares.append(new_square)

running = True
while running:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_SQUARE:
            spawn_square()  # 사각형 생성 이벤트 발생 시 사각형 추가
    
    # 사각형 이동
    for square in falling_squeares[:]:
        square.y += falling_speed * dt # 델타 타임 을 사용한 이동
        if square.top > screen_height:
            falling_squeares.remove(square) # 화면을 벗어나면 제거
    
    screen.fill(WHITE)
    
    for square in falling_squeares:
        pygame.draw.rect(screen, BLUE, square)
    
    pygame.display.flip()

pygame.quit()