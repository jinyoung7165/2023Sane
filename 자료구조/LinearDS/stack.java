package 자료구조.LinearDS;

import java.util.Stack;

public class stack { // 배열 스택으로 구현 -> data 접근 속도 빠름, but, 배열 크기정해짐
    int top; // top idx
    int size; // 원소 개수
    int[] st;
    
    public stack(int size) {
        this.size = size;
        st = new int[size];
        top = -1;
    }

    public void push(int el) {
        this.st[top++] = el;
    }

    public int pop() {
        int el = this.st[top];
        this.st[top--] = 0;
        return el;
    }


    public void useStack() {
        Stack<Integer> st = new Stack<>(); 
        // push, pop, peek, empty, search(idx찾아줌)
        for(int i=1; i<=5 ; i++) {
            st.push(i);
            System.out.println(st.peek()); // top 읽기
        }
    }

    /**
     * linked List로 구현하기 -> stack에 들어가는 data 양 한정x(Java제공 stack은 linkedlist). 조회 느림
     */
    public class Node {
        private int el;
        private Node node; // 이전 node 가리킴

        public Node(int item) {
            this.el = item;
            this.node = null;
        }
        protected int getData() {
            return this.el;
        }
        protected void linkNode(Node node) {
            this.node = node;
        }
        protected Node getNext() {
            return this.node;
        }
    }

    public class linkedListStack {
        Node top; // 가장 최근에 추가된 노드

        public linkedListStack() {
            this.top = null; // 초기에 null. 비어있는 stack
        }

        public void push(int data) {
            Node node = new Node(data); // node 생성
            node.linkNode(top); // 이전 top을 나와 연결
            top = node; // 내가 top이 됨
        }

        public int pop() {
            int now_top = this.peek();
            top = top.getNext(); // 이전 node를 가리킴
            return now_top;
        }

        public int peek() {
            return top.getData();
        }
    }


}
