# 색종이 붙이기
# 1*1, 2*2, 3*3, 4*4, 5*5 다섯 종류 * 5개씩
# 크기가 10*10인 보드 위에 붙이려 함
# 각 칸에 0/1 적힘. 1적힌 칸 모두 색종이로 덮여야 함. 
# 0에는 종이 붙으면 안 됨!!!!
# 1이 적힌 모든 칸을 채우는 데 필요한 색종이 최소 개수
# 불가능한 경우 -1 출력
# (0,0)부터 1인 좌표헤어 크기 1~5 색종이 붙여가며 모든 case 확인
# x 좌표 범위 넘어가면 (0, y+1)로, y가 범위 벗어나면 맨 끝까지 탐색한 것 -> 최솟값 갱신
# board[x][y]=0이면 (x+1, y)로
# 만약 색종이 5장 이미 붙였거나, 범위 벗어나는 크기면 continue
# 붙일 수 있으면 다시 0으로 바꿔줌
# paper 증가 후 (x+k+1, y)로
# paper와 지운 칸 다시 돌려줌
# 해당 칸에 제일 큰 paper 무작정 붙이면 안됨. 그리디 x
# 일단 maps 값이 1이면, 1~5 종이 붙이는 시도. 이 때 5가 제일 많아야 좋긴한데, 한 칸에 무작정 5붙이면 다른 칸에 영향 줘서
# 다른 칸에 크기 작은 종이만 붙여야 해서 paper count가 증가할 수 있음
# 최대한 모든 칸에 쓰는 종이의 크기가 골고루 커야 count 감소
# 1인 종이 붙일 수 있으면, 종이 붙이고, 다음 칸 보며 1 붙일 수 있는지 확인
# 모든 칸에 1 붙일 수 있다는 거 확인 후, 첫 번째 1칸에 2붙일 수 있는지 확인, 다른 칸에 2붙일 수 있는지 확인,, 반복하며
# 모든 칸에 5 붙일 수 있는지 확인,,,
from sys import stdin
input = stdin.readline

pos = [] # 1 좌표
used = [0]*5
board = list(input().split() for _ in range(10))
ans = float('inf')

def dfs(x, y, cnt): # (0,0)~(9,9) 모든 1에 대해 1~5종이 확인
    global ans
    # x, y 오른쪽으로->아래로, 모두 탐색할 건데 maps 범위 벗어난 경우 처리
    if y >= 10: # map 끝까지 확인하며 1인 칸에 대해 모두 종이 붙은 상태
        ans = min(ans, cnt)
        return
    if x >= 10: # 0->오른쪽으로 k크기 종이 확인했음. 아래로 가며 붙일 수 있는 칸 남아있는지 확인하자
        dfs(0, y+1, cnt)
        return
    
    if board[x][y] == '1': # 종이 붙일 수 있는 칸
        for k in range(5):
            if used[k] == 5: # 해당 크기 종이 다 씀-> 다른 크기 종이 확인
                continue
            if x+k >= 10 or y+k >= 10: # 범위 벗어남
                continue
            flag = True
            for i in range(x, x+k+1): # x~x+k
                for j in range(y, y+k+1): # y~y+k
                    if board[i][j] == '0': # 종이 붙일 수 없음
                        flag = False
                        break
                if not flag: break
            if flag: # x~x+k, y~y+k에 대해 k크기의 종이 붙일 수 있으면 방문 처리
                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        board[i][j] = '0' # 방문 처리
                used[k] += 1 # k크기 종이 하나 씀
                dfs(x+k+1, y, cnt+1) # 현재 종이 붙인 칸 이후 오른쪽으로 이동하며 크기 1인 종이 붙일 수 있는지부터 확인
                # 여기서 return 됐다 == maps 끝까지 가서 1인 칸에 종이 모두 붙여서 cnt를 갱신했거나
                # 현재 칸에 k크기인 종이 붙였지만, 현재 칸 제외한 다른 칸에 종이 붙이려다 k크기의 종이 부족 이유로 실패한 경우
                # -> k크기인 종이 여기에 쓰지 마라. 다른 크기의 종이를 여기에 붙여보자. 종이 떼기
                used[k] -= 1 # k크기 종이 다시 쓰지 
                for i in range(x, x+k+1): # 종이 떼라
                    for j in range(y, y+k+1):
                        board[i][j] = '1' # 종이 떼면, k크기 
    else:
        dfs(x+1, y, cnt) # 0이었으면 1나올 때까지 오른쪽으로 이동하며 종이 붙일 수 있는 칸 찾기
dfs(0,0,0) # x,y, 종이 개수

print(ans if ans != float('inf') else -1)