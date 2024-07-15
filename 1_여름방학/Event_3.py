import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
running = True

while running:
    # 이벤트 큐에서 이벤트를 가져옴
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"key pressed: {pygame.key.name(event.key)}.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse button {event.button} clicked at position {event.pos}")

pygame.quit()