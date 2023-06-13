# 잔돈 500, 100, 50, 10, 5, 1엔 충분히
# 거스름돈 개수 가장 적게 잔돈 줌
# 물건 사고, 1000엔 냈을 때, 잔돈 개수
# 잔돈이 모두 배수 -> greedy
n = int(input()) # 물건 금액(1~999)
left = 1000-n
ans = 0
li = [500, 100, 50, 10, 5, 1]
for l in li:
    ans += left // l
    left %= l
print(ans)