'''
부분 문자열
aek, joo, ekj는 baekjoon의 부분 문자열임
s와 p 문자열 주어졌을 때, p가 s의 부분문자열인지 알아보자(1/0)
10^6 길이 미만
'''
s = input().rstrip()
p = input().rstrip()

print(1 if p in s else 0)