'''
반복문
'''
from functools import lru_cache


def fib(n):
    cur, next = 0, 1
    for _ in range(n):
        cur, next = next, cur+next
    return cur
'''
재귀
'''
@lru_cache(maxsize=None) #메모이제이션
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)