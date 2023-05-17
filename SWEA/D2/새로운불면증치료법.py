# n 배수 idx 양을 세기 (idx 1 시작)
# n양, 2n양, ... kn양
# 셌던 번호 각 자리수에서 0-9까지의 모든 숫자를 보는 것은 언제?
# n=1295:1,2,9,5->...>3n(3885):3,8,5->...5n(6475):6,4,5,7
# 1n~5n일 때 0-9 숫자 나옴 => return (5n):6475

tc = int(input())

for _ in range(1, tc+1):
    n = int(input())
    answer = 0
    k = 1
    m = n
    s = set(map(str, range(10)))
    while len(s) != 0:
        n = m*k
        s -= set(str(n))
        k += 1
    answer = n
    print('#'+str(_), answer)