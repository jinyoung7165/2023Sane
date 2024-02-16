# 탑 보기
'''
같은 높이 빌딩 못 봄. 자기보다 높거나 시야 안에서 첫번째로 같은 수면 볼 수 있음(6에서 볼 때-> 7879면, 789 볼 수 있음. 각도 상관x)
빌딩별 시야에 있는 빌딩 출력하라
여러 개면, i번째 빌딩에서 "거리가 가까운 빌딩" (->, <- 두 방향 순회) 중, idx 작은 것부터 출력
빌딩 개수 10**6, 빌딩 크기 10**6
나보다 큰 거 오기를 기다리는 stack
stack에 내림차순 쌓이다가,
top보다 더 높은 거 오면, count[top] += len(stack) 자기보다 큰 왼쪽 애들
top과 같은 거 오면, near공유, count공유 -> 원래 애를 빼라
stack에서 pop하면서 상황에 따라 top에 기록, 현재 애에 기록하니까 틀림 -> 기준 잘 정해서 pop 모두 끝나면 기록하는 유형
'''
from sys import stdin
input = stdin.readline
n = int(input())
buildings = [0]+list(map(int, input().split()))
# 1~n만 진짜
count = [0] * (n+1) # 시야에 보이는 애들 총 합
near = [0] * (n+1) # 그 중 가장 가까운 애의 idx

stack = [] # 나보다 큰 값이 오기를 기다림(내림차순 쌓임)
for i in range(1, n+1):
    while stack and buildings[stack[-1]] <= buildings[i]: # 나보다 같거나 작은 애들은 뺌 -> 나보다 큰 애들만 남음
        top = stack.pop()
    count[i] += len(stack) # 내 왼쪽에 나보다 큰 애들 개수
    
     # 가장 가까운 왼쪽 빌딩을 기록
    if stack: near[i] = stack[-1]
    stack.append(i)

stack = []
for i in range(n, 0, -1): # 거꾸로 순회 n~1, 0(털기 위함)
    while stack and buildings[stack[-1]] <= buildings[i]:
        top = stack.pop()
    count[i] += len(stack) # 내 오른쪽에 나보다 큰 애들 개수
    
    # 가장 가까운 오른쪽 빌딩을 기록할지는, 간격 보고 결정
    if stack:
        if near[i] == 0 or i - near[i] > stack[-1] - i: near[i] = stack[-1]
    stack.append(i)

for i in range(1, n+1):
    if count[i] == 0: print(count[i])
    else: print(count[i], near[i])