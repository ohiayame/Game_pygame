import pygame
import random

pygame.init()

screen_width, screen_height = 630, 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("BINGO GAME")

PURPLE = (242, 230, 255)
GLAY = (100, 112, 125)
WHITE = (255, 255, 255)
PINK = (255, 142, 165)
BLUE = (66, 181, 255)

font = pygame.font.Font(None, 40)

button_size = 70
buttons = []
button_color = WHITE 
selected_color = PINK
numbers = [random.randint(1, 25) for _ in range(25)] 
selected = [False] * 25

for i in range(25):
    x = (i % 5) * (button_size + 20) + 90
    y = (i // 5) * (button_size + 20) + 400
    buttons.append(pygame.Rect(x, y, button_size, button_size))

running = True
while running:
    screen.fill(PURPLE)
    for i, rect in enumerate(buttons):
        pygame.draw.rect(screen, button_color, rect)  # 버튼 색상 적용
        text = font.render(str(i+1), True, BLUE)
        screen.blit(text, (rect.x + (button_size - text.get_width()) // 2, rect.y + (button_size - text.get_height()) // 2))  # 버튼 중앙에 텍스트 표시


    pygame.display.flip()
pygame.time.wait(10)
pygame.quit()