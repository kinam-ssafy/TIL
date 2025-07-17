	
# Git 연습하기
## Git Status, Log, Add, Commit 연습하기 

myFolder 라는 디렉토리를 만들고, Git 초기화를 진행하세요.  

myFolder 디렉토리로 이동 후, test.py 파일을 만드세요

test.py을 staging area 로 추가하세요.

first commit 이라는 커밋명으로 커밋을 추가하세요.

InnerFolder 디렉토리를 생성하고, 해당 디렉토리 내부에 test2.py 와 test3.py, test4.py 파일을 생성하세요.

InnerFolder 안의 test2.py 를 staging area로 추가한 뒤 second commit 이라는 커밋을 추가하세요.

InnerFolder 안에서 커밋에 추가되지 않은 나머지 파일을 third commit 으로 커밋을 추가하세요.

위 과정을 실행한 후 

git status => nothing to commit, working tree clean 문구가 나타나야 함 

git log => third commit -> second commit -> first commit 이 위에서부터 순서대로 나타나야 함

---
작성 코드

cd /c/Users/SSAFY/Desktop

mkdir myFolder

cd myFolder

git init

touch test.py

git add test.py

git commit -m "first commit"

mkdir InnerFolder

cd InnerFolder

touch test2.py

touch test3.py

touch test4.py

git add test2.py

git commit -m "second commit"

git add test3.py

git add test4.py

git commit -m "third commit"

git status

git log

--

## git commit 실습
바탕화면에 git_commit 폴더를 만들고 git 저장소 생성

해당 폴더 안에 a.txt 라는 텍스트 파일을 만들고, "add a.txt" 라는 커밋 메시지로 커밋 생성

이번에는 b.txt 라는 텍스트 파일을 만들고, "add b.txt" 라는 커밋 메시지로 커밋 생성

a.txt 파일을 수정하고, "update a.txt" 라는 커밋 메시지로 커밋 생성

커밋 목록 확인하기

---

작성코드

cd /c/Users/SSAFY/Desktop

mkdir git_commit

cd git_commit

git init

touch a.txt

git add a.txt

git commit -m "add a.txt"

touch b.txt

git add b.txt

git commit -m "add b.txt"

start a.txt

텍스트파일에 타이핑 후 컨트롤 + s 로 저장

git add a.txt

git commit -m "update a.txt"

git status

git log --oneline

---


## commit 메시지 수정 실습

mkdir git-amend-practice

cd git-amend-practice

code .

git init

touch README.md

git add .

git commit -m 'A 기능 구현 완료'

git log --oneline

git commit --amend

i 누르고 메시지 수정

esc 누르기

:wq엔터

w(write)

q(quit)

git log --oneline

touch b.txt

git add .

git commit --amend

i 누르고 메시지 수정

esc :wq 엔터

git log --oneline


github에서 원격 저장소 repo 만들고 url 복사

git remote add origin repourl

git remote -v

git push origin master

sample.txt의 내용 변경

git add sample.txt

git commit -m "third commit"

git push origin master

---

pull -> 변경사항만 가져옴

clone -> remote랑 똑같은 애를 복제함. 로컬에 뭐가 없어야함

git clone remote_repo_url -> url은 git 저장소. .git폴더가 있음

git pull 받아갈지 git clone 받아갈지 -> 내 pc의 상태가 다름

프로젝트를 처음 시작하거나 로컬에 아무것도 없을 때 -> clone

clone 받아올 때 폴더 이름은 pull로 받아올때랑 같을수도 다를수도있음


first-repo랑 origin의 연결 끊기

git remote remove origin

gitignore : 어쨌든 파일임. git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일

ex : 비밀번호 

---

gitignore 사용하기

.gitignore 파일 생성

ignore파일에 추적하지 않을 파일명 작성

git inint

git status 

https://www.toptal.com/developers/gitignore/
링크에 들어가 gitignore 목록 만들기

