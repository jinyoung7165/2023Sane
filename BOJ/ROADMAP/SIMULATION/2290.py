'''
LCD Test
n은 나타낼 수, s는 크기
길이가 s인 -와 |을 이용해 출력
각 숫자는 모두 s+2의 가로와 2s+3 세로로 이뤄짐
나머지는 공백으로 채움. 각 숫자 사이엔 공백 한 칸
2 1234567890
=>
      --   --        --   --   --   --   --   --  
   |    |    | |  | |    |       | |  | |  | |  | 
   |    |    | |  | |    |       | |  | |  | |  | 
      --   --   --   --   --        --   --       
   | |       |    |    | |  |    | |  |    | |  | 
   | |       |    |    | |  |    | |  |    | |  | 
      --   --        --   --        --   --   --  
'''
'''
 -
| |
 -
| |
 - 
'''
# s개만큼 각 작대기 그림
s, n = input().split()
s = int(s)
def construct(cur):
    result = [[' ']*(s+2) for _ in range(2*s+3)]
    for i in range(1, s+1):
        if cur in '23567890': # 맨 위 뚜껑
            result[0][i] = '-'
        if cur in '2345689': # 중간 뚜껑
            result[s+1][i] = '-'
        if cur in '2356890': # 아래 뚜껑
            result[2*s+2][i] = '-'
            
        if cur in '12347890': # 오른 위 기둥
            result[i][-1] = '|'
        if cur in '134567890': # 오른 아래 기둥
            result[s+i+1][-1] = '|'
        if cur in '456890': # 왼쪽 위 기둥
            result[i][0] = '|'
        if cur in '2680': # 왼쪽 아래 기둥
            result[s+i+1][0] = '|'
    return result

display = [construct(i) for i in n] # 각 digit에 대해 숫자 map 생성
for line in zip(*display): # 전체 row 같은 원소끼리 묶기
    for r in line:
        print(''.join(r), end = ' ') # 각 숫자 사이 공백
    print()