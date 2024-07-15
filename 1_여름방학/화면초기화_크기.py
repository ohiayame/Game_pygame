import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 가, 새로 크기 출력
print(screen.get_width(), screen.get_height())

# 중심점 좌표 계산
center_x = int(screen.get_width() / 2)
center_y = int(screen.get_height() / 2)

# 색상 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# # 점 그리기
pygame.draw.circle(screen, RED, (center_x, center_y), 40)  # 중앙
pygame.draw.circle(screen, GREEN, (0, 0), 40)  # 왼쪽 상단 모서리
pygame.draw.circle(screen, BLUE, (799, 599), 40)  # 오른쪽 하단 모서리
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()