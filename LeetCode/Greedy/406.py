# Queue Reconstruction by Height
'''
people[i] = [h, k] h크기. 자기 앞 k명이 h보다 크거나 같은 값 가짐
정보대로 people 재정렬해 return
k 작은 것부터 + k같으면 h작은 애부터
k를 idx로 두고, answer에 끼워넣기 위해선
h가 큰 것부터 먼저 넣은 후, k 같을 때, insert해서 작은 h가 먼저 앞에 오게 됨
'''
def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    result = []
    for h, k in people:
        result.insert(k, [h, k])
    return result