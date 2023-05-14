SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3
    AND TLNO IS NOT NULL
    AND GENDER = 'W'
ORDER BY MEMBER_ID

---- DATE_FORMAT(바꿀날짜및시각, 형태)
-- %Y = 4자리 년도
-- %y = 2자리 년도

-- %m= 2자리 숫자 월
-- %c = 최소자리 숫자 월
-- %M = 문자열 월
-- %b = 짧은 문자열 월

-- %d = 2자리 숫자 일자
-- %e = 최소자리 숫자 일자

-- %W = 긴 요일 영문
-- %a = 짧은 요일 영문

-- %T = hh:mm:ss
-- %r = hh:mm:ss AM,PM

-- %l = 12시간단위 시
-- %H = 24시간단위 시

-- %i = 분
-- %S = 초

---- 예시
-- SELECT DATE_FORMAT(NOW(), '%y %m %D') AS DATE FROM DUAL
-- = 2016 September 22