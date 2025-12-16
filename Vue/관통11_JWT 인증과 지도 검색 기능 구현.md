## 📚 프로젝트 목차

1. **JWT (JSON Web Token)** - 인증 시스템
2. **JWT 실습** - DRF와 Vue 연동
3. **위치 기반 지도 검색 기능** - Geolocation API, iframe, diff 패키지

---

## 1️⃣ JWT (JSON Web Token) 개요

### JWT란?

**정의:**
- JSON Web Token의 약자
- 유저가 스스로 누군지 증명하는 **디지털 출입증**
- 서버가 유저에게 발급해주는 **긴 문자열**
- 해당 문자열 안에는 유저의 정보가 **암호화**되어 들어 있음

**비유:**
- 은행에서 받는 신분증처럼, JWT는 온라인에서 "나는 누구다"를 증명하는 토큰입니다

---

### JWT 구조

JWT는 **점(`.`)으로 구분된 3부분**으로 구성됩니다:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
└──────────────────┬──────────────────┘ └────────────────────┬────────────────────┘ └──────────────┬──────────────┘
         Header                               Payload                           Signature
```

#### 1) Header (헤더)
```json
{
  "alg": "HS256",  // 암호화 알고리즘
  "typ": "JWT"     // 토큰 타입
}
```
- 토큰의 타입과 암호화 알고리즘 정보

---

#### 2) Payload (페이로드)
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```
- **실제 유저 정보가 들어있는 내용물**
- 사용자 ID, 이름, 발급 시간 등

**⚠️ 주의:**
- Payload는 암호화되지 않고 **base64로만 인코딩**됨
- 누구나 디코딩해서 볼 수 있으므로 **민감한 정보(비밀번호 등)는 절대 넣지 말 것!**

---

#### 3) Signature (서명)
```javascript
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  your-256-bit-secret
)
```
- **정보가 조작되지 않았음을 증명하는 위조 방지 도장**
- 서버가 가진 비밀 키(secret)로 위조 유무를 확인할 수 있음

---

### JWT 동작 흐름

```
1. 클라이언트: 로그인 요청
              ↓
2. 서버: 사용자 정보 검증 후 JWT 토큰 발급
              ↓
3. 클라이언트: JWT를 브라우저나 앱에 저장
              ↓
4. 클라이언트: 발급받은 JWT를 header에 담아 API 요청
              ↓
5. 서버: JWT에 포함된 서명을 검증 후 응답
   (별도의 DB 조회 없이!)
```

**핵심:**
- 서버는 매번 DB를 조회할 필요 없이 JWT의 서명만 검증
- 이것이 JWT의 가장 큰 장점입니다!

---

### JWT 특징

#### 장점 ✅

**1) 서버 부담이 적음**
- DB에 저장하여 누가 로그인 중인지 기억할 필요 없음 (**Stateless**)
- 토큰에 모든 정보가 들어있으므로 서버가 세션을 관리하지 않아도 됨

**2) 확장성이 좋음**
- 서버를 여러 대 늘려도 (**Scale-out**) 토큰만 있으면 어떤 서버에서든 인증이 가능
- 로드 밸런싱에 유리

**3) 모바일 친화적**
- 웹뿐만 아니라 앱에서도 쓰기 편함
- 쿠키를 사용하지 않아도 됨

---

#### 단점 ❌

**1) 키를 잃어버렸을 경우 대응하기 어려움**
- 토큰이 탈취되면 만료 시간까지는 막을 방법이 없음
- 해결책: refresh token 사용 (짧은 만료 시간 설정)

**2) Payload에 개인정보가 있을 시 누구든 확인할 수 있음**
- Base64로만 인코딩되어 있어 디코딩 가능
- 절대 중요한 정보를 넣지 말 것!

---

### Token 방식 vs JWT 방식

#### Token 방식 (전통적 방식)
```
Client → Server: 로그인
Server → Client: 랜덤 토큰 발급
Server: DB에 토큰 저장
       (token: "abc123", user_id: 1)

다음 요청:
Client → Server: "abc123" 전송
Server: DB 조회하여 user_id 확인
```

**특징:**
- 키 자체에는 아무런 정보가 없고 정보는 서버가 가지고 있음
- 번거롭지만 키 유출 시 서버에서 Disable 처리하여 대응 가능함
- 로그인 관리가 엄격해야 하는 경우 사용 (예: 은행)

---

#### JWT 방식
```
Client → Server: 로그인
Server → Client: JWT 발급 (유저 정보 포함)
Server: 아무것도 저장 안 함

다음 요청:
Client → Server: JWT 전송
Server: JWT 서명 검증 (DB 조회 없음!)
```

**특징:**
- 키에 정보가 들어있어 서버가 정보를 따로 확인할 필요가 없음
- 서버가 토큰을 해석해서 사용자 인증을 하게 됨
- 간단하지만 키 유출 시 대응하기 힘듦

---

## 2️⃣ JWT 실습 - DRF와 Vue 연동

### 사전 준비

#### 1단계: DRF에서 JWT 설정

**djangorestframework-simplejwt 사용**

DRF 공식 문서에서 JWT 인증을 위해 `djangorestframework-simplejwt` 패키지를 권장합니다.

---

#### 2단계: 패키지 설치

**DRF 프로젝트의 가상환경에서:**

```bash
# 가상환경 활성화
$ source venv/Scripts/activate

# simplejwt 설치
$ pip install djangorestframework-simplejwt

# requirements.txt 업데이트
$ pip freeze > requirements.txt
```

---

#### 3단계: settings.py 설정

**my_api/settings.py**

```python
INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    'rest_framework.authtoken',      # 주석 해제
    'dj_rest_auth',                  # 주석 해제
    'django.contrib.sites',          # 주석 해제
    'allauth',                       # 주석 해제
    'allauth.account',               # 주석 해제
    'allauth.socialaccount',         # 주석 해제
    'dj_rest_auth.registration',     # 주석 해제
    # ...
]

# REST Framework 설정
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # 주석 해제
    ],
    # Permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # 주석 해제
    ],
}

# 사이트 ID 설정
SITE_ID = 1
```

---

#### 4단계: urls.py 설정

**my_api/urls.py**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),              # 주석 해제
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),  # 주석 해제
]
```

**제공되는 URL:**
- `POST /accounts/signup/` - 회원가입
- `POST /accounts/login/` - 로그인
- `POST /accounts/logout/` - 로그아웃
- `GET /accounts/user/` - 현재 사용자 정보

---

#### 5단계: Migration 실행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

---

#### 6단계: 서버 실행 및 테스트

```bash
$ python manage.py runserver
```

**브라우저에서 확인:**
- `http://127.0.0.1:8000/accounts/signup/` - 회원가입 페이지
- `http://127.0.0.1:8000/accounts/login/` - 로그인 페이지

---

### Vue에서 JWT 사용하기

#### 1단계: 회원가입 구현

**stores/user.js** (Pinia Store 생성)

```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  // 회원가입
  const signUp = function(payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then(res => {
        console.log('회원가입 성공')
        // 회원가입 성공 후 자동 로그인
        const password = password1
        logIn({ username, password })
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { API_URL, token, signUp }
})
```

**설명:**
- `axios`로 DRF 서버의 `/accounts/signup/` 엔드포인트에 POST 요청
- `username`, `password1`, `password2`를 보냄
- 회원가입 성공 시 자동으로 로그인 함수 호출

---

**views/SignUpView.vue**

```vue
<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <label for="username">사용자명:</label>
      <input type="text" id="username" v-model.trim="username" required>
      
      <label for="password1">비밀번호:</label>
      <input type="password" id="password1" v-model.trim="password1" required>
      
      <label for="password2">비밀번호 확인:</label>
      <input type="password" id="password2" v-model.trim="password2" required>
      
      <input type="submit" value="가입하기">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}
</script>
```

**핵심:**
- `v-model.trim`으로 입력값의 앞뒤 공백 제거
- `@submit.prevent`로 폼 제출 시 페이지 새로고침 방지
- store의 `signUp` 액션 호출

---

#### 2단계: 로그인 구현

**stores/user.js**

```javascript
export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  // 로그인
  const logIn = function(payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then(res => {
        // 토큰을 받아서 저장
        token.value = res.data.key
        console.log('로그인 성공')
        console.log('토큰:', token.value)
        
        // 메인 페이지로 이동
        router.push({ name: 'ArticleView' })
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { API_URL, token, signUp, logIn }
})
```

**핵심:**
- 로그인 성공 시 서버가 반환하는 `res.data.key`에 **토큰**이 들어있음
- 이 토큰을 `token` state에 저장
- 이후 모든 API 요청 시 이 토큰을 헤더에 담아 보냄

---

**views/LogInView.vue**

```vue
<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <label for="username">사용자명:</label>
      <input type="text" id="username" v-model.trim="username" required>
      
      <label for="password">비밀번호:</label>
      <input type="password" id="password" v-model.trim="password" required>
      
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const username = ref('')
const password = ref('')

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>
```

---

#### 3단계: 인증이 필요한 API 요청

**stores/article.js**

```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useUserStore } from './user'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // 게시글 목록 조회 (인증 필요)
  const getArticles = function() {
    const userStore = useUserStore()
    
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${userStore.token}`  // 토큰을 헤더에 추가!
      }
    })
      .then(res => {
        articles.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { articles, API_URL, getArticles }
})
```

**핵심:**
- `headers`에 `Authorization: Token <토큰값>` 형식으로 토큰 전송
- DRF는 이 헤더를 읽어서 사용자를 인증함

---

#### 4단계: DRF View에서 인증 확인

**articles/views.py**

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # 주석 해제 - 인증 필요!
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)  # 주석 해제 - 작성자 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

**핵심:**
- `@permission_classes([IsAuthenticated])` - 로그인한 사용자만 접근 가능
- `serializer.save(user=request.user)` - 현재 로그인한 사용자를 작성자로 저장

---

#### 5단계: Article 모델에 user 필드 추가

**articles/models.py**

```python
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )  # 주석 해제
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**articles/serializers.py**

```python
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)  # 주석 해제
```

**Migration 실행:**

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

---

### 토큰 저장 (Local Storage)

로그인 후 페이지를 새로고침하면 토큰이 사라집니다. 이를 방지하기 위해 **Local Storage**에 저장합니다.

**stores/user.js** (pinia-plugin-persistedstate 사용)

```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore(
  'user',
  () => {
    const API_URL = 'http://127.0.0.1:8000'
    const token = ref(null)
    const router = useRouter()

    const signUp = function(payload) {
      // ... (위와 동일)
    }

    const logIn = function(payload) {
      // ... (위와 동일)
    }

    const logOut = function() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then(res => {
          token.value = null
          router.push({ name: 'ArticleView' })
        })
        .catch(err => {
          console.log(err)
        })
    }

    return { API_URL, token, signUp, logIn, logOut }
  },
  {
    persist: true  // Local Storage에 저장!
  }
)
```

**핵심:**
- `{ persist: true }` 옵션으로 `token` state가 자동으로 Local Storage에 저장됨
- 페이지를 새로고침해도 토큰이 유지됨

---

### 로그인 상태에 따른 UI 변경

**App.vue**

```vue
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">게시글</RouterLink>
      
      <!-- 로그인하지 않은 경우 -->
      <template v-if="!userStore.token">
        <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
        <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
      </template>
      
      <!-- 로그인한 경우 -->
      <template v-else>
        <RouterLink :to="{ name: 'CreateView' }">게시글 작성</RouterLink>
        <button @click="userStore.logOut">로그아웃</button>
      </template>
    </nav>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
</script>
```

**핵심:**
- `userStore.token`의 존재 여부로 로그인 상태 판단
- 로그인 전/후에 다른 메뉴 표시

---

## 3️⃣ 위치 기반 지도 검색 기능 구현

### 개요

다음 기능들을 구현합니다:

1. **Geolocation API** - 사용자의 현재 위치 가져오기
2. **Google Maps iframe** - 지도 표시
3. **diff 패키지** - 키워드 변경 감지

---

### Geolocation API

**정의:**
- 웹 브라우저에서 사용자의 현재 위치 정보를 가져오는 API
- GPS, Wi-Fi, IP 주소 등을 사용하여 위치 결정

**사용 예시:**

```javascript
import { ref } from 'vue'

// 위도, 경도 저장
const lat = ref(null)
const lng = ref(null)
const error = ref(null)

// 현재 위치 가져오기
const getLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      // 성공 시
      (position) => {
        lat.value = position.coords.latitude
        lng.value = position.coords.longitude
        console.log(`위도: ${lat.value}, 경도: ${lng.value}`)
      },
      // 실패 시
      (err) => {
        error.value = '위치를 가져올 수 없습니다.'
        console.error(err)
      }
    )
  } else {
    error.value = '이 브라우저는 Geolocation을 지원하지 않습니다.'
  }
}

// 컴포넌트 마운트 시 실행
onMounted(() => {
  getLocation()
})
```

**핵심:**
- `navigator.geolocation.getCurrentPosition()` 사용
- 첫 번째 인자: 성공 콜백
- 두 번째 인자: 실패 콜백
- 사용자가 위치 권한을 허용해야 작동함

---

### Google Maps iframe

**정의:**
- `<iframe>` 태그를 사용하여 Google Maps를 웹 페이지에 임베드

**기본 구조:**

```html
<iframe
  :src="mapUrl"
  width="600"
  height="450"
  style="border:0;"
  allowfullscreen=""
  loading="lazy"
></iframe>
```

**URL 구조:**

```javascript
const mapUrl = computed(() => {
  // 키워드가 있으면 키워드 검색
  const query = keyword.value.trim() 
    ? keyword.value 
    : `${lat.value},${lng.value}`  // 없으면 현재 위치

  return `https://maps.google.com/maps?q=${query}&t=&z=14&ie=UTF8&iwloc=&output=embed`
})
```

**파라미터 설명:**
- `q` - 검색 쿼리 (키워드 또는 위도,경도)
- `t` - 지도 타입
- `z` - 줌 레벨 (1~20, 14가 적당)
- `output=embed` - iframe 임베드 모드

---

### diff 패키지

**정의:**
- 두 텍스트를 비교하여 **차이점(변경, 추가, 삭제)**을 찾아주는 패키지
- 키워드가 얼마나 변경되었는지 확인하여 지도 업데이트 여부를 결정

---

#### 1단계: 패키지 설치

```bash
$ npm install diff
```

**package.json에 자동 추가:**

```json
{
  "dependencies": {
    "diff": "^7.0.0"
  }
}
```

---

#### 2단계: diff 패키지 사용

**기본 사용법:**

```vue
<script setup>
import { diffChars } from 'diff'

const oldStr = '변경 전'
const newStr = '변경 후 추가'

const changes = diffChars(oldStr, newStr)

console.log(changes)
/*
[
  { count: 3, added: false, removed: false, value: '변경 ' },
  { count: 1, added: false, removed: true, value: '전' },
  { count: 4, added: true, removed: false, value: '후 추가' }
]
*/
</script>
```

**반환 객체 구조:**
- `count` - 변경된 문자 수
- `added` - 추가되었는지 (true/false)
- `removed` - 삭제되었는지 (true/false)
- `value` - 변경된 문자열

---

#### 3단계: diff 시각화

**변경 부분을 색상으로 표시:**

```vue
<template>
  <div>
    <span
      v-for="(change, index) in changes"
      :key="index"
      :class="{
        add: change.added,
        removed: change.removed
      }"
    >
      {{ change.value }}
    </span>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { diffChars } from 'diff'

const oldStr = ref('변경 전')
const newStr = ref('변경 후 추가')

const changes = diffChars(oldStr.value, newStr.value)
</script>

<style scoped>
.add {
  color: green;
  background-color: #d4edda;
}

.removed {
  color: red;
  background-color: #f8d7da;
  text-decoration: line-through;
}
</style>
```

---

#### 4단계: 변경된 문자 수 계산

```javascript
// 추가되거나 삭제된 부분만 필터링
const diffCount = changes
  .filter(function(char) {
    return char.added || char.removed
  })
  // 각 변경 부분의 count를 합산
  .reduce(function(sum, char) {
    return sum + char.count
  }, 0)

console.log(`총 변경된 문자 수: ${diffCount}`)
```

**설명:**
1. `filter`로 `added` 또는 `removed`가 `true`인 것만 추출
2. `reduce`로 각 `count`를 모두 더함
3. 결과: 총 변경된 문자 수

---

### 완성 코드: 지도 검색 기능

**MapView.vue**

```vue
<template>
  <div>
    <h1>위치 기반 지도 검색</h1>
    
    <!-- 검색 입력 -->
    <div>
      <label for="keyword">검색 키워드:</label>
      <input
        type="text"
        id="keyword"
        v-model="keyword"
        placeholder="장소를 입력하세요"
      >
      <button @click="tryUpdateMap">검색</button>
    </div>
    
    <!-- 오류 메시지 -->
    <p v-if="error" style="color: red;">{{ error }}</p>
    
    <!-- 지도 iframe -->
    <iframe
      v-if="lat && lng"
      :src="mapUrl"
      width="600"
      height="450"
      style="border:0;"
      allowfullscreen=""
      loading="lazy"
    ></iframe>
    
    <!-- 변경 사항 시각화 -->
    <div v-if="changes.length">
      <h3>키워드 변경 내역:</h3>
      <p>
        <span
          v-for="(change, index) in changes"
          :key="index"
          :class="{
            add: change.added,
            removed: change.removed
          }"
        >
          {{ change.value }}
        </span>
      </p>
      <p>총 변경된 문자 수: {{ diffCount }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { diffChars } from 'diff'

// 상태 관리
const lat = ref(null)
const lng = ref(null)
const keyword = ref('')
const prevKeyword = ref('')
const error = ref(null)
const changes = ref([])

// 현재 위치 가져오기
const getLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        lat.value = position.coords.latitude
        lng.value = position.coords.longitude
        error.value = null
      },
      (err) => {
        error.value = '위치를 가져올 수 없습니다.'
        console.error(err)
      }
    )
  } else {
    error.value = '이 브라우저는 Geolocation을 지원하지 않습니다.'
  }
}

// 지도 URL 생성
const mapUrl = computed(() => {
  // 키워드가 비어있으면 현재 위치로 설정
  const query = keyword.value.trim() 
    ? keyword.value 
    : `${lat.value},${lng.value}`

  return `https://maps.google.com/maps?q=${query}&t=&z=14&ie=UTF8&iwloc=&output=embed`
})

// 지도 업데이트 함수
const updateMap = () => {
  // 키워드가 비어있으면 현재 위치로 설정
  const query = keyword.value.trim() 
    ? keyword.value 
    : `${lat.value},${lng.value}`

  // mapUrl computed가 자동으로 업데이트됨
  error.value = null
}

// diff로 키워드 변화 판단 및 지도 갱신 시도
const tryUpdateMap = () => {
  // 이전 키워드와 현재 키워드 비교
  changes.value = diffChars(prevKeyword.value, keyword.value)
  
  // 추가되었거나 제거된 문자열만 필터링
  const diffCount = changes.value
    .filter(function(char) {
      return char.added || char.removed
    })
    // 총 변경된 문자 수 계산
    .reduce(function(sum, char) {
      return sum + char.count
    }, 0)
  
  // 최소 두 글자 이상 바뀌어야 지도 업데이트
  const threshold = 2
  
  if (diffCount > threshold) {
    prevKeyword.value = keyword.value
    updateMap()
    error.value = null
  } else {
    error.value = '키워드가 크게 바뀌지 않았습니다.'
  }
}

// 변경된 문자 수 (computed)
const diffCount = computed(() => {
  return changes.value
    .filter(char => char.added || char.removed)
    .reduce((sum, char) => sum + char.count, 0)
})

// 컴포넌트 마운트 시 실행
onMounted(() => {
  getLocation()
})
</script>

<style scoped>
.add {
  color: green;
  background-color: #d4edda;
}

.removed {
  color: red;
  background-color: #f8d7da;
  text-decoration: line-through;
}

input {
  padding: 8px;
  margin: 0 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

iframe {
  margin-top: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
</style>
```

---

### 동작 흐름 정리

```
1. 컴포넌트 마운트
   ↓
2. getLocation()으로 현재 위치 가져오기
   ↓
3. mapUrl computed가 현재 위치로 지도 표시
   ↓
4. 사용자가 키워드 입력
   ↓
5. "검색" 버튼 클릭 → tryUpdateMap() 호출
   ↓
6. diffChars()로 이전 키워드와 비교
   ↓
7. 변경된 문자 수가 threshold(2) 이상이면
   ↓
8. updateMap() → mapUrl 업데이트 → iframe 새로고침
   ↓
9. 변경 사항 시각화 표시
```

---

### 핵심 포인트 정리

#### JWT 인증
1. **회원가입/로그인** - DRF에서 토큰 발급
2. **토큰 저장** - Local Storage에 persist
3. **API 요청** - `Authorization: Token <토큰>` 헤더 추가
4. **인증 확인** - `@permission_classes([IsAuthenticated])`

#### 지도 검색
1. **Geolocation API** - 현재 위치 가져오기
2. **Google Maps iframe** - 지도 표시
3. **diff 패키지** - 키워드 변경 감지
4. **threshold** - 변경이 일정 이상일 때만 업데이트

---

## 📝 추가 학습 사항

### refresh token 개념

**문제:**
- Access Token이 탈취되면 만료 시간까지 막을 방법이 없음

**해결책: refresh token**

```
1. 로그인 시 2개의 토큰 발급:
   - Access Token (짧은 만료 시간, 예: 15분)
   - Refresh Token (긴 만료 시간, 예: 2주)

2. API 요청 시 Access Token 사용

3. Access Token이 만료되면:
   - Refresh Token으로 새 Access Token 발급
   
4. Refresh Token도 만료되면:
   - 다시 로그인 필요
```

**장점:**
- Access Token 탈취 시 피해 최소화 (15분 후 자동 무효화)
- Refresh Token은 별도 저장소에 안전하게 보관

---


**학습 포인트:**
1. ✅ JWT 인증 시스템 구현
2. ✅ DRF와 Vue 연동 (토큰 기반)
3. ✅ Geolocation API 활용
4. ✅ iframe으로 지도 표시
5. ✅ diff 패키지로 텍스트 비교