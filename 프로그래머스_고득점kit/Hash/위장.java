// 종류당 1/0개 입을 수 있고, 전체 중 하나는 입어야 함
import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        for (String[] clo : clothes) {
            map.put(clo[1], map.getOrDefault(clo[1], 1)+1);
        }

        for (Integer v : map.values()){
            answer *= v;
        }
        return answer-1;
    }
}