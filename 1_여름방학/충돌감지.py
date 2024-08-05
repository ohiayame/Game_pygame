import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rectangle Collision Example")

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# 사각혀의 초기화
rect1 = pygame.Rect(300, 220, 60, 60)
rect2 = pygame.Rect(100, 100, 60, 60)
rect1_speed = [10, 10]
rect2_speed = [5, 5]

# FPS
fps = 30
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(fps) # 설정된 fps에 따라 루프를 진행
    
    # 시각형 움직임
    rect1 = rect1.move(rect1_speed)    
    rect2 = rect2.move(rect2_speed)
    
    # 화면 경계에 충돌 처리 (rect1)
    if rect1.left < 0 or rect1.right > 640:
        rect1_speed[0] = -rect1_speed[0]
    if rect1.top < 0 or rect1.bottom > 480:
        rect1_speed[1] = -rect1_speed[1]
    
    # 화면 경계에 충돌 처리 (rect2)
    if rect2.left < 0 or rect2.right > 640:
        rect2_speed[0] = -rect2_speed[0]
    if rect2.top < 0 or rect2.bottom > 480:
        rect2_speed[1] = -rect2_speed[1]
    
    # 충돌 감지
    if rect1.colliderect(rect2):
        print("Collision Detected!")
    
    screen.fill(black)
    pygame.draw.rect(screen, blue, rect1)
    pygame.draw.rect(screen, red, rect2)
    pygame.display.flip()

pygame.quit()