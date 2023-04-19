// 총 재생 수 많은 장르부터
// 총 재생 수 많은 곡 2개씩 뽑아라
import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answerArr = new ArrayList<>();

        // 장르별 총 재생수
        HashMap<String, Integer> genCount = new HashMap<>();
        // idx, count 저장한 dic 생성(sort후 idx 찾기 위함)
        HashMap<Integer, Integer> countIdx = new HashMap<>();

        for (int i=0; i<genres.length; i++) {
            genCount.put(genres[i], 
                genCount.getOrDefault(genres[i], 0) + plays[i]);
            countIdx.put(i, plays[i]);
        }

        // valList.sort((s1, s2) -> s1.compareTo(s2));
        // 각 dic에 대한 내림차순 정렬
        ArrayList<String> genSort = new ArrayList<>(genCount.keySet());
        Collections.sort(genSort, (k1, k2) -> 
            genCount.get(k2).compareTo(genCount.get(k1))
        );

        ArrayList<Integer> indexSort = new ArrayList<>(countIdx.keySet());
        Collections.sort(indexSort, (k1, k2) -> 
            countIdx.get(k2).compareTo(countIdx.get(k1))
        );

        for (String gen : genSort) {
            int count = 0; // 해당 장르 몇 개 뽑았는지
            for (int idx : indexSort) {
                if (count<2 && genres[idx].equals(gen)) {
                    answerArr.add(idx);
                    count++;
                }
            }
        }
        int[] answer = new int[answerArr.size()];
        for (int i =0; i<answer.length; i++)
            answer[i] = answerArr.get(i);
        return answer;
    }
}

// python처럼 풀고 싶다
class Solution2 {
    public int[] solution(String[] genres, int[] plays) {
        ArrayList<Integer> answerArr = new ArrayList<>();
        // 장르별 총 재생수
        HashMap<String, Integer> genCount = new HashMap<>();
        // 장르별 idx, count 저장
        HashMap<String, ArrayList<int[]>> detailMap = new HashMap<>();

        for (int i=0; i<genres.length; i++) {
            String key = genres[i];
            genCount.put(key, 
                genCount.getOrDefault(key, 0) + plays[i]);

            int[] countIdx = {i, plays[i]}; // idx, count
            ArrayList<int[]> detail = detailMap.getOrDefault(key, new ArrayList<>());
            detail.add(countIdx);
            detailMap.put(key, detail);
        }


        // genre별 총 재생수에 대한 내림차순 정렬
        ArrayList<String> genSort = new ArrayList<>(genCount.keySet());
        Collections.sort(genSort, (k1, k2) -> 
            genCount.get(k2).compareTo(genCount.get(k1))
        );

        for (String gen : genSort) {
            ArrayList<int[]> detail = detailMap.get(gen);
            Collections.sort(detailMap.get(gen), (e1, e2) ->
                Integer.compare(e2[1], e1[1])
            );
            int count = 0;
            for (int[] de : detail) {
                answerArr.add(de[0]);
                if (1 < ++count) break;
            }
        }

        int[] answer = new int[answerArr.size()];
        for (int i =0; i<answer.length; i++)
            answer[i] = answerArr.get(i);
        return answer;
    }
}