import java.util.HashSet;

// 중복 제거 후 종류 수, nums//2 중 min 고르기
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int limit = nums.length / 2;
        // 중복제거 set 만들기
        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        for (int num : numSet) {
            System.out.println(num);
        }
        
        answer = Math.min(numSet.size(), limit);
        return answer;
    }
}