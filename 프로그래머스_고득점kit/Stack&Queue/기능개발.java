import java.util.Arrays;

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