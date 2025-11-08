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



# Git branch 명령어 및 활용법

## 브랜치 확인 및 생성
```bash
# 현재 브랜치 확인
git branch

# 모든 브랜치 확인 (원격 포함)
git branch -a

# 새 브랜치 생성
git branch feature/login

# 브랜치 생성과 동시에 이동
git checkout -b feature/signup

# 또는 (최신 방법)
git switch -c feature/signup

```

## 브랜치 이동
```bash
# 브랜치 이동 (기존 방법)
git checkout main

# 브랜치 이동 (최신 방법)
git switch main
```

## 브런치 삭제
```bash
# 로컬 브랜치 삭제
git branch -d feature/login

# 강제 삭제 (merge 안 된 브랜치도 삭제)
git branch -D feature/login

# 원격 브랜치 삭제
git push origin --delete feature/login
```

## 협업 시 주요 명령어
## 원격 저장소 연동

```bash
# 원격 저장소 확인
git remote -v

# 원격 브랜치 최신 정보 가져오기
git fetch origin

# 원격 브랜치를 로컬로 가져오기
git checkout -b feature/posts origin/feature/posts
```

## 브랜치 푸시
```bash
# 현재 브랜치를 원격에 푸시
git push origin feature/login

# 처음 푸시할 때 (upstream 설정)
git push -u origin feature/login
# 이후부터는 git push만 해도 됨
```


## 브랜치 병합
```bash
# main 브랜치로 이동
git switch main

# feature/login 브랜치를 main에 병합
git merge feature/login

# 충돌 발생 시 해결 후
git add .
git commit -m "Merge feature/login"
```

## Pull (원격 변경사항 가져오기)
```bash
# 현재 브랜치에 원격 변경사항 가져오기
git pull origin main

# rebase 방식으로 가져오기 (더 깔끔한 히스토리)
git pull --rebase origin main
```


# 협업 워크 플로우

## 1단계: 작업 시작

```bash
# 최신 main 받아오기
git switch main
git pull origin main

# 새 기능 브랜치 생성
git switch -c feature/accounts

# 작업 진행...
```

## 2단계: 작업 중 커밋
```bash
# 변경사항 확인
git status

# 스테이징
git add accounts/models.py accounts/forms.py

# 커밋
git commit -m "feat: Add User model and CustomUserCreationForm"
```

## 3단계: 원격에 푸시
```bash
# 처음 푸시
git push -u origin feature/accounts

# 이후 푸시
git push
```


## 4단계: 병합 전 최신화
```bash
# main의 최신 변경사항 가져오기
git switch main
git pull origin main

# 내 브랜치로 돌아가서 main 병합
git switch feature/accounts
git merge main

# 충돌 해결 후
git add .
git commit -m "Merge main into feature/accounts"
git push
```

## 5단계: Merge Request
> GitLab에서 Merge Request 생성 -> 팀원 리뷰 -> 승인 후 병합

## 브런치 상태 확인
```bash
# 브랜치 간 차이 확인
git diff main..feature/accounts

# 커밋 히스토리 확인
git log --oneline --graph --all

# 특정 브랜치의 커밋 확인
git log feature/accounts
```

## Stash(임시 저장)
```bash
# 현재 작업 임시 저장
git stash

# 브랜치 전환 후 다시 불러오기
git switch feature/posts
git stash pop

# stash 목록 확인
git stash list

# 특정 stash 적용
git stash apply stash@{0}
```

## 브랜치 이름 변경
```bash
# 로컬 브랜치 이름 변경
git branch -m old-name new-name

# 현재 브랜치 이름 변경
git branch -m new-name
```

# 충돌 해결하기
```bash
# 충돌 발생 시
<<<<<<< HEAD
# 현재 브랜치의 코드
=======
# 병합하려는 브랜치의 코드
>>>>>>> feature/accounts

# 충돌 해결 후
git add 충돌파일.py
git commit -m "Resolve merge conflict"
```

## 권장 커밋 메시지 컨벤션
```bash
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
style: 코드 포매팅
refactor: 코드 리팩토링
test: 테스트 코드
chore: 빌드 업무, 패키지 설치 등

# 예시
git commit -m "feat: Add login view and template"
git commit -m "fix: Resolve signup form validation error"
git commit -m "docs: Update README with setup instructions"
```

## 예시
## 두 명이 각자 기능 개발
```bash
# 팀원A (accounts 담당)
git switch -c feature/accounts
# 작업...
git add .
git commit -m "feat: Add login/logout functionality"
git push -u origin feature/accounts

# 팀원B (posts 담당)
git switch -c feature/posts
# 작업...
git add .
git commit -m "feat: Add post CRUD functionality"
git push -u origin feature/posts

# 각자 GitLab에서 MR 생성 → 리뷰 → 병합
```

팀원 A 작업이 먼저 병합됨
```bash
# 팀원B는 최신 main을 자기 브랜치에 반영
git switch feature/posts
git fetch origin
git merge origin/main
# 충돌 해결
git push
```











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


