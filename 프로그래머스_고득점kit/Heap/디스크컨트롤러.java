import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0; // 총 대기 시간
        int now = 0; // 현재 시간
        Arrays.sort(jobs, (a, b) -> { // start, dur 순 정렬
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]); // dur 비교
            return Integer.compare(a[0], b[0]); // start 비교
        });
        ArrayDeque<int[]> job_que = new ArrayDeque<>(); // 요청 대기 큐(dur, start). start, dur 순 정렬
        PriorityQueue<int[]> que = new PriorityQueue<int[]>((a, b) -> {
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]); // start 비교
            return Integer.compare(a[0], b[0]); // dur 비교
        }); // 실행 큐(dur, start). dur, start 순 정렬
        
        for (int[] task : jobs) {
            int[] val = {task[1], task[0]};
            job_que.add(val);
        }
        que.add(job_que.poll());

        while (!que.isEmpty()) {
            int[] task = que.poll();
            int dur = task[0], start = task[1];
            now = Math.max(now + dur, start + dur); // req가 이전에 발생(겹쳐진 작업) or req가 now보다 나중(겹치지 않은 작업)
            answer += now - start;

            while (!job_que.isEmpty() && job_que.peek()[1] <= now) { // 이전에 들어온 요청 있으면 실행 큐 삽입
                que.add(job_que.poll());
            }

            if (que.isEmpty() && !job_que.isEmpty()) { // 실행 큐 깔끔하게 끝. 겹치지 않는 이후의 작업이 남았을 때
                que.add(job_que.poll());
            }
        }

        
        return (int) answer / jobs.length;
    }
}