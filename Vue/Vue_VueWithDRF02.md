# Vue with DRF 02

## 📚 목차
1. 인증 with DRF
   - 인증
   - 인증 정책 설정
   - Token 인증 설정
2. Dj-Rest-Auth 라이브러리
   - Token 발급 및 활용
3. 권한 with DRF
   - 권한 정책 설정
   - IsAuthenticated 설정

---

## 🎯 학습 목표

1. ✅ DRF의 토큰 기반 인증 시스템의 동작 방식을 이해한다
2. ✅ dj-rest-auth를 사용하여 인증 관련 API 엔드포인트를 구성한다
3. ✅ 로그인 API 요청을 통해 DRF로부터 인증 토큰을 발급받는다
4. ✅ 발급받은 토큰을 Authorization 헤더에 담아 요청을 보낸다
5. ✅ DRF의 권한(Permission) 개념과 401, 403 에러를 이해한다
6. ✅ @permission_classes로 특정 view에 대한 접근 권한을 설정한다
7. ✅ 게시글 등 데이터를 생성할 때 현재 인증된 사용자와 연결한다

---

## 🏠 학습 시작

**"사용자 인증을 구현할 때, 프론트엔드(Vue)와 백엔드(DRF)는 각각 어떤 역할을 나눠 맡아야 할까요?"**

### 각 역할을 이해하고 백엔드에서의 인증 과정을 집중적으로 살펴봅시다.

#### 1. DRF(백엔드)의 역할
- 사용자 정보를 검증하고 안전한 토큰을 발급
- 어떤 요청이 허가되는지 권한 규칙을 정함

#### 2. Vue(프론트엔드)의 역할
- 로그인 폼을 제공하고 발급받은 토큰을 저장
- 보호된 요청을 보낼 때 토큰을 함께 전송

**프론트엔드와 백엔드의 역할을 이해하고 인증 과정을 학습합니다.**
**더 나아가 인증 후 사용자별 권한을 확인하는 방법도 알아봅시다.**

---

## 1️⃣ 인증 with DRF - 사전 준비

### 사전 준비 (1/4) - User ForeignKey 주석 해제

**인증 로직 진행을 위해 User 모델 관련 코드 활성화**

**articles/models.py**
```python
from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

---

### 사전 준비 (2/4) - read_only_fields

**serializers의 read_only_fields 주석 해제**

**read_only_fields란?**
- 사용자가 수정하면 안 되는 필드
- 읽기 전용 필드로 설정
- 직렬화(Serialization) 시에는 포함되지만, 역직렬화(Deserialization) 시에는 무시됨

**articles/serializers.py**
```python
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
```

**중요:**
- `user` 필드는 직접 입력받지 않고, 서버에서 자동으로 설정되어야 함
- 클라이언트가 임의로 `user` 값을 변경할 수 없도록 보호

---

### 사전 준비 (3/4) - 게시글 생성 시 user 정보 저장

**article_list view 함수에서 게시글 생성 시 user 정보도 저장할 수 있도록 주석 해제**

**articles/views.py**
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 게시글 저장 시 현재 요청한 user를 작성자로 설정
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

**중요:**
- `serializer.save(user=request.user)`: 현재 로그인한 사용자를 게시글 작성자로 설정
- `request.user`: Django가 자동으로 제공하는 현재 인증된 사용자 객체

---

### 사전 준비 (4/4) - DB 초기화

**프로젝트 디렉토리 구조:**
```
django-pjt/
├── accounts/
│   ├── __pycache__/
│   ├── migrations/
│   │   ├── __pycache__/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── signals.py
│   ├── tests.py
│   └── views.py
├── articles/
│   ├── __pycache__/
│   ├── fixtures/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── my_api/
├── venv/
├── db.sqlite3  ← 삭제
├── manage.py
└── requirements.txt
```

**DB 초기화 단계:**

```bash
# 1. DB 파일 삭제
# db.sqlite3 파일 삭제

# 2. migrations 파일 삭제
# accounts/migrations/ 내의 __init__.py를 제외한 모든 파일 삭제
# articles/migrations/ 내의 __init__.py를 제외한 모든 파일 삭제

# 3. Migration 과정 재진행
python manage.py makemigrations
python manage.py migrate

# 4. fixtures 데이터 로드 불가
# fixtures의 articles.json은 user 정보가 없으므로 loaddata 불가능
```

**주의:**
- 기존 `articles.json` fixture는 `user` 필드가 없어 사용 불가
- 새로운 게시글은 인증된 사용자를 통해 작성해야 함

---

## 2️⃣ 인증 (Authentication)

### [복습] 인증의 필요성

**클라이언트와 서버 간의 상태 정보를 유지하기 위해서 쿠키와 세션을 사용**

하지만 클라이언트와 서버는 기본적으로 **무상태(Stateless)** 프로토콜인 HTTP를 사용하므로:
- 사용자를 식별하지 못하고 있는 상태
- 그래서 사용자를 식별하기 위해서 필요한 과정이 바로 **인증(Authentication)**

**다양한 인증 방식이 존재:**
- 아이디와 비밀번호
- 소셜 로그인 (OAuth)
- 생체인증

**Django에서는 사용자 인증과 관련된 가장 중요하고 기본적인 뼈대를 제공**
- Django Authentication System

---

### DRF에서의 인증

**인증은 항상 view 함수 시작 시, 다른 코드의 진행이 허용되기 전에 실행됨**

**인증의 역할:**
- 수신 요청을 해당 요청의 사용자 또는
- 해당 요청이 서명된 토큰(token)과 같은 자격 증명 자료와 연결

**이후:**
- 인증이 완료된 해당 자격 증명을 사용하여 권한 및 제한 정책을 확인하고
- 요청을 허용해야 하는지를 결정

---

### 권한(Permissions)

**정의**: 요청에 대한 접근 허용 또는 거부 여부를 결정

**중요:**
인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 자격 증명만 식별한다는 점에 유의하세요.

**참고 문서:**
https://www.django-rest-framework.org/api-guide/authentication/

---

### 승인되지 않은 응답 및 금지된 응답

**인증되지 않은 요청이 권한을 거부하는 경우, 해당되는 두 가지 오류 코드로 응답:**

#### 1. HTTP 401 Unauthorized
**"요청에 유효한 인증 자격 증명(Authentication Credentials)이 없어 사용자를 식별할 수 없음"을 의미**
- (누구인지를 증명할 자료가 없음)

#### 2. HTTP 403 Forbidden (Permission Denied)
**"서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것"을 의미**
- 401과 다른 점은 **서버는 클라이언트가 누구인지 알고 있음**

---

## 3️⃣ 인증 정책 설정

### 인증 정책 설정 방법 2가지

#### 1. 전역 설정
- 프로젝트 전체에 적용되는 기본 인증 방식

#### 2. View 함수별 설정
- 특정 view 함수에만 적용되는 인증 방식

---

### 1) 전역 설정

**프로젝트 전체에 적용되는 기본 인증 방식을 정의**

`DEFAULT_AUTHENTICATION_CLASSES`를 사용

**기본 값:**
- SessionAuthentication
- BasicAuthentication

**사용 예시 (DRF 공식 문서 참고):**

**settings.py**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

---

### 2) View 함수별 설정

**`authentication_classes` 데코레이터를 사용**

**데코레이터란?**
- 기존 함수를 감싸 특별한 기능을 추가하는 함수

**개별 view에 지정하여 재정의**

**사용 예시 (DRF 공식 문서 참고):**

```python
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def article_list(request):
    pass
```

---

### DRF가 제공하는 인증 체계

#### 1. BasicAuthentication
요청마다 사용자 이름과 비밀번호를 Base64로 인코딩하여 Authorization 헤더에 담아 보내는 방식

#### 2. TokenAuthentication
로그인 시 발급받은 고유한 토큰(Token)을 Authorization 헤더에 담아 요청함으로써 사용자를 인증하는 방식

#### 3. SessionAuthentication
Django의 기본 세션 시스템을 활용하여, 브라우저가 보내는 sessionid 쿠키를 통해 사용자를 인증하는 방식

#### 4. RemoteUserAuthentication
웹 서버 등 외부 시스템이 이미 처리한 인증 결과를 신뢰하고 전달받은 사용자 이름으로 사용자를 인증하는 방식

---

## 4️⃣ TokenAuthentication

### Token이란?

**정의**: 인증 후 발급되는 사용자의 신원이나 권한을 증명하는 값

**token 기반 HTTP 인증 체계:**
- 로그인 시 발급받은 고유한 토큰을 Authorization 헤더에 담아 요청함으로써 사용자를 인증하는 방식

**특징:**
- 기본 데스크톱 및 모바일 클라이언트와 같은 클라이언트-서버 설정에 적합
- 서버가 인증된 사용자에게 토큰을 발급하고
- 사용자는 매 요청마다 발급받은 토큰을 요청과 함께 보내 인증 과정을 거침

**참고 문서:**
https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

---

### TokenAuthentication 설정 (1/3)

#### 1단계: INSTALLED_APPS에 추가

**my_api/settings.py**
```python
INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    'rest_framework.authtoken',  # ← 추가
    # 'dj_rest_auth',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'dj_rest_auth.registration',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**중요:**
- `rest_framework.authtoken` 앱을 추가해야 토큰 인증 기능 사용 가능

---

### TokenAuthentication 설정 (2/3)

#### 2단계: Migration 실행

```bash
python manage.py migrate
```

**실행 결과:**
```
Running migrations:
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
```

**설명:**
- `authtoken` 앱의 migration이 실행되어 Token 모델이 생성됨
- 데이터베이스에 `authtoken_token` 테이블이 추가됨

---

### TokenAuthentication 설정 (3/3)

#### 3단계: DEFAULT_AUTHENTICATION_CLASSES 설정

**my_api/settings.py**
```python
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # Permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
```

**설명:**
- `DEFAULT_AUTHENTICATION_CLASSES`: 전역 인증 방식 설정
- `DEFAULT_PERMISSION_CLASSES`: 전역 권한 설정
  - `AllowAny`: 모든 사용자에게 접근 허용 (기본값)

---

## 5️⃣ Dj-Rest-Auth 라이브러리

### Dj-Rest-Auth란?

**정의**: 회원가입, 인증(Token 발급), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등 다양한 인증 관련 기능을 제공하는 라이브러리

**특징:**
- 복잡한 인증 로직을 직접 구현하지 않아도 됨
- REST API 형태로 즉시 사용 가능한 엔드포인트 제공

**공식 문서:**
https://dj-rest-auth.readthedocs.io/en/latest/

---

### Dj-Rest-Auth 설치

```bash
pip install dj-rest-auth
```

---

### Dj-Rest-Auth 기본 설정 (1/3)

#### 1단계: INSTALLED_APPS에 추가

**my_api/settings.py**
```python
INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',  # ← 추가
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'dj_rest_auth.registration',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

### Dj-Rest-Auth 기본 설정 (2/3)

#### 2단계: URL 등록

**my_api/urls.py**
```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),  # ← 추가
    # path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]
```

**설명:**
- `accounts/` 경로로 dj-rest-auth가 제공하는 기본 인증 엔드포인트 사용 가능
- 주요 엔드포인트:
  - `POST /accounts/login/` - 로그인
  - `POST /accounts/logout/` - 로그아웃
  - `GET /accounts/user/` - 현재 사용자 정보

---

### Dj-Rest-Auth 기본 설정 (3/3)

#### 3단계: Migration 실행

```bash
python manage.py migrate
```

**실행 결과:**
```
No migrations to apply.
```

**설명:**
- dj-rest-auth는 기존 Django 및 DRF 모델을 활용하므로 추가 migration이 필요 없음

---

### Dj-Rest-Auth 엔드포인트 확인

**브라우저 또는 Postman에서 확인:**

```
http://127.0.0.1:8000/accounts/
```

**제공되는 주요 엔드포인트:**

| 엔드포인트 | 메서드 | 설명 |
|-----------|--------|------|
| `/accounts/login/` | POST | 로그인 |
| `/accounts/logout/` | POST | 로그아웃 |
| `/accounts/user/` | GET | 현재 사용자 정보 |
| `/accounts/password/reset/` | POST | 비밀번호 재설정 |
| `/accounts/password/reset/confirm/` | POST | 비밀번호 재설정 확인 |
| `/accounts/password/change/` | POST | 비밀번호 변경 |

---

## 6️⃣ 회원가입 기능 구현

### 회원가입 라이브러리 설치

```bash
pip install 'dj-rest-auth[with_social]'
```

**설명:**
- 소셜 로그인 기능을 포함한 회원가입 기능 설치
- `django-allauth` 라이브러리가 함께 설치됨

---

### 회원가입 설정 (1/4)

#### 1단계: 필요한 앱 추가

**my_api/settings.py**
```python
INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',  # ← 추가
    'allauth',  # ← 추가
    'allauth.account',  # ← 추가
    'allauth.socialaccount',  # ← 추가
    'dj_rest_auth.registration',  # ← 추가
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

### 회원가입 설정 (2/4)

#### 2단계: SITE_ID 설정

**my_api/settings.py**
```python
# 맨 아래에 추가
SITE_ID = 1
```

**설명:**
- `django.contrib.sites` 프레임워크 사용 시 필요
- 여러 사이트를 관리할 때 각 사이트를 구분하는 ID

---

### 회원가입 설정 (3/4)

#### 3단계: MIDDLEWARE에 추가

**my_api/settings.py**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # ← 추가
]
```

---

### 회원가입 설정 (4/4)

#### 4단계: URL 등록 및 Migration

**my_api/urls.py**
```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),  # ← 추가
]
```

**Migration 실행:**
```bash
python manage.py migrate
```

---

### 회원가입 엔드포인트 확인

**브라우저 또는 Postman에서 확인:**

```
http://127.0.0.1:8000/accounts/signup/
```

**제공되는 엔드포인트:**

| 엔드포인트 | 메서드 | 설명 |
|-----------|--------|------|
| `/accounts/signup/` | POST | 회원가입 |

---

### Token 발급 테스트

#### 1) Admin 페이지에서 회원 가입

**브라우저에서 접속:**
```
http://127.0.0.1:8000/admin/
```

**Users 모델에서 새 사용자 추가:**
- Username: test_user
- Password: test_password123!

---

#### 2) Postman에서 로그인 테스트

**요청 설정:**
```
POST http://127.0.0.1:8000/accounts/login/
```

**Body (JSON):**
```json
{
    "username": "test_user",
    "password": "test_password123!"
}
```

**응답 (예시):**
```json
{
    "key": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**설명:**
- `key`: 발급된 인증 토큰
- 이 토큰을 저장하여 이후 인증이 필요한 요청에 사용

---

## 7️⃣ Token 활용

### 게시글 작성 시 Token 사용

#### 요청 방법

**Postman 설정:**

```
POST http://127.0.0.1:8000/api/v1/articles/
```

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Body (JSON):**
```json
{
    "title": "Test Article",
    "content": "This is a test article."
}
```

---

### 작동 흐름

```
1. 클라이언트가 로그인 요청
         ↓
2. 서버가 토큰 발급
         ↓
3. 클라이언트가 토큰 저장
         ↓
4. 게시글 작성 요청 시 Authorization 헤더에 토큰 포함
         ↓
5. 서버가 토큰 검증
         ↓
6. 인증 성공 시 request.user에 사용자 정보 자동 할당
         ↓
7. 게시글 저장 시 user=request.user로 작성자 연결
```

---

### Token 테이블 확인

**Admin 페이지에서 확인:**

```
http://127.0.0.1:8000/admin/authtoken/token/
```

**Token 테이블 구조:**

| Key (토큰 값) | User | Created |
|--------------|------|---------|
| 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b | test_user | 2024-01-15 10:30:00 |

**특징:**
- 각 사용자당 하나의 토큰만 생성됨
- 로그인할 때마다 새로운 토큰이 발급되는 것이 아님
- 기존 토큰이 있으면 그 토큰을 반환

---

### Signals를 통한 Token 자동 생성

**accounts/signals.py**
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

**설명:**
- `post_save` 시그널: User 모델이 저장된 후 자동 실행
- `created=True`: 새로운 사용자가 생성되었을 때만
- 자동으로 해당 사용자의 Token 생성

---

**accounts/apps.py**
```python
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals
```

**설명:**
- 앱이 준비되면 signals.py를 import하여 시그널 등록

---

## 8️⃣ 권한(Permission) with DRF

### 권한 정책 설정

**권한이란?**
- 인증된 사용자가 특정 요청을 보낼 자격이 있는지 결정하는 과정

**권한 설정 방법 2가지:**

#### 1. 전역 설정
- 프로젝트 전체에 적용

#### 2. View 함수별 설정
- 특정 view 함수에만 적용

---

### 1) 전역 권한 설정

**my_api/settings.py**
```python
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # Permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # 모든 사용자 허용
        # 'rest_framework.permissions.IsAuthenticated',  # 인증된 사용자만
    ],
}
```

**주요 권한 클래스:**
- `AllowAny`: 모든 사용자에게 접근 허용 (기본값)
- `IsAuthenticated`: 인증된 사용자만 접근 허용
- `IsAdminUser`: 관리자만 접근 허용
- `IsAuthenticatedOrReadOnly`: 비인증 사용자는 읽기만 허용

---

### 2) View별 권한 설정

**`@permission_classes` 데코레이터 사용**

**articles/views.py**
```python
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # 이 view만 인증 필요
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

**설명:**
- 이 view 함수는 인증된 사용자만 접근 가능
- 토큰이 없으면 401 Unauthorized 응답

---

## 9️⃣ IsAuthenticated 권한 설정

### IsAuthenticated란?

**정의**: 인증되지 않은 사용자에 대한 권한을 거부하고 그렇지 않은 경우 권한을 허용

**특징:**
- 등록된 사용자만 API에 액세스할 수 있도록 하려는 경우에 적합

---

### IsAuthenticated 활용하기 (1/4)

#### 1단계: 전역 권한을 IsAuthenticated로 변경

**my_api/settings.py**
```python
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # Permission
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',  # ← 변경
    ],
}
```

**설명:**
- 이제 모든 view 함수가 기본적으로 인증 필요
- 토큰 없이 요청하면 401 Unauthorized 응답

---

### IsAuthenticated 활용하기 (2/4)

#### 2단계: 게시글 조회 요청 테스트

**Postman에서 테스트:**

```
GET http://127.0.0.1:8000/api/v1/articles/
```

**Headers에 토큰 없이 요청 시:**

**응답 (401 Unauthorized):**
```json
{
    "detail": "Authentication credentials were not provided."
}
```

**설명:**
- 인증 자격 증명이 제공되지 않았음
- Authorization 헤더에 토큰을 포함해야 함

---

### IsAuthenticated 활용하기 (3/4)

#### 3단계: IsAdminUser로 변경 테스트

**articles/views.py**
```python
from rest_framework.permissions import IsAdminUser


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])  # 관리자만 허용
def article_list(request):
    pass
```

---

**테스트 결과:**

**일반 사용자 토큰으로 요청 시:**

**응답 (403 Forbidden):**
```json
{
    "detail": "You do not have permission to perform this action."
}
```

**설명:**
- 인증은 성공했지만 권한이 없음
- 403 Forbidden 응답

---

### IsAuthenticated 활용하기 (4/4)

#### 4단계: IsAuthenticated로 복구

**articles/views.py**
```python
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    pass
```

---

### Token 미포함 결과 확인

**Vue 애플리케이션에서 게시글 조회 시도:**

**브라우저 콘솔 (개발자 도구):**
```
Failed to load resource: the server responded with a status of 401 (Unauthorized)
http://127.0.0.1:8000/api/v1/articles/

AxiosError
```

**설명:**
- 게시글 조회 요청 시 인증에 필요한 수단(token)을 보내지 않고 있으므로
- 게시글 조회가 불가능해진 것

**이후 과정:**
- 다음 시간에 Vue에서 token을 포함시켜 게시글을 조회하는 과정 진행 예정

---

## 🔟 확인 문제

### 문제 1
**인증은 되었지만 접근 권한이 없을 때 발생하는 에러는?**

a) 400 Bad Request
b) 401 Unauthorized
c) 403 Forbidden
d) 404 Not Found

---

### 문제 2
**유효한 자격 증명이 없을 때 발생하는 에러는?**

a) 400 Bad Request
b) 401 Unauthorized
c) 403 Forbidden
d) 404 Not Found

---

### 문제 3
**DRF에서 토큰 기반 인증을 활성화하는 설정은?**

a) SessionAuthentication
b) BasicAuthentication
c) TokenAuthentication
d) RemoteUserAuthentication

---

### 문제 4
**dj-rest-auth 라이브러리의 주요 역할은?**

a) 데이터 직렬화
b) 인증 API 엔드포인트 제공
c) CORS 정책 관리
d) 비동기 작업 처리

---

### 문제 5
**로그인 성공 시 dj-rest-auth가 반환하는 것은?**

a) 세션 ID
b) 사용자 정보
c) 인증 토큰
d) 성공 메시지

---

### 문제 6
**발급받은 토큰을 요청 시 어떤 헤더에 담는가?**

a) Content-Type
b) X-CSRFToken
c) Accept
d) Authorization

---

### 문제 7
**View 함수에 특정 권한을 설정하는 데코레이터는?**

a) @api_view
b) @permission_classes
c) @authentication_classes
d) @action

---

### 문제 8
**인증된 사용자만 접근을 허용하는 권한 클래스는?**

a) AllowAny
b) IsAdminUser
c) IsAuthenticatedOrReadOnly
d) IsAuthenticated

---

### 문제 9
**비인증 사용자는 읽기만, 인증 사용자는 모든 작업을 허용하는 권한은?**

a) AllowAny
b) IsAdminUser
c) IsAuthenticatedOrReadOnly
d) IsAuthenticated

---

### 문제 10
**게시글 생성 시 작성자를 현재 로그인한 유저로 저장하는 방법은?**

a) serializer.save()
b) serializer.save(user=user.pk)
c) serializer.save(user=request.user)
d) serializer.create(user=request.user)

---

## 📝 정답 및 해설

### 1. b) 401 Unauthorized
401 에러는 요청에 유효한 인증 자격 증명이 없어 사용자를 식별할 수 없음을 의미합니다.

### 2. c) 403 Forbidden
403 에러는 사용자가 누구인지는 알지만, 해당 리소스에 접근할 권한이 없음을 의미합니다.

### 3. c) TokenAuthentication
settings.py의 DEFAULT_AUTHENTICATION_CLASSES에 설정하여 토큰 인증을 사용합니다.

### 4. b) 인증 API 엔드포인트 제공
회원가입, 로그인, 로그아웃 등 인증 관련 API를 간편하게 구현할 수 있도록 도와줍니다.

### 5. c) 인증 토큰
로그인 API는 인증 성공의 증표로 고유한 토큰 키(key)를 JSON 형태로 반환합니다.

### 6. d) Authorization
Authorization 헤더에 "Token <key>" 형식으로 토큰을 담아 인증 요청을 보냅니다.

### 7. b) @permission_classes
이 데코레이터를 사용하여 특정 View 함수에만 적용할 권한 클래스를 지정할 수 있습니다.

### 8. d) IsAuthenticated
IsAuthenticated는 요청을 보낸 사용자가 인증(로그인)된 상태인지 확인합니다.

### 9. c) IsAuthenticatedOrReadOnly
IsAuthenticatedOrReadOnly는 비인증 사용자에게는 읽기만 허용하고 인증된 사용자에게는 모든 작업을 허용합니다.

### 10. c) serializer.save(user=request.user)
save() 메서드에 추가 인자로 user=request.user를 전달하여 작성자를 연결합니다.

---

## 📋 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **인증 (Authentication)** | 요청 사용자의 자격 증명을 식별 | 401: 인증 실패 (자격 증명 없음) |
| **권한 (Permission)** | 인증된 사용자의 요청 허용/거부 결정 | 403: 권한 없음 (접근 거부) |
| **토큰 인증** | 발급된 토큰으로 사용자를 인증 | rest_framework.authtoken |
| **dj-rest-auth** | DRF 인증 관련 기능 제공 라이브러리 | 로그인, 회원가입 API 엔드포인트 제공 |
| **Authorization 헤더** | 인증 토큰을 담아 서버에 전송 | Authorization: Token <key> |
| **@permission_classes** | View 함수에 특정 권한을 설정 | @permission_classes([IsAuthenticated]) |
| **IsAuthenticated** | 인증된 사용자만 접근을 허용 | 비인증 사용자 요청은 401 반환 |

---

## 🎯 요약 정리

### 인증 (Authentication)

**요청을 보낸 사용자가 누구인지 식별하는 과정**
- 인증 자체는 접근을 허용하거나 거부하지 않음

### 권한 (Permission)

**인증된 사용자가 특정 요청을 보낼 자격이 있는지 결정하는 과정**

---

### HTTP 응답 코드

#### 401 Unauthorized
유효한 인증 정보가 없어 요청이 실패했음을 의미 (로그인되지 않은 상태)

#### 403 Forbidden
인증은 성공했지만, 해당 요청에 대한 권한이 없음을 의미

---

### DRF 토큰 기반 인증

**작동 흐름:**

1. 사용자가 로그인하면 서버는 고유한 토큰(Token)을 발급
2. 클라이언트(Vue)는 이 토큰을 저장
3. 이후 서버에 데이터를 요청할 때마다, 헤더의 Authorization 필드에 `Token <key>` 형식으로 토큰을 담아 보냄
4. 서버는 이 토큰을 검증하여 사용자를 식별하고 인증

---

### dj-rest-auth 라이브러리

**DRF에서 회원가입, 로그인 등 인증 관련 API 엔드포인트를 쉽게 구현할 수 있도록 도와주는 라이브러리**

**설정 방법:**
- settings.py에서 DEFAULT_AUTHENTICATION_CLASSES를 TokenAuthentication으로 설정하여
- 프로젝트 전반에 토큰 인증을 적용

---

### DRF 권한 설정

#### 전역 설정
settings.py의 DEFAULT_PERMISSION_CLASSES에서 프로젝트의 기본 권한을 설정

#### View별 설정
@permission_classes 데코레이터를 사용하여 특정 View 함수에만 다른 권한을 적용

---

### 주요 권한 클래스

#### IsAuthenticated
인증된 사용자에게만 접근을 허용

#### IsAuthenticatedOrReadOnly
비인증 사용자에게는 읽기만 허용하고 인증된 사용자에게는 모든 작업을 허용

#### AllowAny
모든 사용자에게 접근을 허용

---

## 🎓 활동 정리

**"사용자 인증을 구현할 때, 프론트엔드(Vue)와 백엔드(DRF)는 각각 어떤 역할을 나눠 맡아야 할까요?"**

**백엔드에서의 인증 과정을 이해하고 dj-rest-auth를 활용했습니다.**

**예시 코드:**
```python
# '인증된 사용자만 통과'라는 규칙을 설정
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    pass
```

**다음 시간에는 프론트엔드에서의 인증 과정을 살펴보겠습니다.**

---

## 🚀 학습 완료!

**이제 DRF에서 토큰 기반 인증 시스템을 구축하는 방법을 배웠습니다:**

- ✅ TokenAuthentication 설정
- ✅ dj-rest-auth로 인증 API 구현
- ✅ 권한(Permission) 설정
- ✅ 401과 403 에러 이해
- ✅ 게시글 작성 시 사용자 연결

**다음 시간에는 Vue에서 토큰을 관리하고 사용하는 방법을 학습하겠습니다!** 🎉
