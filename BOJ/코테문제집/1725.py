# 히스토그램
# 각 칸 간격 일정. 높이 주어짐
# 히스토그램 내부 가장 넓이가 큰 직사각형 그릴 때
# 넓이를 구하라
# n:1~100,000(히스토그램 가로칸 수)
# 각 칸 높이(0~1,000,000,000)
# 높이 같거나, 커지는 경우. 이전 거 누적 or 현재 거 등록
# 높이 작아지는 경우. 이전 누적 면적 기록, 끊어지는 게 아니라 나보다 왼쪽에 내 height보다 작은 애 있으면 그 idx부터 시작
# 이어지는 경우. height, 시작idx 저장
# 이어지지 않는 경우, height, 현재idx 저장
# marea 갱신. 갱신되는 경우, 이전 거 pop
import sys
input=sys.stdin.readline
stack = []
marea = 0 # max area
n = int(input())
graph = [int(input()) for _ in range(n)]
stack.append((0, graph[0]))
graph.append(0) # 맨 마지막에 제일 작은 높이 더해. 마지막까지의 너비 구하게 함
for idx in range(1, n+1):
    start = idx # 여기서부터 height로 너비 구할 것
    height = graph[idx]
     # 이전보다 작아지는 구간 시작->현재까지 최대 너비 구함
    while stack and stack[-1][1]>height:
        start, h = stack.pop()
        marea = max(marea, h*(idx-start))
    # 높이 같거나, 커지는 경우, 시작 idx와 height 저장
    stack.append((start, height))
print(marea)
