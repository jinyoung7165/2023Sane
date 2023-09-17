# 뒷자리부터 0이 아니면,
# 5 이하면, 현재수보다 작은 10의 배수 + 마지막 수
# 5 초과 시, 현재수보다 큰 10의 배수 - 마지막 수
# 현재수를 10의 배수로 setting후, 보고 있던 위치가 0 idx될때까지 반복
# 0 idx가 되면, 딱 0 idx 위치의 수만큼 더해주면 됨
# 1 ≤ storey ≤ 100,000,000
# 0이 아닌 수 나올 때까지 = 10으로 계속 나오면 알아서 줄어듦
# 5일 때, 앞자리가 5이상이면, 한자리 올리기
# 95 -> 100 - 5 = 6
# 55 -> 100 - 45 (4+5+1), 50+5=10
def solution(storey):
    answer = 0
    while storey:
        last = storey % 10
        if last < 5: # 작은 10의 배수 + 남은 수만큼 이동
            answer += last
        elif last > 5:
            storey += 10 # 더 큰 10의 배수(10으로 나눌 거기 때문에 마지막 수는 신경x)
            answer += (10-last)
        else: # 딱 5일 때 
            if (storey // 10) % 10 >= 5: # 앞자리가 5이상이면, 올리기
                # 95 -> 100 - 5
                storey += 10
            answer += last
        storey //= 10 # 맨 뒷자리부터 계속 앞으로 순회
    return answer
print(solution(16)) # 6 나와야 함
print(solution(366)) # 11
print(solution(965)) # 9
print(solution(155)) # 11
print(solution(154)) # 10
print(solution(95)) # 6나와야 함
print(solution(15)) # 10