package 자료구조.LinearDS;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class queue { // 배열 큐로 구현
    int limit = 100; // 배열 크기. 큐 최대 크기
    int front, rear; // pop, push할 때 참조할 idx
    int[] que;

    public queue() {
        front = rear = 0; // 초기값 0
        que = new int[limit]; // 배열 생성
    }

    public boolean isEmpty() { // front 제거하며 계속 증가해서 rear까지 왔음
        return front == rear;
    }

    public boolean isFull() { // false full 문제 생길 수 있음(front쪽 삭제되며 공간 낭비)
        if (rear == limit-1) return true;
        return false;
    }

    public int size() { // 현재 data 수
        return rear-front;
    }

    public void push(int value) {
        if (this.isFull()) return;
        que[rear++] = value;
    }

    public int pop() {
        if (this.isEmpty()) return -1;
        int popValue = que[front++];
        return popValue;
    }

    public int peek() {
        if (this.isEmpty()) return -1;
        int popValue = que[front];
        return popValue;
    }

    public Queue<Integer> useQue() {
        Queue<Integer> que = new LinkedList<Integer>();

        que.offer(1); // rear에 삽입
        que.offer(2);

        while (!que.isEmpty()) {
            System.out.println(que.poll()); // front 꺼냄
        }

        return que;
    }

    /**
     * linked List로 구현하기 -> 무한한 que의 크기
     */
    public class queNode {
        private int el;
        private queNode node; // 다음 node 가리킴

        public queNode(int item) { //
            this.el = item;
            this.node = null;
        }
        protected int getData() {
            return this.el;
        }
        protected void linkNode(queNode node) {
            this.node = node;
        }
        protected queNode getNext() {
            return this.node;
        }
    }

    public class linkedListQue {
        queNode front, rear; // 이전, 다음 node

        public linkedListQue() {
            front = rear = null;
        }

        public boolean isEmpty() {
            if (front == null) return true; // node타입이기 때문에, 초기화할 때 front=rear 같은 노드라 empty 아님
            return false;
        }
        
        public void push(int value) {
            queNode node = new queNode(value);
            if (this.isEmpty()) { // 큐 비어있으면 front, rear 자기자신
                front = node;
            }
            else { // 큐에 원소 있으면
                rear.linkNode(node); // rear에 새 node 연결
            }
            rear = node; // rear 이동
        }

        public int pop(){
            if (this.isEmpty()) return -1;
            
            int temp = front.getData();
            queNode nextNode = front.getNext();

            front.el = -1;
            front.node = null;

            front = nextNode; // front 이동
            return temp;
            
        }

        public int peek() {
            if (this.isEmpty()) return -1;
            return front.getData();
        }

        public int size() {
            int count = 0;
            queNode tempFront = front;
            queNode tempRear = rear;
            while(tempFront != tempRear && tempRear !=null) { //큐가 비어있는 경우도 생각해야함
                count++;
                tempRear = tempRear.getNext();
            }
            return count;
        }
    }

    public void useDeque() { // throws InterruptedException
        Deque<Integer> que = new ArrayDeque<>();
        que.offer(1);
        que.offer(2);

        que.peek(); //front에서 peek == peekFirst
        que.peekLast(); // rear에서 peek

        que.poll(); // front에서 제거
        que.pollLast(); // rear에서 제거
    }
}