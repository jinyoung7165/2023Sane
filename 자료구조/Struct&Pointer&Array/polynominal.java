/*
 * 계수가 0이 아닐 때, 지수와 함께 저장하는 방식 -> pos 맞추지 않는다
 * 조건문 주목! and로 비교할 항 남아있을 때만 while문. 끝나지 않은 다항식은 나중에 털어냄
 */

class Solution { 
    class Single { //단항에 관한 정보
        double coef; // 계수
        int exp; // 지수
        
        public Single() {
            this.coef = 0;
            this.exp = 0;
        }
    
        public Single(double coef, int exp) {
            this.coef = coef;
            this.exp = exp;
        }
    }

    public Single[] add(Single[] poly1, Single[] poly2) {
        final int NEW_POLY_SIZE = poly1.length + poly2.length; // 결과 최대 항 개수
        Single[] newPoly = new Single[NEW_POLY_SIZE];

        int poly1_pos = 0, poly1_size = poly1.length-1;
        int poly2_pos = 0, poly2_size = poly2.length-1;
        int pos = 0; // 덧셈 결과 항의 위치

        // 비교할 항 남아있을 때까지만 반복. 남은 다항식의 항은 나중에 털어냄
        while (poly1_pos<=poly1_pos && poly2_pos<=poly2_size) {
            if (poly1[poly1_pos].exp < poly2[poly2_pos].exp) { // poly2의 현재 항 바로 더함
                newPoly[pos++] = new Single(poly2[poly2_pos].coef, poly2[poly2_pos].exp);
                poly2_pos++; // poly2 다음 항 보자
            }
            if (poly1[poly1_pos].exp > poly2[poly2_pos].exp) { // poly1의 현재 항 바로 더함
                newPoly[pos++] = new Single(poly1[poly1_pos].coef, poly1[poly1_pos].exp);
                poly1_pos++; // poly1 다음 항 보자
            }
            if (poly1[poly1_pos].exp == poly2[poly2_pos].exp) { // 덧셈 가능
                double coef = poly1[poly1_pos].coef + poly2[poly2_pos].coef;
                if(coef != 0)
                    // 계수의 합이 0인 경우 포함시키지 않음
                    newPoly[pos++] = new Single(coef, poly1[poly1_pos].exp);
                poly1_pos++; poly2_pos++;
            }
        }
        // 남은 항 추가
        for(; poly1_pos<=poly1_size; poly1_pos++) {
            newPoly[pos++] = new Single(poly1[poly1_pos].coef, poly1[poly1_pos].exp);
        }
        for(; poly2_pos<=poly2_size; poly2_pos++) {
            newPoly[pos++] = new Single(poly1[poly2_pos].coef, poly1[poly2_pos].exp);
        }
            
        return newPoly;
    }

    public void main() {
        Single[] poly1 = {new Single(2, 5), new Single(3.4, 2)};
        Single[] poly2 = {new Single(2, 4), new Single(-5, 3), new Single(-3, 2), new Single(12, 0)};
        Single[] poly3 = add(poly1, poly2);
        // printPoly(poly3);   
    }
}