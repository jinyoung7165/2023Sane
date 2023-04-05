import java.util.*;

class Solution {
    public int[] solution(int []arr) {
        List<Integer> tempList = new ArrayList<Integer>();
        int last = -1;
        for (int el : arr) {
            if (last != el) {
                tempList.add(el);
                last = el;
            }
        }

        int[] answer = new int[tempList.size()];
        for (int i = 0 ; i < answer.length ; i++) {
            answer[i] = tempList.get(i);
        }
        return answer;
    }

    public int[] solution2(int []arr) {
        Stack<Integer> stack = new Stack<Integer>();
        for (int el : arr) {
            if (stack.empty() || stack.peek() != el) {
                stack.add(el);
            }
        }

        int[] answer = new int[stack.size()];
        for (int i = 0 ; i < answer.length ; i++) {
            answer[i] = stack.get(i);
        }
        return answer;
    }
}