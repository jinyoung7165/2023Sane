import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int hIdx = 0;
        Arrays.sort(citations); // 오름차순
        for (int i=citations.length-1; i>=0; i--) {
            if (citations[i] > hIdx) hIdx++;
        }
        return hIdx;
    }
}