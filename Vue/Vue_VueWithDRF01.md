# Vue with DRF01

## 📚 목차
1. 프로젝트 개요
2. DRF 프로젝트 안내
3. Skeleton Code 구조
4. CORS 설정
5. Vue와 DRF 연동
6. 게시글 전체 조회
7. 게시글 상세 조회
8. 게시글 작성
9. 참고사항
10. 확인 문제

---

## 🎯 학습 목표

1. ✅ Vue와 DRF 간 기본적인 요청과 응답 구조를 이해한다
2. ✅ CORS 정책과 SOP의 개념을 이해하고 설정할 수 있다
3. ✅ Pinia actions에서 Axios로 DRF 서버에 요청을 보낸다
4. ✅ DRF에서 JsonResponse로 JSON 데이터를 응답한다
5. ✅ Vue 컴포넌트에서 게시글 CRUD 기능을 구현한다
6. ✅ 동적 라우팅으로 게시글 상세 페이지를 구현한다
7. ✅ CSRF 토큰을 사용하여 안전한 POST 요청을 보낸다

---

## 1️⃣ 프로젝트 개요

### 앞으로 수업에서 진행할 프로젝트

**DRF (Django REST Framework):**
- 장고(Django)로 API 서버를 쉽게 만들도록 도와주는 도구

**학습 내용:**
1. Vue와 DRF 간 기본적인 요청과 응답
2. Vue와 DRF에서의 인증 시스템
3. User 커스터마이징

---

## 2️⃣ DRF 프로젝트 안내

### 프로젝트 제공 사항

**스켈레톤 프로젝트 `django-pjt` 제공:**
- 외부 패키지 및 라이브러리는 `requirements.txt`에 작성되어 있음

**⚠️ 중요:**
**DRF 프로젝트는 제공된 스켈레톤 코드의 '주석을 해제'하여 진행합니다.**

---

## 3️⃣ Skeleton Code 구조

### 1) Model 클래스 확인

**articles/models.py**
```python
class Article(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    # )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**accounts/models.py**
```python
class User(AbstractUser):
    pass
```

---

### 2) URL 확인

**my_api/urls.py**
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    # path('accounts/', include('dj_rest_auth.urls')),
    # path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]
```

**articles/urls.py**
```python
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
```

---

### 3) Serializers 확인

**articles/serializers.py**
```python
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('user',)
```

---

### 4) views.py의 import 부분 확인

**articles/views.py**
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article
```

---

### 5) View 함수 확인

**articles/views.py**
```python
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
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
```

---

### 6) settings.py 확인 (1/2)

**my_api/settings.py**
```python
INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    # 'rest_framework.authtoken',
    # 'dj_rest_auth',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'dj_rest_auth.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# REST_FRAMEWORK = {
#     # Authentication
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     # Permission
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#     ],
# }
```

---

### 7) settings.py 확인 (2/2)

**my_api/settings.py**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
#     'http://127.0.0.1:5173',
#     'http://localhost:5173',
# ]
```

---

### 8) Fixtures 확인

**articles/fixtures/articles.json**
```json
[
  {
    "model": "articles.article",
    "pk": 1,
    "fields": {
      "title": "title",
      "content": "content",
      "created_at": "2023-07-04T08:21:53.976Z",
      "updated_at": "2023-07-04T08:21:53.976Z"
    }
  },
  {
    "model": "articles.article",
    "pk": 2,
    "fields": {
      "title": "제목",
      "content": "내용",
      "created_at": "2023-07-04T12:59:07.671Z",
      "updated_at": "2023-07-04T12:59:07.671Z"
    }
  },
  {
    "model": "articles.article",
    "pk": 3,
    "fields": {
      "title": "제목",
      "content": "내용",
      "created_at": "2023-07-04T13:04:08.680Z",
      "updated_at": "2023-07-04T13:04:08.686Z"
    }
  }
]
```

---

### 9) 가상 환경 생성 및 활성화

```bash
# 가상 환경 생성
$ python -m venv venv

# 가상 환경 활성화
$ source venv/Scripts/activate

# 패키지 설치
$ pip install -r requirements.txt
```

---

### 10) Migration 진행

```bash
# Migration 파일 생성
$ python manage.py makemigrations

# Migration 실행
$ python manage.py migrate

# Fixtures 데이터 로드
$ python manage.py loaddata articles.json
```

---

### 11) Django 서버 실행

```bash
$ python manage.py runserver
```

**확인:**
브라우저에서 `http://127.0.0.1:8000/api/v1/articles/` 접속하여 API 동작 확인

---

## 4️⃣ CORS 정책

### SOP (Same-Origin Policy)

**정의**: 동일 출처 정책

**웹 브라우저의 기본 보안 정책:**
- 한 출처(Origin)에서 로드된 문서나 스크립트가 다른 출처의 리소스와 상호작용하는 것을 제한
- 여기서 '출처'는 **프로토콜, 호스트, 포트 번호**의 조합을 의미

---

### Origin (출처)의 구성 요소

```
https://www.example.com:443/path
└─┬─┘   └───────┬────────┘└┬┘
Protocol      Host        Port
(프로토콜)   (호스트)     (포트)

→ 이 3가지가 모두 같아야 '동일 출처'
```

---

### SOP 예시

**현재 페이지:** `http://localhost:8000`

| URL | 동일 출처? | 이유 |
|-----|-----------|------|
| `http://localhost:8000/api/` | ✅ 예 | 모든 요소가 동일 |
| `https://localhost:8000/` | ❌ 아니오 | 프로토콜 다름 (https) |
| `http://localhost:3000/` | ❌ 아니오 | 포트 다름 (3000) |
| `http://127.0.0.1:8000/` | ❌ 아니오 | 호스트 다름 (127.0.0.1) |

---

### CORS (Cross-Origin Resource Sharing)

**정의**: 교차 출처 리소스 공유

**SOP 제한을 완화하기 위한 정책:**
- 서버가 특정 출처의 요청을 허용하도록 설정
- 서버가 자신의 응답 헤더에 `Access-Control-Allow-Origin` 같은 정보를 포함
- 브라우저에게 다른 출처의 요청을 허용한다고 알리는 정책

---

### CORS 동작 원리

```
Vue App (localhost:5173)
         ↓ 1. API 요청
DRF Server (localhost:8000)
         ↓ 2. 응답 헤더에 CORS 정보 포함
         ↓    Access-Control-Allow-Origin: http://localhost:5173
Vue App
         ↓ 3. 브라우저가 CORS 확인
         ↓ 4. 허용된 출처면 응답 데이터 전달
```

---

### Django에서 CORS 설정

#### 1단계: django-cors-headers 설치

```bash
$ pip install django-cors-headers
```

---

#### 2단계: settings.py 설정

**my_api/settings.py**
```python
INSTALLED_APPS = [
    # ...
    'corsheaders',  # 추가
    # ...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 추가 (CommonMiddleware 위에)
    'django.middleware.common.CommonMiddleware',
    # ...
]

# CORS 허용할 출처 설정
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]
```

**⚠️ 중요:**
- `CorsMiddleware`는 `CommonMiddleware` **위에** 위치해야 함

---

## 5️⃣ Vue 프로젝트 구조

### 디렉토리 구조

```
vue-project/
├── src/
│   ├── assets/
│   ├── components/
│   ├── router/
│   │   └── index.js
│   ├── stores/
│   │   └── article.js
│   ├── views/
│   │   ├── ArticleView.vue
│   │   ├── DetailView.vue
│   │   └── CreateView.vue
│   ├── App.vue
│   └── main.js
├── index.html
└── package.json
```

---

### Router 설정

**router/index.js**
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    }
  ]
})

export default router
```

---

### Pinia Store 설정

**stores/article.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // 전체 게시글 조회
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { articles, API_URL, getArticles }
})
```

---

## 6️⃣ 게시글 전체 조회

### 전체 흐름

```
1. ArticleView 컴포넌트 마운트
         ↓
2. getArticles 액션 호출
         ↓
3. Axios로 DRF 서버에 GET 요청
         ↓
4. DRF에서 전체 게시글 데이터 응답
         ↓
5. Pinia store의 articles에 저장
         ↓
6. ArticleList 컴포넌트에서 v-for로 렌더링
```

---

### 1) ArticleView 컴포넌트

**views/ArticleView.vue**
```vue
<template>
  <div>
    <h1>Article Page</h1>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import ArticleList from '@/components/ArticleList.vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()

// 컴포넌트가 마운트되면 게시글 목록 조회
onMounted(() => {
  store.getArticles()
})
</script>
```

---

### 2) ArticleList 컴포넌트

**components/ArticleList.vue**
```vue
<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()
</script>
```

---

### 3) ArticleListItem 컴포넌트

**components/ArticleListItem.vue**
```vue
<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }">
      [DETAIL]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
```

---

### 4) DRF View 함수

**articles/views.py**
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
```

---

## 7️⃣ 게시글 상세 조회

### 전체 흐름

```
1. 게시글 목록에서 [DETAIL] 링크 클릭
         ↓
2. DetailView로 이동 (URL: /articles/:id)
         ↓
3. useRoute()로 id 파라미터 추출
         ↓
4. getArticle 액션 호출
         ↓
5. Axios로 DRF 서버에 GET 요청
         ↓
6. DRF에서 해당 게시글 데이터 응답
         ↓
7. Pinia store의 article에 저장
         ↓
8. DetailView에서 상세 정보 렌더링
```

---

### 1) Pinia Store - getArticle 액션

**stores/article.js**
```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const article = ref(null)  // 단일 게시글 저장
  const API_URL = 'http://127.0.0.1:8000'

  // 전체 게시글 조회
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }

  // 단일 게시글 조회
  const getArticle = function (id) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/${id}/`
    })
      .then(res => {
        article.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { articles, article, API_URL, getArticles, getArticle }
})
```

---

### 2) DetailView 컴포넌트

**views/DetailView.vue**
```vue
<template>
  <div>
    <h1>Detail Page</h1>
    <div v-if="store.article">
      <p>글 번호: {{ store.article.id }}</p>
      <p>제목: {{ store.article.title }}</p>
      <p>내용: {{ store.article.content }}</p>
      <p>작성일: {{ store.article.created_at }}</p>
      <p>수정일: {{ store.article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()
const route = useRoute()

// 컴포넌트가 마운트되면 해당 게시글 조회
onMounted(() => {
  store.getArticle(route.params.id)
})
</script>
```

---

### 3) DRF View 함수

**articles/views.py**
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
```

---

## 8️⃣ 게시글 작성

### 전체 흐름

```
1. CreateView에서 폼 작성
         ↓
2. v-model로 title, content 바인딩
         ↓
3. 폼 제출 (@submit.prevent)
         ↓
4. createArticle 함수 호출
         ↓
5. Axios로 DRF 서버에 POST 요청
         ↓
6. DRF에서 게시글 생성 후 응답
         ↓
7. router.push()로 목록 페이지 이동
```

---

### 1) Pinia Store - createArticle 액션

**stores/article.js**
```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const article = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  // 게시글 생성
  const createArticle = function (title, content) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/articles/`,
      data: {
        title,
        content
      }
    })
      .then(() => {
        // 게시글 생성 성공 후 목록 페이지로 이동
        router.push({ name: 'ArticleView' })
      })
      .catch(err => console.log(err))
  }

  return { articles, article, API_URL, getArticles, getArticle, createArticle }
})
```

---

### 2) CreateView 컴포넌트 (1/3)

**views/CreateView.vue**
```vue
<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()
const title = ref('')
const content = ref('')

const createArticle = function () {
  store.createArticle(title.value, content.value)
}
</script>
```

---

### 3) CreateView 컴포넌트 (2/3) - 템플릿

**views/CreateView.vue**
```vue
<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목</label>
      <input type="text" id="title" v-model.trim="title"><br>
      
      <label for="content">내용</label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      
      <input type="submit">
    </form>
  </div>
</template>
```

**중요:**
- `@submit.prevent`: submit 이벤트의 기본 동작(페이지 새로고침) 취소
- `v-model.trim`: 입력값의 앞뒤 공백 제거

---

### 4) DRF View 함수

**articles/views.py**
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # ... (전체 조회 코드)
        pass
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

---

### 게시글 작성 결과

**브라우저 화면:**
```
게시글 작성

제목: [입력 필드]
내용: [텍스트 영역]
[제출 버튼]
```

**제출 후 → 게시글 목록 페이지로 자동 이동**

---

## 9️⃣ 참고사항

### 1) axios 요청 구조

**기본 구조:**
```javascript
axios({
  method: 'get',  // 'get', 'post', 'put', 'delete' 등
  url: 'http://127.0.0.1:8000/api/v1/articles/',
  data: {  // POST, PUT 등에서 사용
    title: '제목',
    content: '내용'
  }
})
  .then(response => {
    // 성공 시 처리
    console.log(response.data)
  })
  .catch(error => {
    // 실패 시 처리
    console.log(error)
  })
```

---

### 2) CSRF 토큰 전송 (POST 요청 시)

**Django의 CSRF 보호:**
- POST, PUT, DELETE 등의 요청 시 CSRF 토큰 필요

**Vue에서 CSRF 토큰 전송:**
```javascript
// 쿠키에서 CSRF 토큰 가져오기
function getCookie(name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

// axios 요청 시 헤더에 CSRF 토큰 포함
axios({
  method: 'post',
  url: `${API_URL}/api/v1/articles/`,
  data: {
    title,
    content
  },
  headers: {
    'X-CSRFToken': getCookie('csrftoken')
  }
})
```

---

### 3) data-* 속성 활용

**HTML에 사용자 지정 데이터 저장:**
```html
<div data-user-id="1" data-article-id="5">
  게시글 내용
</div>
```

**JavaScript에서 접근:**
```javascript
const element = document.querySelector('div')
console.log(element.dataset.userId)      // "1"
console.log(element.dataset.articleId)   // "5"
```

---

### 4) useRoute() vs useRouter()

| 함수 | 반환값 | 용도 | 예시 |
|------|--------|------|------|
| **useRoute()** | 현재 라우트 정보 | 읽기 전용 | `route.params.id` |
| **useRouter()** | 라우터 인스턴스 | 페이지 이동 | `router.push()` |

**예시:**
```javascript
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()    // 현재 정보 읽기
const router = useRouter()  // 페이지 이동

// 현재 URL의 id 파라미터 가져오기
const articleId = route.params.id

// 프로그래밍 방식으로 페이지 이동
router.push({ name: 'ArticleView' })
```

---

## 🔟 확인 문제

### 문제

**1. 다른 출처의 리소스 공유를 막는 브라우저 보안 정책은?**
- a) CORS
- b) SOP
- c) API
- d) DOM

---

**2. SOP 제한을 완화하여 다른 출처 간 리소스 공유를 허용하는 정책은?**
- a) CORS
- b) SOP
- c) DRF
- d) JSON

---

**3. Django에서 CORS 설정을 위해 등록해야 하는 앱은?**
- a) django-cors-headers
- b) django-rest-framework
- c) django-axios
- d) django-vue

---

**4. DRF 서버에 비동기 요청을 보내는 Pinia의 구성 요소는?**
- a) state
- b) getters
- c) actions
- d) plugins

---

**5. DRF view에서 JSON 데이터를 응답하기 위해 사용하는 것은?**
- a) render()
- b) redirect()
- c) HttpResponse()
- d) JsonResponse()

---

**6. Vue에서 DRF로 CSRF 토큰을 보내는 방법은?**
- a) URL 파라미터
- b) 요청 데이터(data)
- c) 요청 헤더(headers)
- d) 쿠키(cookie)

---

**7. 컴포넌트가 마운트될 때 API 요청을 보내는 훅은?**
- a) onUpdated
- b) onCreated
- c) onMounted
- d) onBeforeMount

---

**8. 상세 페이지에서 URL의 id 값을 가져오는 방법은?**
- a) useRouter().params.id
- b) useRoute().params.id
- c) defineProps({ id })
- d) this.$route.id

---

**9. 게시글 생성 시 DRF 서버에 보내는 HTTP 메서드는?**
- a) GET
- b) POST
- c) PUT
- d) DELETE

---

**10. 게시글 생성 성공 후 목록 페이지로 이동하는 방법은?**
- a) router.push({ name: 'ArticleView' })
- b) route.push({ name: 'ArticleView' })
- c) location.href = '/'
- d) window.reload()

---

## 📝 정답 및 해설

**1. b) SOP**
- 동일 출처 정책(SOP)은 다른 출처의 리소스 요청을 기본적으로 차단하는 보안 정책입니다.

**2. a) CORS**
- CORS(교차 출처 리소스 공유)는 서버가 허용된 출처에 한해 리소스 접근을 허용하는 정책입니다.

**3. a) django-cors-headers**
- django-cors-headers 라이브러리를 설치하고 앱과 미들웨어에 등록하여 사용합니다.

**4. c) actions**
- actions 내에서 Axios 같은 HTTP 클라이언트를 사용하여 외부 API에 비동기 요청을 보냅니다.

**5. d) JsonResponse()**
- JsonResponse는 Python 딕셔너리를 JSON 형식으로 변환하여 클라이언트에 응답합니다.

**6. c) 요청 헤더(headers)**
- Axios 요청 시 headers 객체에 X-CSRFToken 키로 토큰을 담아 전송해야 합니다.

**7. c) onMounted**
- onMounted 훅은 컴포넌트가 DOM에 렌더링된 직후에 실행되므로 초기 데이터 로드에 적합합니다.

**8. b) useRoute().params.id**
- useRoute 함수는 현재 경로의 파라미터 등 라우트 정보에 접근할 수 있게 해줍니다.

**9. b) POST**
- 새로운 리소스를 생성하기 위해서는 서버에 POST 메서드로 데이터를 전송해야 합니다.

**10. a) router.push({ name: 'ArticleView' })**
- useRouter로 가져온 router 인스턴스의 push 메서드를 사용하여 프로그래밍 방식으로 이동합니다.

---

## 📋 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **CORS** | 다른 출처의 리소스 공유를 허용 | Django corsheaders 설정 |
| **SOP** | 동일 출처의 리소스만 요청 허용 | 다른 도메인의 API 요청 차단 |
| **JsonResponse** | Django에서 JSON 형식으로 응답 | `return JsonResponse(data)` |
| **data-* 속성** | HTML에 사용자 지정 데이터 저장 | `<div data-user-id="1">` |
| **CSRF 토큰 전송** | Axios 요청 헤더에 토큰 포함 | `headers: {'X-CSRFToken': token}` |
| **Pinia action** | Axios로 DRF 서버에 데이터 요청 | `store.getArticles()` |
| **동적 세그먼트** | useRoute로 URL 파라미터 조회 | `route.params.id` |

---

## 🎯 요약 정리

### 동일 출처 정책 (SOP)

**웹 브라우저의 기본 보안 정책:**
- 한 출처(Origin)에서 로드된 문서나 스크립트가 다른 출처의 리소스와 상호작용하는 것을 제한
- 여기서 '출처'는 프로토콜, 호스트, 포트 번호의 조합을 의미

---

### CORS (Cross-Origin Resource Sharing)

**SOP 제한을 완화하기 위한 정책:**
- 서버가 특정 출처의 요청을 허용하도록 설정
- 서버가 자신의 응답 헤더에 `Access-Control-Allow-Origin` 같은 정보를 포함하여
- 브라우저에게 다른 출처의 요청을 허용한다고 알리는 정책

---

### 전체 게시글 조회

**ArticleView가 마운트될 때:**
- `getArticles` 액션을 호출하여 모든 게시글 데이터를 받아오기
- ArticleList 컴포넌트는 store의 articles 배열을 v-for로 순회
- 각 게시글 데이터를 ArticleListItem 자식 컴포넌트에 props로 전달하여 화면에 목록을 출력

---

### 단일 게시글 조회

**동적 라우팅:**
- `router/index.js`에 `/articles/:id`와 같은 동적 경로를 설정

**페이지 이동:**
- ArticleListItem에서 각 게시글의 고유 id를 포함한 RouterLink를 만들어 상세 페이지 이동 링크 생성

**데이터 조회:**
- DetailView 컴포넌트가 마운트되면 `useRoute()`를 사용해 URL의 id 파라미터 값을 가져오기
- 이 id를 이용해 DRF 서버에 특정 게시글 하나에 대한 데이터를 요청하고 받아와 화면에 렌더링

---

### 게시글 작성

**폼 작성:**
- CreateView 컴포넌트에서 v-model을 사용해 `<input>`과 `<textarea>`의 값을 반응형 변수와 양방향 바인딩

**데이터 전송:**
- form을 제출(`@submit.prevent`)하면 createArticle 함수가 호출
- 이 함수는 axios를 사용해 title과 content 데이터를 담아 DRF 서버에 POST 요청 보내기

**페이지 이동:**
- 게시글 생성이 성공하면 `useRouter()`의 push 메서드를 사용해 사용자를 게시글 목록 페이지로 이동시키기

---

## 🚀 학습 완료!

**"게시글 목록 보기" 버튼을 클릭하면 데이터는 어떤 과정을 거쳐 화면에 나타날까요?**

1. Vue에서 시작해 Axios를 통해 DRF 서버로 전달됩니다.
2. 이때 CORS라는 보안 확인 절차를 거칩니다.
3. DRF는 요청받은 데이터를 처리 후 JSON 형태로 응답합니다.
4. Pinia가 응답받은 데이터를 중앙 저장소(store)에 저장하고
5. 컴포넌트는 이 데이터를 화면에 렌더링합니다.

**각 과정을 직접 구현하여, 과정에 필요한 기술을 학습했습니다.**

**지금까지 배워온 프론트엔드(Vue)와 백엔드(Django)를 연결하여,**
**하나의 완전한 웹 애플리케이션을 만들었습니다!**

