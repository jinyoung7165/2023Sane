import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        ArrayDeque<int[]> que = new ArrayDeque<int[]>();
        for (int i=0; i<priorities.length; i++) {
            int[] val = {i, priorities[i]};
            que.offer(val);
        }
        int count = 0;
        while (!que.isEmpty()) {
            int[] idxPri = que.poll();
            boolean flag = false;
            for (int[] left : que){
                if (left[1] > idxPri[1]) {
                    flag = true;
                    break;
                }
            }
            if (flag) que.offer(idxPri);
            else {
                count++;
                if (location == idxPri[0]) return count;
            }
        }
        return count;
    }

    public int solutionWithPQ(int[] priorities, int location) {
        PriorityQueue<Integer> que = new PriorityQueue<>(Collections.reverseOrder()); // priority 내림차순 정렬
        for (int i = 0; i < priorities.length; i++) {
            que.add(priorities[i]);
        }
        int count = 0;
        while (!que.isEmpty()) {
            for (int i=0; i<priorities.length; i++) {
                if (priorities[i] == que.peek()) {
                    count++;
                    if (i == location) return count;
                    que.poll();
                }
            }
        }
        return count;
    }
}