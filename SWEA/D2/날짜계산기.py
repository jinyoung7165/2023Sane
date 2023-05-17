# 월 일로 이뤄진 날짜 2개-> 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력
# 월은 1~12.
# 월,일,월,일 주어짐
# 3.1~3.31 => 31일 째

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
tc = int(input())
for i in range(1, tc+1):
    m1, d1, m2, d2 = map(int, input().split())
    s = (month[m1] - d1 + d2 + 1) if m1 != m2 else (d2 - d1 + 1)
    for j in range(m1+1, m2): #m1+1~m2-1
        s += month[j]
    print('#{} {}'.format(i, s))