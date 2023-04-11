class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node) -> None:
        self.head = Node(node) # 전체 리스트의 첫 번째 원소
        
    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next: # 끝까지 이동
                node = node.next
            node.next = Node(data) # 새 노드 연결
    
    def delete(self, data): # data가진 node 삭제해라
        if self.head is None:
            return
        node = self.head # 첫번째 node부터 탐색
        if node.data == data: # head가 대상이면, 새로운 head 지정
            self.head = node.next
            del node
        else: # singly linked list -> 삭제 시 이전 노드의 link가 삭제노드의 다음 노드 가리켜야 함
            while node.next: # 다음 노드 탐색
                temp = node.next # node:이전 노드, temp:삭제 노드
                if temp.data == data:
                    node.next = temp.next #이전노드가 삭제노드의 다음 가리킴
                    del temp
                    return
                else:
                    node = temp
                    
    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next