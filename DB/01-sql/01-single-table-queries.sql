-- 01. Querying data

SELECT LastName From employees;

SELECT
    LastName, FirstName
FROM
    employees;

SELECT * FROM employees;

SELECT FirstName AS 이름 FROM employees;

SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks;

-- 02. Sorting data
# SELECT statement 실행 순서 : 1. 테이블에서(FROM) 2. 조회하여(SELECT) 3. 정렬(ORDER BY)

SELECT FirstName FROM employees ORDER BY FirstName ASC;

SELECT FirstName FROM employees ORDER BY FirstName DESC;

# country 하나의 필드당 city 오름차순
SELECT Country, City FROM customers ORDER BY Country DESC, City ASC

SELECT Milliseconds / 60000 AS '재생 시간(분)' FROM tracks ORDER BY "Milliseconds" DESC;

# 정렬에서의 NULL
# NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
SELECT reportsTo FROM employees ORDER BY "ReportsTo"



-- NULL 정렬 예시

-- 03. Filtering data

-- Clause (절)
--  - DISTINCT
--  - WHERE
--  - LIMIT

-- Operator (연산자) 
--  - BETWEEN
--  - IN
--  - LIKE

# DISTINCT : 조회 결고에서 중복된 레코드 제거
# 여러 필드 조회하면 같은 필드 중복이 제거. 따라서 하나의 필드에서는 중복 나올 수 있음
SELECT DISTINCT Country, City FROM customers ORDER BY "Country";

# WHERE : 조회 조건
# 테이블 customers에서 City 필드 값이 'Prague'인 데이터의 LastName, FirstName, City 조회

SELECT LastName, FirstName, City FROM customers WHERE City = 'Prague';

# 테이블 customers에서 City 필드 값이 'Prague'가 아닌 데이터의 LastName, FirstName, City 조회
SELECT LastName, FirstName, City FROM customers WHERE City != 'Prague';

# 테이블 customers에서 Company 필드 값이 NULL이고 Country 필드 값이 'USA'인 데이터의 LastName, FirstName, Company, Country 조회
# NULL은 실제 값이 아니므로 NULL = NULL도 틀림. 따라서 명시적으로 IS NULL 또는 IS NOT NULL 사용
SELECT LastName, FirstName, Company, Country FROM customers WHERE "Company" IS NULL AND "Country" = 'USA'

SELECT LastName, FirstName, Company, Country FROM customers WHERE "Company" IS NULL OR "Country" = 'USA'

# 테이블 tracks에서 Bytes 필드 값이 10000이상 500000 이하인 데이터의 Name, Bytes 조회
SELECT Name, Bytes FROM tracks WHERE "Bytes" >= 10000 AND "Bytes" <= 500000;

SELECT Name, Bytes FROM tracks WHERE "Bytes" BETWEEN 10000 AND 500000;

# 테이블 tracks에서 Bytes 필드 값이 10000이상 500000 이하인 데이터의 Name, Bytes를 Bytes 기준으로 조회
# ORDER BY는 WHERE절 뒤로!
SELECT Name, Bytes FROM tracks WHERE "Bytes" BETWEEN 10000 AND 500000 ORDER BY "Bytes";

# 테이블 customers에서 Country 필드 값이 Canada 또는 Germany 또는 France 인 데이터의 LastName, FirstName, Country 조회
SELECT LastName, FirstName, Country From customers WHERE "Country" = 'Canada' OR "Country" = 'Germany' OR "Country" = 'France';

# 포함 관계 연산자 이용
SELECT LastName, FirstName, Country From customers WHERE Country IN ('Canada', 'Germany', 'France');

# 포함 아닌것
SELECT LastName, FirstName, Country From customers WHERE Country NOT IN ('Canada', 'Germany', 'France');

# 테이블 customers에서 LastName 필드 값이 'son' 으로 끝나는 데이터의 LastName, FirstName 조회
# LIKE는 값이 특정 패턴에 일치하는지 확인함!
# % : 0개 이상의 문자열과 일치하는지 확인
# _ : 단일 문자와 일치하는지 확인
# _son이면 son앞에 반드시 문자 하나 존재해야함
SELECT
	LastName, FirstName
FROM
	customers
WHERE
	LastName LIKE '%son';

# 테이블 customers에서 FirstName 필드 값이 4자리면서 'a'로 끝나는 데이터의 LastName, FirstName조회
SELECT
	LastName, FirstName
FROM
	customers
WHERE
FirstName LIKE '___a';

# 전화번호의 경우 %와 _ 적절히 사용해야함

# LIMIT : 조회하는 레코드 수를 제한
# LIMIT : 2, 5 면 2칸 건너뛰고 5칸

# 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 7개만 조회
SELECT
	TrackId, Name, Bytes
FROM 
	tracks
ORDER BY
	Bytes DESC
LIMIT 7;

# 4번째부터 7번째 데이터만 조회
SELECT
	TrackId, Name, Bytes
FROM 
	tracks
ORDER BY
	Bytes DESC
LIMIT 3, 4;

-- 04. Grouping data
# GROUP BY : 집계 함수와 함께 그룹화하여 요약본 생성
# Country 필드를 그룹화

# 중복제거 + 정렬됨. 중복제거 : DISTINT -> 정렬은 안됨 
SELECT
	Country
FROM
	customers
GROUP BY
	"Country";

# COUNT 함수는 그룹별로 묶은 총 수를 반환
SELECT
	Country, COUNT(*)
FROM
	customers
GROUP BY
	"Country";


# 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
SELECT
	Composer, AVG(Bytes) AS avgOfBytes
FROM
	tracks
GROUP BY
	"Composer"
ORDER BY
	AVG(Bytes) DESC;

# 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10 미만인 데이터 조회
# 이렇게 쓰면 에러남
SELECT
	Composer, AVG(Bytes) AS avgOfBytes
FROM
	tracks
WHERE
	avgOfMinute < 10
GROUP BY
	"Composer";

# WHERE는 적용 시점이 FROM과 JOIN 등의 단계 이후, GROUP BY 이전에 적용
# HAVING은 그룹핑 및 집계 함수 적용 후에 조건 평가하므로 HAVING 사용

SELECT
	Composer, AVG(Bytes) AS avgOfBytes
FROM
	tracks
GROUP BY
	"Composer";
HAVING
	avgOfMinute < 10;