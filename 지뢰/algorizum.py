import random

# 표 크기
width = int(input("표의 가로 사이즈를 입력해주세요: "))
height = int(input("표의 세로 사이즈를 입력해주세요: "))

# 주변에 있는 지뢰의 수를 저장할 리스트
num_li = [[0] * width for _ in range(height)]

# 지뢰가 있으면 True
boms = [[False] * width for _ in range(height)]

# 출력상태
check = [[False] * width for _ in range(height)]

# 지뢰의 개수를 정의
bom_random = (width * height) // 5
print("지뢰의 개수:", bom_random)

# 지뢰의 위치를 random으로 설정
random_x = [random.randint(0, height-1) for _ in range(bom_random)]
random_y = [random.randint(0, width-1) for _ in range(bom_random)]

# 정한 위치를 True로 변환
for i in range(len(random_x)):
    boms[random_x[i]][random_y[i]] = True
    num_li[random_x[i]][random_y[i]] = "*"


# index를 한개 씩 넣어서 채크
for x in range(height):
    for y in range(width):
        
        bom_value = 0  # 지뢰의 개수를 세우는 변수
        
        # 주변에 몇개 지뢰가 있는지 확인
        if num_li[x][y] != "*":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx = x + i
                    ny = y + j
                    try :
                        if nx >= 0 and ny >= 0:   # 인덱스 값은 반드시 양수!!!!
                            if boms[nx][ny] == True:  
                                bom_value += 1
                        else:
                            continue
                    except:
                        continue  # index값이 리스트의 범위를 넘어도 애러 x
            num_li[x][y] = bom_value

# print(random_x, random_y)
# for li in num_li:
#     print(li)

game = False
while True:
    
    # 입력
    input_x = int(input(f"세로 1 ~ {height}를 입력하세요."))
    input_y = int(input(f"가로 1 ~ {width}를 입력하세요."))
    
    # 입력 받은 좌표의 출력상태를 벼경
    try:
        if input_x > 0 and input_y > 0:
            check[input_x-1][input_y-1] = True
    except:
        continue
    
    open_value = 0
    # 표를 출력
    for x in range(height):
        for y in range(width):
            if check[x][y] == True:
                open_value += 1
                # 지뢰의 자표를 입력하면 종료
                if num_li[x][y] == "*":
                    print("*", end=" ")
                    msg = "!!! 지뢰 !!!"
                    game = True
                
                else:
                    print(num_li[x][y], end=" ")
                    # 지뢰를 다 피하고 출력이 되면 clear
                    if open_value == (width + height) - bom_random:
                        msg = "Clear!!!"
                        game = True
            else:
                print("-", end=" ")
        print()
    if game:
        break

print(msg)