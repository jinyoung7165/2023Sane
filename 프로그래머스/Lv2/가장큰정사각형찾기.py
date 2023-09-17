'''
1/0 1로 이뤄진 가장 큰 정사각형 -> 넓이 return
dp[i][j]: (i,j)부터 오른쪽으로 1연속 몇 개인지 기록
'''
# 반례 못 찾아서 미해결
# import heapq
# def solution(board):
#     que = []
#     answer = 0
#     flag = False
#     row = len(board)
#     for i in range(row): # 모든 행
#         # 2 연속 없을 경우 대비
#         if not flag and 1 in board[i]: flag = True
#         for j in range(len(board[0])-2, -1, -1): # 오른쪽부터 순회
#             if board[i][j] == 1 and board[i][j+1] > 0:
#                 board[i][j] = board[i][j+1] + 1 # 누적 개수(가로 길이)
#                 # if row-i < board[i][j] or i == row-1: continue -> 이거 때문에 que에 안 들어감
#                 if i == row-1: continue
#                 heapq.heappush(que, (-board[i][j], i, j)) # 가능한 시작점
#     if flag: answer = 1 # 1크기 정사각형
    
#     while que:
#         size, s_x, s_y = heapq.heappop(que)
#         size = -size
#         if size > row - s_x: size = row - s_x
#         tmp = size
#         for i in range(s_x+1, s_x+size): # 시작점 다음 행부터
#             if i < row and board[i][s_y] < tmp:
#                 tmp = board[i][s_y] # 최소 연속수 갱신 -> 최소 크기로 정사각형이 만들어질 것
#         if answer < tmp:
#             answer = tmp
            
#     return answer**2

# 답지 DP
def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[i])): # 아래 행으로 내려오며 자연스럽게 대각선, 위, 왼쪽 추출해 누적
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                if board[i][j] > answer: answer = board[i][j]

    # 연속 2이상의 정사각형 발견 실패 -> 1이라도 찾자
    if answer == 0:
        for i in range(len(board)): # 모든 행
            if board[i][0] == 1:
                answer = 1
                break

    return answer ** 2

print(solution(board = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [0, 1, 1, 1, 1],
  [1, 1, 1, 1, 1]
])) # 4

print(solution(board = [
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 0]
])) # 9


print(solution(board = [
  [1, 1, 1, 1, 1], # 최대 누적 5
  [1, 1, 1, 0, 0], # 최대 누적 3
  [1, 1, 0, 0, 0], # 최대 누적 2
])) # 4
