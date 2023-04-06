package 자료구조.Recursion;

import java.util.ArrayList;

public class hanoi {
    ArrayList<int[]> result;
    public int[][] solution(int n) {
        result = new ArrayList<>(); //[[start,end]]
        han(1, 2, 3, n); // n개의 원판 1->2->3으로 이동
        int[][] answer = new int[result.size()][2]; //start, end 리스트 저장
        for (int i=0; i<result.size(); i++) {
            answer[i][0] = result.get(i)[0];
            answer[i][1] = result.get(i)[1];
        }
        return answer;
    }
    
    private void han(int start, int mid, int end, int n){
        int[] move = {start, end};
        if (n == 1) result.add(move); // 원판 하나면 그냥 이동
        else {
            han(start, end, mid, n-1); //start->mid 이동
            result.add(move); // 자신 1->3 바로 이동
            han(mid, start, end, n-1); //mid->end 이동
        }

    }
}
