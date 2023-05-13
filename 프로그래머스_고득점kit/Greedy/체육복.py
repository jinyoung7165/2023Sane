# 여벌 가진 사람이 바로 앞/뒤 lost에게만 줄 수 있음
# 여벌 가져도 도난 시 (reserve이면서 lost) 빌려줄 수 없음 -> 무조건 자신에게 줘야 함
# -> 반복문 순회에 참여하면 안됨
# 최대한 많은 학생
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lo_re = [lo for lo in lost if lo in reserve] # 여분 가져왔지만 분실
    
    for lo in lo_re:
        lost.remove(lo)
        reserve.remove(lo)
        
    answer = n - len(lost)
    
    l, r = 0, 0
    while (l < len(lost) and r < len(reserve)):
        if (abs(lost[l]-reserve[r]) == 1):
            answer += 1
            l += 1
            r += 1
        elif lost[l] < reserve[r]: l += 1
        else: r += 1
            
    return answer