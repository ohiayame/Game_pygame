import random

# 표 크기
width = int(input("표의 가로 사이즈를 입력해주세요: "))
height = int(input("표의 세로 사이즈를 입력해주세요: "))


num_li = [[0] * width for _ in range(height)]  # 주변에 있는 지뢰의 갯수를 저장할 리스트

boms = [[False] * width for _ in range(height)]  # 지뢰가 있으면 True

check = [[False] * width for _ in range(height)]  # 출력상태

flag = [[False] * width for _ in range(height)] # 지뢰 예상


# 지뢰의 개수를 정의
bom_random = (width * height) // 5
print("지뢰의 개수:", bom_random)

# 지뢰의 위치를 random으로 설정 True로 변환
checknum = 0
while bom_random > checknum:
    random_x = random.randint(0,height-1)
    random_y = random.randint(0, width-1)
    
    if not boms[random_x][random_y]:
        checknum += 1
        boms[random_x][random_y] = True
        num_li[random_x][random_y] = "*"

# ( 함 수 )
# 주변을 검사 메뉴에 따라 작동
def surroundings(x, y, menus):
    bom = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i 
            ny = y + j 
            try :
                if nx >= 0 and ny >= 0:
                    if menus == view:
                        if (not check[nx][ny]) and (not flag[nx][ny]):
                            view(nx, ny)
                    elif menus[nx][ny] == True:
                        bom += 1
            except:
                continue  # index값이 리스트의 범위를 넘어도 애러 x
        
    if menus != view:
        return bom

# 주변을 검사하는 surroundings()함수에서 활용
# 지뢰 아니라면 보이게 check리스트 수정 그안에 0이있으면 0주변도 연속적으로 실행
def view(x, y):
    check[x][y] = True
    if num_li[x][y] == 0:
        surroundings(x, y, view)

# 숫자를 입력받고 해당 리스트의 원소를 True로 변환
def boolingChange(li):
    
    input_x = int(input(f"세로 1 ~ {height}를 입력하세요."))
    input_y = int(input(f"가로 1 ~ {width}를 입력하세요."))
    
    # 입력 받은 좌표의 출력상태를 벼경
    if input_x > 0 and input_y > 0:
        li[input_x-1][input_y-1] = True

# 표를 출력 (지뢰, clear조건도 확인)
def glaf():
    game = False
    msg = None
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
                    if open_value == (width * height) - bom_random:
                        msg = "Clear!!!"
                        game = True
                
            elif flag[x][y] == True:
                print("!", end=" ")
                
            else:
                print("-", end=" ")
        print()
        
    if game:
        print(msg)
        return True


# index를 한개 씩 넣어서 주변에 몇개 지뢰가 있는지 확인
for x in range(height):
    for y in range(width):
        if num_li[x][y] != "*":
            bom_value = surroundings(x, y, boms)
            num_li[x][y] = bom_value


for li in num_li:
    print(li)

while True:
    # 입력
    menu = int(input("\n1: 클릭\n2: flag\n3: 주변 오픈\n메뉴를 선택: "))
    
    # 한개 체크
    if menu == 1:
        boolingChange(check)
    
    # 지뢰 체크
    elif menu == 2:
        boolingChange(flag)


    # 오픈
    elif menu == 3:
        input_x = int(input(f"세로 1 ~ {height}를 입력하세요.")) -1
        input_y = int(input(f"가로 1 ~ {width}를 입력하세요.")) -1
        
        # 주변에 몇개 지뢰가 있는지 확인
        bom = surroundings(input_x, input_y, flag)
        
        # 확인한 수과 거기 주변에 있는 지뢰의 수가 같으면 오픈
        if num_li[input_x][input_y] == bom:
            surroundings(input_x, input_y, view)
        
    # 예외 처리
    else:
        print("입력 가능 숫자: 1 ~ 3")
    
    # 표를 출력 
    # 지뢰, clear조건해당되면 종료
    if glaf():
        break