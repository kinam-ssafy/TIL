## 요약

clone 받을 때

git clone url
받고

git add .
git commit -m ''
git push origin master 로 다시 푸쉬


pull 받을 때

git pull url
전에 받았던 파일들의 변경사항 없어야 pull 받을 수 있음

## git hub에 공유 프로젝트가 아닌데 다른 사용자가 커밋했을 경우

$ git config --global user.name
$ git config --global user.email
을 통해 사용자와 이메일 확인

# "Your Name" 부분에 본인의 GitHub 사용자 이름을 입력하세요.
$ git config --global user.name "Your Name"

# "your_email@example.com" 부분에 본인의 GitHub 이메일을 입력하세요.
$ git config --global user.email "your_email@example.com"

을 통해 이름과 이메일 변경

$ git commit --amend --reset-author

마지막 커밋에 기록된 작성자 정보 리셋함. 수정 내용 없다면 :wq 입력 후 엔터

$ git push --force origin master

변경사항 강제 반영


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

git remote -v 로 사용자명/저장소명 확인가능

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

---

## Git revert

특정 commit을 없었던 일로 만드는 작업

git revert commit id

#### Git revert 작동 원리

"재설정"

단일 commit을 실행 취소 하는 것

프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함

#### Git revert 정리

변경 사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업

commit 기록에서 commit을 삭제하거나 분리하는 대신, 지정된 변경 사항을 반전시키는 새 commit을 생성

git에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성을 높임

---
git log --oneline 으로 커밋 리스트 확인

git revert #### 해쉬코드 4자리입력

:wq 엔터

git log --oneline 으로 revert 되었는지 확인

---

공백을 사용해 여러 commit을 한꺼번에 실행 취소 가능

예시

git revert 7f6c24c 006dc87 3551584

'..' 을 사용해 범위를 지정하여 여러 commit을 한꺼번에 실행 취소 가능

git revert 3551584..7f6c24c

commit 메시지 작성을 위한 편집기를 열지 않은 (자동으로 commit 진행)

git revert --no-edit 7f6c24c

자동으로 commit 하지 않고, Staging Area에만 올림(이후에 직접 commit 해야 함)

이 옵션은 여러 commit을 revert할 때 하나의 commit으로 묶는 것이 가능

git revert --no-commit 7f6c24c


---

## Git reset

특정 commit으로 되돌아가는 작업

git reset [옵션] commit id

#### Git reset 작동 원리

"되돌리기"

시계를 마치 과거로 돌리는 듯한 행위

특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 commit은 모두 삭제


### reset의 3가지 옵션
--soft, --mixed, --hard

reset은 과거 commit으로 되돌아간 후 되돌아간 commit 이후 commit들이 삭제됨

그런데 삭제되는 commit들의 기록을 어떤 영역에 남겨둘 것인지 옵션을 활용해 조정할 수 있음

### 옵션 별 동작 원리
--soft

삭제된 commit의 기록을 staging area에 남김

--mixed

삭제된 commit의 기록을 working directory에 남김 (기본 옵션 값)

working directory로 갔기 때문에 unreacked files 상태가 됨

--hard

삭제된 commit의 기록을 남기지 않음

### 이미 삭제한 commit으로 다시 돌아가고 싶다면?

**git reflog**

HEAD가 이전에 가리켰던 모든 commit을 보여줌

reset의 --hard 옵션을 통해 지워진 commit도 reflog로 조회하여 복구 가능

---

commit 3

commit 2

commit 1

중에서 

git reset --hard commit 1(해쉬번호)

하면 commit 2, commit 3이 삭제됨

되돌릴 때

git reset --hard commit 3 하면

commit 2, commit 3 까지 순서대로 복구됨

**commit 3만 복구되는 줄 알았는데 복구하려는 commit이 생성된 순서까지 복구되었음**

----


