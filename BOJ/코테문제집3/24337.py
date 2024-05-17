# 가희와 탑
'''
1~n 건물
a ...건물들... b
a는 1번, 그리고 다음 건물들의 높이가 더 높을 때 볼 수 있음
b도 마찬가지로 n번, 그리고 다음 건물들의 높이가 더 높을 때 가능
a, b가 각각 볼 수 있는 건물 개수 주어짐
n개 건물들의 높이 정보 출력(123, 124 가능할 때 123)
문제 조건에 맞는 건물들의 높이 존재하지 않으면 -1

a, b 수 충족한 다음,
n길이 못 채우면 1을 안 보이는 한, 가장 왼쪽에 끼워넣어야 함
'''
from sys import stdin
input = stdin.readline

n, a, b = map(int, input().split())
buildings = []

if a >= b:
    for i in range(1, a+1):
        buildings.append(i)
    left = b-1
    # 남은만큼 오른쪽부터 1.. 채워야 함
    for i in range(left, 0, -1):
        buildings.append(i)
    # 길이 남은만큼 왼쪽 1 채우면 됨
    left = n-len(buildings)
    if left >= 0:
        for i in range(left):
            print(1, end=' ')
        print(*buildings)
    else: print(-1)
else:
    for i in range(b, 0, -1):
        buildings.append(i)
    left = a-1
    # 남은만큼 왼쪽부터 1.. 채워야 함
    tmp = []
    for i in range(1, left+1):
        tmp.append(i)
    buildings = tmp + buildings
    # 길이 남은만큼, [1]부터 1 채우면 됨
    left = n-len(buildings)
    if left >= 0:
        print(buildings[0], end=' ')
        for i in range(left):
            print(1, end=' ')
        print(*buildings[1:])
    else: print(-1)
    
# 다른 방법
'''
왼쪽부터 1부터 증가하며 a개수만큼 넣기
단, 마지막 a자리에는 a, b 중 더 큰게 와야 함
a가 더 크면 그대로 1~a(오름차순 a개) 오른쪽의 경우 b-1...1(중심 a에 의해 내림차순 b개 완성)
b가 더 크면, 1...a-1(a-1개지만, b에 의해 오름차순 a개 완성) b b-1 ...1(내림차순 b개 완성)
a, b 모두 충족시켜 넣었는데도 길이가 n이 안되면, 최대한 왼쪽부터 1 부족한 개수만큼 출력
a가 1인 경우, 맨 처음 원소가 1보다 크기 때문에, 그 뒤에 1을 놓아야 함
따라서, 두 번째 자리부터 1 출력
'''
n, a, b = map(int, input().split())
answer = []
# 왼+오 합쳐서 합이 n+1이 최대
# 12321 처럼, n=5일 때, a=3, b=3
if a+b>n+1: print(-1)
else:
    for i in range(1, a):
        answer.append(i)
    answer.append(max(a, b))
    for i in range(b - 1, 0, -1):
        answer.append(i)

    print(answer[0], *[1 for _ in range(n - len(answer))], *answer[1:])