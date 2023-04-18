import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] date = new int[100];
        int now = -1; // 현재까지 누적 date
        for(int i=0; i < progresses.length; i++) {
            while(progresses[i] + (now*speeds[i]) < 100) {
                now++; // 달성 가능할 때까지 누적
            }
            date[now]++; // 해당 date의 count 누적
        }
        return Arrays.stream(date).filter(i -> i!=0).toArray();
    }
}


class Solution2 {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answerArr = new ArrayList<Integer>();
        Deque<Integer> que = new ArrayDeque<Integer>(); 
        // 마지막 date, 누적 기능 수 저장해야 하는데 que.clear로 해결
        
        for (int i=0; i<progresses.length; i++) {
            int date = Math.abs((progresses[i]-100)/speeds[i]);
            if (!que.isEmpty() && que.peek() < date)  { // 새로운 날짜 update
                answerArr.add(que.size()); // 누적 기능 수
                que.clear();
            }
            que.offer(date); // 해당 기능에 소요되는 date 넣음
        }
        answerArr.add(que.size()); // 누적 기능 수
        
        int[] answer = new int[answerArr.size()];
        for (int i=0; i<answer.length; i++) {
            answer[i] = answerArr.get(i);
        }
        return answer;
    }
}