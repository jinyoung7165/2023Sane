class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.prev = prev # llink
        self.data = data
        self.next = next # rlink

# DLL은 head node 항상 존재. 삭제 불가
class DoublyLinkedList:
    def __init__(self, data) -> None:
        self.head = Node(data) # 전체 리스트의 HEAD 노드
        self.tail = self.head # 전체 리스트의 마지막 노드
    
    def insert(self, data):
        if self.head is None: #empty
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next: # 끝까지 이동
                node = node.next
            new = Node(data, prev=node)
            node.next = new # 이전 노드에 새 노드 연결
            self.tail = new # tail이 마지막 노드 가리킴
    
    def insert_before(self, next_data, new_data):
        # next_data전, 중간 삽입
        if self.head is None: #empty
            self.head = Node(new_data)
            self.tail = self.head
        else:
            node = self.tail # 끝에서부터 탐색
            while node.data != next_data:
                node = node.prev
                if node is None: # 못 찾음
                    return False
            prev_node = node.prev # 이전 노드
            new_node = Node(new_data, prev_node, node)
            if prev_node: # 이전 노드에 연결
                prev_node.next = new_node
            else: # 새 노드가 맨 처음 원소
                self.head = new_node
            node.prev = new_node # 다음 노드에 새 노드 연결
            return True
        
            