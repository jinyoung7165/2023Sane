'''
자카드유사도(A,B): 교집합 크기/합집합 크기
A={1,2,3}, B={2,3,4}
교집합: A*B={2,3}
합집합: A+B={1,2,3,4}
자카드유사도: 2/4 = 0.5
둘 다 공집합인 경우, 1로 간주
원소 중복 허용하는 다중집합
A: 1 * 3개, B: 1 * 5개
A*B=min(3,5), A+B=max(3,5)
A: {1,2,2}, B: {1,2,2,3,5}
A*B={1,2,2}, A+B={1,1,2,2,3,5}
자카드유사도: 3/7=0.42
FRANCE, FRENCH -> {FR,RA,AN,NC,CE}, {FR,RE,EN,NC,CH}
교:{FR,NC} 합:{FR,RA,AN,NC,CE,RE,EN,CH} -> 2/8=0.25
영문자로된 글자쌍만 유효. 대소문자 구분X
'''
def cnt_str(s, dic):
    i = 0
    while i < len(s)-1:
        if not s[i].isalpha():
            i += 1
            continue
        if not s[i+1].isalpha():
            i += 2
            continue
        dic[s[i:i+2]] += 1
        i += 1
        
from collections import defaultdict, Counter
def solution(str1, str2):
    answer = 0
    str1 = ''.join(list(map(lambda x: x.lower(), str1)))
    str2 = ''.join(list(map(lambda x: x.lower(), str2)))
    a_dic, b_dic = defaultdict(int), defaultdict(int)
    cnt_str(str1, a_dic)
    cnt_str(str2, b_dic)

    key_list = set(a_dic.keys()) | set(b_dic.keys())
    
    mi, ma = 0, 0
    for key in key_list:
        mi += min(a_dic[key], b_dic[key])
        ma += max(a_dic[key], b_dic[key])
    if ma == 0: answer = 1
    else: answer = mi/ma

    answer = int(answer*65536)
    return answer


print(solution("FRANCE", "french"))

from collections import Counter
def solution(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer