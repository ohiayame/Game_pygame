import pygame
import random
import time

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 142, 165)
BLUE = (66, 181, 255)
PURPLE = (242, 230, 255)
viored = (142, 130, 155)

# 표 크기
width = 20
height = 18
cell_size = 35
info_height = 65 # 정보 영역 높이

screen_width = width * cell_size
screen_height = height * cell_size + info_height  # 화면 높이에 정보 영역 추가

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("지뢰 게임")
clock = pygame.time.Clock()

num_li = [[0] * width for _ in range(height)]  # 주변에 있는 지뢰의 갯수를 저장할 리스트
boms = [[False] * width for _ in range(height)]  # 지뢰가 있으면 True
check = [[False] * width for _ in range(height)]  # 출력상태
flag = [[False] * width for _ in range(height)]  # 지뢰 예상

# 지뢰의 개수를 정의
num_mines = (width * height) // 6
remaining_mines = num_mines  # 남은 지뢰 개수
print("Number of mines:", num_mines)

start_time = time.time()  # 시작 시간

# 게임 상태를 저장할 변수
game_over = False
game_message = ""

# 주변을 검사 메뉴에 따라 작동
def surroundings(x, y, menus):
    bom = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i
            ny = y + j
            if 0 <= nx < height and 0 <= ny < width:
                if menus == view:
                    if not check[nx][ny] and not flag[nx][ny]:
                        view(nx, ny)
                elif menus[nx][ny]:
                    if flag[nx][ny]:
                        bom += 10
                    else:
                        bom += 1

    if menus != view:
        return bom

# 주변을 검사하는 surroundings()함수에서 활용
# 지뢰 아니라면 보이게 check리스트 수정 그안에 0이있으면 0주변도 연속적으로 실행
def view(x, y):
    check[x][y] = True
    if num_li[x][y] == 0:
        surroundings(x, y, view)
        
# 표를 출력 (지뢰, clear조건도 확인)
def glaf():
    global game_over, game_message
    game = False
    msg = None
    open_value = 0
    # 표를 출력
    for x in range(height):
        for y in range(width):
            color = WHITE if check[x][y] else PINK if flag[x][y] else PURPLE
            pygame.draw.rect(screen, color, (y * cell_size, x * cell_size + info_height, cell_size, cell_size))  # close cell
            if check[x][y]:
                open_value += 1
                # 지뢰의 좌표를 입력하면 종료
                if boms[x][y]:
                    draw_text('*', x, y, RED)
                    msg = "!!! Mine !!!"
                    game = True
                # 0은 출력 안함
                elif num_li[x][y] > 0:
                    draw_text(str(num_li[x][y]), x, y, BLUE)
            elif flag[x][y]:
                draw_text('!', x, y, viored)

            pygame.draw.rect(screen, viored, (y * cell_size, x * cell_size + info_height, cell_size, cell_size), 1)  # 囲い線
    # 지뢰를 다 피하고 출력이 되면 clear
    if not game and (num_mines == (width * height) - open_value):
        msg = "Clear!!!"
        game = True
    if game:
        game_message = msg
        game_over = True
        print(msg)
        return True

def draw_text(text, row, col, color):
    font = pygame.font.Font(None , 36)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2 + info_height))
    screen.blit(text_surface, text_rect)

# 타이머 및 남은 지뢰 개수를 표시하는 함수
def draw_info():
    elapsed_time = int(time.time() - start_time)
    timer_text = f'Time: {elapsed_time}'
    mines_text = f'Mines: {remaining_mines}'
    font = pygame.font.Font(None, 36)
    timer_surface = font.render(timer_text, True, RED)
    mines_surface = font.render(mines_text, True, RED)
    screen.blit(timer_surface, (10, 10))
    screen.blit(mines_surface, (10, 40))
    if game_over:  # 게임 종료 메시지를 표시
        game_surface = font.render(game_message, True, RED)
        screen.blit(game_surface, (screen_width // 2, 25))

left_click = False
right_click = False

running = True
game = 0
while running:
    screen.fill(WHITE)
    # 마우스가 있는 좌표를 확인
    x, y = pygame.mouse.get_pos()
    grid_x, grid_y = (y - info_height) // cell_size, x // cell_size  # 수정된 부분

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if y > info_height and not game_over:  # 정보 영역을 클릭하지 않도록 함
                if event.button == 1 and not flag[grid_x][grid_y]:  # 왼쪽 클릭
                    game += 1
                    left_click = True
                    if game == 1:  # 처음 클릭이면 지뢰이외 주변 오픈
                        # 지뢰의 위치를 random으로 설정 True로 변환
                        checknum = 0
                        while checknum < num_mines:
                            random_x = random.randint(0, height - 1)
                            random_y = random.randint(0, width - 1)
                            c = True
                            for i in range(-1, 2):
                                for j in range(-1, 2):
                                    nx = grid_x + i
                                    ny = grid_y + j
                                    if random_x == nx and random_y == ny:
                                        c = False
                            if not boms[random_x][random_y] and c:
                                boms[random_x][random_y] = True
                                checknum += 1
                                num_li[random_x][random_y] = "*"

                        # index를 한개 씩 넣어서 주변에 몇개 지뢰가 있는지 확인
                        for x in range(height):
                            for y in range(width):
                                if num_li[x][y] != "*":
                                    num_li[x][y] = surroundings(x, y, boms)

                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                nx = grid_x + i
                                ny = grid_y + j
                                if 0 <= nx < height and 0 <= ny < width:
                                    if not boms[nx][ny]:
                                        view(nx, ny)
                        
                    elif right_click:  # 오른쪽도 True면 주변 오픈
                        bom = surroundings(grid_x, grid_y, boms)
                        if not boms[grid_x][grid_y] and (num_li[grid_x][grid_y] == bom / 10):
                            surroundings(grid_x, grid_y, view)

                    else:
                        if num_li[grid_x][grid_y] == 0:
                            surroundings(grid_x, grid_y, view)
                        else:
                            check[grid_x][grid_y] = True  # 한 개만 오픈
                    
                elif event.button == 3 :  # 오른쪽 클릭
                    if left_click :  # 왼쪽도 True면 주변 오픈
                        if not flag[grid_x][grid_y]:
                            bom = surroundings(grid_x, grid_y, boms)
                            if not boms[grid_x][grid_y] and (num_li[grid_x][grid_y] == bom / 10):
                                surroundings(grid_x, grid_y, view)
                    else:
                        flag[grid_x][grid_y] = not flag[grid_x][grid_y]
                        if not check[grid_x][grid_y]:
                            remaining_mines += -1 if flag[grid_x][grid_y] else 1
                    right_click = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_click = False
            elif event.button == 3:
                right_click = False

    # 표를 출력 
    if glaf():
        draw_info()
        pygame.display.flip()
        game = 0
        check = [[True] * width for _ in range(height)]
        glaf()
        pygame.display.flip()
        pygame.time.wait(3000)

        game_over = False
        num_li = [[0] * width for _ in range(height)]  # 주변에 있는 지뢰의 갯수를 저장할 리스트
        boms = [[False] * width for _ in range(height)]  # 지뢰가 있으면 True
        check = [[False] * width for _ in range(height)]  # 출력상태
        flag = [[False] * width for _ in range(height)]  # 지뢰 예상
        num_mines = (width * height) // 6
        remaining_mines = num_mines
        start_time = time.time()

    draw_info()
    pygame.display.flip()
pygame.quit()
