'''
시그널
1은 1열*5행
나머지는 3열*5행
숫자 사이에 공백
40 (5로 나누면 8)
###..#..
#.#..#..
###..#..
#.#..#..
###..#..
주어진 길이 5로 나눠 col 생성
행은 항상 5
숫자 사이에 공백 1열 이상의 공백
-맨 위 뚜껑 1/4 비교
-일렬로 쭉 기둥 바로 나오는 거 068
--중간 거 비면 0, 8이 아니면 6
-오른쪽 하나 없는 거 5
-왼쪽 없는 거 7
-왼쪽 하나 있는 거 2
-왼쪽 하나 있는 거 9
-아닌 거 3
col==5일 때 (p행 k열 보고 싶다. col*p+k)
068
'''
n = int(input())
row = input()
result = ''
i = 0 # 맨 위 시작 인덱스 (맨 왼쪽)
col = n//5
flag = False # 현재 고려중인 숫자 존재 여부
while i < col:
    if not flag:
        if row[i] == '.':
            i += 1 # 공백
            continue
        elif i + 1 == col: # 현재 공백 아닌데 다음칸 없으면 1
            result += '1'
            break
        elif row[i+1] == '.': # 현재 공백 아니고 다음칸 공백이면
            if row[2*col+i+1] == '.':
                result += '1'
                i += 2
                continue
            else:
                result += '4'
        elif row[2*col+i] == '.':
            result += '7'
        elif row[col+i] == '.':
            if row[3*col+i] == '.':
                result += '3'
            else:
                result += '2'
        elif row[3*col+i] == '.':
            if row[col+i+2] == '.':
                result += '5'
            else:
                result += '9'
        elif row[col+i+2] == '.':
            result += '6'
        elif row[2*col+i+1] == '.':
            result += '0'
        else:
            result += '8'
        i += 4
print(result)