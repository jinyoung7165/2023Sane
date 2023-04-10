class CircularQueue:
    def __init__(self) -> None:
        self.rear = 0
        self.front = 0
        self.limit = 100
        self.queue = [0 for i in range(self.limit)]
    
    def is_empty(self):
        if self.rear == self.front:
            return True
        return False
    
    def is_full(self): # rear+1 = front이면 full
        if (self.rear+1) % self.limit == self.front:
            return True
        return False
    
    def enqueue(self, x):
        if self.is_full(): return
        self.rear = (self.rear+1) % self.limit
        self.que[self.rear] = x # 증가한 rear 자리에 삽입
    
    def dequeue(self):
        if self.is_empty(): return
        self.front = (self.front+1) % self.limit
        return self.queue[self.front]