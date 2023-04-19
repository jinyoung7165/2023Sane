import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> que = new PriorityQueue<Integer>();
        for (int sco : scoville) {
            que.add(sco);
        }
        while (que.size() > 1 && que.peek() < K) {
            que.add(que.poll() + que.poll()*2);
            answer += 1;
        }
        return que.peek()>=K ? answer : -1;
    }
}