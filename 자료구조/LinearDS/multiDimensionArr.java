package 자료구조.LinearDS;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class multiDimensionArr {

    // 2차원 배열
    public int[][] defaultArr() {
        ArrayList<int[]> result = new ArrayList<>();
        // result에 대한 process -> int[] v = {v1, v2}를 result에 add ...
        int[][] answer = new int[result.size()][2]; // 변수 생성 & 미리 객체 생성->메모리 할당
        // {{1,2}, {2,3}} 형태
        // 초기값 없이 초기화 시 반드시 ! 길이 ! 필요
        // 두 번째 차원부터는 따로 지정 가능
        /* int[][] arr = new int[3][];
            arr[0] = new int[4];
            arr[1] = new int[5];
            arr[2] = new int[6];
         */
        for (int i=0; i<result.size(); i++) {
            answer[i][0] = result.get(i)[0]; // ArrList의 원소 (get)가져와 대입
            answer[i][1] = result.get(i)[1];
        }
        return answer;
    }
    
    // 2중 ArrList
    public ArrayList<String>[] arrList() {
        ArrayList<String>[] result = new ArrayList[2]; // 전체 배열 크기 알아야 함
        for (int i=0; i<3; i++) {
            result[i] = new ArrayList<String>(); // 원소를 인스턴스로 지정
        }
        result[0].add("첫 번째");
        result[0].add("hoo");
        result[0].add("hahah");

        for (int i=0; i<2; i++) {
            for (int j=0; j<result[i].size(); j++) {
                System.out.println(result[i].get(i));
            }
        }

        return result;
    }

    // 2중 ArrList -> 길이 몰라도 됨
    public List<ArrayList<Integer>> arrList2() {
        List<ArrayList<Integer>> a = new ArrayList<>(); 

        ArrayList<Integer> al1 = new ArrayList<Integer>();
        ArrayList<Integer> al2 = new ArrayList<Integer>();
        
        al1.add(1);
        al1.add(2);
        al1.add(3);
        
        al2.add(4);
        al2.add(5);

        a.add(al1);
        a.add(al2);

        for(ArrayList<Integer> obj: a){
            for(Integer num : obj){
                System.out.print(num + " "); 
            }
            System.out.println(); 
        }

        return a;
    }

    // defaultDict(str-list)
    public HashMap<String, ArrayList<String>> joinDic(String[] arr) {
        HashMap<String, ArrayList<String>> dic = new HashMap<>();
        for (int i=0; i<arr.length; i++) {
            String[] line = arr[i].split(",");
            String key = line[5];

            ArrayList<String> list = new ArrayList<>();
            if (dic.containsKey(key)) {
                list = dic.get(key); // 있던 내용 가져옴
                list.add(line[13]);
            } else {
                list.add(line[13]);
            }
            dic.put(key, list);
        }
        for (String key : dic.keySet() ) {  //⑦
            System.out.println(key);
        }
        return dic;
    }
}
