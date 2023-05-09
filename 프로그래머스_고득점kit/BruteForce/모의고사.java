// # 1번 사람: 1,2,3,4,5 순서대로 돌아가먀
// # 2번 사람: 21, 23, 24, 25, 다시 21
// # 3번 사람: 33, 11, 22, 44, 55, 다시 33
// # 01 23 45 67 89
// # 0 2 4 6 8
// # 0 1 2 3 4
// # 정답 배열이 주어졌을 때 가장 많이 맞힌 사람은 누구인지
import java.util.ArrayList;
class Solution {
    public int[] solution(int[] answer) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = new int[3]; // 배열 말고 temp int 3개로 두면 시간 효과 더 좋음

        for(int i=0; i<answer.length; i++) {
            if(answer[i] == a[i%a.length]) {score[0]++;} // (idx % 5) +1 도 가능
            if(answer[i] == b[i%b.length]) {score[1]++;}
            if(answer[i] == c[i%c.length]) {score[2]++;}
        }

        int maxScore = Math.max(score[0], Math.max(score[1], score[2]));

        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<score.length; i++) {
            if(maxScore == score[i]) {list.add(i+1);}
        }
        return list.stream().mapToInt(i->i.intValue()).toArray(); // ArrList -> int[]
    }
}