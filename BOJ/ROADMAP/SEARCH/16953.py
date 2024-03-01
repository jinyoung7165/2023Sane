'''
A->B
정수 A->B 변환
연산 2종류
1. 2곱
2. 1을 수 가장 오른쪽에 추가
2 => 162를 위해선 연산 최소 5번 필요
2-> (*2)4 -> (*2)8 -> 81(+1) -> (*2)162
'''
a, b = map(int, input().split())
candidate = [(a*2, 1), (10*a+1, 1)]
while candidate:
    a, t = candidate.pop()
    if a == b:
        print(t+1)
        break
    elif a > b: continue
    candidate.append((a*2, t+1))
    candidate.append((10*a+1, t+1))

else: print(-1)
''' 간단한 수학이란다...
while a < b:
	cnt += 1
	if b % 2 == 0:
		b //= 2
	elif b % 10 == 1:
		b //= 10
	else:
		break
if a == b:
	print(cnt)
else:
	print(-1)

'''