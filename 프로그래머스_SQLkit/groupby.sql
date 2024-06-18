-- 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기
-- TIMESTAMP의 경우, MONTH, YEAR, HOUR 사용 가능
/* DATE_FORMAT BEWTWEEN 쓰기 */

SELECT MONTH(START_DATE) MONTH, C.CAR_ID, COUNT(*) RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY  C
WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
AND C.CAR_ID IN (SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
    GROUP BY CAR_ID
    HAVING COUNT(*)>=5)
GROUP BY MONTH(START_DATE), C.CAR_ID
HAVING  RECORDS > 0
ORDER BY MONTH ASC, CAR_ID DESC

-- 즐겨찾기가 가장 많은 식당 정보 출력하기
/* Group by로 묶으면서 max 찾을 때, rest_id는 아무 소용이 없음, 집계 기준 기억해서 다시 where 해줘야 함 */
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) 
IN 
(SELECT FOOD_TYPE, MAX(FAVORITES)
FROM REST_INFO
GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC

-- 저자 별 카테고리 별 매출액 집계하기. price*sales만 쓰면, 첫번째 data의 결과만 보여줌.
-- group by쓸 때, select절이나, having에 반드시 집계 함수!!!!!!!!!!!!!!!! SUM(), COUNT(), AVG(), MIN(), MAX()
SELECT book.AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(price*sales) TOTAL_SALES
from book inner join author on book.author_id=author.author_id
inner join book_sales on book.book_id = book_sales.book_id
where date_format(sales_date, '%Y-%m') = '2022-01'
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID, CATEGORY desc;

-- 가격대별 상품 개수 구하기 (만원 단위)
SELECT
    floor(price/10000)*10000 as price_group
    , count(product_id) as products
from product
group by floor(price/10000)
order by floor(price/10000) asc;

-- 년, 월, 성별 별 상품 구매 회원 수 구하기(사람 수 -> 같은 회원이 여러번 구매 가능 -> distinct!!!!!!!!!!!!!!!)
SELECT YEAR(SALES_DATE) YEAR, MONTH(SALES_DATE) MONTH, GENDER, COUNT(distinct(USER_INFO.USER_ID)) USERS
FROM USER_INFO INNER JOIN ONLINE_SALE 
ON USER_INFO.USER_ID = ONLINE_SALE.USER_ID
    WHERE gender is not null
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER

-- 노선별 평균 역 사이 거리 조회하기 -> concat 때문에 order by에 total_distance 넣으면 문자열 정렬되기 때문에, 다시 써줘야 함
select ROUTE, concat(round(sum(D_BETWEEN_DIST),1),'km') TOTAL_DISTANCE, concat(round(avg(D_BETWEEN_DIST),2),'km') AVERAGE_DISTANCE
from SUBWAY_DISTANCE 
group by ROUTE
order by round(sum(D_BETWEEN_DIST),1) desc

-- 특정 조건을 만족하는 물고기별 수와 최대 길이 구하기
-- null의 경우, 10으로 치환해서 avg 구하라 -> ifnull 사용
select count(*) FISH_COUNT, max(ifnull(length, 10)) MAX_LENGTH, FISH_TYPE
from FISH_INFO
group by FISH_TYPE
having avg(ifnull(length, 10)) >= 33
order by FISH_TYPE