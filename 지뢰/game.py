import pygame
import random

# Initialize the game
pygame.init()

# Define the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 142, 165)
BLUE = (66, 181, 255)
PURPLE = (242, 230, 255)
viored = (142, 130, 155)


# Get user input for the size of the grid
width = int(input("Enter the width of the grid: "))
height = int(input("Enter the height of the grid: "))
cell_size = 50

# Calculate screen dimensions
screen_width = width * cell_size
screen_height = height * cell_size

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()

# Define the game variables
num_li = [[0] * width for _ in range(height)]
boms = [[False] * width for _ in range(height)]
check = [[False] * width for _ in range(height)]
flag = [[False] * width for _ in range(height)]

# Define the number of mines
num_mines = (width * height) // 5
print("Number of mines:", num_mines)

# Randomly place mines
checknum = 0
while checknum < num_mines:
    random_x = random.randint(0, height - 1)
    random_y = random.randint(0, width - 1)
    if not boms[random_x][random_y]:
        boms[random_x][random_y] = True
        checknum += 1
        num_li[random_x][random_y] = "*"

# Define the functions
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
                elif menus[nx][ny] == True:
                    bom += 1
    if menus != view:
        return bom

def view(x, y):
    check[x][y] = True
    if num_li[x][y] == 0:
        surroundings(x, y, view)

def glaf():
    game = False
    msg = None
    open_value = 0
    for x in range(height):
        for y in range(width):
            if check[x][y] == True:
                open_value += 1
                if num_li[x][y] == "*":
                    draw_text('*', x, y, RED)
                    msg = "!!! Mine !!!"
                    game = True
                else:
                    draw_text(str(num_li[x][y]), x, y, BLUE)
                    if open_value == (width * height) - num_mines:
                        msg = "Clear!!!"
                        game = True
            elif flag[x][y] == True:
                draw_text('!', x, y, PINK)
            else:
                pygame.draw.rect(screen, PURPLE, (y * cell_size, x * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, viored, (y * cell_size, x * cell_size, cell_size, cell_size), 1)
    
    if game:
        print(msg)
        return True

def draw_text(text, row, col, color):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
    screen.blit(text_surface, text_rect)

# Calculate the number of mines around each cell
for x in range(height):
    for y in range(width):
        if num_li[x][y] != "*":
            num_li[x][y] = surroundings(x, y, boms)
            
    
left_click = False
right_click = False

# Main game loop
running = True
while running:
    
    screen.fill(WHITE)
    
    x, y = pygame.mouse.get_pos()
    grid_x, grid_y = y // cell_size, x // cell_size

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                left_click = True
                if right_click:
                    bom = surroundings(grid_x, grid_y, flag)
                    if num_li[grid_x][grid_y] == bom:
                        surroundings(grid_x, grid_y, view)
                else:
                    check[grid_x][grid_y] = True

            elif event.button == 3:  # Right click
                right_click = True
                if left_click:
                    bom = surroundings(grid_x, grid_y, flag)
                    if num_li[grid_x][grid_y] == bom:
                        surroundings(grid_x, grid_y, view)
                else:
                    flag[grid_x][grid_y] = not flag[grid_x][grid_y]
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left click
                left_click = False
            elif event.button == 3:  # Right click
                right_click = False

    if glaf():
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False
        
    pygame.display.flip()

pygame.quit()
