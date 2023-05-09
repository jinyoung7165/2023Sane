// 정렬을 부수자.

import java.util.ArrayDeque;
import java.util.Arrays;

public class sort {
    
    public static void bubbleSort(String[] args) {
        int []arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
        for (int i=0; i<arr.length-1; i++) { // 각 pass마다 맨 오른쪽에 max가 오게 됨
            boolean swapped = false;
            for (int j=0; j<arr.length-i; j++) { // 각 pass마다 맨 오른쪽 볼 필요 없어짐
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }

            // 해당 pass에서 swap발생x시, 이미 정렬된 상태
            if (swapped == false) break;
            }
        }

    }

    public static void selectionSort(String[] args) {
        
        int []arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
        
        for (int i=0; i<arr.length-1; i++) { // pivot
            int minIndex = i; // 가장 작은 원소 인덱스
            for (int j=i+1; j<arr.length; j++) { // min 위치 찾기
                if (arr[minIndex] > arr[j]) minIndex = j;
            }

            // pivot과 min swap
            int tmp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = tmp;
        }
        System.out.println(Arrays.toString(arr));
    }

    public static void insertionSort(String[] args) {
        
        int []arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
        
        
        for(int i=1; i<arr.length; i++){ // pivot
            for(int j=i; j>=1; j--){ // pivot 왼편, sortedList
                
                if(arr[j] < arr[j-1]){  // sortedList의 원소가 원래 pivot원소보다 크면, 한 칸씩 왼쪽으로 이동
                    int tmp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = tmp;
                }else break;  //자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                
            }
        }
        System.out.println(Arrays.toString(arr));
    }

    public static void shellSort(String[] args) {

        int []arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
        int n = arr.length;

        for (int gap=n/2; gap>0; gap/=2) { // gap: n/2부터 1이 될 때까지 /2
            for (int i=gap; i<n; i++) { // pivot: gap부터 n이 될 때까지 +1
                int j;
                int pivot = arr[i];

                // pivot왼쪽 수가 pivot보다 작으면 끝. gap씩 빼며 pivot에 의해 밀려남
                for (j=i-gap; j>=0&&arr[j]>pivot; j-=gap) {
                    arr[j+gap] = arr[j];
                }
                arr[j+gap] = pivot;
            }
        }

        for (int a: arr) {
            System.out.println(a+" ");
        }

    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length < 2) return arr;

        int mid = arr.length/2;
        int[] leftArr = mergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] rightArr = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));

        int[] result = new int[arr.length];
        int re=0, l=0, r=0; // 결과 배열의 idx, left배열의 idx, right배열의 idx
        while (l<leftArr.length && r<rightArr.length) {
            if (leftArr[l]< rightArr[r]) result[re++] = leftArr[l++];
            else result[re++] = rightArr[r++];
        } 
        while (l<leftArr.length) result[re++] = leftArr[l++];
        while (r<rightArr.length) result[re++] = rightArr[r++];
        return result;
    }

    // in-place update
    public static int[] mergeSortOptimized(int[] arr) {
        div(arr, 0, arr.length);
        return arr;
    }
    // 봐야할 idx만 전달 -> 범위 나누며 쪼갬
    private static void div(int[] arr, int low, int high) {
        if (high-low<2) return;
        int mid = (low+high)/2;
        div(arr, low, mid); // 왼쪽 arr: low~mid
        div(arr, mid, high); // 오른쪽 arr: mid~high
        merge(arr, low, mid, high);
    }
    private static void merge(int[] arr, int low, int mid, int high) {
        int[] temp = new int[high-low];
        int t=0, l=low, r=mid; // temp의 idx, left:low~mid, right:mid~high

        while (l<mid && r<high) {
            if (arr[l]<arr[r]) temp[t++] = arr[l++];
            else temp[t++] = arr[r++];
        }
        // 털기
        while (l<mid) temp[t++] = arr[l++];
        while (r<high) temp[t++] = arr[r++];
        // # x가 [3,4,5,2,3,4]일 때, low1~3high면, temp=[4,5]로 잘림
        // # x[low] = temp[low-low]
        // # x[high] = temp[high-low]
        for (int i=low; i<high; i++) {
            arr[i] = temp[i-low];
        }
    }

    public static void radixSort(String args[]) {

        int arr[] = {7, 5 , 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
        
        for (int pos=1; pos<=10000; pos*=10) { // 1의 자릿수부터 시작
            arr = queSort(arr, pos);
        }
        for (int n:arr) {
            System.out.println(n);
        }
    }
    private static int[] queSort(int[] arr, int pos) {
        int[] out = new int[arr.length]; // 현재 자릿수에 따른 정렬 후 결과
        ArrayDeque[] bucket = new ArrayDeque[10]; // 특정 자릿수의 0-9 bucket
        for (int i=0; i<10; i++) {
            bucket[i] = new ArrayDeque<Integer>();
        }
        
        for (int i=0; i<arr.length; i++) {
            int digit = (arr[i]/pos) % 10; // pos자릿수의 숫자
            bucket[digit].add(arr[i]);
        }
        
        int i=0, idx=0;
        while (i<10) {
            if (!bucket[i].isEmpty()) out[idx++] = (int)bucket[i].poll();
            else i++; // 다음 큐 보자 0-9
        }
        return out;
    }

    public static void countSort(String args[]){ // 계수 정렬
        
        //모든 원소의 값이 0보다 크거나 같다고 가정
        int arr[] = {7, 5 , 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
        
        //모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화, int는 기본적으로 0으로 초기호)
        int []count = new int [Arrays.stream(arr).max().getAsInt()];
        int []result = new int[arr.length];

        for (int i=0; i<arr.length; i++) {
            count[arr[i]] += 1; //각 데이터에 해당하는 인덱스의 값 증가
        }


        for (int i=1; i<count.length; i++) {
            count[i] += count[i-1]; // 빈도수 누적합
        }

        for (int i=arr.length-1; i>=0; i--) {
            int val = arr[i];
            count[val]--;
            result[count[val]] = val;
        }


        for(int i = 0; i < result.length; i++) {
			System.out.print(result[i] + "\t");
		}
    }
}
