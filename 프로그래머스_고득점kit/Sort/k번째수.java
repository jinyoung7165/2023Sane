import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int i = 0;
        for (int[] c: commands) {
            int[] tmp = Arrays.copyOfRange(array, c[0]-1, c[1]);
            Arrays.sort(tmp);
            answer[i++] = tmp[c[2]-1];
        }
        return answer;
    }
    
    // copyOfRange, Arrays.sort 안 쓰고 직접 구현해본다면?
    // lib 안 쓰니 훨 빠름
    public int[] solution2(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int i = 0;
        for (int[] c: commands) {
            int gap = c[1] - c[0] + 1; // 새로 만들 배열의 길이
            if (gap == 1) { // 원소가 하나 -> 바로 삽입
                answer[i++] = array[c[0]-1];
                continue;
            }

            int[] tmp = new int[gap]; // c[0]-1~c[1] 자를 것
            int t = 0;
            for (int j=c[0]-1; j<c[1]; j++) {
                tmp[t++] = array[j];
            }

            // Arrays.sort(tmp) 대신 quickSort 직접 구현
            quickSort(tmp, 0, gap-1); // 0~gap-1까지의 tmp 정렬

            answer[i++] = tmp[c[2]-1];
            //i++ = commands 순회
        }
        return answer;
    }

    private void quickSort(int[] arr, int low, int high) {
        int l = low, r = high;
        int pivot = arr[(low+high)/2];

        do {
            while (arr[l] < pivot) l++;
            while (arr[r] > pivot) r--;
            if (l <= r) {
                int tmp = arr[l];
                arr[l] = arr[r];
                arr[r] = tmp;
                l++;
                r--;
            }
        } while (l <= r);

        // l,r 교차 후 low~r, l~high 쪼갬
        if (low < r) quickSort(arr, low, r);
        if (high > l) quickSort(arr, l, high);
    }
}

