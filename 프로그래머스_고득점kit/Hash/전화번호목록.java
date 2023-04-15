// 한 번호가 다른 번호의 접두어인지
import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book); // Quick Sort
        // 인접 두 개씩 비교
        for (int i=0; i<phone_book.length-1; i++) {
            if (phone_book[i+1].startsWith(phone_book[i]))
            return false;
        }
        return true;
    }
}