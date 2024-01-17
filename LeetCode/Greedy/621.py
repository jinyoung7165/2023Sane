# Task Scheduler
# 각 간격마다 CPU는 1개의 TASK만 실행 가능
# n번의 간격 내에는 동일 태스크를 실행할 수 없음
# 더 이상 태스크실행 불가 시 idle상태
# 모든 태스크를 실행하기 위한 최소 간격 구하라
'''
["A","A","A","B","B","B"], n=2일 때 -> 8(A>B>idle>A>B>idle>A>B)
{A:4, B:2} maxcount:4
A_A_A_A -> maxcount가 나온 원소+idle 나열하고, 나머지 원소를 idle에 끼워넣음
maxcount + idle*(maxcount-1)

if. maxcount인 원소가 여러 개?
AB(CD)AB(C)_AB -> 맨마지막에 maxtask의 길이(2) -1 추가 (선두A는 이미 maxcount로 더해짐)
maxcount(idle 앞 선두) + idle*(maxcount-1) + len(maxtask)-1

if. maxcount가 아닌 원소가 많아서 위의 길이를 초과한다면?
ABCDABCDABEFG -> len(전체 원소)
'''

import collections
def leastInterval(tasks, n):
    if n == 0: return len(tasks)
        
    counts = collections.Counter(tasks)
    max_count = counts.most_common()[0][1] 
    max_task_size = list(counts.values()).count(max_count)  #max count를 가지는 task 여러 개

    ans = max_count + (max_count-1) * n + (max_task_size-1)
    return max(ans, len(tasks))