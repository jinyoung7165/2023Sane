package 자료구조.Recursion;
// 나머지가 0이될 때까지 큰 수에서 작은 수를 나눔
public class gcd {
    private static int recursive(int a, int b){
        if (b == 0) return a;
        return recursive(b, a % b);
    }

    private static int iterative(int a, int b) {
        int tmp, n; //a에 큰 값을 위치시키기 위한 조건이다.
        if (a < b) { tmp = a; a = b; b = tmp; }
        while (b != 0) { n = a % b; a = b; b = n; }
        return a;
    }

    // 최소 공배수
    public static int lcm(int x, int y) {
        //0이 아닌 두 수의 곱 / 두 수의 최대공약수
        return (x * y) / recursive(x, y);
    }
}
