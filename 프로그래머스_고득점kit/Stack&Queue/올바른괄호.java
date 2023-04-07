class Solution {
    boolean solution(String s) {
        int st = 0;
        // charArr로 안 바꾸려면, s.charAt 쓰면 됨
        char[] charArr = s.toCharArray();
        for (char c : charArr) {
            if (c == ')') st--;
            else st++;
            if (st < 0) return false;
        }
        return st==0;
    }
}