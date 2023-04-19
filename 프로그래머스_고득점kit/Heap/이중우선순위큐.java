import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        PriorityQueue<Integer> maxQ = new PriorityQueue<Integer>(Collections.reverseOrder());
        PriorityQueue<Integer> minQ = new PriorityQueue<Integer>();

        for (String op : operations) {
            if (op.equals("D 1")) { // 최대 힙 제거
                if (!maxQ.isEmpty()) {
                    maxQ.poll();
                    // 혹은 java의 pq에선 remove 바로 사용 가능
                    //minQ.remove(el)
                    if (maxQ.isEmpty() ||  maxQ.peek() < minQ.peek()) {
                        maxQ.clear();
                        minQ.clear();
                    }
                }
            } else if (op.equals("D -1")) { // 최소 힙 제거
                if (!minQ.isEmpty()) {
                    minQ.poll();
                    if (minQ.isEmpty() || maxQ.peek() < minQ.peek()) {
                        maxQ.clear();
                        minQ.clear();
                    }
                }
            } else {
                int num = Integer.valueOf(op.split(" ")[1]);
                maxQ.add(num);
                minQ.add(num);
            }
        }

        if (!minQ.isEmpty()) {
            answer[0] = maxQ.peek();
            answer[1] = minQ.peek();
        }
        return answer;
    }



}