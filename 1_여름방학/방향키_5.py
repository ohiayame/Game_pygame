import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
x = 400
y = 300
new_x = x
new_y = y
running = True
while running:
    
    pygame.draw.line(screen, (r, g, b), (x, y), (new_x, new_y))
    pygame.display.flip()
    
    x = new_x
    y = new_y
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            keys = pygame.key.get_pressed()  
            
            if keys[pygame.K_LEFT]:
                new_x -= 10
                
            elif keys[pygame.K_RIGHT]:
                new_x += 10
                
            elif keys[pygame.K_DOWN]:
                new_y += 10
                
            elif keys[pygame.K_UP]:
                new_y -= 10
    
pygame.quit()