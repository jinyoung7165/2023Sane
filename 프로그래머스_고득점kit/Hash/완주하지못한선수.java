// completion에 없는 유일한 participant 구하라
import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {       
        HashMap<String, Integer> map = new HashMap<>();
        for (String com : completion) {
            map.put(com, map.getOrDefault(com, 0)+1);
        }
        for (String par : participant) {
            int exist = map.getOrDefault(par, 0);
            if (exist == 0) return par;
            map.put(par, --exist);
        }
        return "";
    }
}