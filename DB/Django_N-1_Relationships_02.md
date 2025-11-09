# Django Many To One Relationships 02

## 목차
1. [Article & User](#article--user)
   - 모델 관계 설정
   - 게시글 CREATE
   - 게시글 READ
   - 게시글 UPDATE
   - 게시글 DELETE
2. [Comment & User](#comment--user)
   - 모델 관계 설정
   - 댓글 CREATE
   - 댓글 READ
   - 댓글 DELETE
3. [View decorators](#view-decorators)
   - Allowed HTTP methods
4. [ERD](#erd)
   - ERD 구성 요소
   - ERD 제작 사이트
5. [참고](#참고)
   - 추가 기능 구현

---

## 학습 목표

- User와 Article, User와 Comment 모델 간의 N:1 관계를 정의할 수 있다.
- 인증된 사용자만 게시글/댓글을 작성하거나 삭제할 수 있도록 구현할 수 있다.
- Django의 ORM을 활용해 CREATE/READ/UPDATE/DELETE 기능을 실습할 수 있다.
- View decorators를 통해 HTTP 요청 방식에 따라 기능을 제어할 수 있다.
- ERD를 활용해 모델 관계 구조를 시각적으로 표현하고 설명할 수 있다.

---

## Article & User

### 모델 관계 설정

#### User 외래 키 정의

```python
# articles/models.py
from django.conf import settings

# User 모델을 직접 import 해서 사용하지 않음을 유의
class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### User 모델을 직접 Import 하지 않는 이유

💡 **TIP**: Article 클래스 생성 시점이 User 클래스 시점보다 빠른 경우 외래 키 설정에서 참고할 User 모델을 찾지 못해 에러가 발생할 수 있어요. `models.py`에서는 안정적인 참조가 필요하기 때문에 `settings.AUTH_USER_MODEL`의 값을 사용해요.

#### User 모델을 참조하는 2가지 방법

1. **settings.AUTH_USER_MODEL**
   - `settings.py`에서 정의된 `AUTH_USER_MODEL` 설정 값을 가져옴
   - 반환 값: `'accounts.User'` (문자열)
   - `models.py`에서 User 모델을 참조할 때 주로 사용

2. **get_user_model()**
   - 현재 `settings.py`에 정의되어 활성화된 User 모델을 가져옴
   - 반환 값: User Object (객체)
   - `models.py`를 제외한 다른 모든 위치에서 사용

💡 **TIP**: `settings.AUTH_USER_MODEL`의 반환 값이 문자열이어도 괜찮은 이유는 모델의 경로 형태인 문자열이 ForeignKey의 참조 모델로 설정되면 Django에서 내부적으로 해당 모델이 완전히 로딩된 후 모델 클래스를 가져와 처리하는 지연 평가(lazy evaluation) 방식으로 동작하기 때문입니다.

#### Migration

**1단계: makemigrations 실행**

기존에 테이블이 있는 상황에서 필드를 추가하려고 하기 때문에 발생하는 과정입니다.
기본적으로 모든 필드에는 NOT NULL 제약 조건이 설정되어 있어, 데이터 없이 새로운 필드를 추가할 수 없습니다.

```bash
$ python manage.py makemigrations
```

```
It is impossible to add a non-nullable field 'user' to article without specifying a default.
This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option:
```

'1'을 입력하고 Enter 진행 (다음 화면에서 직접 기본 값 입력)

**2단계: 기본값 입력**

추가하는 외래 키 필드에 어떤 데이터를 넣을 것인지 직접 입력해야 합니다.
마찬가지로 '1'을 입력하고 Enter 진행합니다.
기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됩니다.

```
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>>
```

⚠️ **주의**: 1번 회원이 없는 경우 migrate 시 에러 발생할 수 있음을 유의

**3단계: migrate 진행**

migrations 파일 생성 후 migrate 진행

```bash
$ python manage.py migrate
```

`articles_article` 테이블에 `user_id` 필드 생성 확인

---

### 게시글 CREATE

#### CREATE 구현 (1/5): 문제 발견

새 게시글 작성 시 ArticleForm 출력 변화 확인
- 새롭게 추가된 ForeignKey 필드인 User 필드 확인됨
- User 모델에 대한 사용자 입력 창이 나오지만 사용자가 입력하지 않아야 하는 입력
- 다른 사람을 선택하게 되면 인증에 대한 문제가 발생할 수 있음

#### CREATE 구현 (2/5): Form 수정

기존 ArticleForm에서 사용자가 입력할 수 있는 필드를 변경
- 글 작성자는 사용자가 선택하지 않아도 되는 정보
- 사용자는 게시글 제목과 내용만 입력하도록 수정

```python
# articles/forms.py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
```

#### CREATE 구현 (3/5): 에러 발생

게시글을 작성하면 아래와 같이 에러가 발생
```
NOT NULL constraint failed: articles_article.user_id
```

`user_id` 필드 데이터가 누락되어 NOT NULL 제약 조건에 위배

#### CREATE 구현 (4/5): 해결 방법

게시글 작성 시 작성자 정보가 자동으로 저장될 수 있도록 view 함수 수정

```python
# articles/views.py
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

#### CREATE 구현 (5/5): 작동 원리

**`save(commit=False)`의 역할**
- DB에 저장하지 않고 인스턴스만 반환
- 외래 키 데이터를 따로 처리해야 할 때 사용

**작성자 정보 저장**
```python
article = form.save(commit=False)  # DB 저장 전 인스턴스만 생성
article.user = request.user         # 작성자 정보 추가
article.save()                      # 최종 DB 저장
```

---

### 게시글 READ

#### 작성자 정보 출력

게시글 목록 및 상세 페이지에서 각 게시글의 작성자 출력

```django
<!-- articles/index.html -->
{% for article in articles %}
  <p>작성자: {{ article.user }}</p>
  <p>제목: {{ article.title }}</p>
  <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
  <hr>
{% endfor %}
```

```django
<!-- articles/detail.html -->
<h1>DETAIL</h1>
<h3>{{ article.pk }}번째 글</h3>
<hr>
<p>작성자: {{ article.user }}</p>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성 시각: {{ article.created_at }}</p>
<p>수정 시각: {{ article.updated_at }}</p>
```

---

### 게시글 UPDATE

#### 본인 확인 추가

게시글 수정 요청 사용자와 게시글 작성자를 비교하여 본인인 경우에만 수정 진행

```python
# articles/views.py
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

#### 템플릿 수정 버튼 표시

해당 게시글의 작성자가 아니라면 수정/삭제 버튼을 출력하지 않음

```django
<!-- articles/detail.html -->
{% if request.user == article.user %}
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
{% endif %}
```

---

### 게시글 DELETE

#### 본인 확인 추가

삭제 요청 사용자와 게시글 작성자를 비교하여 본인인 경우에만 삭제 진행

```python
# articles/views.py
@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')
```

---

## Comment & User

### 모델 관계 설정

#### User 외래 키 정의

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### Migration

이전과 동일하게 기존 댓글의 작성자를 '1'로 설정하고 migration 진행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

---

### 댓글 CREATE

#### CommentForm 수정

User 필드는 사용자로부터 입력 받지 않도록 수정

```python
# articles/forms.py
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
```

#### 댓글 작성 로직 수정

작성자 정보가 자동으로 저장될 수 있도록 view 함수 수정

```python
# articles/views.py
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)
```

---

### 댓글 READ

#### 작성자 정보 출력

댓글 목록에서 각 댓글의 작성자 출력

```django
<!-- articles/detail.html -->
<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}
    <li>
      {{ comment.user }} - {{ comment.content }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% endfor %}
</ul>
```

---

### 댓글 DELETE

#### 본인 확인 추가

삭제 요청 사용자와 댓글 작성자를 비교하여 본인인 경우에만 삭제 진행

```python
# articles/views.py
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

#### 템플릿 삭제 버튼 표시

해당 댓글의 작성자가 아니라면 삭제 버튼을 출력하지 않음

```django
<!-- articles/detail.html -->
<ul>
  {% for comment in comments %}
    <li>
      {{ comment.user }} - {{ comment.content }}
      {% if request.user == comment.user %}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      {% endif %}
    </li>
  {% endfor %}
</ul>
```

---

## View decorators

### Allowed HTTP methods

#### 개요

View 함수가 특정 요청 method에서만 실행되도록 하는 데코레이터

#### 종류

**1. require_http_methods()**
- View 함수가 특정 요청 method만 허용하도록 설정

```python
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def create(request):
    pass

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    pass
```

**2. require_POST()**
- View 함수가 POST 요청 method만 허용하도록 설정

```python
from django.views.decorators.http import require_POST

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

**3. require_safe()**
- View 함수가 GET 및 HEAD 요청 method만 허용하도록 설정

```python
from django.views.decorators.http import require_safe

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_safe
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

#### 405 Method Not Allowed 에러

허용하지 않는 요청을 받았을 때 반환되는 HTTP 응답 상태 코드

---

## ERD

### ERD (Entity-Relationship Diagram)

데이터베이스의 구조를 시각적으로 표현하는 다이어그램
- 데이터베이스 설계의 핵심 도구
- 테이블 간의 관계를 명확히 보여줌

### ERD 구성 요소

#### 1. Entity (개체)
- 데이터베이스에 저장되는 객체나 개념
- 테이블에 해당

#### 2. Attribute (속성)
- Entity가 가지는 속성이나 특성
- 테이블의 컬럼에 해당

#### 3. Relationship (관계)
- Entity 간의 관계
- 테이블 간의 연결을 나타냄

### Relationship 표현 방법

**1:1 (One to One)**
```
Entity A ──── Entity B
```

**1:N (One to Many)**
```
Entity A ────< Entity B
```

**N:M (Many to Many)**
```
Entity A >────< Entity B
```

### Cardinality (기수)

관계에 참여하는 Entity의 수를 나타냄
- (1, 1): 정확히 1개
- (0, 1): 0개 또는 1개
- (1, N): 1개 이상
- (0, N): 0개 이상

### ERD 예시

**User - Article - Comment 관계**
```
User ────< Article ────< Comment
(1)        (N)          (N)
```

- 한 명의 User는 여러 Article을 작성할 수 있음 (1:N)
- 한 명의 User는 여러 Comment를 작성할 수 있음 (1:N)
- 하나의 Article은 여러 Comment를 가질 수 있음 (1:N)

### ERD 제작 사이트

**1. Draw.io (diagrams.net)**
- 별도의 회원가입 없이 바로 사용 가능
- 다양한 다이어그램 템플릿 제공
- https://app.diagrams.net/

**2. ERDCloud**
- 실시간 협업 기능 지원
- https://www.erdcloud.com/

---

## 참고

### 추가 기능 구현

#### 인증된 사용자만 댓글 작성 및 삭제

로그인 사용자만 댓글을 작성할 수 있도록 데코레이터 추가

```python
# articles/views.py
@login_required
def comments_create(request, pk):
    pass

@login_required
def comments_delete(request, article_pk, comment_pk):
    pass
```

---

## 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| User 참조 방법 | `settings.AUTH_USER_MODEL`로 사용자 모델을 참조 | `user = models.ForeignKey(settings.AUTH_USER_MODEL, ...)` |
| View Decorator | View 함수에 조건을 부여해 특정 요청만 허용 | `@require_http_methods(["POST"])` |
| 인증 기반 기능 | 로그인한 사용자만 특정 기능을 수행할 수 있도록 제한 | `request.user.is_authenticated` 조건문 활용 |
| ERD 구성 요소 | 모델 이름, 필드명, 관계(선) 등으로 구성된 데이터베이스 구조도 | 게시글 - 댓글 - 사용자 사이의 관계선 연결 |
| 댓글 기능 제한 | 비로그인 사용자의 댓글 작성/삭제 요청은 처리하지 않음 | `if not request.user.is_authenticated: return redirect()` |
| Article-User 관계 | 하나의 User가 여러 개의 Article을 작성할 수 있는 구조 | 여러 게시글 > 하나의 작성자 |
| Comment-User 관계 | 하나의 User가 여러 개의 Comment를 작성할 수 있는 구조 | 여러 댓글 > 하나의 작성자 |

---

## 요약 및 정리

1. **`settings.AUTH_USER_MODEL`을 활용해 사용자와 게시글, 댓글 모델 간의 관계를 설정합니다.**
   - 이를 통해 로그인 사용자 기반의 기능 구현이 가능합니다.

2. **게시글과 댓글의 CRUD 기능은 Django ORM을 통해 처리됩니다.**
   - View decorator를 사용해 HTTP 메서드에 따른 요청 제한도 학습했습니다.
   - 허용한 요청이 아닌 경우 HttpResponseNotAllowed(405) 에러가 발생합니다.

3. **인증되지 않은 사용자는 댓글 작성 및 삭제를 할 수 없도록 기능을 제한하는 로직을 실습했습니다.**

4. **ERD를 통해 Article, Comment, User 모델 간의 관계를 시각적으로 정리하고 구조를 이해했습니다.**

5. **다음 단계**
   - 참조 필드는 N:1에서 N에 해당하는 모델 클래스에 작성합니다.
   - 각각 N:1 관계를 가지도록 모델을 설계합니다.
     - 유저(1) : 게시글(N)
     - 유저(1) : 댓글(N)
   - User 모델은 `settings.AUTH_USER_MODEL`을 참조해 게시글과 댓글 작성자를 `ForeignKey`를 사용하여 연결합니다.
   - Django의 ORM을 활용해 Article과 Comment 모델의 CRUD 기능을 구현합니다.
   - View decorators를 사용해 허용된 HTTP 요청만 처리하고 그 외 요청은 에러 처리할 수 있습니다.
   - ERD를 통해 모델 간 관계를 시각적으로 정리하고 구조를 한눈에 파악하여 프로젝트의 이해를 높일 수 있습니다.
   - 로그인 확인 decorator를 통해 인증된 사용자만 글 작성을 할 수 있게 만들었습니다.

---

## 확인 문제 정답

1. **ForeignKey(settings.AUTH_USER_MODEL, ...)** - User 모델을 안전하게 참조하기 위해 `settings.AUTH_USER_MODEL`을 사용한다. N:1 관계에는 ForeignKey를 사용합니다.

2. **c) models.py 외부 파일** - `get_user_model()`은 `settings.AUTH_USER_MODEL`을 객체로 반환하며, `models.py`를 제외한 `views.py`, `forms.py` 등 외부에서 사용됩니다.

3. **b) 기본값 입력** - NOT NULL 제약 조건 때문에 기존 데이터에 대한 기본값을 입력해야 마이그레이션이 가능합니다.

4. **c) article.user = request.user** - 작성자 정보는 `form.save(commit=False)` 이후 `request.user`를 직접 할당해 저장해야 합니다.

5. **b) NOT NULL constraint failed** - user 필드가 비어 있으면 DB의 NOT NULL 제약 조건 위반으로 에러가 발생합니다.

6. **c) 로그인한 사용자만 접근 허용** - `@login_required` 데코레이터는 인증된 사용자만 해당 뷰를 사용할 수 있게 제한합니다.

7. **b) POST만 허용** - `require_POST`는 해당 뷰가 POST 요청만 처리하도록 제한하고 다른 요청은 405 에러를 반환합니다.

8. **a) 테이블** - ERD에서 엔티티는 데이터베이스의 테이블을 의미하며, 저장되는 개체나 개념을 나타냅니다.

9. **b) 컬럼 정보** - 속성(Attribute)은 엔티티가 가지는 데이터 항목이며 데이터베이스에서는 컬럼으로 표현됩니다.

10. **b) request.user와 comment.user** - 댓글 작성자만 삭제할 수 있도록 하기 위해 요청한 사용자(`request.user`)와 댓글의 작성자(`comment.user`)를 비교합니다.

11. **c) {{ comment.user }} {{ comment.content }}** - 템플릿에서는 comment 객체의 user(작성자)와 content(내용) 속성을 함께 출력하여 댓글 정보를 표시합니다.

12. **c) 작성자 본인인지 확인** - 작성자 본인만 수정 또는 삭제할 수 있도록 하기 위해 `request.user`와 객체의 user를 비교합니다.

13. **b) 테이블 구조 시각화** - ERD는 데이터베이스의 테이블과 관계를 시각적으로 표현하여 구조를 쉽게 이해하고 설계할 수 있게 돕는 도구입니다.

14. **request.user** - `request.user`는 현재 요청을 보낸 사용자이며, `comment.user`는 댓글을 작성한 사용자입니다. 두 값을 비교해 작성자 본인인지 확인합니다.

15. **c) 에러 없이 안전하게 참조하려고** - `settings.AUTH_USER_MODEL`은 모델 로딩 순서에 상관없이 User를 안정적으로 참조할 수 있게 합니다.

16. **request.user** - 로그인한 사용자의 정보를 게시글의 작성자로 저장하기 위해 `article.user`에 `request.user`를 할당합니다.
