import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

WHITE = (255, 255, 255)
screen.fill(WHITE)
pygame.display.flip()

# 원 그리기
value = random.randint(5, 20)

for _ in range(value):
    x = random.randint(0, 799)
    y = random.randint(0, 599)
    size = random.randint(5, 70)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    pygame.draw.circle(screen, (r, g, b), (x, y), size)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit