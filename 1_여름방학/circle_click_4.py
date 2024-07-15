import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, WHITE, event.pos, 10)
            pygame.display.flip()
pygame.quit()