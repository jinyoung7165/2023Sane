# 무손실 압축 알고리즘 lzw
'''
# 1. 길이 1인 모든 단어 포함하도록 사전 초기화
# 2. 사전에서 입력과 일치하는 가장 긴 문자열 w 찾기
# 3. w에 해당하는 사전의 idx 출력. 입력에서 w 제거
# 4. 입력에서 처리x 글자 c 남아있으면, w+c 사전 등록
# 5. 다시 단계 2
'''
# 영문 대문자만 처리 가능.
# 사전 idx 1~26 -> val A~Z
# 입력 KAKAO
# 첫 글자 K만 사전에 등록돼 있음(idx 11 출력)
# 다음 글자인 A를 포함한 KA를 사전 27 idx 등록

# 두 번째 글자 A 사전에 등록돼 있음(idx 1 출력)
# 다음 글자 K를 포함한 AK를 사전 28에 등록
# 세 번째 글자 KA가 사전에 존재(idx 27 출력)
# 다음 글자 O를 포함한 KAO를 사전 29에 등록

# 마지막 글자 O가 사전에 등록돼 있음(idx 15 출력)
# 위를 통해 KAKAO가 4개의 IDX [11, 1, 27, 15]로 압축됨
# TOBEORNOTTOBEORTOBEORNOT -> [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# ABABABABABABABAB -> [1, 2, 27, 29, 28, 31, 30]
def solution(msg): # 영문 대문자로만 이뤄진 문자열
    DICT = {chr(64 + al): al for al in range(1, 27)}
    
    IDX = 27
    answer = []
    idx, last = 0, ''
    while idx < len(msg):
        last += msg[idx]
        if last in DICT: # 확장 가능
            idx += 1
        else:
            DICT[last] = IDX # 새로운 단어 등록
            IDX += 1
            # last[:-1] : 마지막 글자 제외한 last는 dict에 존재
            answer.append(DICT[last[:-1]])
            last = '' # 그 다음 원소부터는 초기화
    
    # 마지막 원소는 항상 last에 남음
    answer.append(DICT[last])
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))