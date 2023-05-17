# 주어진 문장에서 특정 문자열 개수를 반환(연속된 문자)
# sweetst -> st 검색 시 1 return
# 총 10개의 tc
# 한 문장에서 하나의 문자열만 검색
for _ in range(1, 11):
    input()
    answer = 0
    search = input() # 찾을 문자열
    total = input() # 전체 문자열
    
    t_size, s_size = len(total), len(search)
    
    for i in range(0, t_size-s_size+1):
        if total[i:i+s_size] == search: answer += 1
    
    print("#"+str(_), answer)
    
def another():
    for t in range(1, 11) :

        N = int(input().strip())

        words = input().strip()
        lines = input().strip()

        strs = lines.split(words) # 단어 기준으로 나눠버리기
        # or 그냥 문자열.count(문자열)도 존재

        print("#" + str(N) + " " + str(len(strs)-1))