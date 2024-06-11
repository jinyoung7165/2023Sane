# 트리
'''
B-Tree의 전위(부모왼오), 중위(왼부모오) 주어지면,
후위순회(왼오부모) 결과 나타내라

# preorder에서 먼저 나오는 게 루트,
# inorder에서 root왼쪽(left), root오른쪽(right) 나눌 수 있음
# left, right 길이 1이하면 그대로 root에 붙일 수 있음
# left쭉 따라서 출력하다가, 다시 root로 돌아와서 right가서 left쭉, 다시 right
'''
from sys import stdin
input = stdin.readline
def post(root_pre, start, end):
    if end==start: return # 크기 0
    idx = inorder.index(preorder[root_pre])
    # preorder의 앞쪽부터 쭉 루트가 됨
    # root_pre+1로 root_pre 제거,
    # 왼쪽 부분을 지나고 나서부터 right root 시작
    post(root_pre+1, start, idx)
    post(root_pre+1+(idx-start), idx+1, end)
    answer.append(preorder[root_pre]) # root출력
for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    answer = []
    post(0, 0, n)
    print(*answer)