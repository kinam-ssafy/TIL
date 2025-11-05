-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN
SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id;

SELECT articles.title, users.name 
FROM articles
INNER JOIN users
  ON articles.userId = users.id;

SELECT articles.title, users.name 
FROM articles
INNER JOIN users
  ON articles.userId = users.id
WHERE
  users.id = 1;


-- LEFT JOIN
SELECT * FROM articles
LEFT JOIN users
  ON articles.userId = users.id;


-- "게시글이 없는 사용자 조회하기"
-- 1단계. 모든 사용자와 게시글 조회
SELECT * FROM users
LEFT JOIN articles
  ON articles.userId = users.id;

-- 2단계. 게시글이 없는 사용자 조회
SELECT * FROM users
LEFT JOIN articles
  ON articles.userId = users.id
WHERE articles.userId IS NULL;

-- 3단계. 게시글이 없는 사용자 이름만 조회
SELECT users.name FROM users
LEFT JOIN articles
  ON articles.userId = users.id
WHERE articles.userId IS NULL;
