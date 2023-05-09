/*
# 일정 피로도 이용해 던전 탐험
# 각 던전마다 필요한 준비물 최소 피로도, 종료시 소모 피로도
# 던전을 최대한 여러 개 탐험하려고 함 -> 최대 던전 수
# 최소 필요 >= 소모 피로도
# 80, [[80,20],[50,40],[30,10]] -> 3(1->3->2 순 탐색)
# 최장 경로 -> heapq 생각 버리자!!! DFS
 */
class Solution {  
    static boolean[] visited;  
    static int answer = 0;  
  
    public int solution(int k, int[][] dungeons) {  
        visited = new boolean[dungeons.length];  
        dfs(0, k, dungeons); // 방문 수, 기력, 던전
        return answer;  
    } 

    static void dfs(int depth, int fatigue, int[][] dungeons){
        if (depth > answer) answer = depth; // 최대 방문 수 갱신
        for (int i = 0; i < dungeons.length; i++){  
            // 방문하지 않았고, 기력이 충분할 때
            if (!visited[i] && fatigue>=dungeons[i][0]) {
                visited[i] = true;  
                dfs(depth + 1, fatigue - dungeons[i][1], dungeons);  
                visited[i] = false;  
            }
        }
    }
}