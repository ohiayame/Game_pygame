import pygame

# Pygame 초기화 
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Movement")

# 색상 정의
white = (255, 255, 255)

# 이미지 로드
blue_image = pygame.image.load("blue_rect.png")
red_image = pygame.image.load("red_rect.png")

# 이미지 초기 위치 설정
blue_rect = blue_image.get_rect()
blue_rect.topleft = (100, 100)

red_rect = red_image.get_rect()
red_rect.topleft = (200, 200)

# 이동 속도 설정
speed = 200
delta_speed = 0

# FPS 설정
clock = pygame.time.Clock()
fps = 30

# 게임 루프
running = True
while running:
    delta_speed = speed * (clock.tick(fps) / 1000.0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue_rect.x -= delta_speed
    if keys[pygame.K_RIGHT]:
        blue_rect.x += delta_speed
    if keys[pygame.K_UP]:
        blue_rect.y -= delta_speed
    if keys[pygame.K_DOWN]:
        blue_rect.y += delta_speed
    
    if keys[pygame.K_a]:
        red_rect.x -= delta_speed
    if keys[pygame.K_d]:
        red_rect.x += delta_speed
    if keys[pygame.K_w]:
        red_rect.y -= delta_speed
    if keys[pygame.K_s]:
        red_rect.y += delta_speed
    
    # 이미지가 화면 밖으로 나가지 않도록 경계 처리
    blue_rect.x = max(0, min(blue_rect.x, screen.get_width() - blue_rect.width))
    blue_rect.y = max(0, min(blue_rect.y, screen.get_height() - blue_rect.height))
    red_rect.x = max(0, min(red_rect.x, screen.get_width() - red_rect.width))
    red_rect.y = max(0, min(red_rect.y, screen.get_height() - red_rect.height))
    
    # 화면을 흰색으로 채우기
    screen.fill(white)
    
    # 이미지 그리기
    screen.blit(blue_image, blue_rect)
    screen.blit(red_image, red_rect)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()