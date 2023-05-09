/*
# 중앙이 노란색, 테두리가 갈색으로 색칠된 격자
# 10, 2 -> [4,3]
# 1 1 1 1
# 1 0 0 1
# 1 1 1 1
# 두 색 격자의 수 주어질 때, 카펫의 가로, 세로 크기는?
# 가로 >= 세로
# 전체 = yellow + brown = w*h
# yellow = (w-2)*(h-2)
# brown = 전체 - yellow
 */
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int sum = brown + yellow;

        // w,h는 sum의 약수. 둘 다 최소 3
        for (int i = 3; i < sum; i++) { // 최소 3
            int j = sum / i; // 근데 나눠떨어져야 함
            if (sum % i == 0 && j >= 3) { 
                int center = (i - 2) * (j - 2);
                
                if (center == yellow) {
                    answer[0] = Math.max(i, j); 
                    answer[1] = Math.min(i, j);
                    return answer;
                }
            }
        }
        return answer;
    }
}