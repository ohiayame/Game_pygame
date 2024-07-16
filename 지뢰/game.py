import pygame
import random
import sys

# 초기화
pygame.init()

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 화면 크기
width, height = 400, 300
rows, cols = 3, 4
cell_size = width // cols

# 화면 설정
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Minesweeper')

# 지뢰판 설정
num_li = [[0] * cols for _ in range(rows)]
boms = [[False] * cols for _ in range(rows)]
revealed = [[False] * cols for _ in range(rows)]
flags = [[False] * cols for _ in range(rows)]

# 지뢰의 개수
bom_count = 3

# 지뢰 위치 설정
for _ in range(bom_count):
    x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
    while boms[x][y]:
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
    boms[x][y] = True
    num_li[x][y] = "*"

# 주변 지뢰 수 계산
for x in range(rows):
    for y in range(cols):
        if num_li[x][y] != "*":
            bom_value = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < rows and 0 <= ny < cols and boms[nx][ny]:
                        bom_value += 1
            num_li[x][y] = bom_value

def open_cell(x, y):
    if revealed[x][y] or flags[x][y]:
        return
    revealed[x][y] = True
    if num_li[x][y] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < rows and 0 <= ny < cols:
                    open_cell(nx, ny)

def check_victory():
    for x in range(rows):
        for y in range(cols):
            if boms[x][y] and not flags[x][y]:
                return False
    return True

# 게임 루프
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x, grid_y = y // cell_size, x // cell_size
            
            if event.button == 1:  # 왼쪽 클릭
                if boms[grid_x][grid_y]:
                    print("Boom! Game Over!")
                    running = False
                else:
                    open_cell(grid_x, grid_y)
            elif event.button == 3:  # 오른쪽 클릭
                flags[grid_x][grid_y] = not flags[grid_x][grid_y]
            elif event.button == 2:  # 양쪽 클릭 (중앙 클릭)
                if revealed[grid_x][grid_y]:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            nx, ny = grid_x + i, grid_y + j
                            if 0 <= nx < rows and 0 <= ny < cols and not flags[nx][ny]:
                                if num_li[nx][ny] == 0:
                                    open_cell(nx, ny)
                                revealed[nx][ny] = True

        if check_victory():
            print("Congratulations! You cleared the minefield!")
            running = False

    # 그리드 그리기
    for x in range(rows):
        for y in range(cols):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, rect, 1)
            if revealed[x][y]:
                pygame.draw.rect(screen, WHITE, rect)
                if num_li[x][y] != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(num_li[x][y]), True, BLACK)
                    screen.blit(text, rect.topleft)
            elif flags[x][y]:
                pygame.draw.rect(screen, GREEN, rect)
            elif boms[x][y] and not running:
                pygame.draw.circle(screen, RED, rect.center, cell_size // 4)

    pygame.display.flip()

pygame.quit()
