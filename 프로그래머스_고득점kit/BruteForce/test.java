/*
 * 더 적은 간선을 가지는 노드에 대해선 끊을 필요 없음
 */

 import java.util.ArrayList;
 import java.util.Arrays;
 
  class Solution {
  
      static ArrayList<Integer>[] graph; //(n+1)*연결된 수 모름
      static int answer;
  
      public int solution(int n, int[][] wires) {
          answer = n;
          graph = new ArrayList[n+1];
          for (int i=1; i<=n; i++) {
             graph[i] = new ArrayList<>();
          }
 
          int[] count = new int[n+1]; // 각 노드 간선 수
          for (int[] wire : wires) { // graph의 노드 간 연결
             int v1 = wire[0];
             int v2 = wire[1];
             graph[v1].add(v2);
             graph[v2].add(v1);
             count[v1]++;
             count[v2]++;
          }
  
          // 가장 많은 연결 수 가진 노드만 관심
          int maxLen = Arrays.stream(count).max().getAsInt();
          for (int i=1; i<=n; i++) {
              if (count[i] == maxLen) {
                 boolean[] visited = new boolean[n+1];
                 for (int j=0; j<graph[i].size(); j++) { // 해당 노드와 연결된 간선 끊어보자
                    int temp = graph[i].get(j); 
                    graph[i].remove(j);
                     answer = Math.min(dfs(i, 1, visited), answer);
                     graph[i].add(temp);
                 }
                 
             }
          }
  
          return answer;
      }
  
  
      // 가장 많은 간선 가진 노드로부터 떨어져 나온 노드
      public int dfs(int node, int depth, boolean[] visited) { // 출발 노드, 이동 수 
         visited[node] = true;
         for (int next : graph[node]) {
             System.out.println(next);
             if(!visited[next]) { 
                 dfs(next, ++depth, visited);
             
            }
        }
  
         return Math.abs(2*depth - graph.length + 1);
    }
  }