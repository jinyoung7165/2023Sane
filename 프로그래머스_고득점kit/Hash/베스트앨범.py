# 장르별 최다 재생곡 2개씩 모을 것
# 총 재생수가 큰 장르부터 수록
# 최다 재생곡부터 수록
# 고유번호가 낮은 노래부터 수록
# ["classic", "pop", "classic", "classic", "pop"]
# [500, 600, 150, 800, 2500]
# -> [4,1,3,0]
from collections import defaultdict
def solution(genres, plays):
    answer = []
    gen_dic = defaultdict(int)
    count_idx = defaultdict(list)
    idx = 0
    for gen, count in zip(genres, plays):
        gen_dic[gen] += count
        count_idx[gen].append([count, idx])
        idx += 1
        
    # 재생횟수가 큰 순서대로 장르 sort -> [('pop', 3100), ('classic', 1450)]
    gen_seq = sorted(gen_dic.items(), key=lambda x: x[1], reverse=True)
    for gen, _ in gen_seq:
        count_idx[gen].sort(key = lambda x: (-x[0], x[1]))
        for _, c in count_idx[gen][:2]:
            answer.append(c)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))