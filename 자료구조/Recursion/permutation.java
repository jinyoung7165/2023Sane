package 자료구조.Recursion;

public class permutation {
    /*
     * 숫자 노드에 대한 순열 -> dfs
     */
    int n, r;
    int[] output, check, arr;
    public void dfs(int depth) {
        if (depth == r) { // 원하는 개수만큼 뽑았다
            for(int num : output) {
                System.out.print(num+" ");
            }
            System.out.println();
        } else {
            for(int i=0; i<n; i++) {
                if (check[i]==0) { // 방문 처리
                    check[i] = 1;
                    output[depth] = arr[i];
                    dfs(depth+1);
                    check[i]=0;
                }
            }
        }
    }


    /**
     * 배열의 원소에 대한 순열 -> 결과 배열
     */
    public void permutationRecur(boolean visited[], int depth) {
        if (depth == r) { // r개만큼 뽑았으면 성공
            for (int i=0; i<r; i++) {
                System.out.print(output[i]+" ");
            }
            System.out.println();
            return;
        }

        for (int i=0; i<arr.length; i++) {
            if (!visited[i]) { // 방문 처리
                visited[i] = true;
                output[depth] = arr[i];
                permutationRecur(visited, depth+1);
                visited[i] = false;
            }
        }
    }
}
