import pygame

pygame.init()
# 화면 설정
screen = pygame.display.set_mode((800, 600))
# 시계
clock = pygame.time.Clock()

# 원의 초기 위치
x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40  # 원의 반지름

# 원의 이동 속도
speed = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 델타 타임 계산 : 마지막 프레임 이후 경과 시간 초 단위로 변환
    # 이 값은 각 프레임 간의 시간차으로, 게임의 모든 시간 기반 계산에 사용
    dt = clock.tick(30) / 1000.0  # FPS를 30으로 고정, 결과는 초 단위
    
    # 화면 지우기
    screen.fill((0, 0, 0))
    
    #원 그리기
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)
    
    # 원 위치 업데이트
    x += speed * dt
    
    # 경계 처리 : 원이 화면 가강자리에 닿으면 방향 전환
    if x - radius <= 0 or x + radius >= screen.get_width():
        speed = -speed # 속도의 부호를 반전시켜 반대 방향으로 이동
    
    # 화면 업데이트
    pygame.display.flip()

pygame.quit()