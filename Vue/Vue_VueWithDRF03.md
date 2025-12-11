# Vue with DRF 03

## 📚 목차
1. 인증 with Vue
   - 회원가입
   - 로그인
   - 요청과 토큰
   - 인증 여부 확인
2. User Customize
   - User Model Field 수정
   - RegisterSerializer 수정
3. 참고
   - 로그아웃
   - 기타 기능 구현
   - Django Signals
   - 환경 변수
   - Vue 참고 자료
   - 설치한 라이브러리 정리

---

## 🎯 학습 목표

1. ✅ DRF에 로그인 요청 후 Pinia store에 인증 토큰을 저장한다
2. ✅ Pinia store의 토큰을 Authorization 헤더에 담아 요청한다
3. ✅ store의 토큰 유무에 따라 computed로 로그인 상태를 관리한다
4. ✅ Navigation Guard를 사용해 인증 여부에 따라 접근을 제어한다
5. ✅ dj-rest-auth의 회원가입 Serializer를 커스터마이징한다
6. ✅ Vue에서 회원가입 form을 만들고 DRF 서버에 데이터를 전송한다
7. ✅ 로그아웃 요청 후 store의 토큰 정보를 삭제할 수 있다

---

## 🏠 학습 시작

**"지난 시간, DRF에 권한 설정을 추가하자 게시글 조회가 401 Unauthorized 오류와 함께 막혔습니다. 어떻게 해결할 수 있을까요?"**

### 문제 상황

```
Articles 페이지
[CREATE]
AxiosError

Failed to load resource: the server responded with status of 401 (Unauthorized)
127.0.0.1:8000/api/v1/articles/ :1
```

**401 오류**: 인증에 필요한 수단(token)을 보내지 않고 있어 게시글 조회 불가

---

### 해결 방법

**인증 과정에서 프론트엔드(Vue)의 역할:**

1. **Vue에서 로그인을 요청하여 DRF로부터 토큰을 받습니다**
2. **이 토큰을 Pinia에 저장한 뒤, 모든 게시글 조회 요청에 토큰을 포함하여 보냅니다**

이 과정을 구현하여 401 오류를 해결하고 완전한 인증 시스템을 구축합니다!

---

## 1️⃣ 사전 준비

### DB 초기화

**기존 fixtures 데이터는 user 정보가 없으므로 사용 불가능**

```bash
# 1. db.sqlite3 삭제

# 2. Migration 과정 재진행
$ python manage.py makemigrations
$ python manage.py migrate

# 3. 관리자 계정 생성
$ python manage.py createsuperuser

# 4. 게시글 1개 이상 작성
```

---

### 시작하기 전에

**정상 작동하던 게시글 전체 조회가 작동하지 않음**
- 401 status code 확인
- 게시글 조회 요청 시 인증에 필요한 수단(token)을 보내지 않고 있으므로 게시글 조회가 불가능해진 것

**오늘의 목표:**
회원가입/로그인 과정에서 token을 발급받아 store에 저장하고, 인증이 필요한 요청마다 token을 함께 보내는 과정을 진행합니다.

401 오류가 해결되고 게시글이 정상적으로 출력되는 모습을 확인하는 게 목표입니다!

---

## 2️⃣ 회원가입

### 회원가입 로직 구현 (1/9)

**SignUpView route 관련 코드 주석 해제**

**router/index.js**
```javascript
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // ...
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    }
  ]
})

export default router
```

---

### 회원가입 로직 구현 (2/9)

**App 컴포넌트에 SignUpView 컴포넌트로 이동하는 RouterLink 작성**

**App.vue**
```vue
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      <RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>
```

---

### 회원가입 로직 구현 (3/9)

**회원가입 form 작성**

**views/SignUpView.vue**
```vue
<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username:</label>
      <input type="text" id="username" v-model.trim="username">
      <br>
      
      <label for="password1">password:</label>
      <input type="password" id="password1" v-model.trim="password1">
      <br>
      
      <label for="password2">password confirmation:</label>
      <input type="password" id="password2" v-model.trim="password2">
      <br>
      
      <input type="submit" value="signup">
    </form>
  </div>
</template>
```

---

### 회원가입 로직 구현 (4/9)

**사용자 입력 데이터와 바인딩될 반응형 변수 작성**

**views/SignUpView.vue**
```vue
<script setup>
import { ref } from 'vue'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
</script>
```

---

### 회원가입 로직 구현 (5/9)

**SignUpView 컴포넌트 출력 확인**

브라우저에서 `http://localhost:5173/signup` 접속하여 확인

```
Sign Up Page

username: [입력 필드]
password: [입력 필드]
password confirmation: [입력 필드]
[SignUp 버튼]
```

---

### 회원가입 로직 구현 (6/9)

**회원가입 요청을 보내기 위한 signUp 함수가 해야 할 일**

1. 사용자 입력 데이터를 받아
2. 서버로 회원가입 요청을 보냄

**stores/accounts.js**
```javascript
export const useAccountStore = defineStore('account', () => {
  const signUp = function() {
    // 회원가입 로직
  }
  
  return {
    signUp
  }
}, { persist: true })
```

---

### 회원가입 로직 구현 (7/9)

**컴포넌트에 사용자 입력 데이터를 저장 후 store의 signUp 함수를 호출하는 함수 작성**

**views/SignUpView.vue**
```vue
<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const store = useAccountStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

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

---

### 회원가입 로직 구현 (8/9)

**signUp 함수 완성**

**stores/accounts.js**
```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  
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
      .then((res) => {
        console.log('회원가입 성공')
        // 회원가입 성공 후 로그인 페이지로 이동
        router.push({ name: 'LogInView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return {
    signUp
  }
}, { persist: true })
```

---

### 회원가입 로직 구현 (9/9)

**회원가입 테스트**

1. 회원가입 페이지 접속
2. 폼 작성 및 제출
3. 회원가입 성공 후 로그인 페이지로 이동 확인

---

## 3️⃣ 로그인

### 로그인 로직 구현 (1/9)

**LogInView route 관련 코드 주석 해제**

**router/index.js**
```javascript
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // ...
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

export default router
```

---

### 로그인 로직 구현 (2/9)

**App 컴포넌트에 LogInView 컴포넌트로 이동하는 RouterLink 작성**

**App.vue**
```vue
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      <RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink>
      <RouterLink :to="{ name: 'LogInView' }">LogInPage</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>
```

---

### 로그인 로직 구현 (3/9)

**로그인 form 작성**

**views/LogInView.vue**
```vue
<template>
  <div>
    <h1>Log In Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username:</label>
      <input type="text" id="username" v-model.trim="username">
      <br>
      
      <label for="password">password:</label>
      <input type="password" id="password" v-model.trim="password">
      <br>
      
      <input type="submit" value="login">
    </form>
  </div>
</template>
```

---

### 로그인 로직 구현 (4/9)

**사용자 입력 데이터와 바인딩될 반응형 변수 작성**

**views/LogInView.vue**
```vue
<script setup>
import { ref } from 'vue'

const username = ref(null)
const password = ref(null)
</script>
```

---

### 로그인 로직 구현 (5/9)

**LogInView 컴포넌트 출력 확인**

브라우저에서 `http://localhost:5173/login` 접속하여 확인

```
Log In Page

username: [입력 필드]
password: [입력 필드]
[login 버튼]
```

---

### 로그인 로직 구현 (6/9)

**로그인 요청을 보내기 위한 logIn 함수가 해야 할 일**

1. 사용자 입력 데이터를 받아
2. 서버로 로그인 요청을 보내고
3. **응답 받은 토큰을 저장**

**stores/accounts.js**
```javascript
export const useAccountStore = defineStore('account', () => {
  const token = ref(null)  // 토큰 저장할 state
  
  const signUp = function(payload) {
    // ...
  }
  
  const logIn = function(payload) {
    // 로그인 로직
  }
  
  return {
    signUp,
    logIn,
    token
  }
}, { persist: true })
```

---

### 로그인 로직 구현 (7/9)

**컴포넌트에 사용자 입력 데이터를 저장 후 store의 logIn 함수를 호출하는 함수 작성**

**views/LogInView.vue**
```vue
<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const store = useAccountStore()

const username = ref(null)
const password = ref(null)

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

### 로그인 로직 구현 (8/9)

**logIn 함수 완성**

**stores/accounts.js**
```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const token = ref(null)
  
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
      .then((res) => {
        // 응답으로 받은 토큰을 저장
        token.value = res.data.key
        
        console.log('로그인 성공')
        // 로그인 성공 후 메인 페이지로 이동
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return {
    signUp,
    logIn,
    token
  }
}, { persist: true })
```

**핵심**: 응답으로 받은 `res.data.key`를 `token.value`에 저장!

---

### 로그인 로직 구현 (9/9)

**로그인 테스트**

1. 로그인 페이지 접속
2. 회원가입한 계정으로 로그인
3. 로그인 성공 후 메인 페이지로 이동 확인
4. **개발자 도구 → Application → Local Storage**에서 토큰 저장 확인

```json
{
  "token": "토큰값이 여기에 저장됨"
}
```

---

## 4️⃣ 요청과 토큰

### 인증된 요청 보내기

**게시글 조회 시 토큰을 헤더에 포함하여 요청**

**헤더 형식:**
```javascript
headers: {
  Authorization: `Token ${token}`
}
```

---

### getArticles 함수 수정

**stores/articles.js**
```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAccountStore } from './accounts'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  
  const getArticles = function() {
    // account store에서 토큰 가져오기
    const accountStore = useAccountStore()
    
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return {
    articles,
    API_URL,
    getArticles
  }
})
```

**핵심**: `Authorization: Token ${accountStore.token}` 헤더 추가!

---

### 테스트

**이제 401 오류가 해결되고 게시글이 정상적으로 출력됩니다!**

```
Article Page
[CREATE]
Article List
제목
내용
[DETAIL]
```

---

## 5️⃣ 인증 여부 확인

### 로그인 상태 관리

**토큰의 존재 여부로 로그인 상태를 판단하는 computed 속성 생성**

**stores/accounts.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const token = ref(null)
  
  // 로그인 여부 확인 computed
  const isLogin = computed(() => {
    return token.value !== null
  })
  
  const signUp = function(payload) {
    // ...
  }
  
  const logIn = function(payload) {
    // ...
  }
  
  return {
    signUp,
    logIn,
    token,
    isLogin
  }
}, { persist: true })
```

---

### 로그인 상태에 따른 UI 변경

**App.vue**
```vue
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      
      <!-- 로그인 안 된 경우 -->
      <template v-if="!accountStore.isLogin">
        <RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink>
        <RouterLink :to="{ name: 'LogInView' }">LogInPage</RouterLink>
      </template>
      
      <!-- 로그인 된 경우 -->
      <template v-else>
        <span>{{ accountStore.token }}</span>
        <button @click="accountStore.logOut">로그아웃</button>
      </template>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()
</script>
```

---

### Navigation Guard로 접근 제어

**router/index.js**
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import { useAccountStore } from '@/stores/accounts'

import ArticleView from '@/views/ArticleView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
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
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    }
  ]
})

// 전역 Navigation Guard
router.beforeEach((to, from) => {
  const accountStore = useAccountStore()
  
  // 로그인이 필요한 페이지
  const authRequired = ['ArticleView', 'CreateView']
  
  // 로그인 없이 접근 가능한 페이지
  const authNotRequired = ['SignUpView', 'LogInView']
  
  // 로그인이 필요한 페이지에 비로그인 사용자 접근 시
  if (authRequired.includes(to.name) && !accountStore.isLogin) {
    alert('로그인이 필요합니다')
    return { name: 'LogInView' }
  }
  
  // 로그인된 사용자가 회원가입/로그인 페이지 접근 시
  if (authNotRequired.includes(to.name) && accountStore.isLogin) {
    return { name: 'ArticleView' }
  }
})

export default router
```

---

## 6️⃣ User Customize

### User Model Field 수정 (1/3)

**age 필드 추가**

**accounts/models.py**
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
```

---

### User Model Field 수정 (2/3)

**Migration 진행**

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

---

### User Model Field 수정 (3/3)

**DB 초기화 (선택사항)**

기존 데이터와 충돌이 발생할 경우:

```bash
# 1. db.sqlite3 삭제
# 2. migrations 폴더의 파일들 삭제 (__init__.py 제외)
# 3. Migration 재진행
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

---

### RegisterSerializer 수정 (1/6)

**CustomRegisterSerializer 생성**

**accounts/serializers.py**
```python
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    # age 필드 추가
    age = serializers.IntegerField(required=False)
    
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', None)
        return data
    
    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age', None)
        user.save()
        return user
```

---

### RegisterSerializer 수정 (2/6)

**settings.py에 커스텀 Serializer 등록**

**my_api/settings.py**
```python
REST_AUTH = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}
```

---

### RegisterSerializer 수정 (3/6)

**Vue 회원가입 폼에 age 필드 추가**

**views/SignUpView.vue**
```vue
<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username:</label>
      <input type="text" id="username" v-model.trim="username">
      <br>
      
      <label for="password1">password:</label>
      <input type="password" id="password1" v-model.trim="password1">
      <br>
      
      <label for="password2">password confirmation:</label>
      <input type="password" id="password2" v-model.trim="password2">
      <br>
      
      <!-- age 필드 추가 -->
      <label for="age">age:</label>
      <input type="number" id="age" v-model.number="age">
      <br>
      
      <input type="submit" value="signup">
    </form>
  </div>
</template>
```

---

### RegisterSerializer 수정 (4/6)

**age 반응형 변수 추가**

**views/SignUpView.vue**
```vue
<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accounts'

const store = useAccountStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)  // age 변수 추가

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value  // age 포함
  }
  
  store.signUp(payload)
}
</script>
```

---

### RegisterSerializer 수정 (5/6)

**signUp 함수에 age 추가**

**stores/accounts.js**
```javascript
const signUp = function(payload) {
  const { username, password1, password2, age } = payload
  
  axios({
    method: 'post',
    url: `${API_URL}/accounts/signup/`,
    data: {
      username,
      password1,
      password2,
      age  // age 포함
    }
  })
    .then((res) => {
      console.log('회원가입 성공')
      router.push({ name: 'LogInView' })
    })
    .catch((err) => {
      console.log(err)
    })
}
```

---

### RegisterSerializer 수정 (6/6)

**회원가입 테스트**

1. 회원가입 페이지에서 age 포함하여 회원가입
2. Django admin에서 User 모델 확인
3. age 필드가 정상적으로 저장되었는지 확인

---

## 7️⃣ 로그아웃

### 로그아웃 로직 구현

**stores/accounts.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const token = ref(null)
  
  const isLogin = computed(() => {
    return token.value !== null
  })
  
  const signUp = function(payload) {
    // ...
  }
  
  const logIn = function(payload) {
    // ...
  }
  
  // 로그아웃 함수
  const logOut = function() {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // 토큰 삭제
        token.value = null
        
        console.log('로그아웃 성공')
        // 로그인 페이지로 이동
        router.push({ name: 'LogInView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return {
    signUp,
    logIn,
    logOut,
    token,
    isLogin
  }
}, { persist: true })
```

**핵심**:
1. DRF 서버에 로그아웃 요청
2. **토큰을 `null`로 변경** (가장 중요!)
3. 로그인 페이지로 이동

---

## 8️⃣ 기타 기능 구현

### 회원가입 후 자동 로그인

**회원가입 성공 후 바로 로그인 액션 호출**

**stores/accounts.js**
```javascript
const signUp = function(payload) {
  const { username, password1, password2, age } = payload
  
  axios({
    method: 'post',
    url: `${API_URL}/accounts/signup/`,
    data: {
      username,
      password1,
      password2,
      age
    }
  })
    .then((res) => {
      console.log('회원가입 성공')
      
      // 회원가입 성공 후 자동 로그인
      const loginPayload = {
        username: username,
        password: password1
      }
      logIn(loginPayload)
    })
    .catch((err) => {
      console.log(err)
    })
}
```

---

## 9️⃣ Django Signals

### Django Signals란?

**특정 이벤트가 발생했을 때 자동으로 특정 코드를 실행하도록 하는 기능**

**예시**: User가 생성될 때 자동으로 Profile 생성

**accounts/models.py**
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

**동작**: User가 생성되면 자동으로 Profile도 함께 생성됨

---

## 🔟 환경 변수

### .env.local 파일 생성

**보안이 필요한 정보는 환경 변수로 관리**

**프로젝트 루트에 `.env.local` 파일 생성:**

```
VITE_API_URL=http://127.0.0.1:8000
VITE_TMDB_API_KEY=eyJhfiwnfdk2o2f...
```

---

### 환경 변수 사용

**stores/accounts.js**
```javascript
export const useAccountStore = defineStore('account', () => {
  // 환경 변수 사용
  const API_URL = import.meta.env.VITE_API_URL
  
  // ...
})
```

**중요**:
- Vite는 `VITE_` 접두사가 붙은 환경 변수만 클라이언트에 노출
- `.env.local`은 `.gitignore`에 추가하여 Git에 올리지 않기

---

## 1️⃣1️⃣ Vue 참고 자료

### Awesome Vue.js

**Vue와 관련하여 엄선된 유용한 자료를 아카이빙 및 관리하는 프로젝트**

- GitHub: https://github.com/vuejs/awesome-vue
- 웹사이트: https://awesome-vue.js.org/

---

### Vuetify

**Vue를 위한 UI 라이브러리 (예: Bootstrap)**

- 웹사이트: https://vuetifyjs.com/en/

---

## 1️⃣2️⃣ 설치한 라이브러리 정리

### Vue 라이브러리

| 라이브러리 | 설명 |
|-----------|------|
| **pinia-plugin-persistedstate** | Pinia의 상태를 브라우저의 localStorage에 자동으로 저장해주는 플러그인 |
| **axios** | Vue가 Django 서버와 데이터를 주고받기 위해 사용하는 HTTP 통신 라이브러리 |

---

### Django 라이브러리

| 라이브러리 | 설명 |
|-----------|------|
| **djangorestframework** | Django로 REST API를 구축하기 위한 핵심 프레임워크 |
| **django-cors-headers** | CORS(교차 출처 리소스 공유) 헤더를 처리해주는 라이브러리 |
| **dj-rest-auth** | Django의 기본 인증 시스템을 기반으로 로그인/로그아웃/비밀번호 변경 등의 기능을 API 엔드포인트로 제공 |
| **dj-rest-auth[with-social]** | 기본 dj-rest-auth 기능에 더해 소셜 로그인 API를 구현하는 데 필요한 django-allauth 라이브러리를 함께 설치 |

---

## 📝 확인 문제

### 문제

**1. 로그인 성공 후, DRF가 보내준 토큰을 저장하는 곳은?**
- a) 로컬 변수
- b) Pinia store의 state
- c) 브라우저 쿠키
- d) 컴포넌트 props

**2. 인증이 필요한 요청 시 토큰을 보내는 방법은?**
- a) URL 파라미터에 포함
- b) Axios 요청 data에 포함
- c) Axios 요청 headers에 포함
- d) Pinia getters에 포함

**3. Pinia store에서 로그인 여부를 판단하는 가장 좋은 방법은?**
- a) ref를 사용한 변수
- b) computed를 사용한 속성
- c) watch를 사용한 감시자
- d) actions에 함수 작성

**4. 로그인 여부에 따라 페이지 접근을 제어하는 기능은?**
- a) Props와 Emit
- b) 라이프사이클 훅
- c) 내비게이션 가드
- d) v-if 디렉티브

**5. DRF User 모델에 새 필드를 추가한 후 해야 할 일은?**
- a) npm install
- b) makemigrations & migrate
- c) collectstatic
- d) createsuperuser

**6. 회원가입 시 추가 필드를 처리하기 위해 수정할 것은?**
- a) User 모델
- b) dj-rest-auth의 RegisterSerializer
- c) settings.py의 AUTH_USER_MODEL
- d) urls.py의 회원가입 경로

**7. Vite 프로젝트에서 환경 변수 이름에 필요한 접두사는?**
- a) VUE_APP_
- b) VITE_
- c) APP_
- d) ENV_

**8. DRF가 커스텀 Serializer를 사용하게 하는 설정은?**
- a) SERIALIZER_CLASSES
- b) CUSTOM_SERIALIZERS
- c) REST_FRAMEWORK
- d) REST_AUTH

**9. 로그아웃 시 Vue에서 가장 중요한 처리 로직은?**
- a) Pinia store의 토큰을 null로 변경
- b) DRF에 로그아웃 요청만 보내기
- c) 브라우저 쿠키 삭제
- d) 페이지를 새로고침

**10. 회원가입 성공 후 바로 로그인 시키는 방법은?**
- a) 회원가입 응답으로 토큰을 받는다
- b) 로그인 페이지로 이동시킨다
- c) 회원가입 액션에서 로그인 액션을 호출한다
- d) localStorage에 직접 토큰을 저장한다

---

## 📋 정답 및 해설

**1. b) Pinia store의state**
- 여러 컴포넌트에서 공유하고 상태를 유지하기 위해 Pinia 중앙 저장소에 토큰을 저장합니다.

**2. c) Axios 요청 headers에 포함**
- Authorization 헤더에 `Token <key>` 형식으로 토큰을 담아 서버에 전송해야 합니다.

**3. b) computed를 사용한 속성**
- 토큰의 존재 여부에 따라 로그인 상태를 계산하는 computed 속성을 만드는 것이 효율적입니다.

**4. c) 내비게이션 가드**
- Vue Router의 beforeEach 같은 내비게이션 가드를 사용하여 페이지 접근 권한을 제어합니다.

**5. b) makemigrations & migrate**
- 모델의 변경 사항을 데이터베이스 스키마에 반영하기 위해 마이그레이션을 진행해야 합니다.

**6. b) dj-rest-auth의 RegisterSerializer**
- 기본 RegisterSerializer를 상속받아 추가된 필드를 처리하도록 커스터마이징해야 합니다.

**7. b) VITE_**
- Vite는 보안을 위해 `VITE_` 접두사가 붙은 환경 변수만 클라이언트 코드에 노출합니다.

**8. d) REST_AUTH**
- settings.py의 `REST_AUTH` 딕셔너리에서 `REGISTER_SERIALIZER`를 지정합니다.

**9. a) Pinia store의 토큰을 null로 변경**
- DRF 로그아웃 요청 후 클라이언트의 로그인 상태를 관리하는 Pinia의 토큰을 반드시 제거해야 합니다.

**10. c) 회원가입 액션에서 로그인 액션을 호출한다**
- 회원가입 성공 후 해당 정보로 로그인 액션을 호출하여 토큰을 발급받는 것이 일반적입니다.

---

## 🎯 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| **토큰 인증** | 발급된 토큰으로 사용자를 인증 | `Authorization: Token <key>` |
| **dj-rest-auth** | DRF 인증 기능 제공 라이브러리 | 회원가입, 로그인 API 제공 |
| **Pinia에 토큰 저장** | 로그인 성공 시 응답 토큰을 저장 | `token.value = res.data.key` |
| **인증된 요청** | 요청 헤더에 토큰을 포함하여 전송 | `headers: { Authorization }` |
| **내비게이션 가드** | 인증 여부에 따라 페이지 접근 제어 | `router.beforeEach((to, from) => {})` |

---

## 📄 요약 정리

### DRF 인증과 Vue 연동 (1/3)

**DRF 서버의 토큰 기반 인증 시스템을 Vue 애플리케이션과 연동하여 회원가입/로그인/로그아웃 기능을 구현**

#### 회원가입
- Vue에서 회원가입 폼을 만들고 v-model로 사용자 입력 받기
- 폼을 제출하면 Pinia의 signUp 액션을 호출
- signUp 액션은 axios를 사용해 DRF의 회원가입 API(`accounts/signup/`)로 POST 요청 보내기

---

### DRF 인증과 Vue 연동 (2/3)

#### 로그인 및 토큰 관리
- Vue에서 로그인 폼을 만들고 v-model로 사용자 입력을 받기
- 폼을 제출하면 Pinia의 logIn 액션을 호출
- logIn 액션은 axios를 사용해 DRF의 로그인 API(`accounts/login/`)로 POST 요청을 보내기
- 요청이 성공하면 DRF 서버는 응답으로 인증 토큰(Token)을 보내주고 Pinia state에 token을 저장하여 로그인 상태를 유지

---

### DRF 인증과 Vue 연동 (3/3)

#### 인증된 요청 보내기
- 게시글 조회처럼 인증이 필요한 API를 요청할 때는 Pinia에 저장된 토큰을 axios 요청 헤더에 포함하기
- 헤더 형식은 `headers: { Authorization: 'Token ${token}' }` 와 같이 구성

---

### 인증 여부에 따른 접근 제어

#### 로그인 상태 확인
- Pinia store의 token의 존재 여부에 따라 true 또는 false를 반환하는 computed 속성(isLogin)을 만들어 로그인 상태를 쉽게 확인

#### 내비게이션 가드 활용
- Vue Router의 전역 가드(beforeEach)를 사용하여 페이지 접근을 제어
- 로그인이 필요한 페이지에 비로그인 사용자가 접근하면 로그인 페이지로 redirection
- 로그인된 사용자가 회원가입이나 로그인 페이지에 접근하면 메인 페이지로 redirection

---

### DRF User 모델 커스터마이징

**dj-rest-auth의 기본 회원가입 기능에 age와 같은 추가 필드를 포함시키기 위해 Serializer를 커스터마이징**

#### Django 모델 수정
- `accounts/models.py`의 User 모델에 age 필드를 추가하고 makemigrations 및 migrate를 실행

#### 커스텀 Serializer 생성
- dj-rest-auth의 RegisterSerializer를 상속받는 CustomRegisterSerializer를 생성하고 age 필드를 추가
- cleaned_data와 Save 메서드도 오버라이딩하여 age 데이터를 처리하도록 수정

#### Django 설정
- settings.py에서 dj-rest-auth가 이 커스텀 Serializer를 사용하도록 REST_AUTH 설정을 추가

#### Vue 폼 수정
- Vue의 회원가입 폼에도 age를 입력받는 `<input>` 필드를 추가

---

## 🎓 학습 완료!

**"지난 시간, DRF에 권한 설정을 추가하자 게시글 조회가 401 Unauthorized 오류와 함께 막혔습니다. 어떻게 해결할 수 있을까요?"**

### 해결 방법

**인증 과정 중에서 프론트엔드(Vue)의 역할을 알아봤습니다:**

1. **로그인을 통해 DRF로부터 토큰을 발급받아 Pinia에 저장했고**
2. **이후 모든 요청 헤더에 토큰을 담아 보내면서 권한 문제를 해결했습니다**

```javascript
// 1. 로그인 요청 후 응답받은 토큰을 state에 저장합니다
export const useAccountStore = defineStore('account', () => {
  const token = ref(null)
  
  const logIn = function(payload) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: payload
    })
      .then(res => {
        token.value = res.data.key
      })
      .catch(err => console.log(err))
  }
  
  return { signUp, logIn, token }
}, { persist: true })

// 2. 인증이 필요한 요청 시, 저장된 토큰을 헤더에 담아 보냅니다
axios({
  method: 'get',
  url: API_URL,
  headers: {
    Authorization: `Token ${accountStore.token}`
  }
})
```

---
