import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(50, 100, 80, 40)

# 객체 이동 속도
speed = 100 # 100 pixel / 1 sec
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(30) / 1000

    rect1.x += speed * dt
    
    # if rect1.x + rect1.width 값이 > screen.width
    #    rect1.x = screen.width - rect1.width
    
    if rect1.x + rect1.width > screen.get_width():
        rect1.x = screen.get_width() - rect1.width
        speed = -speed 
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()


