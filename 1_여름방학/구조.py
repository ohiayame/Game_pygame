import pygame

####  초기화  ####
pygame.init()

screen = pygame.display.set_mode((640, 480))  # 너비: 800px, 높이: 600px
clock = pygame.time.Clock()
running = True

####  이벤트 처리  ####
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

####  종료  ####
pygame.quit