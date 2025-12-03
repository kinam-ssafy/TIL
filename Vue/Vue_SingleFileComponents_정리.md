# Vue Single File Components 교안 정리

## 📚 목차
1. Component
2. Single-File Components (SFC)
3. SFC 구성요소
4. SFC build tool
5. Vite
6. Vue Project
7. NPM
8. 모듈과 번들러
9. Vue Project 구조
10. Vue Component 활용
11. Virtual DOM
12. Composition API & Option API
13. Vue Style Guide
14. 참고사항

---

## 🎯 학습 목표

1. ✅ SFC의 개념과 `<template>`, `<script>`, `<style>` 구조를 안다
2. ✅ Vite와 NPM의 역할을 이해하고 프로젝트 개발에 활용한다
3. ✅ `npm create vue@latest` 명령어로 Vue 프로젝트를 생성한다
4. ✅ `package.json`과 `package-lock.json`의 차이점을 안다
5. ✅ 자식 컴포넌트를 부모 컴포넌트에 등록하고 사용할 수 있다
6. ✅ `<style scoped>`를 사용해 컴포넌트의 스타일 범위를 지정한다
7. ✅ Virtual DOM의 개념과 효율적인 DOM 업데이트 원리를 안다

---

## 🏠 학습 시작: 집 짓기 비유

애플리케이션을 하나의 집을 짓는 것에 비유해봅시다.

**모든 가구를 한 방에 넣는 것 vs. 각 방을 용도에 맞게 설계하는 것**
- 어느 쪽이 더 살기 좋을까요?

### SFC 방식의 장점

**SFC 방식은 구조, 로직, 디자인이 완벽하게 분리된 '방'을 제시합니다.**

1. **독립성**: 각 방의 인테리어(`<style scoped>`)가 서로를 침범하지 않습니다
2. **재사용성**: 잘 만든 방(컴포넌트)은 다른 집(프로젝트)에서도 그대로 쓸 수 있습니다
3. **생산성**: 최신 건축 도구(Vite) 덕분에 설계 변경이 즉시 집에 반영됩니다

**SFC 방식을 활용하여 체계적이고 효율적인 '집'을 짓는 방법을 학습해 봅시다.**

---

## 1️⃣ Component

### 정의

**Component**: 재사용 가능한 코드 블록

컴포넌트는 웹 페이지를 구성하는 재사용 가능한 UI 블록으로, 마치 **'레고 블록'** 처럼 독립적인 기능을 가집니다.

이 '레고 블록'들을 조립하여 페이지를 만들기 때문에:
- 코드의 재사용성이 높아지고
- 유지보수가 매우 쉬워집니다

---

### Component 특징

**UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음**

자연스럽게 애플리케이션은 **중첩된 Component의 트리 형태**로 구성됨

> **UI (User Interface)**: 사용자가 마주하는 화면의 시각적 디자인

```
<Root>
  ├── <Header>
  ├── <Main>
  │     ├── <Aside>
  │     └── <Articles> (x2)
  │           └── <Item> (x3)
  └── <Footer>
```

---

### Component 예시

**웹 서비스는 여러 개의 Component로 이루어져 있음**

예시: 음악 스트리밍 서비스
- Header 컴포넌트 (로고, 검색, 메뉴)
- Navigation 컴포넌트 (투데이, 차트, 최신앨범)
- Playlist 컴포넌트
- Player 컴포넌트 (재생 컨트롤)
- Sidebar 컴포넌트
- News 컴포넌트
- 등등...

각 컴포넌트는 독립적으로 작동하며 재사용 가능합니다.

---

## 2️⃣ Single-File Components (SFC)

### 정의

**Single-File Components (SFC)**: 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식 (`*.vue` 파일)

SFC는 하나의 `.vue` 파일 안에 컴포넌트의 **HTML, JavaScript, CSS** 코드를 모두 담는 Vue의 개발 방식입니다.

### SFC의 구조

- **`<template>`**: 화면 구조를 담당
- **`<script>`**: 로직을 담당
- **`<style>`**: 스타일을 담당

관련된 코드가 한곳에 모여 있어 컴포넌트 단위의 개발과 유지보수가 매우 편리하고 체계적으로 이루어집니다.

---

### SFC 파일 예시

**Vue SFC는 HTML, CSS, JavaScript를 단일 파일로 합친 것**

`<template>`, `<script>` 및 `<style>` 블록은 하나의 파일에서 컴포넌트의 뷰, 로직 및 스타일을 독립적으로 배치

**MyComponent.vue**
```vue
<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('Hello World!')
</script>

<style scoped>
.greeting {
  color: red;
}
</style>
```

**브라우저 렌더링 결과:**
```
Hello World!  (빨간색 텍스트)
```

---

## 3️⃣ SFC 구성요소

### SFC 구조

**각 `*.vue` 파일은 세 가지 유형의 최상위 언어 블록으로 구성됨**

```vue
<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('Hello World!')
</script>

<style scoped>
.greeting {
  color: red;
}
</style>
```

**작성 순서:**
- 언어 블록의 작성 순서는 상관 없으나
- 일반적으로 `template` → `script` → `style` 순서로 작성

---

### 1) `<template>` 블록

**각 `*.vue` 파일은 최상위 `<template>` 블록을 하나만 포함할 수 있음**

```vue
<template>
  <div class="greeting">{{ msg }}</div>
</template>
```

**역할:**
- 컴포넌트의 HTML 구조 정의
- Vue 템플릿 문법 사용 가능 ({{ }}, v-if, v-for 등)

---

### 2) `<script setup>` 블록

**각 `*.vue` 파일은 `<script setup>` 블록을 하나만 포함할 수 있음**

```vue
<script setup>
import { ref } from 'vue'

const msg = ref('Hello World!')
</script>
```

**역할:**
- 컴포넌트의 로직 정의
- 반응형 데이터 선언
- 메서드 정의
- 다른 컴포넌트 import

**특징:**
- `<script setup>`은 컴포넌트의 `setup()` 함수를 대체하는 문법
- 코드가 더 간결하고 가독성이 좋음

---

### 3) `<style scoped>` 블록

**각 `*.vue` 파일은 여러 `<style>` 태그를 포함할 수 있음**

```vue
<style scoped>
.greeting {
  color: red;
}
</style>
```

**`scoped` 속성:**
- 현재 컴포넌트에만 스타일 적용
- 다른 컴포넌트에 영향을 주지 않음
- 스타일 충돌 방지

**작동 방식:**
```vue
<!-- 소스 코드 -->
<div class="greeting">Hello</div>

<style scoped>
.greeting {
  color: red;
}
</style>
```

```html
<!-- 컴파일 후 -->
<div class="greeting" data-v-7ba5bd90>Hello</div>

<style>
.greeting[data-v-7ba5bd90] {
  color: red;
}
</style>
```

Vue는 고유한 속성(`data-v-*`)을 추가하여 스타일이 해당 컴포넌트에만 적용되도록 함

---

## 4️⃣ SFC build tool

### SFC를 사용하려면?

**브라우저는 `.vue` 파일을 직접 이해할 수 없음**

`.vue` 파일을 브라우저가 이해할 수 있는 JavaScript와 CSS로 변환하는 **빌드 과정**이 필요

### 빌드 도구의 역할

**빌드 도구 (Build Tool)**: 개발자가 작성한 코드를 브라우저가 실행할 수 있는 형태로 변환

**주요 기능:**
1. `.vue` 파일을 HTML, JavaScript, CSS로 변환
2. 최신 JavaScript 문법을 구형 브라우저에서도 동작하도록 변환
3. 코드 최적화 및 압축
4. 개발 서버 제공

---

## 5️⃣ Vite

### Vite란?

**Vite** (프랑스어로 '빠르다'는 뜻): 프론트엔드 개발 도구

**특징:**
- 매우 빠른 개발 서버 시작
- 빠른 Hot Module Replacement (HMR)
- 최적화된 빌드

### Vite의 역할

```
개발자 코드 (.vue 파일)
         ↓
    Vite (빌드)
         ↓
브라우저가 실행 가능한 코드
```

**개발 모드:**
- 파일 변경 시 즉시 브라우저에 반영 (HMR)
- 빠른 개발 서버

**프로덕션 모드:**
- 코드 최적화 및 압축
- 배포 가능한 파일 생성

---

### Vite 특징

#### 1) 빠른 콜드 스타트
전통적인 번들러는 모든 모듈을 번들링한 후 서버를 시작하지만, Vite는 **즉시 서버를 시작**

#### 2) HMR (Hot Module Replacement)
파일을 수정하면 전체 페이지를 새로고침하지 않고 **변경된 모듈만 교체**

#### 3) 최적화된 빌드
프로덕션 빌드 시 **Rollup을 사용**하여 최적화된 번들 생성

---

## 6️⃣ Vue Project

### Vue 프로젝트 생성

#### 1단계: 프로젝트 생성

```bash
npm create vue@latest
```

**실행 시 나타나는 옵션:**
```
✔ Project name: … my-vue-project
✔ Add TypeScript? … No / Yes
✔ Add JSX Support? … No / Yes
✔ Add Vue Router for Single Page Application development? … No / Yes
✔ Add Pinia for state management? … No / Yes
✔ Add Vitest for Unit Testing? … No / Yes
✔ Add an End-to-End Testing Solution? › No
✔ Add ESLint for code quality? … No / Yes
```

---

#### 2단계: 프로젝트 디렉토리 이동

```bash
cd my-vue-project
```

---

#### 3단계: 패키지 설치

```bash
npm install
```

**역할:**
- `package.json`에 명시된 모든 패키지를 설치
- `node_modules` 폴더가 생성됨

---

#### 4단계: 개발 서버 실행

```bash
npm run dev
```

**결과:**
```
VITE v5.0.0  ready in 500 ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
➜  press h + enter to show help
```

브라우저에서 `http://localhost:5173/` 접속

---

## 7️⃣ NPM

### NPM이란?

**NPM (Node Package Manager)**: Node.js의 기본 패키지 관리자

**역할:**
1. **패키지 설치**: 필요한 외부 라이브러리 설치
2. **패키지 관리**: 버전 관리 및 의존성 관리
3. **스크립트 실행**: `package.json`에 정의된 명령어 실행

---

### 주요 NPM 명령어

#### 1) `npm install` (또는 `npm i`)

**전체 패키지 설치:**
```bash
npm install
```

**특정 패키지 설치:**
```bash
npm install <패키지명>
```

**예시:**
```bash
npm install axios
npm install lodash
npm install -D vite  # 개발 의존성으로 설치
```

---

#### 2) `npm run <스크립트명>`

`package.json`의 `scripts` 섹션에 정의된 명령어 실행

**package.json 예시:**
```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

**사용 예시:**
```bash
npm run dev      # 개발 서버 시작
npm run build    # 프로덕션 빌드
npm run preview  # 빌드된 결과 미리보기
```

---

## 8️⃣ 모듈과 번들러

### 모듈 (Module)

**모듈**: 기능을 기준으로 분리한 각각의 JavaScript 파일

**예시:**
```
src/
  ├── utils.js       (모듈 1)
  ├── api.js         (모듈 2)
  └── components/
        ├── Header.vue  (모듈 3)
        └── Footer.vue  (모듈 4)
```

**모듈의 장점:**
- 코드 재사용성
- 유지보수 용이
- 네임스페이스 관리

---

### 모듈 시스템

#### ES6 모듈 문법

**내보내기 (Export):**
```javascript
// utils.js
export function add(a, b) {
  return a + b
}

export const PI = 3.14159
```

**가져오기 (Import):**
```javascript
// main.js
import { add, PI } from './utils.js'

console.log(add(2, 3))  // 5
console.log(PI)         // 3.14159
```

---

### 번들러 (Bundler)

**번들러**: 여러 모듈 파일들을 브라우저가 효율적으로 로드할 수 있도록 하나(또는 여러 개)의 파일로 묶어주는 도구

**번들러가 필요한 이유:**

**1) HTTP 요청 최소화**
```
Before: 100개의 파일 → 100번의 HTTP 요청
After:  1개의 번들 파일 → 1번의 HTTP 요청
```

**2) 의존성 관리**
- 모듈 간 의존성을 자동으로 해결
- 올바른 순서로 코드 실행

**3) 코드 최적화**
- 압축 (Minification)
- 트리 쉐이킹 (Tree Shaking) - 사용하지 않는 코드 제거

---

### Vite의 번들링 과정

**개발 모드:**
```
.vue 파일 → ESM(ES Modules) → 브라우저
```
- 번들링 없이 각 모듈을 개별적으로 제공
- 변경된 모듈만 다시 로드 (빠른 HMR)

**프로덕션 모드:**
```
.vue 파일 → Rollup 번들링 → 최적화된 번들 파일
```
- 모든 모듈을 하나의 최적화된 파일로 번들링
- 코드 압축, 트리 쉐이킹 적용

---

## 9️⃣ Vue Project 구조

### 기본 프로젝트 구조

```
my-vue-project/
├── node_modules/        # 설치된 패키지들
├── public/              # 정적 파일
│   └── favicon.ico
├── src/                 # 소스 코드
│   ├── assets/          # 이미지, 폰트 등
│   ├── components/      # 재사용 컴포넌트
│   ├── App.vue          # 루트 컴포넌트
│   └── main.js          # 진입점
├── .gitignore           # Git 제외 파일
├── index.html           # HTML 진입점
├── package.json         # 프로젝트 정보
├── package-lock.json    # 패키지 버전 잠금
├── README.md            # 프로젝트 설명
└── vite.config.js       # Vite 설정
```

---

### 주요 파일 설명

#### 1) `index.html`

**프로젝트의 진입점**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vite App</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>
```

**특징:**
- Vite는 `index.html`을 소스 코드의 일부로 취급
- `<div id="app"></div>`에 Vue 앱이 마운트됨

---

#### 2) `src/main.js`

**Vue 애플리케이션의 시작점**

```javascript
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

**역할:**
1. Vue 애플리케이션 인스턴스 생성
2. 루트 컴포넌트 (`App.vue`) 지정
3. DOM 요소 (`#app`)에 마운트

---

#### 3) `src/App.vue`

**최상위 루트 컴포넌트**

```vue
<template>
  <div id="app">
    <Header />
    <Main />
    <Footer />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Main from './components/Main.vue'
import Footer from './components/Footer.vue'
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
```

**특징:**
- 모든 컴포넌트를 감싸는 최상위 컴포넌트
- 전역 스타일 설정
- 레이아웃 구성

---

#### 4) `src/components/`

**재사용 가능한 컴포넌트를 저장하는 폴더**

```
components/
  ├── Header.vue
  ├── Main.vue
  ├── Footer.vue
  └── common/
        ├── Button.vue
        └── Input.vue
```

---

### 패키지 관리 파일

#### 1) `package.json`

**프로젝트의 메타데이터와 의존성을 정의**

```json
{
  "name": "my-vue-project",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.4.0"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.0",
    "vite": "^5.0.0"
  }
}
```

**주요 필드:**
- `name`: 프로젝트 이름
- `version`: 프로젝트 버전
- `scripts`: 실행 가능한 명령어
- `dependencies`: 프로덕션 의존성
- `devDependencies`: 개발 의존성

---

#### 2) `package-lock.json`

**실제 설치된 패키지의 정확한 버전 정보를 기록**

```json
{
  "name": "my-vue-project",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "my-vue-project",
      "version": "0.0.0",
      "dependencies": {
        "vue": "^3.4.0"
      }
    },
    "node_modules/vue": {
      "version": "3.4.15",
      "resolved": "https://registry.npmjs.org/vue/-/vue-3.4.15.tgz",
      "integrity": "sha512-..."
    }
  }
}
```

**역할:**
- 정확한 패키지 버전 보장
- 다른 환경에서도 동일한 버전 설치
- 의존성 트리 전체 기록

---

### `package.json` vs `package-lock.json`

| 구분 | package.json | package-lock.json |
|------|--------------|-------------------|
| **목적** | 의존성 정의 | 정확한 버전 잠금 |
| **버전 표기** | 범위 (`^3.4.0`) | 정확한 버전 (`3.4.15`) |
| **수정** | 직접 편집 가능 | 자동 생성/업데이트 |
| **공유** | 필수 (Git 포함) | 권장 (Git 포함) |

**버전 표기 예시:**
```json
{
  "dependencies": {
    "vue": "^3.4.0"  // 3.4.0 이상 4.0.0 미만
  }
}
```

---

#### 3) `node_modules/`

**실제 설치된 패키지 파일들이 저장되는 폴더**

**특징:**
- 매우 큰 용량 (수백 MB ~ 수 GB)
- Git에 포함하지 않음 (`.gitignore`에 추가)
- `npm install`로 언제든 재생성 가능

---

## 🔟 Vue Component 활용

### 컴포넌트 등록 및 사용

#### 1단계: 자식 컴포넌트 생성

**src/components/MyComponent.vue**
```vue
<template>
  <div>
    <h2>안녕하세요!</h2>
    <p>저는 재사용 가능한 컴포넌트입니다.</p>
  </div>
</template>

<script setup>
// 로직이 필요한 경우 여기에 작성
</script>

<style scoped>
h2 {
  color: blue;
}
</style>
```

---

#### 2단계: 부모 컴포넌트에서 import

**src/App.vue**
```vue
<template>
  <div id="app">
    <h1>메인 페이지</h1>
    <MyComponent />
    <MyComponent />
  </div>
</template>

<script setup>
import MyComponent from './components/MyComponent.vue'
</script>

<style scoped>
#app {
  padding: 20px;
}
</style>
```

**결과:**
```
메인 페이지
안녕하세요!
저는 재사용 가능한 컴포넌트입니다.
안녕하세요!
저는 재사용 가능한 컴포넌트입니다.
```

---

### 컴포넌트 명명 규칙

#### PascalCase (권장)
```javascript
import MyComponent from './components/MyComponent.vue'
```

```html
<MyComponent />
```

**장점:**
- HTML 태그와 구분 용이
- JSX와 일관성

---

#### kebab-case
```html
<my-component />
```

**사용 가능하지만 덜 권장됨**

---

### 컴포넌트 중첩 예시

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <Header />
    <Main>
      <Article />
      <Sidebar />
    </Main>
    <Footer />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Main from './components/Main.vue'
import Article from './components/Article.vue'
import Sidebar from './components/Sidebar.vue'
import Footer from './components/Footer.vue'
</script>
```

**컴포넌트 트리 구조:**
```
App
├── Header
├── Main
│   ├── Article
│   └── Sidebar
└── Footer
```

---

## 1️⃣1️⃣ Virtual DOM

### Virtual DOM이란?

**Virtual DOM**: 실제 DOM의 구조를 복사한 가상의 DOM을 메모리에 저장해두는 프로그래밍 개념

---

### 실제 DOM의 문제점

**직접 DOM 조작은 느리고 비효율적**

```javascript
// 비효율적인 예시
for (let i = 0; i < 1000; i++) {
  const div = document.createElement('div')
  div.textContent = `Item ${i}`
  document.body.appendChild(div)  // DOM 조작 1000번!
}
```

**문제점:**
- DOM 조작은 비용이 큼 (리플로우, 리페인트)
- 여러 번 변경하면 성능 저하

---

### Virtual DOM 작동 원리

```
1. 데이터 변경
   ↓
2. Virtual DOM에서 새로운 트리 생성
   ↓
3. 이전 Virtual DOM과 비교 (Diffing)
   ↓
4. 변경된 부분만 계산
   ↓
5. 실제 DOM에 한 번에 적용 (Patching)
```

---

### Virtual DOM의 장점

#### 1) 성능 최적화

**Before (직접 DOM 조작):**
```javascript
// 3번의 DOM 업데이트
element.style.color = 'red'     // DOM 업데이트 1
element.style.fontSize = '20px' // DOM 업데이트 2
element.textContent = 'Hello'   // DOM 업데이트 3
```

**After (Virtual DOM):**
```vue
<script setup>
import { ref } from 'vue'

const color = ref('red')
const fontSize = ref('20px')
const text = ref('Hello')

// 데이터만 변경
function updateAll() {
  color.value = 'blue'
  fontSize.value = '24px'
  text.value = 'Hi'
  // → Virtual DOM이 한 번에 실제 DOM 업데이트
}
</script>
```

---

#### 2) 배치 업데이트

**여러 변경사항을 모아서 한 번에 처리**

```javascript
// Vue가 자동으로 처리
count.value++        // 변경 1
count.value++        // 변경 2
count.value++        // 변경 3
// → 실제 DOM은 한 번만 업데이트됨
```

---

#### 3) 효율적인 Diffing 알고리즘

**변경된 부분만 정확히 찾아서 업데이트**

```vue
<template>
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </ul>
</template>
```

**배열에 항목 추가 시:**
- Virtual DOM이 변경 사항 계산
- 새로운 `<li>` 하나만 추가
- 기존 `<li>`는 재사용

---

### Virtual DOM 작동 예시

**초기 상태:**
```javascript
const items = ref([
  { id: 1, name: 'Apple' },
  { id: 2, name: 'Banana' }
])
```

**Virtual DOM:**
```
<ul>
  <li key="1">Apple</li>
  <li key="2">Banana</li>
</ul>
```

---

**항목 추가:**
```javascript
items.value.push({ id: 3, name: 'Cherry' })
```

**새로운 Virtual DOM:**
```
<ul>
  <li key="1">Apple</li>
  <li key="2">Banana</li>
  <li key="3">Cherry</li>  ← 새로 추가
</ul>
```

**Diffing 결과:**
- `<li key="1">`, `<li key="2">`: 변경 없음 (재사용)
- `<li key="3">`: 새로 추가됨

**실제 DOM 업데이트:**
- `<li key="3">` 하나만 추가

---

## 1️⃣2️⃣ Composition API & Option API

### Vue의 두 가지 API 스타일

#### 1) Options API (기존 방식)

```vue
<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  mounted() {
    console.log('컴포넌트 마운트됨')
  }
}
</script>
```

**특징:**
- 옵션 객체로 컴포넌트 정의
- `this`를 사용하여 데이터 접근
- 초보자에게 직관적

---

#### 2) Composition API (권장)

```vue
<script setup>
import { ref, onMounted } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}

onMounted(() => {
  console.log('컴포넌트 마운트됨')
})
</script>
```

**특징:**
- 함수 기반 API
- `this` 사용 안 함
- 더 유연하고 재사용 가능
- TypeScript 지원 우수

---

### Composition API vs Options API

| 특성 | Options API | Composition API |
|------|-------------|-----------------|
| **구조** | 옵션 기반 | 함수 기반 |
| **데이터 접근** | `this.count` | `count.value` |
| **코드 구조** | 옵션별 분리 | 기능별 그룹화 |
| **재사용성** | Mixins | Composables |
| **타입 지원** | 제한적 | 우수 |
| **학습 곡선** | 완만 | 조금 가파름 |

---

## 1️⃣3️⃣ Vue Style Guide

### Vue의 스타일 가이드 규칙

**Vue의 스타일 가이드는 우선순위에 따라 4가지 범주로 나뉨**

#### Priority A: Essential (필수)
**오류를 방지하는 데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수**

**예시:**
- 컴포넌트 이름에 항상 합성어 사용
- `v-for`에 `key` 사용
- `v-if`와 `v-for`를 같은 요소에 사용하지 않기

---

#### Priority B: Strongly Recommended (적극 권장)
**가독성 및 개발자 경험 향상**

**예시:**
- 컴포넌트 파일명은 PascalCase
- 단일 파일 컴포넌트 파일명 규칙

---

#### Priority C: Recommended (권장)
**일관성 보장**

**예시:**
- 컴포넌트/인스턴스 옵션 순서
- 요소 속성 순서

---

#### Priority D: Use with Caution (주의 필요)
**잠재적 위험 특성 고려**

**예시:**
- `v-if`/`v-for` 우선순위
- 암묵적 부모-자식 통신

---

**공식 문서:** https://vuejs.org/style-guide/

---

## 1️⃣4️⃣ 참고사항

### 1) Single Root Element

**Vue 2에서는 컴포넌트가 단일 루트 요소를 가져야 했음**

```vue
<!-- Vue 2: 에러 발생 -->
<template>
  <div>First</div>
  <div>Second</div>
</template>
```

**Vue 3에서는 다중 루트 요소 지원**

```vue
<!-- Vue 3: 정상 작동 -->
<template>
  <div>First</div>
  <div>Second</div>
</template>
```

**권장 사항:**
- 여전히 단일 루트 요소를 사용하는 것이 일반적
- 레이아웃 관리가 더 명확함

---

### 2) CSS Scoped

#### Scoped CSS 작동 방식

**소스 코드:**
```vue
<template>
  <div class="example">Hello</div>
</template>

<style scoped>
.example {
  color: red;
}
</style>
```

**컴파일 후:**
```html
<div class="example" data-v-f3f3eg9>Hello</div>
```

```css
.example[data-v-f3f3eg9] {
  color: red;
}
```

---

#### Scoped 스타일의 특징

**1) 자식 컴포넌트의 루트 요소에는 영향**

```vue
<!-- Parent.vue -->
<template>
  <Child class="parent-style" />
</template>

<style scoped>
.parent-style {
  color: red;  /* Child의 루트 요소에 적용됨 */
}
</style>
```

**이유:**
- 부모가 레이아웃 목적으로 자식의 루트 요소 스타일을 제어할 수 있어야 함

---

**2) Deep Selector**

자식 컴포넌트 내부 요소에 스타일 적용이 필요한 경우:

```vue
<style scoped>
/* :deep() 사용 */
:deep(.child-element) {
  color: blue;
}
</style>
```

---

**3) Slotted Selector**

슬롯 콘텐츠에 스타일 적용:

```vue
<style scoped>
:slotted(.slot-content) {
  font-weight: bold;
}
</style>
```

---

**4) Global Selector**

전역 스타일 정의:

```vue
<style scoped>
:global(.global-class) {
  margin: 0;
}
</style>
```

---

#### CSS Scoped를 적용한 이유

**Vue 공식 입장:**

Vue는 부모 컴포넌트가 자식 컴포넌트의 최상위 요소 스타일을 제어할 수 있어야 레이아웃(배치) 목적을 쉽게 달성할 수 있다고 판단했기 때문

**결과:**
- 자식 컴포넌트의 root element는 부모와 자식 모두의 scoped 스타일이 영향을 미칠 수 있음

**권장 사항:**
- 최상위 `App` 컴포넌트에서 레이아웃 스타일을 전역적으로 구성할 수 있지만
- 다른 모든 컴포넌트는 범위가 지정된 스타일을 사용하는 것을 권장

**참고:** https://vuejs.org/style-guide/rules-essential.html#use-component-scoped-styling

---

### 3) Scaffolding

#### 정의

**Scaffolding (스캐폴딩)**: 새로운 프로젝트나 모듈을 시작할 때, 초기 구조와 코드를 자동으로 생성하는 과정

**비유:**
스캐폴딩은 새 건물을 지을 때 세우는 뼈대처럼, 새로운 프로젝트를 시작할 때 필요한 기본적인 파일과 폴더 구조를 자동으로 생성해주는 기능입니다.

**예시:**
```bash
npm create vue@latest
```

이 명령어로 필요한 초기 파일, 코드가 자동으로 만들어집니다.

**장점:**
- 초기 설정 작업에 시간을 낭비하지 않음
- 곧바로 개발에 집중 가능
- 일관된 프로젝트 구조

---

### 4) 관심사항의 분리

**"HTML/CSS/JS를 한 파일에 혼합하는 게 괜찮을까?"**

**전통적인 방식:**
```
파일 타입에 따른 분리
├── index.html
├── style.css
└── script.js
```

**SFC 방식:**
```
사용 목적에 따른 분리
├── Header.vue    (Header 관련 HTML, CSS, JS)
├── Content.vue   (Content 관련 HTML, CSS, JS)
└── Footer.vue    (Footer 관련 HTML, CSS, JS)
```

---

**프론트엔드 앱의 사용 목적이 점점 더 복잡해짐에 따라:**
- 단순 파일 유형으로만 분리하게 될 경우
- 프로젝트의 목표를 달성하는 데 도움이 되지 않게 됨

**SFC의 철학:**
- 관련된 코드를 함께 배치
- 컴포넌트 단위로 관리
- 재사용과 유지보수 용이

---

### 5) 패키지 관리 주의사항

#### 1) `npm install`을 입력하는 위치

**항상 프로젝트 루트 디렉토리(프로젝트를 생성한 폴더)에서 실행**

```bash
my-vue-project/          ← 여기서 실행
├── node_modules/
├── src/
└── package.json
```

---

#### 2) `node_modules` 폴더 관리 주의

**필요할 때마다 `npm install`을 통해 재생성할 수 있으므로:**
- 직접 수정하거나
- Git으로 관리할 필요 없음

**.gitignore에 추가:**
```
node_modules/
```

---

#### 3) `package.json`과 `package-lock.json` 직접 편집 자제

**`npm install <패키지명>` 명령을 통해 자동 업데이트하는 것이 안전**

```bash
# 좋은 방법
npm install axios

# 나쁜 방법
# package.json을 직접 수정 후 npm install
```

---

#### 4) 문제가 발생했을 때 재설치 고려

**패키지 버전 충돌이나 이상 동작이 의심될 때:**

```bash
# 1. node_modules 폴더 삭제
rm -rf node_modules

# 2. package-lock.json 삭제 (선택사항)
rm package-lock.json

# 3. 재설치
npm install
```

---

## 📝 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **컴포넌트** | 재사용 가능한 독립적인 UI 조각 | `<Header />`, `<ArticleList />` |
| **SFC** | `.vue` 확장자를 가진 단일 파일 컴포넌트 | `<template>`, `<script>`, `<style>` |
| **Vite** | 빠른 속도의 프론트엔드 빌드 도구 | `npm run dev`로 개발 서버 실행 |
| **NPM** | JavaScript 패키지 관리자 및 저장소 | `npm install <package-name>` |
| **package.json** | 프로젝트 의존성 및 정보 명세 파일 | 패키지 목록, 버전 범위 기록 |
| **Virtual DOM** | 실제 DOM을 복사한 가상의 DOM | 효율적인 DOM 업데이트 |

---

## 📋 요약 정리

### Single-File Components (SFC)

Vue에서 사용하는 특별한 파일 형식(`*.vue`)으로, 컴포넌트 하나를 구성하는 HTML, JavaScript, CSS를 한 파일에 모두 담아 관리하는 방식

---

### SFC의 구조

- **`<template>`**: 컴포넌트의 HTML 구조를 정의하는 부분
- **`<script setup>`**: 컴포넌트의 반응형 데이터와 로직(JavaScript)을 작성하는 부분
- **`<style scoped>`**: 컴포넌트의 CSS를 작성하는 부분

---

### SFC 개발 환경

`.vue` 파일은 브라우저가 직접 이해할 수 없으므로 웹에서 실행 가능한 코드로 변환하는 **빌드(build) 과정**이 필요

**Vite:**
- Vue의 공식 빌드 도구
- 빠른 개발 서버와 최적화된 빌드 기능 제공

**NPM (Node Package Manager):**
- Vue, Vite 등 프로젝트에 필요한 외부 패키지를 설치하고 관리하는 도구

---

### 모듈과 번들러

**모듈:**
- 기능을 기준으로 분리한 각각의 JavaScript 파일

**번들러:**
- 여러 모듈 파일들을 브라우저가 효율적으로 로드할 수 있도록 하나(또는 여러 개)의 파일로 묶어주는 도구

---

### Vue 프로젝트 (1/2)

#### 프로젝트 생성
터미널에서 `npm create vue@latest` 명령어를 실행하여 프로젝트의 기본 구조(scaffolding)를 자동으로 생성

#### 패키지 관리
- **package.json**: 프로젝트의 이름, 버전 정보와 필요한 패키지들의 목록(의존성)을 기록하는 설계도
- **package-lock.json**: `package.json`을 바탕으로 실제로 설치된 패키지들의 정확한 버전 정보를 기록하여 다른 환경에서도 동일한 개발 환경을 보장
- **node_modules**: 설치된 모든 패키지 파일들이 실제로 저장되는 폴더

---

### Vue 프로젝트 (2/2)

#### 주요 구조
- **src/main.js**: Vue 앱 인스턴스를 생성하고 DOM에 마운트하는 프로젝트의 시작점
- **src/App.vue**: 모든 컴포넌트를 감싸는 최상위 루트 컴포넌트
- **src/components/**: 재사용할 자식 컴포넌트들을 저장하는 폴더

---

### 가상 DOM (Virtual DOM)

실제 DOM의 구조를 복사한 가상의 DOM을 메모리에 저장해두는 프로그래밍 개념

**작동 원리:**
1. 데이터가 변경되면 Vue는 실제 DOM을 직접 수정하는 대신
2. 가상 DOM에서 변경 사항을 먼저 계산
3. 그 후 계산된 최소한의 변경 사항만 실제 DOM에 딱 한 번 적용

**장점:**
- 불필요한 렌더링을 줄임
- 성능을 크게 향상

---

## 🏠 집 짓기 비유로 마무리

'집 짓기' 비유로 학습을 시작했습니다.

이제 우리는 SFC라는 '방'들을 조립하여 하나의 '집'을 완성하는 방법을 압니다.

**MyComponent.vue** (침실)
```vue
<template>
  <div>
    <h2>여기는 침실입니다.</h2>
  </div>
</template>
```

**App.vue** (거실)
```vue
<template>
  <h1>우리 집 거실</h1>
  <MyComponent />
</template>

<script setup>
import MyComponent from '@/components/MyComponent.vue'
</script>
```

---

## ✅ 확인 문제 정답

1. **d) `<component>`** - `.vue` 파일의 세 가지 주요 구성 요소가 아닌 것
2. **c) 컴포넌트의 로직과 데이터를 정의한다** - `<script setup>`에 대한 설명
3. **b) 해당 컴포넌트에만 스타일을 적용한다** - `<style scoped>` 속성의 역할
4. **b) 프론트엔드 빌드 도구** - Vite의 역할
5. **c) Vue 프로젝트의 기본 구조를 생성한다** - `npm create vue@latest` 명령어의 역할
6. **a) package.json** - 프로젝트의 의존성과 정보를 기록하는 파일
7. **b) package-lock.json** - 실제 설치된 패키지의 정확한 버전을 기록하는 파일
8. **c) main.js** - Vue 프로젝트의 시작점이 되는 파일
9. **d) App.vue** - 모든 컴포넌트를 포함하는 최상위 컴포넌트
10. **b) 성능 향상을 위해** - Virtual DOM을 사용하는 가장 큰 이유

---

## 🚀 실전 활용 팁

### 1. 컴포넌트 구조 예시

```
src/
├── components/
│   ├── common/           # 공통 컴포넌트
│   │   ├── Button.vue
│   │   ├── Input.vue
│   │   └── Modal.vue
│   ├── layout/           # 레이아웃 컴포넌트
│   │   ├── Header.vue
│   │   ├── Sidebar.vue
│   │   └── Footer.vue
│   └── features/         # 기능별 컴포넌트
│       ├── UserProfile.vue
│       └── ProductList.vue
├── App.vue
└── main.js
```

---

### 2. 효율적인 개발 워크플로우

```bash
# 1. 프로젝트 생성
npm create vue@latest

# 2. 의존성 설치
cd my-vue-project
npm install

# 3. 개발 서버 시작
npm run dev

# 4. 새 패키지 설치
npm install axios

# 5. 빌드
npm run build
```

---

### 3. Git 관리

**.gitignore 설정:**
```
# Dependencies
node_modules/

# Build output
dist/

# Local env files
.env.local
.env.*.local

# IDE
.vscode/
.idea/
```

---

## 🎓 학습 완료!

이제 Vue Single File Components의 핵심을 모두 학습했습니다:
- ✅ SFC의 구조와 작성 방법
- ✅ Vite를 사용한 프로젝트 개발
- ✅ NPM으로 패키지 관리
- ✅ 컴포넌트 기반 개발
- ✅ Virtual DOM의 효율성

이 지식을 바탕으로 체계적이고 유지보수하기 쉬운 Vue 애플리케이션을 만들 수 있습니다! 🎉
