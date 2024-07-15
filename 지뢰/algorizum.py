import random

# 표 크기
width = 4
height = 3

# 주변에 있는 지뢰의 수를 저장할 리스트
num_li = [[0] * width for _ in range(height)]

# 지뢰가 있으면 True
boms = [[False] * width for _ in range(height)]

# 지뢰의 개수를 정의
bom_random = 3

# 지뢰의 위치를 random으로 설정
random_x = random.sample(range(3), bom_random)
random_y = random.sample(range(4), bom_random) 

# 정한 위치를 True로 변환
for i in range(bom_random):
    boms[random_x[i]][random_y[i]] = True
    num_li[random_x[i]][random_y[i]] = "*"


# index를 한개 씩 넣어서 채크
for x in range(3):
    for y in range(4):
        
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
for li in num_li:
    print(li)