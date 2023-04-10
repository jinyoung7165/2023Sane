# linked list로 queue 구현
# append, popleft시 O(1)
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList(object):
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, node:Node): # 삽입
        if self.front == None: # 비어있을 때
            self.front = node # 빈 front 상태로 둘 수 없기 때문에, linked list의 경우 front, rear 같아도 empty 아님. front가 null이면 empty
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next # rear 이동
    
    def dequeue(self): # 삭제
        if self.front == None: # 비어있을 때
            return
            
        v = self.front.data
        self.front = self.front.next # front 이동
        
        if self.front == None: # 비게 되면 rear도 비운다(메모리 낭비 방지)
            self.rear = None
        return v
    
    def print(self):
        cur = self.front
        string = ""
        while cur:
            string += str(cur.data)
            if cur.next:
                string += "->"
            cur = cur.next
        print(string)

if __name__ == "__main__":
    s = SinglyLinkedList()
    s.enqueue(Node(1))
    s.enqueue(Node(2))
    s.enqueue(Node(3))
    s.print()
    
    s.dequeue()
    s.print() # 2->3
    s.dequeue()
    s.print() # 3
    s.enqueue(Node(1))
    s.print() # 3->1
    s.dequeue()
    s.print() # 1
    s.dequeue()
    s.print() # empty
    s.enqueue(Node(1))
    s.enqueue(Node(2))
    s.enqueue(Node(3))
    s.print() # 1->2->3