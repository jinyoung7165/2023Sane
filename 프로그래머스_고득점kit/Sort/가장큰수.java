import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] result = new String[numbers.length];
        for(int i=0; i<numbers.length; i++){ // int->str
            result[i]=String.valueOf(numbers[i]);
        }
        
        Arrays.sort(result,(s1,s2)->(s2+s1).compareTo(s1+s2));
        //(b+a).compareTo(a+b) 을 했을 경우 'b+a'가 더 크다면 자리를 바꿈
        if(result[0].equals("0")) return "0";
        for(String s : result){
            answer+=s;
        }

        return answer;
    }
}
