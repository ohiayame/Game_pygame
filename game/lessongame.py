import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("My First Game")

player = pygame.image.load('C:\Game_pygame\game\player.png')
player_rect = player.get_rect()
player_rect.x = (screen.get_width() - player_rect.width) / 2
player_rect.y = screen.get_height() - player_rect.height
player_speed = 5

enemy = pygame.image.load('C:\Game_pygame\game\enemy.png')
enemy_rect = enemy.get_rect()
enemy_rect.x = random.randint(0,screen.get_width() - enemy_rect.width) # 0
enemy_rect.y = 0
enemy_speed = 7

num_enemies = 3
enemy_rects = [enemy.get_rect() for _ in range(num_enemies)]
for rect in enemy_rects:
    rect.x = random.randint(0, screen.get_width() - rect.width)
    rect.y = random.randint(-500,-rect.height)

# timer_start = 10
font = pygame.font.SysFont(None,74)
game_over_text = font.render("Game Over",True,(255,0,0))

running = True
game_over = False
clock = pygame.time.Clock()
FPS = 60

while running:
    
    clock.tick(FPS)
    # dt = clock.tick(FPS) / 1000
    # timer_start -= dt
    # if timer_start <= 0:
    #     running = False
    #     print("Time's up!")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # elif event.type == pygame.KEYDOWN:
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed               
        if player_rect.x < 0:
            player_rect.x = 0
                    
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
        if player_rect.x + player_rect.width > screen.get_width():
            player_rect.x = screen.get_width() - player_rect.width
                    
    # if keys[pygame.K_UP]:
    #     player_rect.y -= player_speed                     
    #     if player_rect.y < 0:
    #         player_rect.y = 0   
            
    # if keys[pygame.K_DOWN]:
    #     player_rect.y += player_speed               
    #     if player_rect.y + player_rect.height > screen.get_height():
    #         player_rect.y = screen.get_height() - player_rect.height
    
    # if player_rect.colliderect(enemy_rect):
    #     print("Collision detected")
    for rect in enemy_rects:        
        rect.y += enemy_speed
        if rect.y + rect.height >= screen.get_height():
            rect.y = -rect.height # 0
            rect.x = random.randint(0,screen.get_width() - rect.width)
            
        if player_rect.colliderect(rect) and not game_over:
            print("Collision detected")
            game_over = True
            screen.fill((255,255,255)) 
            screen.blit(game_over_text,(screen.get_width() / 2 - game_over_text.get_width() / 2,\
                screen.get_height() / 2 - game_over_text.get_height() / 2))  
            pygame.display.flip()
            time.sleep(5)
            running = False
    
    if not game_over:
        screen.fill((255,255,255)) 
        # timer_text = font.render(str(round(timer_start,2))+"s",True,(0,0,0))     
        # screen.blit(timer_text,(10,10))
        for rect in enemy_rects:
            screen.blit(enemy, rect)
        # screen.blit(enemy,enemy_rect)      
        screen.blit(player,player_rect)
    
        pygame.display.flip()
    
pygame.quit()  