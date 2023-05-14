-- 코드를 입력하세요
SELECT A.BOOK_ID, B.AUTHOR_NAME, DATE_FORMAT(A.PUBLISHED_DATE, '%Y-%m%-%d') AS PUBLISHED_DATE
FROM BOOK A
JOIN AUTHOR B
ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE A.CATEGORY = '경제'
GROUP BY A.BOOK_ID
ORDER BY A.PUBLISHED_DATE ASC