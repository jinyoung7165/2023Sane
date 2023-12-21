/*
# n개의 송전탑이 전선을 통해 하나의 트리 형태
# 전선 중 하나 끊어 전력망 네트워크를 2개로 분할
# 두 전력망이 갖게 되는 송전탑의 개수를 비슷하게 맞추자
# 두 망의 송전탑 개수 차를 return
# n=9, wires=[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# -> 3 (6-3) : 3-4 또는 4-7 끊음
# n=4, wires=[[1,2],[2,3],[3,4]]
# -> 0 (2-2) : 2-3 끊음
# 간선을 두 개 이상 가진 노드의 간선을 끊어야 함
# 더 적은 간선 가지는 노드에 대해선 볼 필요 없음
 */
import java.util.LinkedList;
import java.util.Queue;
class Solution {
    static int[][] arr;
    public int solution(int n, int[][] wires) {
        int answer = n;
        arr= new int[n+1][n+1];
        
        //1. 인접행렬에 input
        for(int i=0; i<wires.length; i++){
            arr[wires[i][0]][wires[i][1]]=1;
            arr[wires[i][1]][wires[i][0]]=1;
        }
        
        //2. 선을 하나씩 끊어보며 순회
        int a, b;
        for(int i=0; i<wires.length; i++){
            a= wires[i][0];
            b= wires[i][1];
            
            //선을 하나 끊고
            arr[a][b]=0;
            arr[b][a]=0;
            
            //bfs
            answer= Math.min(answer, bfs(n, a));
            
            //선 다시 복구
            arr[a][b]=1;
            arr[b][a]=1;
        }
        
        return answer;
    }
    
    public int bfs(int n, int start){
        int[] visit= new int[n+1];
        int cnt=1;
        
        Queue<Integer> queue= new LinkedList<>();
        queue.offer(start);
        
        while(!queue.isEmpty()){
            int point= queue.poll();
            visit[point]= 1;
            
            for(int i=1; i<=n; i++){ //point와 연결된 애들 중에 방문한적 없는 노드 전부 큐에 넣기
                if(visit[i]==1) continue;
                if(arr[point][i]==1) {
                    queue.offer(i);
                    cnt++;
                }
            }
        }
        return (int)Math.abs(n-2*cnt); //cnt-(n-cnt);
    }//bfs
}
