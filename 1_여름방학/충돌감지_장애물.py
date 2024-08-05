import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('COllidelist Example')

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# (x, y, width, height)
obstacles = [
    pygame.Rect(150, 100, 100, 100),
    pygame.Rect(300, 300, 150, 50),
    pygame.Rect(500, 200, 50, 150),
    pygame.Rect(400, 400, 200, 50)
]


moving_rect = pygame.Rect(50, 50, 50, 50)

# 이동 속도
velocity = 300

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 이전 위치 저장
    previous_position = moving_rect.topleft
    
    # 델타 타임 계산
    dt = clock.tick(60) / 1000.0
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt
    
    # 충돌 감지
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"Collision with obstacle {collision_index}")
        # 충돌이 발생한 경우 이전 위치로 되돌리기
        moving_rect.topleft = previous_position
    
    screen.fill(white)
    
    # 장애물 그리기 
    for obs in obstacles:
        pygame.draw.rect(screen, blue, obs)
    
    pygame.draw.rect(screen, red, moving_rect)
    
    pygame.display.flip()

pygame.quit()