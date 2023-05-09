/*
# 한자리 숫자 조각들 붙여 몇 개의 소수 만들 수 있나
# 17 -> 3 [7, 17, 71]
# 011 -> 2 [11, 101] 11==011 
# int(str) 적용 시 자동 맨 앞 0 제거 -> set으로 중복 제거
*/
import java.util.*;
class Solution {
    static HashSet<Integer> set = new HashSet<>(); // 전체 순열
    static boolean[] visit = new boolean[7]; // 주어질 숫자의 최대 길이 7. 방문했는지
    
    public int solution(String numbers) {
        int answer = 0;
        perm(numbers, ""); // 주어진 전체 문자열, 시작 문자열
        
        for (int number: set) { // 순열 탐색
            if(prime(number)) answer++; // 각 숫자 조회하며 소수 체크
        }
        return answer;
  
    }

    //백트래킹 -> 순열 만들어라
	static void perm(String numbers, String prefix) { // 전체 문자열, 현재 문자열
        // 순열에 현재 문자열 추가
        if (!prefix.equals("")) set.add(Integer.valueOf(prefix));
        
        int len = numbers.length(); // 주어진 전체 길이
        for (int i=0; i<len; i++) {
            // 현재 문자열에 i번째 문자 더함
            // 추가한 원소 빼고 전체 문자열 전달
            // 재귀 돌면서 numbers에는 prefix에 더한 원소가 없음
            perm(numbers.substring(0, i)+numbers.substring(i+1, len), prefix+numbers.charAt(i));
        }
    
    }

	//소수 판단. 제곱근까지만 확인
	static boolean prime(int n) {
		if(n<2) return false;
		
		for(int i=2; i<=Math.sqrt(n); i++) {
			if(n % i == 0) return false;
		}
		
		return true;
	}

}