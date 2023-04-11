# 한 번호가 다른 번호의 접두어인 경우가 있으면 false
# ["12","123","1235","567","88"] > false
# 문자열 in 연산 시 -> 포함관계만 따짐
'''
인접 2개씩 비교 -> startswith(p == k[:len(p)])빠름
'''
def solution(phone_book:list):
    phone_book.sort()
    for i in range(len(phone_book)-1): # sort했으니 인접 2개만 비교
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

print(solution(["12","123","1235","567","88"]))

'''
hash맵 이용 풀이
'''
def solution(phone_book):
    answer = True
    dic = {}
    for phone_number in phone_book:
        dic[phone_number] = 1 # dic이 set보다 in 연산 빠름
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dic and temp != phone_number:
                answer = False
    return answer

def solution(phone_book):
    dic = {}
    phone_book.sort()
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dic and temp != phone_number:
                return False
        dic[phone_number] = 1   
    return True