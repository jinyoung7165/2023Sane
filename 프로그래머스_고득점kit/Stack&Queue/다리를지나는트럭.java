// FIFO 두 QUEUE 같이 이동
import java.util.*;;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        ArrayDeque<Integer> que = new ArrayDeque<Integer>();
        for (int i=0;i<bridge_length; i++) {
            que.add(0);
        }
        ArrayDeque<Integer> stack = new ArrayDeque<Integer>();
        for (int truck : truck_weights) {
            stack.add(truck);
        }
        int sum = 0;
        while (!stack.isEmpty()) {
            int truck = stack.peek();
            sum -= que.poll();
            if (sum + truck > weight) {
                que.add(0);
            } else {
                stack.poll();
                que.add(truck);
                sum += truck;
            }
            answer++;
        }
        return answer+bridge_length; // 맨 마지막 트럭을 올리고 다리 길이만큼 이동
    }
}