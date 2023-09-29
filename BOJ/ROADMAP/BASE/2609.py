'''
최대공약수와 최소공배수
두 자연수 입력받아 최대 공약수와 최소 공배수 출력
두 수의 최대공약수, 최소공배수 출력
'''
a, b = map(int, input().split())
if a < b: a, b = b, a
G = 1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a* b // G

G = gcd(a, b)
print(G)
print(lcm(a, b))