import pygame
import random

pygame.init()

screen_width, screen_height = 1000, 670
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("카드 맞추기 게임")

PURPLE = (242, 230, 255)
GLAY = (100, 112, 125)
WHITE = (255, 255, 255)
PINK = (255, 142, 165)
BLUE = (66, 181, 255)
RED = (255, 0, 0)

font = pygame.font.Font(None, 40)

button_size_x = 70
button_size_y = 100
buttons = [] 
button_color = WHITE
selected_color = PINK
num = 1
data = [num+i for i in range(20)]
random_list = [d for d in data for _ in range(2)]
random.shuffle(random_list) 
print(random_list)

selected = [False for _ in range(len(random_list))]
opened = [False for _ in range(len(random_list))]

clock = pygame.time.Clock()

# 버튼의 위치
for i in range(len(random_list)):
    # +90는 왼쪽의 여백, +400는 위의 여백
    x = (i % 10) * (button_size_x + 20) + 60
    y = (i // 10) * (button_size_y + 20) + 90
    buttons.append(pygame.Rect(x, y, button_size_x, button_size_y))

def listTrue(li):
    count = 0
    for s in li:
        if s == True:
            count += 1
    return count
number_texts = [font.render(" ", True, BLUE) for _ in  range(len(random_list))]
screen.fill(PURPLE)
for i, rect in enumerate(buttons):
    pygame.draw.rect(screen, button_color, rect)
    screen.blit(number_texts[i], (rect.x + (button_size_x - number_texts[i].get_width()) // 2,
                                  rect.y + (button_size_y - number_texts[i].get_height()) // 2))
pygame.display.flip()
running = True
open_c = None
play_c = 0
while running:
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(buttons):
                if rect.collidepoint(event.pos) and not selected[i] and not opened[i]:
                    selected[i] = True
                    # 숫자의 색
                    number_texts = [font.render(str(random_list[number]), True, BLUE) if opened[number] or selected[number] else font.render(" ", True, BLUE) for number in  range(len(random_list))]
                    for j, rect in enumerate(buttons):
                        color = selected_color if selected[j] else button_color
                        pygame.draw.rect(screen, color, rect)
                        screen.blit(number_texts[j], (rect.x + (button_size_x - number_texts[j].get_width()) // 2,
                                                        rect.y + (button_size_y - number_texts[j].get_height()) // 2))
                    
                    if listTrue(selected) >= 2 :
                        if random_list[open_c] == random_list[i]:
                            opened[open_c] = True
                            opened[i] = True
                            if listTrue(opened) == len(random_list):
                                game_surface = font.render("!!! Clear !!!", True, RED)
                                screen.blit(game_surface, (screen_width // 2 - 85, 25))
                        selected[open_c] = False
                        selected[i] = False
                    else:
                        open_c = i

pygame.quit()