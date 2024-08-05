import pygame

pygame.init()

# (x, y, width, height)
obstacles = [
    pygame.Rect(350, 150, 100, 100),
    pygame.Rect(300, 300, 150, 50),
    pygame.Rect(500, 200, 50, 150),
    pygame.Rect(400, 400, 200, 50)
]

# 충돌 감지를 수행할 대상 Rect 객체 생성 : 파란색 사각형
moving_rect = pygame.Rect(420, 220, 100, 100)

# moving_rect가 obstacles 리스트의 어떤 Rect와 충돌하는지 확인
# collidelist 메서드는 충돌한 Rect의 인덱스를 반환. 충돌이 없으면 -1을 반환한다
collision_indices = moving_rect.collidelistall(obstacles)

if collision_indices != -1:
    # 충돌이 발생한 경우, 충돌한 Rect의 인덱스를 출력
    print(f"moving_rect가 obstacles[{collision_indices}]와 충돌했습니다.")
else:
    # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
    print("충돌이 없습니다.")