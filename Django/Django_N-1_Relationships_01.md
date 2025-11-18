# Django Many To One Relationships 01

## 목차
1. [Many to one relationships](#many-to-one-relationships)
   - 모델 관계
   - 댓글 모델 정의
   - 댓글 생성 연습
2. [관계 모델 참조](#관계-모델-참조)
   - 역참조
3. [댓글 구현](#댓글-구현)
   - 댓글 CREATE
   - 댓글 READ
   - 댓글 DELETE
4. [참고](#참고)
   - 데이터 무결성
   - admin site 댓글 등록
   - 댓글 추가 구현

---

## 학습 목표

- Django의 Many to One 모델 관계를 이해하고 정의할 수 있다.
- ForeignKey를 활용한 관계형 모델 구축 방법을 실습할 수 있다.
- Django shell을 이용해 댓글 데이터를 생성하고 관계를 확인할 수 있다.
- CREATE/READ/DELETE 기능을 사용해 댓글 기능을 Django 프로젝트에 구현할 수 있다.
- 역참조를 통해 관계 모델에서 데이터를 효율적으로 조회할 수 있다.
- admin 페이지에서 댓글 관리를 수행할 수 있다.
- for-empty 문법을 활용해 사용자 경험을 개선할 수 있다.

---

## Many to one relationships

### 모델 관계

#### 관계(relationship)의 정의

**관계(relationship)**
- 데이터베이스 내 여러 테이블 간의 논리적인 연결 관계를 나타냄

**예시**
데이터베이스에는 '강사' 테이블과 '학생' 테이블이 있을 때, "이삼성 강사가 김싸피 학생을 가르치고 있다"는 정보를 저장하려면 두 테이블 간의 관계(relationship)를 설정해야 합니다.

이러한 관계를 표현하기 위해, 한 테이블에 다른 테이블의 기본 키(Primary Key)를 저장합니다. 이처럼 다른 테이블의 기본 키를 참조하는 속성을 **외래 키(Foreign Key)**라고 합니다.

외래 키는 두 테이블 간의 논리적인 연결 고리 역할을 하여, 이를 통해 관계형 데이터베이스에서 연관된 데이터를 효율적으로 관리할 수 있습니다.

---

#### 관계의 종류

**1. 1:1 (One to One) 관계**
- 한 테이블의 레코드는 다른 테이블의 한 레코드와 연결됨
- 예시: 한 사람당 하나의 주민등록번호

```
사람 ──── 주민등록번호
```

| 사람 | | 주민등록번호 |
|------|---|--------------|
| 사람 ID | | 등록번호 |
| 이름 | | 주소 |
| | | 사람 ID |

**2. N:1 (Many to One) 관계**
- 여러 개의 레코드가 하나의 레코드와 연결됨
- 예시: 여러 교육생(N)을 한 강사(1)가 가르침

```
강사 ────< 교육생
```

| 강사 | | 교육생 |
|------|---|--------|
| 강사 ID | | 교육생 ID |
| 이름 | | 이름 |
| 과목 | | 강사 ID |

**3. N:M (Many to Many) 관계**
- 여러 레코드가 여러 레코드와 상호 연결됨
- 보통 중간 테이블(예: 수강신청)을 사용해 구현
- 예시: 여러 학생(N)이 여러 과목(M)을 수강함

```
학생 >────< 수강신청 >────< 과목
```

| 학생 | | 수강신청 | | 과목 |
|------|---|----------|---|------|
| 학생 ID | | 학생 ID | | 과목 ID |
| 이름 | | 과목 ID | | 과목명 |

💡 **참고**: 1:1 관계는 N:1 관계와 사용방법은 유사하며, N:M 관계는 추후 진행될 예정

---

#### Many to one relationships

**N:1 또는 1:N 관계**
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

---

#### Many to one relationships 예시

**1. SSAFY Track : Student**
- SSAFY Track (1) : Student (N)
- 하나의 트랙에는 여러 명의 교육생이 포함됨
- 한 명의 교육생은 트랙이 중복되어서는 안 됨

**2. Order : Customer**
- Order (N) : Customer (1)
- 한 명의 고객이 여러 주문 가능
- 하나의 주문을 여러 명의 고객이 낼 수 없음

**3. Account : Bank**
- Account (N) : Bank (1)
- 하나의 계좌는 한 은행에만 소속되어 있음
- 한 은행은 여러 개의 계좌를 가질 수 있음

**4. Country : City**
- Country (1) : City (N)
- 하나의 국가는 여러 도시를 가짐
- 한 도시가 중복된 국가에 포함되지 않음

**5. Baseball Team : Member**
- Baseball Team (1) : Member (N)
- 한 팀에 여러 명의 선수가 소속됨
- 한 선수가 다른 야구 팀에 소속될 수 없음

**6. Movie : Actor**
- Movie (N) : Actor (M) => **N:1 관계 아님 (N:M 관계)**
- 영화에 여러 배우들이 출연 가능함
- 배우도 여러 영화에 출연 가능함

---

#### 댓글과 게시글의 관계

**Comment(N) : Article(1)**
- 하나의 게시글에는 여러 개의 댓글이 달림
- 단, 게시글에 댓글이 없는 경우도 존재함
- 댓글이 소속된 게시글이 없는 경우는 없음
- 즉, **0개 이상의 댓글은 1개의 게시글에 작성될 수 있다**

---

#### 테이블 관계 설정

**❌ 잘못된 방법 (1/2): 1의 테이블에 외래 키 설정**

관계 설정을 위한 Foreign Key(외래 키, FK)를 N:1에서 1을 담당하는 테이블에 위치시키면 안 됨

Article Table에 Foreign Key 컬럼을 위치시키면 **중복 데이터로 인해 낭비가 발생함**

| Article Table | | Comment에 대한 정보 (외래 키) |
|---------------|---|-------------------------------|
| id | | |
| title | | |
| content | | |
| created_at | | |
| updated_at | | |

| Comment Table |
|---------------|
| id |
| content |
| created_at |
| updated_at |

⚠️ 댓글 생성마다 Comment의 정보와 함께 Article 정보(id, title, content, ...)가 매번 중복 저장됨

---

**✅ 올바른 방법 (2/2): N의 테이블에 외래키 설정**

관계 설정을 위한 Foreign Key(외래 키, FK)의 적절한 위치는 바로 **N:1에서 N을 담당하는 테이블에 위치**

Comment가 생성되면 Article의 정보만 저장하면 됨

| Comment Table | | Article Table |
|---------------|---|---------------|
| id | | id |
| content | | title |
| created_at | | content |
| updated_at | | created_at |
| Article에 대한 정보 (외래 키) | | updated_at |

✅ 외래 키 컬럼에 저장되는 데이터는 참조하는 데이터를 대표하는 **Primary Key(PK) 정보를 저장함**

---

### 댓글 모델 정의

#### ForeignKey 필드

**ForeignKey(to, on_delete)**
- 한 모델이 다른 모델을 참조하는 관계를 설정하는 필드
- N:1 관계 표현할 때 사용
- 데이터베이스에서 외래 키로 구현됨

---

#### ForeignKey 필드 속성

**데이터 무결성**
- 데이터가 정확하고 일관되며, 신뢰할 수 있도록 유지되는 상태

**ForeignKey(to, on_delete)**

**1. to 속성**
- 참조하는 모델 class 이름 (N:1에서 N이 아닌 1의 class 정보)

**2. on_delete 속성**
- 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할지를 정의하는 설정 (데이터 무결성)

⚠️ **to**와 **on_delete** 속성은 ForeignKey 설정에 필수 요소

---

#### on_delete 속성 종류

**1. CASCADE**
- 참조된 객체(부모 객체)가 삭제될 때 이를 참조하는 모든 객체도 삭제되도록 지정
- 예) 게시글이 삭제되면 해당 게시글의 모든 댓글을 삭제

**2. PROTECT**
- 삭제하려는 부모 객체에 자식 객체가 존재한다면 해당 부모 객체를 삭제하지 못하도록 지정
- 예) 게시글을 삭제할 때 해당 게시글에 댓글이 존재하면 게시글 삭제 불가

**3. SET_NULL**
- 부모 객체가 삭제되면 해당 필드에 값이 NULL로 저장되도록 지정
- 단, 해당 ForeignKey 필드 설정이 `null=True`가 설정되어야 함
- 예) 게시글이 삭제되면 댓글의 게시글 정보가 NULL로 변경

**4. SET_DEFAULT**
- 부모 객체가 삭제되면 해당 필드에 기본값이 저장되도록 지정
- 단, 해당 ForeignKey 필드 설정이 `default` 값이 설정되어야 함

**5. SET()**
- 부모 객체가 삭제되면 지정된 함수의 반환값으로 설정
- 예) `SET(get_sentinel_user)` - 특정 사용자로 설정

**6. DO_NOTHING**
- 아무 작업도 수행하지 않음
- 데이터베이스 무결성 에러 발생 가능

---

#### Comment 모델 정의

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

**주요 구성 요소:**
- `article`: Article 모델을 참조하는 ForeignKey 필드
- `on_delete=models.CASCADE`: 게시글 삭제 시 댓글도 함께 삭제
- `content`: 댓글 내용 (최대 200자)
- `created_at`: 댓글 생성 시각
- `updated_at`: 댓글 수정 시각

---

#### Migration 진행

모델 클래스 변경사항을 DB에 최종 반영

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

**확인:**
- `articles_comment` 테이블 생성 확인
- `article_id` 필드 생성 확인 (ForeignKey 필드는 자동으로 `_id` 접미사가 붙음)

---

### 댓글 생성 연습

#### Django shell 실행 및 게시글 작성

```bash
$ python manage.py shell_plus
```

```python
# 게시글 생성
Article.objects.create(title='title', content='content')

# 댓글 생성 시도 (실패)
Comment.objects.create(content='first comment')
# IntegrityError: NOT NULL constraint failed: articles_comment.article_id
```

⚠️ **에러 발생 이유:**
- Comment 모델의 ForeignKey 필드인 `article`이 비어있음
- NOT NULL 제약 조건에 위배됨

---

#### 댓글 생성 (성공)

**방법 1: 게시글 객체를 직접 전달**

```python
# 게시글 조회
article = Article.objects.get(pk=1)

# 댓글 생성 (article 객체 전달)
comment = Comment.objects.create(content='first comment', article=article)

# 댓글 속성 확인
comment
# <Comment: first comment>

comment.pk
# 1

comment.content
# 'first comment'
```

---

**방법 2: 게시글의 pk 값을 직접 전달**

ForeignKey 필드에 값을 전달할 때는 객체 또는 `_id` 접미사를 붙인 pk 값 모두 가능

```python
comment = Comment.objects.create(content='second comment', article_id=1)

comment.pk
# 2

comment.content
# 'second comment'
```

---

#### 댓글 속성 값 확인

**comment.article 확인**

```python
comment.article
# <Article: title>

comment.article.pk
# 1

comment.article.content
# 'content'
```

- `comment.article`은 Article 모델의 인스턴스를 반환
- 이를 통해 댓글이 참조하는 게시글의 모든 정보에 접근 가능

---

**comment.article_id 확인**

```python
comment.article_id
# 1
```

- `comment.article_id`는 외래 키 필드의 실제 값(게시글의 pk)을 반환
- 데이터베이스에 실제로 저장되는 값

---

**두 번째 댓글 생성**

```python
# 1번 게시글에 두 번째 댓글 작성
comment = Comment.objects.create(content='second comment', article=article)

comment.pk
# 2

comment.article.pk
# 1
```

---

## 관계 모델 참조

### 역참조

#### 개념

**역참조 (Reverse Reference)**
- N:1 관계에서 1(Article)에서 N(Comment)을 참조하는 것
- N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만, 1은 N에 대한 참조 방법이 없음
- Django가 **역참조 매니저**를 자동으로 생성하여 제공

---

#### 역참조 매니저 이름 규칙

**기본 규칙: `모델명_set`**

```python
article.comment_set.all()
```

- 특정 게시글(article)에 작성된 모든 댓글을 조회
- `article.comment_set`은 해당 게시글과 관련된 댓글 QuerySet을 반환하는 매니저

---

#### 역참조 실습

```python
# 1번 게시글 조회
article = Article.objects.get(pk=1)

# 1번 게시글에 작성된 모든 댓글 조회 (역참조)
article.comment_set.all()
# <QuerySet [<Comment: first comment>, <Comment: second comment>]>

# 1번 게시글에 작성된 댓글의 개수
article.comment_set.count()
# 2

# 역참조 매니저를 통한 댓글 생성
article.comment_set.create(content='third comment')
# <Comment: third comment>
```

---

#### related_name

**역참조 매니저 이름 변경**

ForeignKey의 `related_name` 인자를 사용하여 역참조 매니저 이름을 변경할 수 있음

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Migration 필수**
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

**사용 예시**
```python
# 변경 전
article.comment_set.all()

# 변경 후
article.comments.all()
```

⚠️ **주의:**
- `related_name`을 설정하면 기존의 `_set` 매니저는 사용할 수 없음
- 역참조 시 항상 설정한 `related_name`을 사용해야 함

---

## 댓글 구현

### 댓글 CREATE

#### CommentForm 정의

```python
# articles/forms.py
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
```

💡 **중요:**
- 댓글 작성 시 어떤 게시글에 작성하는지(article 필드)는 사용자가 선택하는 것이 아님
- URL을 통해 게시글 정보를 받아서 자동으로 설정되어야 함
- 따라서 `fields`에 `'article'`을 포함시키지 않음

---

#### detail view 함수 수정

```python
# articles/views.py
from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

---

#### detail 템플릿 수정

```django
<!-- articles/detail.html -->
<h1>DETAIL</h1>
<h3>{{ article.pk }}번째 글</h3>
<hr>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성 시각: {{ article.created_at }}</p>
<p>수정 시각: {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
<a href="{% url 'articles:index' %}">BACK</a>
<hr>
<h4>댓글 작성</h4>
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit" value="작성">
</form>
```

---

#### URL 설정

```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    # ... 기존 URL 패턴들 ...
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

---

#### comments_create view 함수 작성

```python
# articles/views.py
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

**핵심 로직:**
1. `comment_form.save(commit=False)`: DB에 저장하지 않고 인스턴스만 반환
2. `comment.article = article`: 댓글이 어떤 게시글에 속하는지 설정
3. `comment.save()`: 최종 DB 저장

💡 **save(commit=False)**
- 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
- 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용

---

### 댓글 READ

#### detail view 함수 수정

```python
# articles/views.py
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

---

#### detail 템플릿 수정

```django
<!-- articles/detail.html -->
<h1>DETAIL</h1>
<h3>{{ article.pk }}번째 글</h3>
<hr>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성 시각: {{ article.created_at }}</p>
<p>수정 시각: {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
<a href="{% url 'articles:index' %}">BACK</a>
<hr>
<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% endfor %}
</ul>
<hr>
<h4>댓글 작성</h4>
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit" value="작성">
</form>
```

---

### 댓글 DELETE

#### URL 설정

```python
# articles/urls.py
app_name = 'articles'
urlpatterns = [
    # ... 기존 URL 패턴들 ...
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', 
         views.comments_delete, 
         name='comments_delete'),
]
```

---

#### comments_delete view 함수 작성

```python
# articles/views.py
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

---

## 참고

### 데이터 무결성

**데이터베이스의 무결성**
- 데이터베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
- 데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적

#### 무결성 제약 조건의 종류

**1. 개체 무결성 (Entity Integrity)**
- 모든 테이블이 기본 키(Primary Key)를 가져야 함
- 기본 키는 NULL 값을 가질 수 없으며, 중복될 수 없음

**2. 참조 무결성 (Referential Integrity)**
- 외래 키(Foreign Key) 값은 참조하는 테이블의 기본 키 값이어야 함
- 외래 키는 NULL 값을 가질 수 있음
- **Django의 on_delete 옵션이 참조 무결성을 유지하는 역할**

**3. 도메인 무결성 (Domain Integrity)**
- 모든 컬럼은 정의된 도메인(데이터 타입, 형식, 범위)에 속한 값만 가져야 함
- 예) 나이 필드는 음수가 될 수 없음

---

### admin site 댓글 등록

#### Comment 모델 등록

```python
# articles/admin.py
from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```

**확인:**
- admin site에서 댓글 데이터 확인
- 댓글 생성, 수정, 삭제 테스트

---

### 댓글 추가 구현

#### 1. 댓글이 없는 경우 대체 콘텐츠 출력

**DTL의 for-empty 태그 활용**

for 문에 반복할 요소가 없는 경우 empty 태그가 실행됨

```django
<!-- articles/detail.html -->
<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% empty %}
    <p>댓글이 없어요 :(</p>
  {% endfor %}
</ul>
```

---

#### 2. 댓글 개수 출력하기

**방법 1: DTL filter의 'length' 활용**

```django
<!-- views.py에서 전달받은 댓글로 길이 확인 -->
{{ comments|length }}

<!-- 역참조를 이용하여 댓글 길이 확인 -->
{{ article.comment_set.all|length }}
```

**방법 2: QuerySet API의 count() 메서드 활용**

```django
<!-- 역참조로 QuerySet API 이용 댓글 길이 확인 -->
{{ article.comment_set.count }}
```

💡 **차이점:**
- `length` 필터: 모든 데이터를 가져온 후 길이를 계산 (메모리 사용)
- `count()` 메서드: 데이터베이스에서 직접 COUNT 쿼리 실행 (더 효율적)

---

## 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| ForeignKey | 다른 모델과 N:1 관계를 정의할 때 사용하는 필드 | `comment = models.ForeignKey(Article, on_delete=...)` |
| Many to One | 여러 개의 하위 객체가 하나의 상위 객체를 참조하는 모델 관계 | 여러 댓글 > 하나의 게시글 |
| ORM | Django에서 데이터베이스를 객체처럼 다루는 방식 | `Comment.objects.create(...)` |
| 역참조 | 상위 모델에서 연결된 하위 모델을 조회하는 방식 | `article.comment_set.all()` |
| admin 등록 | admin 사이트에서 모델을 시각적으로 관리하도록 설정 | `admin.site.register(Comment)` |
| for-empty 문법 | 반복문에서 데이터가 없을 경우를 처리하는 Django 템플릿 문법 | `{% for comment in comments %}...{% empty %}...{% endfor %}` |
| 데이터 무결성 | 모델 관계 설정 시 데이터 일관성과 안정성을 유지하는 설계 방법 | `on_delete=models.CASCADE` |

---

## 요약 및 정리

1. **N:1 관계는 여러 개의 댓글이 하나의 게시글에 연결되는 구조이며, Django에서는 ForeignKey를 사용해 구현합니다.**

2. **Django shell을 활용한 ORM 실습을 통해 관계형 데이터 생성과 조회를 연습했습니다.**

3. **댓글 기능 구현(CREATE, READ, DELETE)을 통해 실제 웹 애플리케이션의 동작 원리를 파악했습니다.**

4. **역참조 기능을 통해 게시글에서 관련 댓글을 불러올 수 있으며, admin 페이지를 활용한 댓글 관리도 실습했습니다.**

5. **for-empty 문법을 적용하여 댓글이 없을 경우도 고려한 UX 개선을 수행했습니다.**

6. **다음 단계:**
   - 게시글과 댓글을 관계를 설정하여 데이터베이스에 저장할 수 있습니다.
   - 게시글과 댓글은 N:1 관계이므로 모델 간 관계 설정이 필요해 ForeignKey를 사용해 댓글 모델을 정의해야 합니다.
   - 역참조 개념을 활용하면 게시글에서 관련된 댓글을 쉽게 조회할 수 있습니다.
   - for-empty 문법을 사용하면 댓글이 없는 경우에도 자연스러운 UI를 구현할 수 있습니다.
   - admin 페이지에 댓글을 등록하고 관리하여 쉽게 관련 데이터를 관리할 수 있습니다.
   - N:1 관계 설정을 이용해서 누가 작성한 게시글 혹은 댓글인지 만들어 볼 수 있습니다.

---

## 확인 문제 정답

1. **b) article.comment_set.all()** - ForeignKey에서 `related_name`을 별도로 설정하지 않으면 Django는 자동으로 '참조하는모델명_set' (소문자) 형태의 역참조 매니저를 생성합니다.

2. **a) Comment.objects.create(...)** - `create()` 메서드를 사용하여 ForeignKey 필드는 객체 또는 '_id' 접미사를 붙인 pk 값으로 지정할 수 있습니다.

3. **X** - 'N'쪽에서 '1'쪽으로 접근하는 것은 '참조'이며, '1'쪽에서 자신을 참조하는 'N'쪽 객체 목록에 접근하는 것이 '역참조'입니다.

4. **b) {% empty %}** - `{% for comment in comments %}...{% empty %}...{% endfor %}` 형태로 사용하면 댓글이 없을 때 대체 콘텐츠를 자연스럽게 출력할 수 있습니다. Django의 for-empty 문법은 사용자 경험을 고려한 표현입니다.

5. **admin.site.register** - `admin.py`에서 `admin.site.register()` 함수를 사용하여 모델을 관리자 페이지에 등록할 수 있습니다.

6. **b) 하나의 게시글에 여러 댓글이 달린다.** - N:1 관계는 여러 댓글이 하나의 게시글을 참조하는 구조입니다.

7. **c) ForeignKey** - ForeignKey는 N:1 관계를 정의할 때 사용하는 필드입니다.

8. **O** - Django shell에서는 ORM을 통해 객체를 직접 생성할 수 있으며, ForeignKey 필드에는 참조할 객체(post)를 전달해야 합니다.

9. **X** - `related_name`은 명시적으로 설정하지 않으면 자동으로 생성되지 않습니다. 대신 Django는 기본적으로 `모델명_set` 형식의 역참조 매니저를 제공합니다.

10. **b) 생성 후 필드 추가 설정** - `form.save(commit=False)`는 폼 데이터를 기반으로 객체를 생성하되, 데이터베이스에는 저장하지 않습니다. 이 시점에서 객체를 수정하거나 관계 필드(post, user 등)를 설정한 후, `.save()`를 호출하여 저장할 수 있습니다. N:1 관계에서 외래 키를 설정할 때 자주 사용됩니다.

11. **d) 여러 명의 배우가 여러 영화에 출연한다.** - d의 경우는 N:M 관계입니다. 배우는 여러 영화에 출연할 수 있고, 영화도 여러 배우를 가질 수 있기 때문입니다. N:1 관계는 여러 개의 레코드가 하나의 레코드와 연결되는 구조입니다.

12. **'model class', 'on_delete'** - ForeignKey 필드를 정의할 때 참조할 모델 클래스(to)와 참조 대상이 삭제될 때 처리 방식을 지정하는 on_delete는 필수로 작성해야 합니다.

13. **X** - 게시글(Article) 모델에는 댓글(Comment)을 직접 참조하는 필드가 없기 때문에, 직접 접근할 수 없습니다. 대신 Django는 역참조 기능을 통해 `article.comment_set.all()`과 같은 방식으로 참조하는 데이터를 거꾸로 조회할 수 있도록 지원합니다.

14. **c) 참조하는 모델의 클래스명을 소문자 단수형으로 쓴다.** - ForeignKey 필드명은 참조하는 모델을 단일 객체로 가리키므로 의미가 명확하도록 소문자 단수형으로 작성하는 것이 좋습니다. 예: `article = models.ForeignKey(...)`
