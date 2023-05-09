public class heapSort {
    
    // 부모 인덱스 return
    private static int getParent(int child) {
        return (child-1)/2;
    } 

    // 두 인덱스의 원소 교환
    private static void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    private static void heapify(int[] a, int parentIdx, int lastIdx) {
        /*
         * 현재 트리에서 부모 노드, 자식 노드 인덱스 구함
         * 현재 부모 인덱스가 가장 큰 값 가진다
         */
        int leftChildIdx = 2*parentIdx + 1;
        int rightChildIdx = 2*parentIdx + 2;
        int largestIdx = parentIdx;

        /*
         * left child node와 비교
         * 자식 노드 인덱스가 마지막 인덱스 넘지 않으며
         * 현재 가장 큰 인덱스보다 왼쪽 자식이 더 클 경우
         * largestIdx 갱신
         */
        if (leftChildIdx<lastIdx && a[largestIdx]<a[leftChildIdx]) {
            largestIdx = leftChildIdx;
        }

        /*
         * right child node와 비교
         */
        if(rightChildIdx < lastIdx && a[largestIdx] < a[rightChildIdx]) {
			largestIdx = rightChildIdx;
		}

        /*
         * 부모 노드보다 큰 자식 존재 -> swap
         */
        if (parentIdx!=largestIdx) {
            swap(a, largestIdx, parentIdx);
            heapify(a, largestIdx, lastIdx);
        }
    }

    public static void heapsort(int[] arr) {
        int size = arr.length;
        if (size<2) return;

        // 가장 아래 subtree부터 재구성
        int parentIdx = getParent(size-1); // 가장 마지막 노드의 부모(반드시 존재)
        for (int i=parentIdx; i>=0; i--) { // maxheap 만들기
            heapify(arr, i, size-1); // 부모 노드 값을 1씩 줄이며 heap조건 만족하도록 재구성
        }

        // 최대 힙 구성 후, 오름차순으로 정렬하기 위해
        // 힙의 root노드를 맨 마지막으로 보내고, 마지막 원소 빼고 다시 heap 구성
        for (int i=size-1; i>0; i--) {
            swap(arr, 0, i); // root와 마지막 노드 swap
            heapify(arr, 0, i-1); // 뒤로 간 root빼고 heap화
        }

    }

}
