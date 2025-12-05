# Vue Router

## 📚 목차
1. Routing
2. Vue Router
3. Basic Routing
4. Named Routes
5. Dynamic Route Matching
6. Nested Routes
7. Programmatic Navigation
8. Navigation Guard
9. 참고사항 (Lazy Loading Routes)

---

## 🎯 학습 목표

1. ✅ `RouterLink`와 `RouterView`를 사용해 기본 라우팅을 구현한다
2. ✅ 경로 대신 이름을 사용한 Named Routes로 페이지를 이동한다
3. ✅ 동적 라우팅을 설정하고 `useRoute`로 파라미터 값을 얻는다
4. ✅ `useRouter`의 `push` 메서드를 사용해 프로그래밍 방식으로 이동한다
5. ✅ `children` 속성을 사용하여 중첩된 라우트를 구성할 수 있다
6. ✅ 전역 가드 `beforeEach`를 사용해 라우팅을 제어할 수 있다
7. ✅ 컴포넌트 가드로 페이지를 떠나거나 업데이트할 때를 제어한다

---

## 🏠 학습 시작

**웹사이트에 Home과 About 페이지를 만들려고 합니다.**
**SPA(Single Page Application)에서는 어떻게 페이지를 나눌 수 있을까요?**

**Vue Router는 이 문제를 해결하는 공식 도구입니다.**

### Vue Router의 핵심 요소

1. **`<RouterLink>`**: 페이지 이동 링크를 만드는 컴포넌트
2. **`<RouterView>`**: 현재 주소에 맞는 컴포넌트가 그려질 위치

**SPA에서 페이지를 바꾸지 않고 링크를 설정하는 방법을 배워봅시다!**

---

## 1️⃣ Routing

### Routing이란?

**정의**: 네트워크에서 경로를 선택하는 프로세스

**라우팅**: 사용자가 접속한 URL 주소에 따라 적절한 페이지(컴포넌트)를 보여주는 기능

**역할:**
- `/home` 주소는 Home 컴포넌트로
- `/about` 주소는 About 컴포넌트로 연결

미리 정의된 경로에 따라 어떤 내용을 보여줄지 결정합니다.

---

### SSR에서의 Routing

**SSR (Server-Side Rendering):**
- 서버에서 완성된 HTML 페이지를 만들어 브라우저에 보내는 방식

**SSR에서 routing은 서버 측에서 수행:**

```
Client                Server
   │                    │
   │─── URL 요청 ──────→│
   │                    │
   │                 (서버가 HTML 생성)
   │                    │
   │←── 완성된 HTML ────│
```

**특징:**
- 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송
- 링크를 클릭하면 브라우저는 서버로부터 HTML 응답을 수신
- 새 HTML로 전체 페이지를 다시 로드

---

### CSR에서의 Routing

**CSR (Client-Side Rendering):**
- 서버는 뼈대만 주고 브라우저가 직접 페이지를 그리는 방식

**CSR에서의 routing은 클라이언트(브라우저)에서 수행:**

```
Client                Server
   │                    │
   │─── 최초 요청 ─────→│
   │←── HTML 뼈대 ──────│
   │                    │
   │─── Ajax 요청 ─────→│
   │←── JSON 데이터 ────│
   │                    │
 (브라우저에서 화면 렌더링)
```

**특징:**
- 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져옴
- 전체 페이지를 다시 로드하지 않음

---

### SPA에서 Routing이 없다면?

**SPA (Single Page Application):**
- 하나의 페이지 안에서 내용만 바뀌어 보여주는 웹앱

**문제점:**

1. **URL 변화 감지 불가**
   - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음

2. **상태 인식 불가**
   - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음

3. **새로고침 문제**
   - URL이 1개이기 때문에 새로 고침 시 처음 페이지로 되돌아감

4. **링크 공유 불가**
   - 링크를 공유할 시 첫 페이지만 공유 가능

5. **브라우저 기능 제한**
   - 브라우저의 뒤로 가기 기능을 사용할 수 없음

**해결책:**
페이지는 1개이지만, 주소에 따라 여러 컴포넌트를 새로 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 함

---

## 2️⃣ Vue Router

### Vue Router란?

**정의**: Vue 공식 라우터 (The official Router for Vue.js)

**Vue.js의 공식 라우팅 라이브러리로 Vue로 만든 SPA에서 페이지 이동 기능을 구현할 때 사용됩니다.**

### Vue Router의 핵심 컴포넌트

#### 1) `<RouterLink>`
- 페이지를 새로고침하지 않는 링크를 만듦
- HTML의 `<a>` 태그로 렌더링됨

#### 2) `<RouterView>`
- 현재 URL에 맞는 컴포넌트를 보여주는 위치

**어떤 URL 경로에 어떤 컴포넌트를 보여줄지 정의하기만 하면 Vue Router가 연결해줍니다.**

---

### 사전 준비 (1/2)

#### Vite로 프로젝트 생성 시 Router 추가

```bash
npm create vue@latest
```

**실행 시 나타나는 화면:**

```
✔ Project name: … vue-project
✔ Add TypeScript? … No / Yes
✔ Add JSX Support? … No / Yes
✔ Add Vue Router for Single Page Application development? … No / Yes  ← 선택!
✔ Add Pinia for state management? … No / Yes
✔ Add Vitest for Unit Testing? … No / Yes
✔ Add an End-to-End Testing Solution? › No
✔ Add ESLint for code quality? … No / Yes
✔ Add Prettier for code formatting? … No / Yes
```

**Vue Router 옵션을 Yes로 선택합니다!**

---

### 사전 준비 (2/2)

#### 서버 실행 후 Router로 인한 프로젝트 변화 확인

**프로젝트 생성 후 실행 단계:**

```bash
# 1. 프로젝트 폴더로 이동
cd vue-project

# 2. 패키지 설치
npm install

# 3. 서버 실행
npm run dev
```

**브라우저에서 확인:**
- `http://localhost:5173/` 접속
- Home과 About 링크에 따라 변경되는 URL과 새로 렌더링 되는 화면을 확인

---

### Vue 프로젝트 구조 변화

#### Router 추가로 인한 변화

**1. `App.vue` 코드 변화**

**2. `router` 폴더 신규 생성**
```
src/
  router/
    index.js  ← 라우터 설정 파일
```

**3. `views` 폴더 신규 생성**
```
src/
  views/
    HomeView.vue
    AboutView.vue
```

**전체 구조:**
```
vue-project/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── router/
│   │   └── index.js     ← 라우터 설정
│   ├── views/           ← 페이지 컴포넌트
│   │   ├── HomeView.vue
│   │   └── AboutView.vue
│   ├── App.vue
│   └── main.js
├── index.html
└── package.json
```

---

## 3️⃣ Basic Routing

### App.vue 코드 변화

#### 1) RouterLink

**페이지를 다시 로드하지 않고 URL을 변경하여 URL 생성 및 관련 로직을 처리**

HTML의 `<a>` 태그를 렌더링

**App.vue**
```vue
<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
```

**렌더링 결과 (브라우저 개발자 도구):**
```html
<nav>
  <a href="/" class="">Home</a>
  <a href="/about" class="">About</a>
</nav>
```

---

#### 2) RouterView

**현재 URL에 해당하는 컴포넌트를 표시**

URL이 변경되면 `<RouterView>`가 자동으로 해당 컴포넌트로 교체됨

**App.vue**
```vue
<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </header>

  <RouterView />  <!-- 현재 경로의 컴포넌트가 여기에 렌더링 -->
</template>
```

**동작:**
- `/` 경로: `HomeView.vue` 렌더링
- `/about` 경로: `AboutView.vue` 렌더링

---

### router/index.js 파일

**라우터의 경로와 컴포넌트를 매핑하는 설정 파일**

**router/index.js**
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
```

---

### router 객체 구조

```javascript
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [...]
})
```

| 속성 | 설명 |
|------|------|
| **history** | 브라우저 히스토리 모드 설정 |
| **routes** | 경로와 컴포넌트 매핑 배열 |

---

### routes 배열 구조

```javascript
routes: [
  {
    path: '/',           // URL 경로
    name: 'home',        // 라우트 이름
    component: HomeView  // 렌더링할 컴포넌트
  }
]
```

| 속성 | 설명 | 예시 |
|------|------|------|
| **path** | URL 경로 | `'/'`, `'/about'` |
| **name** | 라우트 이름 (선택) | `'home'`, `'about'` |
| **component** | 렌더링할 컴포넌트 | `HomeView` |

---

### views 폴더

**라우팅으로 렌더링될 페이지 컴포넌트들을 저장하는 폴더**

**HomeView.vue**
```vue
<template>
  <div class="home">
    <h1>This is a home page</h1>
  </div>
</template>

<script setup>
// 홈 페이지 로직
</script>
```

**AboutView.vue**
```vue
<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<script setup>
// About 페이지 로직
</script>
```

---

### components vs views

| 구분 | components/ | views/ |
|------|-------------|--------|
| **용도** | 재사용 가능한 컴포넌트 | 라우팅으로 표시되는 페이지 |
| **예시** | Button, Input, Card | HomeView, AboutView |
| **특징** | 작고 독립적 | 페이지 단위 구성 |

**⚠️ TIP:**
- `views/` 폴더의 컴포넌트는 일반적으로 `~View.vue` 형식으로 명명
- 페이지 역할을 하는 컴포넌트임을 명확히 표현

---

### Basic Routing 흐름 정리

```
1. 사용자가 URL 입력 또는 RouterLink 클릭
          ↓
2. Vue Router가 routes 배열에서 일치하는 경로 탐색
          ↓
3. 해당 경로의 component를 찾음
          ↓
4. RouterView 위치에 컴포넌트 렌더링
```

**예시:**

```
사용자가 "/about" 클릭
     ↓
Router가 routes에서 path: '/about' 찾기
     ↓
component: AboutView 확인
     ↓
<RouterView />에 AboutView 렌더링
```

---

## 4️⃣ Named Routes

### Named Routes란?

**정의**: 경로에 이름을 부여하여 이름으로 페이지를 연결하는 방식

### 기존 방식 (경로 사용)

**App.vue**
```vue
<template>
  <RouterLink to="/about">About</RouterLink>
</template>
```

**문제점:**
- URL 경로가 변경되면 모든 링크를 수정해야 함
- 긴 경로의 경우 오타 발생 가능

---

### Named Routes 방식 (이름 사용)

**router/index.js**
```javascript
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',      // 이름 지정
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',     // 이름 지정
      component: () => import('../views/AboutView.vue')
    }
  ]
})
```

---

**App.vue**
```vue
<template>
  <nav>
    <!-- 이름으로 참조 -->
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'about' }">About</RouterLink>
  </nav>

  <RouterView />
</template>
```

**중요:**
- `:to="{ name: 'home' }"` 형식 사용 (v-bind 필요)
- 객체 형태로 작성

---

### Named Routes의 장점

#### 1) 유지보수성 향상

**시나리오**: URL 경로를 `/about`에서 `/about-us`로 변경

**기존 방식 (경로 사용):**
```vue
<!-- 모든 파일에서 수정 필요 -->
<RouterLink to="/about">About</RouterLink>
<RouterLink to="/about">About</RouterLink>
<RouterLink to="/about">About</RouterLink>
```

**Named Routes 방식:**
```javascript
// router/index.js만 수정
{
  path: '/about-us',  // 경로만 변경
  name: 'about',      // 이름은 유지
  component: () => import('../views/AboutView.vue')
}
```

```vue
<!-- 다른 파일은 수정 불필요 -->
<RouterLink :to="{ name: 'about' }">About</RouterLink>
```

---

#### 2) 코드 가독성

```vue
<!-- 더 명확한 의도 표현 -->
<RouterLink :to="{ name: 'userProfile' }">프로필</RouterLink>

<!-- vs -->
<RouterLink to="/users/profile">프로필</RouterLink>
```

---

#### 3) 자동완성 지원

IDE에서 라우트 이름 자동완성이 가능하여 오타 방지

---

### Named Routes 사용 예시

**router/index.js**
```javascript
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/user/profile',
      name: 'userProfile',
      component: UserProfileView
    },
    {
      path: '/articles',
      name: 'articles',
      component: ArticlesView
    }
  ]
})
```

---

**App.vue**
```vue
<template>
  <nav>
    <RouterLink :to="{ name: 'home' }">홈</RouterLink>
    <RouterLink :to="{ name: 'about' }">소개</RouterLink>
    <RouterLink :to="{ name: 'userProfile' }">프로필</RouterLink>
    <RouterLink :to="{ name: 'articles' }">게시글</RouterLink>
  </nav>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
```

---

## 5️⃣ Dynamic Route Matching

### Dynamic Route Matching이란?

**정의**: URL의 일부를 변수(파라미터)로 사용하여 동적으로 라우트를 매칭하는 기능

**사용 예시:**
- `/users/1` - 1번 사용자 프로필
- `/users/2` - 2번 사용자 프로필
- `/users/100` - 100번 사용자 프로필

**같은 컴포넌트를 사용하지만, 다른 데이터를 표시**

---

### 동적 세그먼트 (Dynamic Segment)

**콜론(`:`)을 사용하여 경로의 일부를 변수로 지정**

**router/index.js**
```javascript
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/users/:id',  // :id가 동적 세그먼트
      name: 'user',
      component: UserView
    }
  ]
})
```

**매칭 예시:**

| URL | params |
|-----|--------|
| `/users/1` | `{ id: '1' }` |
| `/users/2` | `{ id: '2' }` |
| `/users/alice` | `{ id: 'alice' }` |

---

### useRoute() 함수

**현재 활성화된 라우트의 정보를 가져오는 함수**

**UserView.vue**
```vue
<template>
  <div>
    <h1>User {{ userId }}의 프로필</h1>
    <p>사용자 정보를 표시합니다.</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, watch } from 'vue'

const route = useRoute()
const userId = ref(route.params.id)

// 라우트 파라미터 변경 감지
watch(
  () => route.params.id,
  (newId) => {
    userId.value = newId
    console.log(`사용자 ID가 ${newId}로 변경되었습니다.`)
  }
)
</script>
```

---

### route 객체의 주요 속성

```javascript
const route = useRoute()

console.log(route.params)  // { id: '1' }
console.log(route.path)    // '/users/1'
console.log(route.name)    // 'user'
console.log(route.query)   // URL 쿼리 파라미터
```

| 속성 | 설명 | 예시 |
|------|------|------|
| **params** | 동적 세그먼트 값 | `{ id: '1' }` |
| **path** | 현재 경로 | `'/users/1'` |
| **name** | 라우트 이름 | `'user'` |
| **query** | 쿼리 파라미터 | `{ page: '2' }` |

---

### 여러 개의 동적 세그먼트

**router/index.js**
```javascript
const router = createRouter({
  routes: [
    {
      path: '/users/:id/posts/:postId',
      name: 'userPost',
      component: UserPostView
    }
  ]
})
```

**매칭 예시:**

| URL | params |
|-----|--------|
| `/users/1/posts/5` | `{ id: '1', postId: '5' }` |
| `/users/alice/posts/hello` | `{ id: 'alice', postId: 'hello' }` |

---

**UserPostView.vue**
```vue
<template>
  <div>
    <h1>User {{ userId }}의 Post {{ postId }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = route.params.id
const postId = route.params.postId
</script>
```

---

### Named Routes와 함께 사용

**params를 객체로 전달**

```vue
<template>
  <nav>
    <!-- 동적 세그먼트에 값 전달 -->
    <RouterLink :to="{ name: 'user', params: { id: 1 } }">
      User 1
    </RouterLink>
    <RouterLink :to="{ name: 'user', params: { id: 2 } }">
      User 2
    </RouterLink>
  </nav>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
```

---

### 실전 예시: 게시글 상세 페이지

**router/index.js**
```javascript
const router = createRouter({
  routes: [
    {
      path: '/articles',
      name: 'articles',
      component: ArticlesView
    },
    {
      path: '/articles/:id',
      name: 'articleDetail',
      component: ArticleDetailView
    }
  ]
})
```

---

**ArticlesView.vue** (게시글 목록)
```vue
<template>
  <div>
    <h1>게시글 목록</h1>
    <ul>
      <li v-for="article in articles" :key="article.id">
        <RouterLink :to="{ name: 'articleDetail', params: { id: article.id } }">
          {{ article.title }}
        </RouterLink>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const articles = ref([
  { id: 1, title: 'Vue Router 배우기' },
  { id: 2, title: 'Dynamic Routing 이해하기' },
  { id: 3, title: 'Navigation Guards 활용' }
])
</script>
```

---

**ArticleDetailView.vue** (게시글 상세)
```vue
<template>
  <div>
    <h1>게시글 {{ articleId }}</h1>
    <div v-if="article">
      <h2>{{ article.title }}</h2>
      <p>{{ article.content }}</p>
    </div>
    <RouterLink :to="{ name: 'articles' }">목록으로</RouterLink>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRoute, RouterLink } from 'vue-router'

const route = useRoute()
const articleId = ref(route.params.id)
const article = ref(null)

// 게시글 데이터 로드
const loadArticle = () => {
  // 실제로는 API 호출
  article.value = {
    id: articleId.value,
    title: `게시글 ${articleId.value} 제목`,
    content: '게시글 내용입니다.'
  }
}

// 초기 로드
loadArticle()

// 파라미터 변경 감지
watch(
  () => route.params.id,
  (newId) => {
    articleId.value = newId
    loadArticle()
  }
)
</script>
```

---

## 6️⃣ Nested Routes

### Nested Routes란?

**정의**: 라우트 안에 또 다른 라우트를 중첩하여 구성하는 방식

**사용 예시:**
- 사용자 프로필 페이지 안에 "정보", "게시글", "팔로워" 탭
- 대시보드 안에 여러 섹션

---

### 중첩 라우트 구조

```
/user/profile
├── /user/profile              (기본 화면)
├── /user/profile/info         (정보 탭)
├── /user/profile/posts        (게시글 탭)
└── /user/profile/followers    (팔로워 탭)
```

---

### children 속성 사용

**router/index.js**
```javascript
const router = createRouter({
  routes: [
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,
      children: [
        {
          // /user/:id/profile로 접근
          path: 'profile',
          name: 'userProfile',
          component: UserProfile
        },
        {
          // /user/:id/posts로 접근
          path: 'posts',
          name: 'userPosts',
          component: UserPosts
        }
      ]
    }
  ]
})
```

**중요:**
- 자식 경로의 `path`는 `/`로 시작하지 않음
- 부모 경로에 자동으로 연결됨

---

### 부모 컴포넌트에 RouterView 추가

**UserView.vue** (부모 컴포넌트)
```vue
<template>
  <div>
    <h1>User {{ userId }}</h1>
    
    <nav>
      <RouterLink :to="{ name: 'userProfile', params: { id: userId } }">
        프로필
      </RouterLink>
      <RouterLink :to="{ name: 'userPosts', params: { id: userId } }">
        게시글
      </RouterLink>
    </nav>

    <!-- 자식 라우트가 여기에 렌더링됨 -->
    <RouterView />
  </div>
</template>

<script setup>
import { useRoute, RouterLink, RouterView } from 'vue-router'

const route = useRoute()
const userId = route.params.id
</script>
```

---

### 자식 컴포넌트

**UserProfile.vue**
```vue
<template>
  <div>
    <h2>사용자 프로필</h2>
    <p>프로필 정보를 표시합니다.</p>
  </div>
</template>
```

**UserPosts.vue**
```vue
<template>
  <div>
    <h2>사용자 게시글</h2>
    <ul>
      <li>게시글 1</li>
      <li>게시글 2</li>
      <li>게시글 3</li>
    </ul>
  </div>
</template>
```

---

### 렌더링 구조

```
UserView (부모)
├── <h1>User 1</h1>
├── <nav>
│   ├── 프로필 링크
│   └── 게시글 링크
└── <RouterView>
    └── UserProfile 또는 UserPosts (자식)
```

---

### 실전 예시: 대시보드

**router/index.js**
```javascript
const router = createRouter({
  routes: [
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      children: [
        {
          path: '',  // /dashboard 기본 화면
          name: 'dashboardHome',
          component: DashboardHome
        },
        {
          path: 'stats',  // /dashboard/stats
          name: 'dashboardStats',
          component: DashboardStats
        },
        {
          path: 'settings',  // /dashboard/settings
          name: 'dashboardSettings',
          component: DashboardSettings
        }
      ]
    }
  ]
})
```

---

**DashboardView.vue**
```vue
<template>
  <div class="dashboard">
    <aside class="sidebar">
      <h2>대시보드</h2>
      <nav>
        <RouterLink :to="{ name: 'dashboardHome' }">
          홈
        </RouterLink>
        <RouterLink :to="{ name: 'dashboardStats' }">
          통계
        </RouterLink>
        <RouterLink :to="{ name: 'dashboardSettings' }">
          설정
        </RouterLink>
      </nav>
    </aside>

    <main class="content">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.dashboard {
  display: flex;
}

.sidebar {
  width: 200px;
  padding: 20px;
  background-color: #f5f5f5;
}

.content {
  flex: 1;
  padding: 20px;
}
</style>
```

---

### 중첩 라우트의 중요 포인트

**1. 부모 컴포넌트에 반드시 `<RouterView>` 필요**
```vue
<!-- 부모 컴포넌트 -->
<template>
  <div>
    <h1>부모 내용</h1>
    <RouterView />  <!-- 필수! -->
  </div>
</template>
```

---

**2. 자식 경로는 `/` 없이 작성**
```javascript
// ✅ 올바름
children: [
  { path: 'profile', component: Profile }
]

// ❌ 잘못됨
children: [
  { path: '/profile', component: Profile }
]
```

---

**3. 기본 자식 라우트 설정**
```javascript
children: [
  {
    path: '',  // 빈 문자열 = 부모 경로와 동일
    component: DefaultChild
  }
]
```

---

## 7️⃣ Programmatic Navigation

### Programmatic Navigation이란?

**정의**: `<RouterLink>`를 클릭하는 대신 JavaScript 코드로 페이지를 이동시키는 기능

**사용 시나리오:**
- 폼 제출 후 다른 페이지로 이동
- 로그인 성공 후 홈으로 이동
- 조건에 따라 다른 페이지로 이동

---

### useRouter() 함수

**라우터 인스턴스를 가져오는 함수**

**기본 사용법:**
```vue
<template>
  <button @click="goToHome">홈으로 이동</button>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToHome = () => {
  router.push({ name: 'home' })
}
</script>
```

---

### router.push()

**새로운 히스토리 항목을 추가하면서 페이지 이동**

**사용 방법:**

#### 1) 경로로 이동
```javascript
router.push('/about')
```

#### 2) 이름으로 이동
```javascript
router.push({ name: 'about' })
```

#### 3) params와 함께 이동
```javascript
router.push({ name: 'user', params: { id: 123 } })
```

#### 4) query와 함께 이동
```javascript
router.push({ name: 'articles', query: { page: 2 } })
// 결과: /articles?page=2
```

---

### router.replace()

**현재 히스토리를 교체하면서 페이지 이동**

**특징:**
- 뒤로 가기 버튼으로 이전 페이지로 돌아갈 수 없음
- 히스토리 스택에 새 항목을 추가하지 않음

```javascript
router.replace({ name: 'home' })
```

**사용 예시:**
- 로그인 페이지 → 홈 (로그인 페이지로 다시 돌아가지 못하게)
- 결제 완료 페이지 (뒤로 가기 방지)

---

### router.push() vs router.replace()

| 메서드 | 히스토리 | 뒤로 가기 | 사용 예시 |
|--------|----------|-----------|-----------|
| **push()** | 새 항목 추가 | 가능 | 일반적인 페이지 이동 |
| **replace()** | 현재 항목 교체 | 불가능 | 로그인 후, 결제 완료 후 |

---

### router.go()

**히스토리 스택에서 앞/뒤로 이동**

```javascript
// 한 단계 뒤로
router.go(-1)
// === router.back()

// 한 단계 앞으로
router.go(1)
// === router.forward()

// 3단계 앞으로
router.go(3)

// 범위를 벗어나면 이동 실패 (조용히 실패)
router.go(-100)
```

---

### 실전 예시 1: 로그인 후 이동

**LoginView.vue**
```vue
<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="사용자명" />
      <input v-model="password" type="password" placeholder="비밀번호" />
      <button type="submit">로그인</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')

const login = async () => {
  // 로그인 로직 (예시)
  if (username.value && password.value) {
    // 로그인 성공
    alert('로그인 성공!')
    
    // 홈으로 이동 (뒤로 가기로 로그인 페이지 못 돌아감)
    router.replace({ name: 'home' })
  } else {
    alert('사용자명과 비밀번호를 입력하세요.')
  }
}
</script>
```

---

### 실전 예시 2: 게시글 작성 후 이동

**ArticleCreateView.vue**
```vue
<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input v-model="title" placeholder="제목" />
      <textarea v-model="content" placeholder="내용"></textarea>
      <button type="submit">작성</button>
      <button type="button" @click="cancel">취소</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const title = ref('')
const content = ref('')

const createArticle = async () => {
  // 게시글 생성 로직
  const newArticle = {
    id: Date.now(),
    title: title.value,
    content: content.value
  }
  
  // 생성 완료 후 상세 페이지로 이동
  router.push({
    name: 'articleDetail',
    params: { id: newArticle.id }
  })
}

const cancel = () => {
  // 목록으로 돌아가기
  router.go(-1)  // 또는 router.back()
}
</script>
```

---

### 실전 예시 3: 조건부 이동

**DashboardView.vue**
```vue
<template>
  <div>
    <h1>대시보드</h1>
    <button @click="goToAppropriateRoute">다음 단계</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const userRole = 'admin'  // 예시 사용자 역할

const goToAppropriateRoute = () => {
  if (userRole === 'admin') {
    router.push({ name: 'adminPanel' })
  } else if (userRole === 'user') {
    router.push({ name: 'userProfile' })
  } else {
    router.push({ name: 'login' })
  }
}
</script>
```

---

### useRoute() vs useRouter()

| 함수 | 반환값 | 용도 | 예시 |
|------|--------|------|------|
| **useRoute()** | 현재 라우트 정보 | 읽기 전용 | `route.params.id` |
| **useRouter()** | 라우터 인스턴스 | 페이지 이동 | `router.push()` |

**함께 사용하는 예시:**
```vue
<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()   // 현재 정보 읽기
const router = useRouter()  // 페이지 이동

const userId = route.params.id  // 현재 사용자 ID
const goBack = () => router.go(-1)  // 뒤로 가기
</script>
```

---

## 8️⃣ Navigation Guard

### Navigation Guard란?

**정의**: 특정 URL로의 접근을 제어하고, 조건에 따라 다른 경로로 리다이렉트하거나 취소하는 기능

**주요 용도:**
- 사용자 인증 확인
- 권한 검사
- 페이지 이탈 확인
- 데이터 로딩 완료 대기

---

### Navigation Guard의 종류

```
1. Globally Guard (전역 가드)
   - beforeEach
   - beforeResolve
   - afterEach

2. Per-route Guard (라우트별 가드)
   - beforeEnter

3. In-component Guard (컴포넌트 가드)
   - onBeforeRouteEnter
   - onBeforeRouteUpdate
   - onBeforeRouteLeave
```

---

## 9️⃣ Globally Guard

### beforeEach

**모든 라우트 변경이 일어나기 직전에 실행되는 전역 가드**

**router/index.js**
```javascript
const router = createRouter({
  // routes 설정...
})

router.beforeEach((to, from) => {
  // 네비게이션 가드 로직
})

export default router
```

---

### beforeEach 매개변수

```javascript
router.beforeEach((to, from) => {
  // to: 이동할 라우트 객체
  // from: 현재 라우트 객체
})
```

| 매개변수 | 설명 | 예시 |
|----------|------|------|
| **to** | 이동할 라우트 | `to.name`, `to.params` |
| **from** | 현재 라우트 | `from.path` |

---

### beforeEach 반환값

```javascript
router.beforeEach((to, from) => {
  // 1. 이동 허용
  return true
  // 또는 아무것도 반환하지 않음
  
  // 2. 이동 취소
  return false
  
  // 3. 다른 위치로 리다이렉트
  return { name: 'login' }
  return '/login'
})
```

---

### 실전 예시 1: 로그인 확인

**router/index.js**
```javascript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/my-page',
      name: 'myPage',
      component: MyPageView,
      meta: { requiresAuth: true }  // 인증 필요 표시
    }
  ]
})

// 전역 가드 설정
router.beforeEach((to, from) => {
  // 로그인 상태 확인 (실제로는 Vuex나 Pinia 사용)
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'
  
  // 인증이 필요한 페이지인지 확인
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  
  if (requiresAuth && !isLoggedIn) {
    // 인증 필요한데 로그인 안 됨 → 로그인 페이지로
    alert('로그인이 필요합니다.')
    return { name: 'login' }
  }
  
  // 로그인 상태에서 로그인 페이지 접근 → 홈으로
  if (to.name === 'login' && isLoggedIn) {
    return { name: 'home' }
  }
  
  // 그 외의 경우 정상 진행
  return true
})

export default router
```

---

### 실전 예시 2: 권한 확인

**router/index.js**
```javascript
const router = createRouter({
  routes: [
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
      meta: {
        requiresAuth: true,
        requiresAdmin: true  // 관리자 권한 필요
      }
    }
  ]
})

router.beforeEach((to, from) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'
  const userRole = localStorage.getItem('userRole')
  
  // 인증 확인
  if (to.meta.requiresAuth && !isLoggedIn) {
    alert('로그인이 필요합니다.')
    return { name: 'login' }
  }
  
  // 관리자 권한 확인
  if (to.meta.requiresAdmin && userRole !== 'admin') {
    alert('관리자 권한이 필요합니다.')
    return { name: 'home' }
  }
  
  return true
})
```

---

### meta 필드 활용

**라우트에 추가 정보를 저장하는 필드**

```javascript
{
  path: '/admin',
  name: 'admin',
  component: AdminView,
  meta: {
    requiresAuth: true,
    requiresAdmin: true,
    title: '관리자 페이지',
    description: '관리자 전용 페이지입니다'
  }
}
```

**접근 방법:**
```javascript
router.beforeEach((to, from) => {
  console.log(to.meta.requiresAuth)    // true
  console.log(to.meta.title)           // '관리자 페이지'
})
```

---

## 🔟 Per-route Guard

### beforeEnter

**특정 라우트에만 적용되는 가드**

**router/index.js**
```javascript
const router = createRouter({
  routes: [
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
      beforeEnter: (to, from) => {
        // 이 라우트에만 적용되는 가드
        const isAdmin = localStorage.getItem('userRole') === 'admin'
        
        if (!isAdmin) {
          alert('관리자 권한이 필요합니다.')
          return { name: 'home' }
        }
        
        return true
      }
    }
  ]
})
```

---

### beforeEnter 배열로 사용

**여러 가드를 순차적으로 실행**

```javascript
// 재사용 가능한 가드 함수들
function checkAuth(to, from) {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true'
  if (!isLoggedIn) {
    return { name: 'login' }
  }
}

function checkAdmin(to, from) {
  const isAdmin = localStorage.getItem('userRole') === 'admin'
  if (!isAdmin) {
    return { name: 'home' }
  }
}

const router = createRouter({
  routes: [
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
      beforeEnter: [checkAuth, checkAdmin]  // 배열로 여러 가드 적용
    }
  ]
})
```

---

## 1️⃣1️⃣ In-component Guard

### 컴포넌트 가드란?

**컴포넌트 내에서 정의하는 가드**

**Composition API에서 사용 가능한 가드:**
- `onBeforeRouteLeave`
- `onBeforeRouteUpdate`

---

### onBeforeRouteLeave

**현재 페이지를 떠나기 전에 실행**

**사용 예시: 저장하지 않은 변경사항 확인**

```vue
<template>
  <div>
    <h1>게시글 작성</h1>
    <form>
      <input v-model="title" placeholder="제목" />
      <textarea v-model="content" placeholder="내용"></textarea>
      <button @click="save">저장</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { onBeforeRouteLeave } from 'vue-router'

const title = ref('')
const content = ref('')
const isSaved = ref(false)

const save = () => {
  // 저장 로직
  isSaved.value = true
  alert('저장되었습니다.')
}

// 페이지를 떠나기 전에 확인
onBeforeRouteLeave((to, from) => {
  // 내용이 있고 저장하지 않았다면
  if ((title.value || content.value) && !isSaved.value) {
    const answer = window.confirm(
      '저장하지 않은 내용이 있습니다. 정말 나가시겠습니까?'
    )
    
    // 취소를 선택하면 이동 취소
    if (!answer) {
      return false
    }
  }
  
  // 확인 또는 저장된 경우 이동 허용
  return true
})
</script>
```

---

### onBeforeRouteUpdate

**현재 라우트가 변경될 때 (같은 컴포넌트가 재사용될 때) 실행**

**사용 예시: 동적 파라미터 변경 감지**

```vue
<template>
  <div>
    <h1>User {{ userId }}의 프로필</h1>
    <div v-if="user">
      <p>이름: {{ user.name }}</p>
      <p>이메일: {{ user.email }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)
const user = ref(null)

// 사용자 데이터 로드
const loadUser = async (id) => {
  // API 호출 예시
  console.log(`Loading user ${id}...`)
  user.value = {
    name: `User ${id}`,
    email: `user${id}@example.com`
  }
}

// 초기 로드
loadUser(userId.value)

// 라우트 파라미터 변경 감지
onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
  loadUser(to.params.id)
  
  return true
})
</script>
```

---

### Navigation Guard 실행 순서

```
1. 전역 beforeEach
        ↓
2. 라우트 beforeEnter
        ↓
3. 컴포넌트 onBeforeRouteUpdate (재사용되는 경우)
        ↓
4. 전역 beforeResolve
        ↓
5. 네비게이션 확정
        ↓
6. 전역 afterEach
        ↓
7. DOM 업데이트
        ↓
8. 컴포넌트 onBeforeRouteLeave (이전 컴포넌트)
```

---

## 1️⃣2️⃣ 참고사항

### Lazy Loading Routes

**정의**: Vue 애플리케이션 첫 빌드 시 해당 컴포넌트를 로드하지 않고, 해당 경로를 처음으로 방문할 때 컴포넌트를 로드하는 것

**이유:**
- 빌드할 때 처음부터 모든 컴포넌트를 준비하면
- 컴포넌트의 크기에 따라 페이지 로드 시간이 길어질 수 있기 때문

---

### Lazy Loading 구현

**router/index.js**
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView  // 일반 import (즉시 로드)
    },
    {
      path: '/about',
      name: 'about',
      // Lazy Loading (동적 import)
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
```

---

### 일반 Import vs Lazy Loading

**일반 Import:**
```javascript
import HomeView from '../views/HomeView.vue'

{
  path: '/',
  component: HomeView
}
```
- 앱 시작 시 즉시 로드
- 번들 파일에 포함

**Lazy Loading:**
```javascript
{
  path: '/about',
  component: () => import('../views/AboutView.vue')
}
```
- `/about` 경로를 처음 방문할 때 로드
- 별도의 청크(chunk) 파일로 분리됨

---

### Lazy Loading의 장점

#### 1) 초기 로딩 속도 개선

**Before (모든 컴포넌트 즉시 로드):**
```
app.js (500KB)
├── HomeView
├── AboutView
├── UserView
├── AdminView
└── ...
```

**After (Lazy Loading):**
```
app.js (100KB)
└── HomeView

About.[hash].js (50KB)
User.[hash].js (80KB)
Admin.[hash].js (150KB)
```

---

#### 2) 네트워크 대역폭 절약

사용자가 방문하지 않는 페이지는 다운로드하지 않음

---

#### 3) 메모리 사용 최적화

필요한 컴포넌트만 메모리에 로드

---

### Chunk 이름 지정

**주석을 사용하여 청크 파일명 지정**

```javascript
{
  path: '/about',
  name: 'about',
  component: () => import(
    /* webpackChunkName: "about" */
    '../views/AboutView.vue'
  )
}
```

**생성되는 파일:**
- `about.[hash].js`

---

### 실전 권장 사항

**즉시 로드:**
- 홈 페이지
- 자주 방문하는 페이지
- 작은 컴포넌트

**Lazy Loading:**
- 관리자 페이지
- 설정 페이지
- 크고 복잡한 컴포넌트
- 드물게 방문하는 페이지

---

**예시:**
```javascript
const router = createRouter({
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView  // 즉시 로드
    },
    {
      path: '/articles',
      name: 'articles',
      component: ArticlesView  // 즉시 로드 (자주 방문)
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue')  // Lazy
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/SettingsView.vue')  // Lazy
    }
  ]
})
```

---

## 📝 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **Vue 라우터** | Vue의 공식 라우팅 라이브러리 | URL에 따라 다른 컴포넌트 표시 |
| **RouterLink** | 페이지 이동을 위한 링크 컴포넌트 | `<RouterLink to="/about">` |
| **RouterView** | 현재 경로의 컴포넌트를 렌더링 | `<RouterView />` |
| **이름 있는 라우트** | 경로 대신 이름으로 라우트를 연결 | `:to="{ name: 'home' }"` |
| **동적 라우팅** | URL 일부를 변수로 사용해 매칭 | `'/users/:id'` |
| **프로그래밍 방식 이동** | JS 코드로 페이지를 이동시키는 기능 | `router.push({ name: 'home' })` |
| **내비게이션 가드** | URL 접근 제어 및 리다이렉트 | `router.beforeEach((to, from))` |

---

## 📋 요약 정리

### 라우팅

**사용자가 접속한 URL 주소에 따라 적절한 페이지(컴포넌트)를 보여주는 과정**

---

### SPA(Single Page Application)에서의 라우팅

**SPA는 단일 페이지로 구성되므로:**
- 페이지 이동 시 새로고침 없이 화면을 동적으로 교체하기 위해
- 클라이언트 측 라우팅은 필수

---

### Vue Router

**Vue.js의 공식 라우팅 라이브러리로 SPA에서 페이지 이동 기능을 구현**

#### RouterLink
- 페이지를 새로고침하지 않고 URL을 변경하는 링크를 생성
- `<a>` 태그로 렌더링

#### RouterView
- 현재 URL 경로와 일치하는 컴포넌트를 렌더링하는 자리 표시자 역할

#### 라우터 설정 (router/index.js)
- 각 URL 경로(path)에 어떤 컴포넌트(component)를 보여줄지 정의하는 설정 파일

---

### 다양한 라우팅 기법 (1/2)

#### Named Routes
- 경로에 name을 부여하고 대신 이 이름을 사용해 라우트를 연결하는 방식
- `:to="{ name: 'routeName' }"`
- URL 경로가 변경되어도 링크 코드를 수정할 필요가 없어 유지보수에 유리

#### Dynamic Route Matching
- `/users/:id`와 같이 URL 경로의 일부를 변수(파라미터)로 사용하여 여러 URL을 하나의 컴포넌트에 연결
- 컴포넌트 내에서는 `useRoute()` 훅을 사용해 `route.params.id`와 같이 파라미터 값 가져오기 가능

---

### 다양한 라우팅 기법 (2/2)

#### Programmatic Navigation
- `<RouterLink>`를 클릭하는 대신 JavaScript 코드 내에서 페이지를 이동시키는 기능
- `useRouter()` 훅으로 라우터 인스턴스를 가져온 후 `router.push({ name: 'routeName' })`와 같은 메서드를 호출하여 사용

#### Nested Routes
- 라우트 설정에서 `children` 옵션을 사용하여 라우트를 중첩
- 부모 컴포넌트의 `<RouterView>` 내부에 자식 컴포넌트가 렌더링되어, 대시보드 같은 UI를 구성할 때 유용

---

### 내비게이션 가드 (Navigation Guards)

**특정 URL로의 이동을 허용하거나 취소하고 다른 경로로 리다이렉트하는 등 라우팅을 제어하는 기능**

**주로 사용자 인증 여부를 확인할 때 사용**

#### 전역 가드 (beforeEach)
- 모든 라우트 변경이 일어나기 직전에 실행되는 가드
- `router/index.js` 파일에 `router.beforeEach((to, from) => { ... })` 형태로 등록
- `to`는 이동할 라우트 객체, `from`은 현재 라우트 객체를 의미
- 콜백 함수 내에서 조건에 따라 `return { name: 'login' }`과 같이 다른 페이지로 리다이렉트시키거나
- `return false`로 이동 취소 가능

---

## ✅ 확인 문제 정답

1. **b) 라우팅 (Routing)** - 라우팅은 사용자가 요청한 URL에 따라 해당하는 화면(컴포넌트)으로 연결해주는 과정입니다.

2. **b) `<RouterLink />`** - `<RouterLink />`는 페이지를 다시 로드하지 않고 URL을 변경하여 SPA의 장점을 살립니다.

3. **a) `<RouterView />`** - `<RouterView />`는 현재 경로와 일치하는 컴포넌트를 표시하는 자리 표시자 역할을 합니다.

4. **c) 유지보수성 향상** - URL 경로가 변경되어도 링크 코드를 수정할 필요가 없어 유지보수에 매우 유리합니다.

5. **c) `:` (colon)** - `'/users/:id'`와 같이 콜론을 사용하여 경로의 일부를 동적 파라미터로 만들 수 있습니다.

6. **b) useRoute()** - `useRoute()`는 현재 활성화된 경로의 파라미터, 쿼리 등 정보가 담긴 객체를 반환합니다.

7. **b) useRouter()** - `useRouter()`는 라우터 인스턴스를 반환하며, `router.push()` 등으로 페이지를 이동시킵니다.

8. **d) router.replace()** - `replace`는 현재 히스토리 스택을 교체하므로 사용자가 뒤로 가기 버튼을 사용할 수 없습니다.

9. **c) children** - 부모 라우트 객체의 `children` 배열 안에 자식 라우트 객체들을 정의하여 중첩 구조를 만듭니다.

10. **c) 내비게이션 가드** - 내비게이션 가드는 라우트 이동 전후에 실행되어, 인증 확인 등 접근 제어 로직을 구현합니다.

11. **c) beforeEach** - `router.beforeEach`는 어떤 페이지로 이동하든 항상 가장 먼저 실행되는 전역 가드입니다.

12. **a) onBeforeRouteLeave** - 컴포넌트 내에서 정의하며 사용자가 페이지를 떠나는 것을 확인하거나 막을 때 사용합니다.

---

## 🎯 최종 정리

**웹사이트에 Home과 About 페이지를 만들려고 합니다.**
**SPA(Single Page Application)에서는 어떻게 페이지를 나눌 수 있을까요?**

### 1. URL 주소와 보여줄 컴포넌트를 짝지어 정의합니다.

```javascript
const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/about', name: 'about', component: AboutView }
]
```

### 2. RouterLink와 RouterView로 화면을 구성합니다.

```vue
<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
  </nav>
  <RouterView />
</template>
```

---

**핵심 포인트:**
1. **라우팅**: URL과 컴포넌트 연결
2. **RouterLink**: 페이지 이동 링크
3. **RouterView**: 컴포넌트 렌더링 위치
4. **Named Routes**: 경로 대신 이름으로 관리
5. **Dynamic Routing**: URL 파라미터 활용
6. **Nested Routes**: 중첩된 UI 구조
7. **Navigation Guard**: 접근 제어
8. **Lazy Loading**: 성능 최적화

