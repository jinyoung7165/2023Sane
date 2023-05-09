public class quickSort { // 이런 게 있구나,, 공부하자
	
	public static void sort(int[] a) {
		m_pivot_sort(a, 0, a.length - 1); // 중간 pivot
	}
	

	private static void m_pivot_sort(int[] a, int lo, int hi) {

		if(lo >= hi) {
			return;
		}
		
		/*
		 * 피벗을 기준으로 요소들이 왼쪽과 오른쪽으로 약하게 정렬 된 상태로
		 * 만들어 준 뒤, 최종적으로 pivot의 위치를 얻는다.
		 * 
		 * 그리고나서 해당 피벗을 기준으로 왼쪽 부분리스트와 오른쪽 부분리스트로 나누어
		 * 분할 정복을 해준다.
		 */
        
		int pivot = partition(a, lo, hi);	
		
		m_pivot_sort(a, lo, pivot-1); // lo~pivot-1
		m_pivot_sort(a, pivot, hi); // pivot~hi
	}
	
	
	
	private static int partition(int[] arr, int low, int high) {
        int pivot = arr[(low + high) / 2]; // 중간 pivot
        while (low <= high) { // 교차할 때까지 반복
            while (arr[low] < pivot) low++; // 왼쪽에서 pivot보다 큰 수 찾거나 pivot까지 오는 것 기다림
            while (arr[high] > pivot) high--;
            if (low <= high) { // 교차해 지나치지 않았으면
                swap(arr, low, high); // 약한 정렬
                low++;
                high--;
            }
        }
        return low; // 교차해 지나쳤다면 low를 다음 pivot으로 삼음
    }
	
	
	
	private static void swap(int[] a, int i, int j) {
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
	
}