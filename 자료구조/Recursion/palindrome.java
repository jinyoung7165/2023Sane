package 자료구조.Recursion;

public class palindrome {
    /*
    * 반복문
    */
    public boolean isPalindrome(String text) {
        String cleanString = text.toLowerCase().replaceAll("[^0-9a-z]", "");
        int length = cleanString.length();
        int start = 0, end = length-1;
        while (start < end) { // 양끝 계속 확인
            char startChar = cleanString.charAt(start++);
            char endChar = cleanString.charAt(end--);
            if (startChar != endChar) return false;
        } 
        return true;
    }
    /*
    * 문자열 뒤집기 (stringbuilder -> append 사용)
    */
    public boolean isPalindromeReverseString(String text) {
        StringBuilder reverseString = new StringBuilder();
        String cleanString = text.toLowerCase().replaceAll("[^0-9a-z]", "");
        char[] charArr = cleanString.toCharArray(); //하나하나 떼서 reverse에 붙이기 위함
        for (int i=charArr.length-1; i>=0; i--) { // charArr 뒤집기
            reverseString.append(charArr[i]);
        }
        return reverseString.toString().equals(cleanString);
    }

    /*
    * 문자열 뒤집기 (stringbuilder -> reverse 사용) -> 제일 나음
    */
    public boolean isPalindromeReverse2(String text) {
        String cleanString = text.toLowerCase().replaceAll("[^0-9a-z]", "");
        StringBuilder reverseString = new StringBuilder(cleanString).reverse();
        return reverseString.toString().equals(cleanString);
    }

    /*
    * 재귀(start, end 매개변수로 전달)
    */
    private boolean recursivePalindrome(String text, int start, int end) {
        if (text.length() < 2) return true; // text 내부로 들어가다가 길이 0/1 되면 true
        if ((text.charAt(start) != text.charAt(end))) return false;
        if (start < end) return recursivePalindrome(text, start+1, end-1);
        return true;
    }

    public boolean isPalindromeRecursive(String text) {
        String cleanString = text.toLowerCase().replaceAll("[^0-9a-z]", "");
        System.out.println(cleanString);
        return recursivePalindrome(cleanString, 0, cleanString.length()-1);
        // 재귀 함수에 start, end 전달 필수!
    }
}
