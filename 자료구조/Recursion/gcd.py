# 최대공약수
# 나머지가 0이될 때까지 큰 수에서 작은 수를 나눔
'''
재귀
'''
def gcd(x, y):
    if y == 0: # 작은 수가 0이면 큰 수 자체가 최대공약수
        return x
    else:
        return gcd(y, x%y)

print(gcd(72, 60)) # 12
'''
반복문(두 수 모두를 나누어 떨어지게 하는 최대의 수 찾아라)
'''
def gcd2(a, b):
    if a > b: small = b
    else: small = a
    for i in range(1, small+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd

'''
유클리드 알고리즘
'''
def gcd3(p, q):
   while(q != 0):
       p, q = q, p % q
   return p