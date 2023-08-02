from collections import defaultdict

def solution(fees:list, records:list):
    times = defaultdict(list)
    for record in records:
        time, car, flag = record.split()
        h, m = map(int, time.split(':'))
        cur = 60*h + m
        if flag == 'OUT': # 출차 - 입차기록
            times[car].append(cur)
        else:
            times[car].append(-cur)
            
    answer = []
    for car, inout in sorted(times.items()):
        if len(inout) % 2 != 0:
            inout.append(23*60 + 59)
            s_time = sum(inout)
            # 전체 시간 더하기
            if s_time > fees[0]: # 기본 시간 초과
                answer.append(fees[1]-((fees[0] - s_time) // fees[2]) * fees[3])
            else:
                answer.append(fees[1])
    return answer

