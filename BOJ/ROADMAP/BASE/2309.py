# 일곱 난쟁이
# 아홉 키가 주어졌을 때, 키 합이 100되는 7명 조합
# 7명 오름차순으로 출력
heights = sorted(int(input()) for _ in range(9))
answer = None
tmp = []
def dfs(depth, start):
    global tmp, answer
    if answer: return
    if depth == 7:
        if sum(tmp) == 100:
            answer = tmp[:]
        return
    for i in range(start, len(heights)):
        tmp.append(heights[i])
        dfs(depth+1, i+1)
        tmp.pop() 
dfs(0, 0)
for an in answer:
    print(an)
    
    
