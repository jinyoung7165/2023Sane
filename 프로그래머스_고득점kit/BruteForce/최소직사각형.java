/*
# 명함의 가로 세로 길이가 주어짐 -> 눕혀서 수납 가능
# 모두 수납할 수 있는 최소 크기의 직사각형 만들어라
# [[60, 50], [30, 70], [60, 30], [80, 40]]-> 4000(80*50)
 */
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int max_v=0;
        int max_h=0;
        for(int i=0;i<sizes.length;i++){
            int v=Math.max(sizes[i][0],sizes[i][1]);
            int h=Math.min(sizes[i][0],sizes[i][1]);
            max_v=Math.max(max_v,v);
            max_h=Math.max(max_h,h);
        }
        return answer=max_v*max_h;
    }
}