# SQL 02 - 데이터베이스 관리

## 📚 목차

1. **Managing Tables**
   - Create a table
   - Modifying table fields
   - Delete a table

2. **Modifying Data**
   - Insert data
   - Update data
   - Delete data

3. **Multi table queries**
   - Join
   - Joining tables

4. **참고**
   - 타입 선호도
   - NOT NULL
   - 날짜와 시간

---

## 🎯 학습 목표

- SQL의 기본 문법 구조를 이해한다
- CREATE TABLE 문을 사용하여 테이블을 생성할 수 있다
- INSERT 문을 활용하여 테이블에 데이터를 삽입할 수 있다
- SELECT 문으로 테이블에서 원하는 데이터를 조회할 수 있다
- ALTER TABLE 문을 통해 테이블 구조를 수정할 수 있다
- DROP TABLE 문으로 테이블을 삭제할 수 있다
- UPDATE와 DELETE 문으로 데이터를 수정하거나 삭제할 수 있다
- INNER JOIN과 LEFT JOIN의 차이점을 이해하고 사용할 수 있다
- 제약 조건(CONSTRAINT)의 의미를 알고 테이블 생성 시 적용할 수 있다

---

## 📊 SQL Statements 유형

| 유형 | 역할 | SQL 키워드 |
|------|------|------------|
| **DDL** (Data Definition Language) | 데이터의 기본 구조 및 형식 변경 | CREATE, DROP, ALTER |
| **DQL** (Data Query Language) | 데이터 검색 | SELECT |
| **DML** (Data Manipulation Language) | 데이터 조작 (추가, 수정, 삭제) | INSERT, UPDATE, DELETE |
| **DCL** (Data Control Language) | 데이터 및 작업에 대한 사용자 권한 제어 | COMMIT, ROLLBACK, GRANT, REVOKE |

---

## 1️⃣ Managing Tables

### CREATE TABLE

#### 📝 Syntax

```sql
CREATE TABLE table_name (
    column_1 data_type constraints,
    column_2 data_type constraints,
    ...
);
```

- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건(constraints) 작성

#### 💡 예시: examples 테이블 생성

```sql
CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);
```

#### 🔍 테이블 구조 확인 (PRAGMA)

```sql
PRAGMA table_info('examples');
```

**결과:**

| cid | name | type | notnull | dflt_value | pk |
|-----|------|------|---------|------------|----|
| 0 | ExamId | INTEGER | 0 | NULL | 1 |
| 1 | LastName | VARCHAR(50) | 1 | NULL | 0 |
| 2 | FirstName | VARCHAR(50) | 1 | NULL | 0 |

> **TIP:** `cid`는 Column ID를 의미하며 각 컬럼의 고유한 식별자를 나타내는 정수 값입니다. 직접 사용하지 않으며 PRAGMA 명령과 같은 메타데이터 조회에서 출력 값으로 활용됩니다.

---

### 📌 SQLite 데이터 타입

| 데이터 타입 | 설명 |
|------------|------|
| **NULL** | 아무런 값도 포함하지 않음을 나타냄 |
| **INTEGER** | 정수 |
| **REAL** | 부동 소수점 |
| **TEXT** | 문자열 |
| **BLOB** | 이미지, 동영상, 문서 등의 바이너리 데이터 |

---

### 🔒 제약 조건 (Constraints)

**제약 조건이란?**
- 테이블의 필드에 적용되는 규칙 또는 제한 사항
- 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장

#### 대표 제약 조건 3가지

| 제약 조건 | 설명 | 특징 |
|----------|------|------|
| **PRIMARY KEY** | 해당 필드를 기본 키로 지정 | INTEGER 타입에만 적용됨 (INT, BIGINT 등은 적용 안됨) |
| **NOT NULL** | 해당 필드에 NULL 값을 허용하지 않음 | - |
| **FOREIGN KEY** | 다른 테이블과의 외래 키 관계를 정의 | - |

---

### ⚡ AUTOINCREMENT 키워드

**특징:**
- 필드의 자동 증가를 나타내는 특수한 키워드
- 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
- 주로 PRIMARY KEY 필드에 적용

**동작 방식:**
- `INTEGER PRIMARY KEY AUTOINCREMENT`가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
- 삭제된 값은 무시되며 재사용할 수 없게 됨

---

### ALTER TABLE

**역할:** 테이블 및 필드 조작

#### 1️⃣ ADD COLUMN - 필드 추가

```sql
ALTER TABLE table_name
ADD COLUMN column_definition;
```

**예시:**
```sql
ALTER TABLE examples
ADD COLUMN Country VARCHAR(100) NOT NULL DEFAULT 'default value';
```

#### 2️⃣ RENAME COLUMN - 필드 이름 변경

```sql
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;
```

**예시:**
```sql
ALTER TABLE examples
RENAME COLUMN Address TO PostCode;
```

#### 3️⃣ DROP COLUMN - 필드 삭제

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

**예시:**
```sql
ALTER TABLE examples
DROP COLUMN PostCode;
```

#### 4️⃣ RENAME TO - 테이블 이름 변경

```sql
ALTER TABLE table_name
RENAME TO new_table_name;
```

**예시:**
```sql
ALTER TABLE examples
RENAME TO new_examples;
```

---

### DROP TABLE

**역할:** 테이블 삭제

```sql
DROP TABLE table_name;
```

**예시:**
```sql
DROP TABLE examples;
```

> ⚠️ **주의:** 한 번 삭제된 테이블은 복구할 수 없습니다!

---

## 2️⃣ Modifying Data

### INSERT

**역할:** 테이블에 새 레코드 삽입

#### Syntax

```sql
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```

#### 예시

```sql
INSERT INTO articles (title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01');
```

**여러 행 삽입:**
```sql
INSERT INTO articles (title, content, createdAt)
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');
```

---

### UPDATE

**역할:** 테이블 레코드 수정

#### Syntax

```sql
UPDATE table_name
SET column_name = expression,
    [column_name = expression, ...]
[WHERE condition];
```

#### 예시

```sql
UPDATE articles
SET title = 'update Title'
WHERE id = 1;
```

**여러 필드 수정:**
```sql
UPDATE articles
SET title = 'update Title',
    content = 'update Content'
WHERE id = 2;
```

> ⚠️ **주의:** WHERE 절을 생략하면 모든 레코드가 수정됩니다!

---

### DELETE

**역할:** 테이블 레코드 삭제

#### Syntax

```sql
DELETE FROM table_name
[WHERE condition];
```

#### 예시

```sql
DELETE FROM articles
WHERE id = 1;
```

**여러 레코드 삭제:**
```sql
DELETE FROM articles
WHERE id IN (1, 2, 3);
```

**나머지 레코드 모두 삭제:**
```sql
DELETE FROM articles
WHERE id NOT IN (1, 2, 3);
```

> ⚠️ **주의:** WHERE 절을 생략하면 모든 레코드가 삭제됩니다!

---

## 3️⃣ Multi Table Queries - JOIN

### JOIN이란?

- 둘 이상의 테이블에서 데이터를 검색하는 방법
- 관계형 데이터베이스의 핵심 기능
- 테이블 간의 관계를 기반으로 데이터를 결합

---

### INNER JOIN

**특징:** 두 테이블에서 **양쪽 모두에 값이 있는 행만** 반환

#### Syntax

```sql
SELECT select_list
FROM table_a
INNER JOIN table_b
    ON table_b.fk = table_a.pk;
```

#### 예시

```sql
SELECT *
FROM articles
INNER JOIN users
    ON users.id = articles.userId;
```

**결과:** articles와 users 양쪽 모두에 데이터가 있는 레코드만 조회

---

### LEFT JOIN

**특징:** 
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 **모든 레코드** 반환
- 오른쪽 테이블에 일치하는 레코드가 없으면 NULL 표시

#### Syntax

```sql
SELECT select_list
FROM table_a
LEFT JOIN table_b
    ON table_b.fk = table_a.pk;
```

#### 예시

```sql
SELECT *
FROM articles
LEFT JOIN users
    ON users.id = articles.userId;
```

**결과:** 모든 articles 레코드를 조회하되, 연결된 users 정보가 없으면 NULL로 표시

---

### JOIN 비교

| 구분 | INNER JOIN | LEFT JOIN |
|------|-----------|-----------|
| **기준** | 양쪽 모두 매칭되는 데이터만 | 왼쪽 테이블 기준 |
| **결과** | 교집합 | 왼쪽 테이블 전체 + 매칭되는 오른쪽 데이터 |
| **NULL 여부** | NULL 없음 | 매칭 안 되면 NULL |

---

## 📝 참고사항

### 타입 선호도 (Type Affinity)

- SQLite는 데이터 타입에 유연함
- 명시적 타입이 없어도 데이터를 저장하고 추론할 수 있는 타입 선호도를 가짐
- 각 컬럼은 선호하는 타입이 있지만, 강제하지 않음

### NOT NULL 제약조건

- 해당 컬럼에 NULL 값 저장 불가
- 데이터 무결성 보장
- 필수 입력 필드에 주로 사용

### 날짜와 시간

- SQLite는 별도의 날짜/시간 타입이 없음
- TEXT, REAL, INTEGER 타입으로 저장
- 날짜 관련 함수로 처리
  - `DATE()`, `TIME()`, `DATETIME()`, `JULIANDAY()`, `STRFTIME()`

---

## 🎯 핵심 키워드 정리

| 명령어 | 설명 | 예시 |
|--------|------|------|
| **CREATE TABLE** | 새로운 테이블 생성 | `CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);` |
| **INSERT** | 테이블에 새 데이터 삽입 | `INSERT INTO users (name) VALUES ('홍길동');` |
| **SELECT** | 테이블에서 데이터 조회 | `SELECT * FROM users;` |
| **UPDATE** | 기존 데이터 수정 | `UPDATE users SET name = '김민수' WHERE id = 1;` |
| **DELETE** | 테이블의 데이터 삭제 | `DELETE FROM users WHERE id = 1;` |
| **ALTER TABLE** | 테이블 구조 변경 | `ALTER TABLE users ADD COLUMN age INTEGER;` |
| **DROP TABLE** | 테이블 자체를 삭제 | `DROP TABLE users;` |
| **PRIMARY KEY** | 각 행을 고유하게 식별하는 열 | `id INTEGER PRIMARY KEY` |
| **NOT NULL** | 해당 열에 반드시 값이 있어야 함 | `name TEXT NOT NULL` |
| **FOREIGN KEY** | 다른 테이블의 값을 참조 | `userId INTEGER REFERENCES users(id)` |
| **AUTOINCREMENT** | 자동으로 숫자 증가 | `id INTEGER PRIMARY KEY AUTOINCREMENT` |
| **INNER JOIN** | 두 테이블에서 일치하는 데이터만 조회 | `SELECT * FROM articles INNER JOIN users ON users.id = articles.userId;` |
| **LEFT JOIN** | 왼쪽 테이블의 모든 행 유지하여 조회 | `SELECT * FROM users LEFT JOIN articles ON users.id = articles.userId;` |
| **PRAGMA** | 테이블 메타데이터 정보 확인 | `PRAGMA table_info('users');` |

---

## 📌 요약 및 정리

1. **CREATE TABLE** 문을 통해 새로운 테이블을 만들고 각 열에 데이터 타입과 제약 조건을 설정할 수 있다

2. **제약 조건(Constraints)**은 데이터의 무결성과 일관성을 유지하기 위해 사용되며, PRIMARY KEY, NOT NULL, FOREIGN KEY 등이 있다

3. **INSERT / SELECT / UPDATE / DELETE** 문을 활용해 테이블에 데이터를 추가, 조회, 수정, 삭제할 수 있다

4. **ALTER TABLE** 문을 사용하면 테이블에 열을 추가하거나 이름을 변경하고, 열을 삭제하거나 테이블 이름을 바꿀 수 있다

5. **DROP TABLE** 명령은 테이블 자체를 삭제할 때 사용된다

6. **JOIN**을 사용하면 분리된 여러 테이블을 조합하여 하나의 결과로 조회할 수 있다

7. **INNER JOIN**은 양쪽 모두에 데이터가 있는 경우만, **LEFT JOIN**은 왼쪽 기준으로 모두 보여준다

8. SQLite는 데이터 타입에 유연하며, 명시적 타입이 없어도 데이터를 저장하고 추론할 수 있는 타입 선호도(Type Affinity)를 가진다

9. 날짜와 시간은 별도 타입 없이 TEXT, REAL, INTEGER 타입으로 저장하여 함수로 처리한다

---

## 💡 학습 비유

> "나만의 작은 도서관, 직접 만들어 볼까요?"
> 
> 집에 있는 책을 정리해서 나만의 도서관을 만든다고 상상해 보세요.
> 
> 1. 책장 하나를 **CREATE TABLE** 문으로 만들고
> 2. 책 정보를 **INSERT** 문으로 채워 넣습니다
> 3. '2020년 이후에 산 책'만 **SELECT** 문으로 골라볼 수도 있죠
> 
> SQL은 데이터를 정리하는 책장 같은 도구입니다.
> 원하는 데이터를 빠르게 찾을 수 있도록 도와줍니다!
