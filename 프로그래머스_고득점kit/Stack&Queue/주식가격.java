import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        Stack<int[]> stack = new Stack<int[]>();
        int length = prices.length;
        int[] answer = new int[length];
        for (int i=0; i<length; i++) { // stack top이 자신보다 작거나 같아야 함
            while (!stack.empty() && stack.peek()[1] > prices[i]) {
                int[] idxPri = stack.pop();
                answer[idxPri[0]] = i-idxPri[0];
            }
            int[] val = {i, prices[i]};
            stack.add(val);
        }
        for (int[] el : stack) {
            answer[el[0]] = length - el[0] - 1;
        }
        return answer;
    }
}