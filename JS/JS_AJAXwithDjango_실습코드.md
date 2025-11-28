# Django Ajax 실습 프로젝트 완전 정리

## 📚 목차

1. [프로젝트 구조](#1-프로젝트-구조)
2. [프로젝트 설정 (settings.py)](#2-프로젝트-설정-settingspy)
3. [URL 라우팅 구조](#3-url-라우팅-구조)
4. [Accounts 앱 (사용자 관리)](#4-accounts-앱-사용자-관리)
5. [Articles 앱 (게시글 관리)](#5-articles-앱-게시글-관리)
6. [Ajax 비동기 처리](#6-ajax-비동기-처리)
7. [이 코드 스타일의 장점](#7-이-코드-스타일의-장점)
8. [학습 포인트](#8-학습-포인트)

---

## 1. 프로젝트 구조

### 프로젝트 개요

**프로젝트명**: `crud`  
**앱 구성**: `accounts`(사용자 관리), `articles`(게시글 관리)

```
crud/                          # 프로젝트 루트
├── crud/                      # 프로젝트 설정 디렉토리
│   ├── settings.py            # 프로젝트 전역 설정
│   └── urls.py                # 프로젝트 메인 URL 설정
│
├── accounts/                  # 사용자 관리 앱
│   ├── models.py              # User 모델 (커스텀)
│   ├── forms.py               # 회원가입/정보수정 폼
│   ├── views.py               # 로그인/회원가입/팔로우 등
│   ├── urls.py                # accounts 관련 URL
│   └── templates/accounts/    # accounts 템플릿
│       ├── login.html         # 로그인
│       ├── signup.html        # 회원가입
│       ├── profile.html       # 프로필 (팔로우 기능)
│       ├── update.html        # 회원정보 수정
│       └── password.html      # 비밀번호 변경
│
└── articles/                  # 게시글 관리 앱
    ├── models.py              # Article, Comment 모델
    ├── forms.py               # 게시글/댓글 폼
    ├── views.py               # CRUD, 댓글, 좋아요 등
    ├── urls.py                # articles 관련 URL
    └── templates/articles/    # articles 템플릿
        ├── index.html         # 게시글 목록 (좋아요 기능)
        ├── detail.html        # 게시글 상세
        ├── create.html        # 게시글 작성
        └── update.html        # 게시글 수정
```

**핵심 기능**:
1. **사용자 인증**: 로그인, 회원가입, 정보수정, 탈퇴
2. **팔로우 시스템**: 사용자 간 팔로우/언팔로우 (Ajax)
3. **게시글 CRUD**: 생성, 조회, 수정, 삭제
4. **댓글 기능**: 게시글에 댓글 작성/삭제
5. **좋아요 기능**: 게시글 좋아요/취소 (Ajax)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

---

## 2. 프로젝트 설정 (settings.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

### settings.py - 핵심 설정

```python
"""
Django settings for crud project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-s^sy*1s!!n!je6ka3bh_4j^t#j0ydhr89yo6qpw3q32npik!cd'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'articles',        # 게시글 앱
    'accounts',        # 사용자 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF 보안
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # 각 앱의 templates 폴더 자동 인식
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crud.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ⭐ 커스텀 User 모델 사용 (매우 중요!)
AUTH_USER_MODEL = 'accounts.User'

# 이메일을 콘솔에 출력 (개발 환경)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

**핵심 포인트**:

### 1. INSTALLED_APPS 순서
```python
INSTALLED_APPS = [
    'articles',    # 커스텀 앱을 먼저 등록
    'accounts',
    'django.contrib.admin',  # 기본 앱들
    # ...
]
```
**이유**: 커스텀 앱을 먼저 등록하면 템플릿이나 static 파일을 찾을 때 우선순위를 가짐

### 2. AUTH_USER_MODEL 설정
```python
AUTH_USER_MODEL = 'accounts.User'
```
**매우 중요!** Django 기본 User 모델 대신 커스텀 User 모델 사용
- **반드시 프로젝트 시작 시** 설정해야 함
- 나중에 변경하면 데이터베이스 마이그레이션 문제 발생
- M:N 관계(팔로우)를 위해 필요

### 3. CSRF 보안
```python
'django.middleware.csrf.CsrfViewMiddleware',
```
- POST 요청 시 CSRF 토큰 검증
- Ajax 요청에서도 **반드시** CSRF 토큰을 헤더에 포함해야 함

---

## 3. URL 라우팅 구조

### 프로젝트 메인 urls.py

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

```python
"""
URL configuration for crud project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),    # articles 앱 URL
    path('accounts/', include('accounts.urls')),    # accounts 앱 URL
    path('accounts/', include('django.contrib.auth.urls')),  # Django 기본 인증 URL
]
```

**URL 구조**:
```
/admin/                          → Django 관리자 페이지
/articles/                       → 게시글 목록
/articles/<pk>/                  → 게시글 상세
/articles/create/                → 게시글 작성
/articles/<pk>/likes/            → 좋아요 (Ajax) ⭐
/accounts/login/                 → 로그인
/accounts/signup/                → 회원가입
/accounts/profile/<username>/    → 프로필
/accounts/<user_pk>/follow/      → 팔로우 (Ajax) ⭐
```

**핵심 포인트**:
- `include()`로 앱별 URL 분리 → **모듈화**
- `app_name`으로 네임스페이스 분리 → **충돌 방지**
- Ajax 요청 URL도 동일한 패턴 사용 → **일관성**

---

## 4. Accounts 앱 (사용자 관리)

### 4.1. Models (accounts/models.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax with follow" 섹션

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # M:N 관계: 팔로우 기능
    followings = models.ManyToManyField(
        'self',                     # 자기 자신을 참조
        symmetrical=False,          # 비대칭 관계 (맞팔 자동 X)
        related_name='followers'    # 역참조 이름
    )
```

**핵심 개념**:

### ManyToManyField 파라미터 설명

```python
followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

**1. `'self'` - 자기 참조**:
- User 모델이 User 모델을 참조
- 사용자가 다른 사용자를 팔로우하는 관계

**2. `symmetrical=False` - 비대칭**:
```python
# symmetrical=True (대칭)이면:
A가 B를 팔로우 → B도 자동으로 A를 팔로우 (친구 관계)

# symmetrical=False (비대칭)이면:
A가 B를 팔로우 → B는 A를 자동으로 팔로우하지 않음 (인스타그램 스타일) ⭐
```

**3. `related_name='followers'` - 역참조**:
```python
# user1이 user2를 팔로우한 경우:
user1.followings.all()  # user1이 팔로우하는 사람들
user2.followers.all()   # user2를 팔로우하는 사람들
```

**데이터베이스 구조**:
```
User 테이블:
id | username | email | ...
1  | alice    | ...   | ...
2  | bob      | ...   | ...
3  | charlie  | ...   | ...

User_followings 테이블 (중간 테이블 자동 생성):
from_user_id | to_user_id
1            | 2         (alice가 bob을 팔로우)
1            | 3         (alice가 charlie를 팔로우)
2            | 3         (bob이 charlie를 팔로우)
```

**실제 사용 예시**:
```python
# alice가 bob을 팔로우
alice.followings.add(bob)

# alice가 팔로우하는 사람들
alice.followings.all()  # [bob, charlie]

# bob을 팔로우하는 사람들
bob.followers.all()     # [alice]

# 팔로우 취소
alice.followings.remove(bob)
```

---

### 4.2. Forms (accounts/forms.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """회원가입 폼"""
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # settings.AUTH_USER_MODEL 사용


class CustomUserChangeForm(UserChangeForm):
    """회원정보 수정 폼"""
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
        )
```

**핵심 포인트**:

**1. `get_user_model()` 사용**:
```python
# ❌ 잘못된 방법
from accounts.models import User

# ✅ 올바른 방법
from django.contrib.auth import get_user_model
User = get_user_model()
```
**이유**: settings.AUTH_USER_MODEL을 동적으로 가져오므로 모델 변경 시 유연함

**2. Meta 클래스 상속**:
```python
class Meta(UserCreationForm.Meta):
    model = get_user_model()
```
**이유**: 부모 클래스의 Meta 설정을 상속받아 필요한 부분만 수정

**3. CustomUserChangeForm에서 fields 제한**:
```python
fields = ('email', 'first_name', 'last_name',)
```
**이유**: 
- 일반 사용자가 수정하면 안 되는 필드 제외 (is_staff, is_superuser 등)
- 보안 강화

---

### 4.3. Views (accounts/views.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "비동기 팔로우 구현" 섹션

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.http import JsonResponse


# ========== 로그인 ==========
def login(request):
    # 이미 로그인한 사용자는 메인으로
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# ========== 로그아웃 ==========
@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


# ========== 회원가입 ==========
def signup(request):
    # 이미 로그인한 사용자는 메인으로
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


# ========== 회원탈퇴 ==========
@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')


# ========== 회원정보 수정 ==========
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


# ========== 비밀번호 변경 ==========
@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호 변경 후 세션 유지
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)


# ========== 프로필 페이지 ==========
def profile(request, username):
    """해당 프로필 페이지의 유저를 조회"""
    User = get_user_model()
    person = User.objects.get(username=username)
    
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


# ========== 팔로우 (Ajax) ⭐ ==========
@login_required
def follow(request, user_pk):
    """
    팔로우/언팔로우를 비동기로 처리
    - HTML 페이지 대신 JSON 응답 반환
    """
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    
    # 자기 자신은 팔로우할 수 없음
    if person != request.user:
        # 이미 팔로우 중이면 언팔로우
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            is_followed = False
        # 팔로우하지 않았으면 팔로우
        else:
            person.followers.add(request.user)
            is_followed = True
        
        # JSON 응답 데이터 준비
        context = {
            'is_followed': is_followed,
            'followings_count': person.followings.count(),
            'followers_count': person.followers.count()
        }
        
        # ⭐ HTML 대신 JSON 반환
        return JsonResponse(context)
    
    # 자기 자신을 팔로우하려고 하면 프로필로 리다이렉트
    return redirect('accounts:profile', person.username)
```

**핵심 포인트**:

### 1. 함수 이름 충돌 방지
```python
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    auth_login(request, user)  # Django의 login 함수 사용
```
**이유**: 뷰 함수 이름과 Django 내장 함수 이름이 겹치지 않도록

### 2. @login_required 데코레이터
```python
@login_required
def logout(request):
    auth_logout(request)
```
**역할**: 로그인하지 않은 사용자의 접근 차단

### 3. 비밀번호 변경 후 세션 유지
```python
user = form.save()
update_session_auth_hash(request, user)
```
**이유**: 비밀번호 변경 시 세션이 무효화되어 자동 로그아웃되는 것을 방지

### 4. follow 함수의 Ajax 처리 핵심

**기존 동기 방식**:
```python
def follow(request, user_pk):
    # ... 팔로우 로직 ...
    return redirect('accounts:profile', person.username)  # 페이지 새로고침
```

**비동기 방식 (Ajax)**:
```python
@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    
    if person != request.user:
        # 팔로우/언팔로우 처리
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            is_followed = False
        else:
            person.followers.add(request.user)
            is_followed = True
        
        # ⭐ JSON 응답 반환 (페이지 새로고침 없음)
        context = {
            'is_followed': is_followed,
            'followings_count': person.followings.count(),
            'followers_count': person.followers.count()
        }
        return JsonResponse(context)
    
    return redirect('accounts:profile', person.username)
```

**JsonResponse의 역할**:
```python
return JsonResponse({
    'is_followed': True,
    'followers_count': 10
})

# JavaScript에서 받는 데이터:
{
    "is_followed": true,
    "followers_count": 10
}
```

### 5. .exists() vs .count() vs .all()

```python
# 존재 여부만 확인 (가장 빠름) ⭐
if person.followers.filter(pk=request.user.pk).exists():

# 개수 확인
followers_count = person.followers.count()

# 전체 데이터 가져오기 (느림)
followers_list = person.followers.all()
```

**성능 비교**:
- `exists()`: 데이터 존재만 확인 → **가장 빠름**
- `count()`: 개수만 세기 → **빠름**
- `all()`: 전체 데이터 로드 → **느림**

---

### 4.4. URLs (accounts/urls.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax with follow" 섹션

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    path('profile/<username>/', views.profile, name='profile'),
    # ⭐ Ajax 팔로우 URL
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

**핵심 포인트**:

**1. app_name으로 네임스페이스 설정**:
```python
app_name = 'accounts'
```
→ 템플릿에서 `{% url 'accounts:login' %}`으로 사용

**2. URL 패턴 순서**:
```python
path('profile/<username>/', ...)  # 문자열 파라미터
path('<int:user_pk>/follow/', ...)  # 정수 파라미터
```
→ 더 구체적인 패턴을 위에 배치

**3. Ajax URL도 동일한 RESTful 패턴**:
```python
path('<int:user_pk>/follow/', views.follow, name='follow')
```
→ `/accounts/1/follow/` 형태로 명확함

---

### 4.5. Templates

#### profile.html - 팔로우 기능 (Ajax)

**교안 참조**: JavaScript_Ajax_with_Django.md - "비동기 팔로우 구현" 전체 섹션

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>{{ person.username }}님의 프로필</h1>
  
  <!-- ⭐ 팔로워/팔로잉 수 (동적으로 업데이트됨) -->
  <div>
    팔로워 : <span id='followers-count'>{{ person.followers.all|length }}</span> / 
    팔로우 : <span id='followings-count'>{{ person.followings.all|length }}</span>
  </div>

  <!-- ⭐ 팔로우 버튼 (자기 자신 제외) -->
  {% if request.user != person %}
    <!-- data-user-id: Django → JavaScript 데이터 전달 ⭐ -->
    <form action="{% url "accounts:follow" person.pk %}" 
          method="POST" 
          id="follow-form" 
          data-user-id="{{ person.pk }}"> 
      {% csrf_token %}
      
      {% if request.user in person.followers.all %}
        <input type="submit" value='UnFollow'>
      {% else %}
        <input type="submit" value='Follow'>
      {% endif %}
    </form>
  {% endif %}
  
  <hr>

  <!-- 게시글 목록 -->
  <h2>{{ person.username }} 작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
  <hr>

  <!-- 댓글 목록 -->
  <h2>{{ person.username }} 작성한 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}
  <hr>

  <!-- 좋아요 한 게시글 -->
  <h2>{{ person.username }} 좋아요 한 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <!-- ⭐ Axios CDN -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // ========== 1. HTML 요소 선택 ==========
    const formTag = document.querySelector('#follow-form')
    
    // ========== 2. 폼 제출 이벤트 리스너 ==========
    formTag.addEventListener('submit', function (event){
      // ⭐ 기본 동작(새로고침) 막기
      event.preventDefault()
      
      // ========== 3. 데이터 수집 ==========
      
      // 방법1. event.currentTarget: 이벤트 리스너가 부착된 요소(formTag) ⭐ 추천
      // - 가장 명시적이고 안정적
      // - 화살표 함수와 호환됨
      const userId = event.currentTarget.dataset.userId
      
      // 방법2. this: 일반 함수에서만 이벤트 리스너가 부착된 요소를 가리킴
      // - 화살표 함수에서는 작동하지 않음 ❌
      // const userId = this.dataset.userId
      
      // 방법3. formTag: 직접 참조
      // - 이벤트 핸들러가 formTag에 접근할 수 있는 스코프여야 함
      // const userId = formTag.dataset.userId
      
      // CSRF 토큰 가져오기
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      
      // ========== 4. Axios 요청 ==========
      axios({
        method: 'POST',
        url: `/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken},  // ⭐ CSRF 토큰 필수
      })
      
      // ========== 5. 응답 처리 (.then) ==========
      .then((response) => {
        // Django에서 보낸 JSON 데이터
        const isFollowed = response.data.is_followed
        const followingsCount = response.data.followings_count
        const followersCount = response.data.followers_count
        
        // ========== 6. DOM 업데이트 ==========
        
        // 버튼 텍스트 변경
        const followBtn = document.querySelector('input[type=submit]')
        if (isFollowed === true) {
          followBtn.value = 'UnFollow'
        } else {
          followBtn.value = 'Follow'
        }
        
        // 팔로워/팔로잉 수 업데이트
        const followingsCountTag = document.querySelector('#followings-count')
        const followersCountTag = document.querySelector('#followers-count')
        followingsCountTag.textContent = followingsCount
        followersCountTag.textContent = followersCount
      })
    })
  </script>
</body>
</html>
```

**핵심 개념**:

### 1. data-* 속성으로 Django → JavaScript 데이터 전달

**HTML (Django 템플릿)**:
```html
<form data-user-id="{{ person.pk }}">
```
→ `<form data-user-id="1">`로 렌더링

**JavaScript**:
```javascript
const userId = formTag.dataset.userId  // "1"
```

**왜 이 방법을 사용할까?**
- URL에 직접 하드코딩하지 않아도 됨
- 동적으로 데이터 전달 가능
- HTML의 data-* 표준 활용

### 2. event.currentTarget vs event.target vs this

```javascript
formTag.addEventListener('submit', function (event) {
  // event.currentTarget: 이벤트 리스너가 부착된 요소 (formTag)
  const userId = event.currentTarget.dataset.userId  // ✅ 추천
  
  // event.target: 실제로 이벤트가 발생한 요소 (버튼 등)
  // 버블링 시 다른 요소일 수 있음
  
  // this: 일반 함수에서는 formTag, 화살표 함수에서는 상위 스코프
  // const userId = this.dataset.userId  // 일반 함수에서만 작동
})
```

**추천**: `event.currentTarget` - 명시적이고 안정적

### 3. CSRF 토큰 처리

**1단계: HTML에서 토큰 가져오기**:
```javascript
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
```

**2단계: Axios 헤더에 포함**:
```javascript
axios({
  headers: {'X-CSRFToken': csrftoken}
})
```

**중요**: Django의 CSRF 보안을 통과하려면 **반드시** 필요

### 4. 비동기 처리 흐름

```
1. 버튼 클릭
   ↓
2. event.preventDefault() → 새로고침 막기
   ↓
3. userId, csrftoken 수집
   ↓
4. axios() → Django 서버에 POST 요청
   ↓
5. (백그라운드) 서버 처리
   ↓
6. .then() → JSON 응답 받기
   ↓
7. DOM 업데이트 (버튼 텍스트, 숫자 변경)
```

**장점**: 페이지 새로고침 없이 부분적으로만 업데이트!

---

#### 기타 템플릿 (login.html, signup.html 등)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

이 템플릿들은 **일반적인 Django Form 렌더링**을 사용합니다.

**공통 구조**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>페이지 제목</h1>
  <form action="{% url 'app_name:view_name' %}" method="POST">
    {% csrf_token %}
    {{ form }}  <!-- Django Form 자동 렌더링 -->
    <input type="submit">
  </form>
</body>
</html>
```

**특징**:
- Ajax를 사용하지 않음 (일반 동기 방식)
- `{{ form }}`: Django가 자동으로 input 필드 생성
- 제출 시 페이지 새로고침 발생

---

## 5. Articles 앱 (게시글 관리)

### 5.1. Models (articles/models.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax with likes" 섹션

```python
from django.db import models
from django.conf import settings


# ========== 게시글 모델 ==========
class Article(models.Model):
    # 작성자 (ForeignKey: 1:N 관계)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # User 모델 참조
        on_delete=models.CASCADE   # 사용자 삭제 시 게시글도 삭제
    )
    
    # 좋아요 (ManyToManyField: M:N 관계)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_articles'  # user.like_articles.all()
    )
    
    # 게시글 필드
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시각
    updated_at = models.DateTimeField(auto_now=True)      # 수정 시각


# ========== 댓글 모델 ==========
class Comment(models.Model):
    # 게시글 (ForeignKey: 1:N 관계)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE  # 게시글 삭제 시 댓글도 삭제
    )
    
    # 작성자 (ForeignKey: 1:N 관계)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    # 댓글 필드
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**핵심 개념**:

### 1. settings.AUTH_USER_MODEL 사용

```python
# ❌ 직접 import (나중에 문제 발생 가능)
from accounts.models import User

# ✅ settings 사용 (권장)
from django.conf import settings
user = models.ForeignKey(settings.AUTH_USER_MODEL, ...)
```

**이유**:
- User 모델이 변경되어도 코드 수정 불필요
- 앱 간 의존성 감소

### 2. 관계 이해하기

**1:N 관계 (ForeignKey)**:
```python
# User(1) : Article(N)
user = models.ForeignKey(settings.AUTH_USER_MODEL, ...)
```
→ 한 사용자가 여러 게시글 작성 가능

```python
# 역참조
user.article_set.all()  # 사용자가 작성한 모든 게시글
```

**M:N 관계 (ManyToManyField)**:
```python
# User(M) : Article(N) - 좋아요
like_users = models.ManyToManyField(
    settings.AUTH_USER_MODEL,
    related_name='like_articles'
)
```
→ 한 사용자가 여러 게시글에 좋아요 가능  
→ 한 게시글이 여러 사용자로부터 좋아요 받기 가능

```python
# 사용 예시
article.like_users.all()      # 게시글을 좋아요한 사용자들
user.like_articles.all()      # 사용자가 좋아요한 게시글들
```

### 3. auto_now vs auto_now_add

```python
created_at = models.DateTimeField(auto_now_add=True)  # 생성 시각 (한 번만)
updated_at = models.DateTimeField(auto_now=True)      # 수정 시각 (매번 업데이트)
```

**차이점**:
- `auto_now_add`: 객체 생성 시 **한 번만** 자동 설정
- `auto_now`: 객체 저장 시 **매번** 자동 업데이트

---

### 5.2. Forms (articles/forms.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

```python
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    """게시글 작성/수정 폼"""
    class Meta:
        model = Article
        # fields = '__all__'  # 모든 필드 (작성자 포함 - 문제 발생)
        fields = ('title', 'content',)  # ✅ 제목, 내용만


class CommentForm(forms.ModelForm):
    """댓글 작성 폼"""
    class Meta:
        model = Comment
        fields = ('content',)  # 댓글 내용만
```

**핵심 포인트**:

### fields 선택의 중요성

```python
# ❌ 모든 필드 포함 (문제 발생)
fields = '__all__'
# → user, like_users 필드까지 form에 나타남
# → 사용자가 다른 사람을 작성자로 선택 가능 (보안 문제)

# ✅ 필요한 필드만 포함
fields = ('title', 'content',)
# → user는 views.py에서 request.user로 자동 설정
```

**왜 이렇게 할까?**
- 보안: 사용자가 수정하면 안 되는 필드 제외
- 편의성: 불필요한 필드를 form에서 제거

---

### 5.3. Views (articles/views.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "비동기 좋아요 구현" 섹션

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse


# ========== 게시글 목록 ==========
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# ========== 게시글 상세 ==========
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


# ========== 게시글 작성 ==========
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # ⭐ DB에 바로 저장하지 않음
            article.user = request.user         # 작성자 설정
            article.save()                      # 이제 저장
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


# ========== 게시글 삭제 ==========
@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    
    # 작성자만 삭제 가능
    if request.user == article.user:
        article.delete()
    
    return redirect('articles:index')


# ========== 게시글 수정 ==========
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    # 작성자만 수정 가능
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


# ========== 댓글 작성 ==========
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article       # 게시글 연결
        comment.user = request.user     # 작성자 설정
        comment.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


# ========== 댓글 삭제 ==========
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    # 작성자만 삭제 가능
    if request.user == comment.user:
        comment.delete()
    
    return redirect('articles:detail', article_pk)


# ========== 좋아요 (Ajax) ⭐ ==========
@login_required
def likes(request, article_pk):
    """
    좋아요/취소를 비동기로 처리
    - HTML 페이지 대신 JSON 응답 반환
    """
    article = Article.objects.get(pk=article_pk)
    
    # 이미 좋아요를 눌렀으면 취소
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    # 좋아요하지 않았으면 추가
    else:
        article.like_users.add(request.user)
        is_liked = True
    
    # JSON 응답 데이터 준비
    context = {
        'is_liked': is_liked
    }
    
    # ⭐ HTML 대신 JSON 반환
    return JsonResponse(context)
```

**핵심 포인트**:

### 1. commit=False의 중요성

```python
# ❌ 잘못된 방법
article = form.save()          # 바로 DB에 저장
article.user = request.user    # 저장 후 수정 (비효율)
article.save()                 # 다시 저장

# ✅ 올바른 방법
article = form.save(commit=False)  # DB에 저장하지 않고 객체만 생성
article.user = request.user         # 작성자 설정
article.save()                      # 한 번만 저장
```

**장점**:
- DB 쿼리 최소화
- 필수 필드(user) 설정 후 한 번에 저장

### 2. 권한 검사

```python
# 작성자만 삭제/수정 가능
if request.user == article.user:
    article.delete()
```

**보안**: 다른 사용자가 URL로 직접 접근해도 실행 불가

### 3. likes 함수의 Ajax 처리

**기존 동기 방식**:
```python
def likes(request, article_pk):
    # ... 좋아요 로직 ...
    return redirect('articles:detail', article_pk)  # 페이지 새로고침
```

**비동기 방식 (Ajax)**:
```python
@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    # 좋아요/취소 토글
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    
    # ⭐ JSON 응답 반환 (페이지 새로고침 없음)
    context = {'is_liked': is_liked}
    return JsonResponse(context)
```

**차이점**:
- `redirect()` 대신 `JsonResponse()` 반환
- JavaScript가 받아서 DOM 업데이트

---

### 5.4. URLs (articles/urls.py)

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax with likes" 섹션

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comments_delete,
        name='comments_delete',
    ),
    # ⭐ 좋아요 Ajax URL
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

**핵심 포인트**:

**RESTful URL 설계**:
```python
# 게시글 관련
/articles/                     # 목록 (GET)
/articles/create/              # 작성 (GET, POST)
/articles/<pk>/                # 상세 (GET)
/articles/<pk>/update/         # 수정 (GET, POST)
/articles/<pk>/delete/         # 삭제 (POST)

# 댓글 관련
/articles/<pk>/comments/       # 댓글 작성 (POST)
/articles/<pk>/comments/<pk>/delete/  # 댓글 삭제 (POST)

# 좋아요 관련 (Ajax)
/articles/<pk>/likes/          # 좋아요 (POST, Ajax)
```

**장점**:
- URL만 봐도 기능 파악 가능
- 일관된 패턴으로 유지보수 쉬움

---

### 5.5. Templates

#### index.html - 게시글 목록 (좋아요 기능)

**교안 참조**: JavaScript_Ajax_with_Django.md - "비동기 좋아요 구현" 전체 섹션

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h3>Hello, {{ user.username }}</h3>

  <h1>메인 페이지</h1>

  <!-- 로그인/로그아웃 UI -->
  {% if request.user.is_authenticated %}
    <a href="{% url "accounts:profile" user.username %}">내 프로필</a>
    <form action="{% url "accounts:logout" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <a href="{% url "accounts:update" %}">회원정보수정</a>
    <form action="{% url "accounts:delete" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
    <a href="{% url "articles:create" %}">CREATE</a>
  {% else %}
    <a href="{% url "accounts:login" %}">Login</a>
    <a href="{% url "accounts:signup" %}">회원가입</a>
  {% endif %}

  <hr>
  
  <!-- ⭐ 게시글 목록 컨테이너 (이벤트 버블링 활용) -->
  <article class="article-container">
  {% for article in articles %}
    <div>
      <p>
        작성자 :
        <a href="{% url "accounts:profile" article.user.username %}">
          {{ article.user }}
        </a>
      </p>
      <p>글 번호: {{ article.pk }}</p>
      <p>
        글 제목: 
        <a href="{% url "articles:detail" article.pk %}">
          {{ article.title }}
        </a>
      </p>
      <p>글 내용: {{ article.content }}</p>
      
      <!-- ⭐ 좋아요 폼 (data-article-id로 게시글 구분) -->
      <form action="{% url "articles:likes" article.pk %}" 
            method="POST" 
            data-article-id="{{ article.pk }}"> 
        {% csrf_token %}
        
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소" id="like-{{article.pk}}">
        {% else %}
          <input type="submit" value="좋아요" id="like-{{article.pk}}">
        {% endif %}
      </form>
    </div>
    <hr>
  {% endfor %}
  </article>
  
  <!-- ⭐ Axios CDN -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // ========== 1. 공통 부모 요소 선택 (이벤트 버블링 활용) ⭐ ==========
    const articleContainer = document.querySelector('.article-container')
    
    // CSRF 토큰은 한 번만 가져오기
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    
    console.log(articleContainer)

    // ========== 2. 부모 요소에 이벤트 리스너 등록 (한 번만!) ==========
    articleContainer.addEventListener('submit', function (event) {
      // ⭐ 기본 동작(새로고침) 막기
      event.preventDefault()
      
      // ========== 3. 어떤 게시글의 폼인지 확인 ==========
      // event.target: 실제로 submit이 발생한 form 요소
      const articleId = event.target.dataset.articleId

      // ========== 4. Axios 요청 ==========
      axios({
        method: 'post',
        url: `/articles/${articleId}/likes/`,
        headers: {'X-CSRFToken': csrftoken},  // CSRF 토큰 포함
      })
      
      // ========== 5. 응답 처리 ==========
      .then((response) => {
        console.log(response)
        
        // Django에서 보낸 JSON 데이터
        const isLiked = response.data.is_liked
        
        // ========== 6. 해당 게시글의 버튼만 선택 ==========
        const likeBtn = document.querySelector(`#like-${articleId}`)
        
        // 버튼 텍스트 변경
        if(isLiked === true){
          likeBtn.value = "좋아요 취소"
        }else{
          likeBtn.value = "좋아요"
        }
      })
      .catch((error) => {
        console.log(error)
      })
    })
  </script>
</body>
</html>
```

**핵심 개념**:

### 1. 이벤트 버블링 (Event Bubbling)

**문제 상황**:
```html
<!-- 게시글이 100개라면? -->
<form id="like-1">...</form>  <!-- 이벤트 리스너 1 -->
<form id="like-2">...</form>  <!-- 이벤트 리스너 2 -->
<!-- ... -->
<form id="like-100">...</form>  <!-- 이벤트 리스너 100 -->
```
→ 100개의 이벤트 리스너 필요! (비효율적 ❌)

**해결책: 이벤트 버블링 활용**:
```html
<article class="article-container">  <!-- 이벤트 리스너 1개만! ⭐ -->
  <form data-article-id="1">...</form>
  <form data-article-id="2">...</form>
  <!-- ... -->
  <form data-article-id="100">...</form>
</article>
```

```javascript
// 부모에 이벤트 리스너 하나만 등록
articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()
  
  // 어떤 자식 form에서 이벤트가 발생했는지 확인
  const articleId = event.target.dataset.articleId  // ⭐
  
  // 해당 게시글 처리
  axios({
    url: `/articles/${articleId}/likes/`,
    // ...
  })
})
```

**이벤트 버블링이란?**
```
<article>           ← 이벤트가 여기까지 전파됨 (버블링)
  <form>            ← 이벤트가 여기서도 감지됨
    <input>         ← 실제 클릭한 곳 (event.target)
  </form>
</article>
```

**장점**:
- 이벤트 리스너 **1개**로 여러 요소 관리
- 동적으로 추가되는 요소에도 자동 적용
- 메모리 효율적

### 2. event.target vs event.currentTarget

```javascript
articleContainer.addEventListener('submit', function (event) {
  // event.target: 실제로 이벤트가 발생한 요소 (form)
  const articleId = event.target.dataset.articleId  // ⭐ 각 게시글 구분
  
  // event.currentTarget: 이벤트 리스너가 부착된 요소 (article-container)
  // const articleId = event.currentTarget.dataset.articleId  // ❌ undefined
})
```

**왜 event.target을 사용할까?**
- 여러 form 중 어떤 것이 submit되었는지 알아야 함
- `event.target`으로 실제 클릭된 form을 특정

### 3. 특정 버튼 선택하기

```javascript
// ❌ 잘못된 방법: 첫 번째 버튼만 선택됨
const likeBtn = document.querySelector('input[type=submit]')

// ✅ 올바른 방법: ID로 특정 버튼 선택
const likeBtn = document.querySelector(`#like-${articleId}`)
```

**HTML**:
```html
<input type="submit" value="좋아요" id="like-1">  <!-- 게시글 1 -->
<input type="submit" value="좋아요" id="like-2">  <!-- 게시글 2 -->
<input type="submit" value="좋아요" id="like-3">  <!-- 게시글 3 -->
```

**JavaScript**:
```javascript
const articleId = 2  // 게시글 2의 좋아요를 눌렀다면
const likeBtn = document.querySelector(`#like-${articleId}`)  // #like-2 선택
```

---

#### detail.html - 게시글 상세

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Detail</h1>
  <h2>{{ article.pk }} 번째 글</h2>
  <hr>
  
  <!-- 게시글 정보 -->
  <p>작성자 : {{ article.user }}</p>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성일: {{ article.created_at }}</p>
  <p>수정일: {{ article.updated_at }}</p>

  <hr>
  
  <!-- 댓글 목록 -->
  <ul>
  {% for comment in comments %}
    <li>
      {{ comment.user }} - {{ comment.content }}
      
      <!-- 댓글 작성자만 삭제 가능 -->
      {% if request.user == comment.user %}
        <form action="{% url "articles:comments_delete" article.pk comment.pk %}" 
              method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
        </form>
      {% endif %}
    </li>
  {% endfor %}
  </ul>

  <hr>
  
  <!-- 댓글 작성 폼 -->
  <form action="{% url "articles:comments_create" article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>

  <hr>

  <!-- 게시글 작성자만 수정/삭제 가능 -->
  {% if request.user == article.user %}
    <a href="{% url "articles:update" article.pk %}">수정하기</a><br>
    <form action="{% url "articles:delete" article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제하기">
    </form>
  {% endif %}
  
  <a href="{% url "articles:index" %}">[메인 페이지로]</a>
</body>
</html>
```

**핵심 포인트**:
- Ajax 사용하지 않음 (일반 동기 방식)
- 댓글과 게시글 수정/삭제 권한 검사
- `{% if request.user == article.user %}`로 작성자 확인

---

#### create.html, update.html - 게시글 작성/수정

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax와 서버" 섹션

**공통 구조**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Create / Update</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form }}  <!-- ArticleForm 자동 렌더링 -->
    <input type="submit">
  </form>
  
  <hr>
  <a href="{% url "articles:index" %}">[back]</a>
</body>
</html>
```

**특징**:
- Django Form 자동 렌더링 사용
- Ajax 없이 일반 POST 요청
- 제출 시 페이지 이동

---

## 6. Ajax 비동기 처리

### 6.1. 동기 vs 비동기 비교

**교안 참조**: JavaScript_Ajax_with_Django.md - 전체 문서

### 동기 방식 (기존)

```
1. 사용자 버튼 클릭
   ↓
2. form 제출 (POST 요청)
   ↓
3. 서버 처리
   ↓
4. 전체 HTML 페이지 반환
   ↓
5. 브라우저가 새 페이지로 전환 (새로고침)
```

**단점**:
- 전체 페이지 새로고침 (깜빡임)
- 네트워크 비용 증가 (HTML 전체 전송)
- 사용자 경험 저하

### 비동기 방식 (Ajax)

```
1. 사용자 버튼 클릭
   ↓
2. JavaScript가 Axios로 요청
   ↓
3. 서버 처리
   ↓
4. JSON 데이터만 반환
   ↓
5. JavaScript가 DOM의 일부만 업데이트
```

**장점**:
- 페이지 새로고침 없음 (부드러운 UX)
- 필요한 데이터만 전송 (효율적)
- 빠른 응답 속도

---

### 6.2. Ajax 구현 패턴

**교안 참조**: JavaScript_Ajax_with_Django.md - "핵심 정리" 섹션

#### 패턴 1: 단일 요소 (팔로우)

**HTML**:
```html
<form id="follow-form" data-user-id="{{ person.pk }}">
  {% csrf_token %}
  <input type="submit" value="Follow">
</form>
```

**JavaScript**:
```javascript
// 1. 요소 선택
const formTag = document.querySelector('#follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

// 2. 이벤트 리스너
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  
  const userId = event.currentTarget.dataset.userId
  
  // 3. Ajax 요청
  axios({
    method: 'POST',
    url: `/accounts/${userId}/follow/`,
    headers: {'X-CSRFToken': csrftoken}
  })
  .then((response) => {
    // 4. DOM 업데이트
    const isFollowed = response.data.is_followed
    const followBtn = document.querySelector('input[type=submit]')
    
    if (isFollowed) {
      followBtn.value = 'UnFollow'
    } else {
      followBtn.value = 'Follow'
    }
  })
})
```

**Django**:
```python
@login_required
def follow(request, user_pk):
    # ... 로직 ...
    
    context = {
        'is_followed': is_followed,
        'followers_count': person.followers.count()
    }
    return JsonResponse(context)
```

---

#### 패턴 2: 여러 요소 (좋아요)

**HTML**:
```html
<article class="article-container">  <!-- 부모 -->
  {% for article in articles %}
    <form data-article-id="{{ article.pk }}">  <!-- 자식들 -->
      {% csrf_token %}
      <input type="submit" value="좋아요" id="like-{{ article.pk }}">
    </form>
  {% endfor %}
</article>
```

**JavaScript** (이벤트 버블링):
```javascript
// 1. 부모 요소에 이벤트 리스너 하나만
const articleContainer = document.querySelector('.article-container')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()
  
  // 2. 어떤 자식에서 이벤트가 발생했는지 확인
  const articleId = event.target.dataset.articleId
  
  // 3. Ajax 요청
  axios({
    method: 'post',
    url: `/articles/${articleId}/likes/`,
    headers: {'X-CSRFToken': csrftoken}
  })
  .then((response) => {
    // 4. 해당 게시글의 버튼만 업데이트
    const isLiked = response.data.is_liked
    const likeBtn = document.querySelector(`#like-${articleId}`)
    
    if (isLiked) {
      likeBtn.value = '좋아요 취소'
    } else {
      likeBtn.value = '좋아요'
    }
  })
})
```

**Django**:
```python
@login_required
def likes(request, article_pk):
    # ... 로직 ...
    
    context = {'is_liked': is_liked}
    return JsonResponse(context)
```

---

### 6.3. CSRF 토큰 처리

**교안 참조**: JavaScript_Ajax_with_Django.md - "Ajax 적용" 섹션들

**Django의 CSRF 보호**:
- POST, PUT, DELETE 요청 시 CSRF 토큰 필수
- Ajax 요청도 예외 없음

**처리 방법**:

**1단계: HTML에 CSRF 토큰 포함**:
```html
<form>
  {% csrf_token %}  <!-- Django가 자동으로 생성 -->
  <!-- 실제 HTML: -->
  <!-- <input type="hidden" name="csrfmiddlewaretoken" value="토큰값"> -->
</form>
```

**2단계: JavaScript에서 토큰 가져오기**:
```javascript
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
```

**3단계: Axios 헤더에 포함**:
```javascript
axios({
  method: 'POST',
  url: '/some-url/',
  headers: {'X-CSRFToken': csrftoken}  // ⭐ 필수!
})
```

**주의사항**:
- 헤더 이름은 반드시 `'X-CSRFToken'` (대소문자 정확히)
- 토큰이 없으면 `403 Forbidden` 에러 발생

---

### 6.4. data-* 속성 활용

**교안 참조**: JavaScript_Ajax_with_Django.md - "data-* 속성" 섹션

**HTML → JavaScript 데이터 전달**:

**HTML (Django 템플릿)**:
```html
<!-- kebab-case로 작성 -->
<form data-user-id="{{ person.pk }}" 
      data-article-id="{{ article.pk }}"
      data-is-followed="true">
```

**JavaScript**:
```javascript
// camelCase로 자동 변환됨
const userId = formTag.dataset.userId        // "1"
const articleId = formTag.dataset.articleId  // "2"
const isFollowed = formTag.dataset.isFollowed  // "true" (문자열!)
```

**주의사항**:

**1. 네이밍 규칙**:
```html
<!-- HTML: kebab-case -->
<div data-user-name="alice" data-user-age="25">

<script>
// JavaScript: camelCase
const userName = div.dataset.userName  // "alice"
const userAge = div.dataset.userAge    // "25"
</script>
```

**2. 데이터 타입**:
```javascript
// dataset의 모든 값은 문자열!
const pk = formTag.dataset.userId  // "1" (문자열)
const pkNum = Number(formTag.dataset.userId)  // 1 (숫자)

// 템플릿 리터럴에서는 문자열로 사용 가능
url: `/accounts/${userId}/follow/`  // "/accounts/1/follow/"
```

**3. 사용 금지 규칙**:
```html
<!-- ❌ 'xml'로 시작 불가 -->
<div data-xml-data="...">

<!-- ❌ 세미콜론 포함 불가 -->
<div data-my:id="...">

<!-- ❌ 대문자 포함 불가 -->
<div data-userId="...">  <!-- data-user-id로 작성 -->
```

---

## 7. 이 코드 스타일의 장점

### 7.1. 아키텍처 장점

**1. 앱 분리로 모듈화**:
```
accounts/     # 사용자 관련 기능만
articles/     # 게시글 관련 기능만
```
**장점**:
- 코드 재사용 용이
- 유지보수 쉬움
- 팀 협업 시 충돌 최소화

**2. MTV 패턴 준수**:
```
Model (models.py)     → 데이터베이스 로직
Template (*.html)     → UI 렌더링
View (views.py)       → 비즈니스 로직
```
**장점**:
- 관심사의 분리
- 각 계층이 독립적
- 테스트 용이

**3. RESTful URL 설계**:
```
GET  /articles/              → 목록
GET  /articles/1/            → 상세
POST /articles/create/       → 생성
POST /articles/1/update/     → 수정
POST /articles/1/delete/     → 삭제
POST /articles/1/likes/      → 좋아요 (Ajax)
```
**장점**:
- URL만 봐도 기능 파악
- 직관적인 API 설계
- 확장 용이

---

### 7.2. Ajax 사용의 장점

**1. 사용자 경험 개선**:
```
동기 방식:   클릭 → 새로고침 (깜빡) → 페이지 로드 (느림)
비동기 방식: 클릭 → 즉시 반영 (부드러움) ⭐
```

**2. 네트워크 효율**:
```
동기 방식:   HTML 전체 (수십 KB)
비동기 방식: JSON 데이터만 (수백 B) ⭐
```

**3. 서버 부하 감소**:
```
동기 방식:   템플릿 렌더링 + HTML 전송
비동기 방식: JSON 직렬화만 (빠름) ⭐
```

---

### 7.3. 이벤트 버블링의 장점

**문제 상황**:
```javascript
// ❌ 게시글 100개 = 이벤트 리스너 100개
document.querySelector('#like-1').addEventListener(...)
document.querySelector('#like-2').addEventListener(...)
// ... 100개 ...
```

**해결책**:
```javascript
// ✅ 이벤트 리스너 1개로 해결
document.querySelector('.article-container').addEventListener(...)
```

**장점**:
1. **메모리 효율**: 리스너 1개만 유지
2. **동적 요소 대응**: 나중에 추가되는 게시글에도 자동 적용
3. **코드 간결**: 반복문 불필요
4. **유지보수 쉬움**: 한 곳만 수정

---

### 7.4. 보안 장점

**1. CSRF 토큰**:
```python
# Django가 자동으로 검증
@require_POST
def follow(request, user_pk):
    # CSRF 토큰이 없으면 403 에러
```
**보호**: Cross-Site Request Forgery 공격 차단

**2. 권한 검사**:
```python
# 작성자만 수정/삭제 가능
if request.user == article.user:
    article.delete()
```
**보호**: 다른 사용자의 데이터 무단 조작 방지

**3. @login_required**:
```python
@login_required
def delete(request, pk):
    # 로그인하지 않으면 로그인 페이지로 리다이렉트
```
**보호**: 인증되지 않은 접근 차단

---

### 7.5. 유지보수 장점

**1. 일관된 패턴**:
```python
# 모든 Ajax 뷰 함수가 동일한 패턴
@login_required
def ajax_view(request, pk):
    # ... 로직 ...
    context = {'key': value}
    return JsonResponse(context)
```

**2. 명확한 책임 분리**:
```
Django:       데이터 처리, JSON 응답
JavaScript:   DOM 조작, UI 업데이트
```

**3. 테스트 용이**:
```python
# Django 뷰 테스트
response = client.post('/accounts/1/follow/')
self.assertEqual(response.json()['is_followed'], True)

# JavaScript는 브라우저 테스트 프레임워크 사용
```

---

## 8. 학습 포인트

### 8.1. Django 핵심 개념

**1. Model 관계**:
- **ForeignKey (1:N)**: 사용자-게시글, 게시글-댓글
- **ManyToManyField (M:N)**: 팔로우, 좋아요

**2. Form 처리**:
- `commit=False`로 객체 생성 후 추가 설정
- `fields`로 보안 강화

**3. JsonResponse**:
- HTML 대신 JSON 응답
- Ajax 통신의 핵심

---

### 8.2. JavaScript 핵심 개념

**1. Axios**:
- Promise 기반 HTTP 클라이언트
- `.then()`, `.catch()`로 응답 처리

**2. 이벤트 처리**:
- `event.preventDefault()`: 기본 동작 막기
- `event.target`: 실제 이벤트 발생 요소
- `event.currentTarget`: 리스너 부착 요소

**3. DOM 조작**:
- `querySelector()`: 요소 선택
- `textContent`: 텍스트 변경
- `value`: input 값 변경

---

### 8.3. 디버깅 팁

**1. 개발자 도구 활용**:
```javascript
// Console 탭
console.log(response)
console.log(response.data)

// Network 탭
// - XHR 필터로 Ajax 요청만 보기
// - 요청/응답 헤더 확인
// - 응답 데이터 확인
```

**2. Django 에러 확인**:
```python
# views.py
print(request.user)  # 사용자 확인
print(request.POST)  # POST 데이터 확인
```

**3. CSRF 에러 해결**:
```javascript
// 토큰 값 확인
console.log(csrftoken)

// 헤더 확인
console.log(axios.defaults.headers)
```

---

### 8.4. 추가 개선 사항

**1. 에러 처리 강화**:
```javascript
axios(...)
  .then((response) => {
    // 성공 처리
  })
  .catch((error) => {
    // ⭐ 사용자에게 에러 알림
    alert('요청에 실패했습니다.')
    console.error(error)
  })
```

**2. 로딩 인디케이터**:
```javascript
// 요청 시작
loadingSpinner.style.display = 'block'

axios(...)
  .then((response) => {
    // 요청 완료
    loadingSpinner.style.display = 'none'
  })
```

**3. 응답 검증**:
```javascript
.then((response) => {
  if (response.data.is_followed !== undefined) {
    // 정상 응답 처리
  } else {
    // 응답 형식 오류
    console.error('Invalid response format')
  }
})
```

---

## 📝 참고 자료

**교안 참조**:
- JavaScript_AJAX.md - 비동기 처리 기본
- JavaScript_Ajax_with_Django.md - Django Ajax 통합 (전체)

**Django 문서**:
- Models: https://docs.djangoproject.com/en/stable/topics/db/models/
- Forms: https://docs.djangoproject.com/en/stable/topics/forms/
- JsonResponse: https://docs.djangoproject.com/en/stable/ref/request-response/#jsonresponse-objects

**MDN 문서**:
- data-* 속성: https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*
- 이벤트 버블링: https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Events#%EC%9D%B4%EB%B2%A4%ED%8A%B8_%EB%B2%84%EB%B8%94%EB%A7%81

---

**작성일**: 2024  
**과정**: SSAFY Django Ajax 실습  
**프로젝트**: crud (accounts + articles)  
**기반 교안**: JavaScript_Ajax_with_Django.md
