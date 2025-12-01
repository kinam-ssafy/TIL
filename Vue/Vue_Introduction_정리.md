# Vue Introduction 교안 정리

## 📚 목차
1. Frontend Development
2. Client-side frameworks
3. SPA (Single Page Application)
4. CSR (Client-Side Rendering)
5. Vue 개요
6. Component
7. Vue Tutorial
8. 참고사항 (ref 객체, SEO, CSR과 SSR)

---

## 1️⃣ Frontend Development

### 정의
- 웹사이트와 웹 애플리케이션의 **사용자 인터페이스(UI)**와 **사용자 경험(UX)**을 만들고 디자인하는 것
- HTML, CSS, JavaScript 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발

```
Client ←→ Frontend Framework ←→ Server
```

---

## 2️⃣ Client-side frameworks

### 정의
클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 **JavaScript 기반 프레임워크**

### 특징
- 웹사이트의 사용자 인터페이스(UI)를 효율적으로 만들기 위해 미리 짜놓은 코드의 뼈대
- 복잡한 웹 애플리케이션을 마치 레고 조립하듯 재사용 가능한 부품 단위로 쉽게 개발
- 대표적인 프레임워크: **Vue, React, Angular**

### 필요한 이유

#### 1) 단순히 무언가를 읽는 곳에서 → 무언가를 하는 곳으로 변화
- 사용자는 이제 웹에서 문서만을 읽는 것이 아닌 음악을 스트리밍하고 영화를 보고 지구 반대편 사람들과 텍스트 및 영상 채팅을 통해 즉시 통신
- 이처럼 현대적이고 복잡한 대화형 웹 사이트를 **"웹 애플리케이션(web applications)"**이라 부름
- JavaScript 기반의 Client-side frameworks가 등장하면서 매우 동적인 대화형 애플리케이션을 훨씬 더 쉽게 구축할 수 있게 됨

#### 2) 다루는 데이터가 많아짐
예: SNS에서 친구가 이름을 변경했다면?
- 페이지로 전환
- 친구 목록, 타임라인, 스토리 등 친구 이름이 출력되는 모든 곳이 함께 변경되어야 함
- 애플리케이션의 기본 데이터를 안정적으로 추적하고 업데이트(렌더링, 추가, 삭제 등) 하는 도구가 필요
- 애플리케이션의 상태가 변경될 때마다 UI가 일관성 있게 업데이트되어야 함

### Vanilla JS의 한계

**불필요한 코드의 반복**

```html
<label for="inputArea">Username:</label>
<input type="text" id="inputArea" name="inputArea">
<hr>

<h1>안녕하세요 <span id="username1"></span></h1>
<div><span id="username2"></span>님의 친구 목록</div>
<div><span id="username3"></span>님의 알림 목록</div>
<div><span id="username4"></span>님의 친구 요청 목록</div>
```

```javascript
const initialText = 'Unknown User';

const inputArea = document.querySelector('#inputArea');
const username1 = document.querySelector('#username1');
const username2 = document.querySelector('#username2');
const username3 = document.querySelector('#username3');
const username4 = document.querySelector('#username4');

username1.textContent = initialText;
username2.textContent = initialText;
username3.textContent = initialText;
username4.textContent = initialText;

inputArea.addEventListener('input', function(e) {
  username1.textContent = e.target.value;
  username2.textContent = e.target.value;
  username3.textContent = e.target.value;
  username4.textContent = e.target.value;
});
```

### Client-side frameworks의 필요성

1. **동적이고 반응적인 웹 애플리케이션 개발**
   - 실시간 데이터 업데이트

2. **코드 재사용성 증가**
   - 컴포넌트 기반 아키텍처
   - 모듈화된 코드 구조

3. **개발 생산성 향상**
   - 강력한 개발 도구 지원

---

## 3️⃣ SPA (Single Page Application)

### 정의
**단일 페이지에서 동작하는 웹 애플리케이션**

- 하나의 HTML 파일 위에서 JavaScript가 필요한 부분만 교체하여 '진짜' 페이지 이동 없이 동작
- 마치 하나의 무대에서 배우와 배경만 계속 바꾸는 연극과 같음
- 빠르고 부드러운 사용자 경험을 제공

### 작동 원리

1. **최초 로드 시** 애플리케이션에 필요한 주요 리소스를 다운로드

2. **페이지 갱신 시** 필요한 데이터만을 비동기적으로 전달받아 화면의 필요한 부분만 동적으로 갱신
   - AJAX와 같은 기술을 사용하여 필요한 데이터만 비동기적으로 로드
   - 페이지 전체를 다시 로드할 필요 없이 필요한 데이터만 서버로부터 가져와서 화면에 표시

3. **JavaScript를 사용**하여 클라이언트 측에서 동적으로 콘텐츠 생성하고 업데이트
   - CSR 방식

---

## 4️⃣ CSR (Client-Side Rendering)

### 정의
**클라이언트에서 콘텐츠 렌더링하는 방식**

- 일단 빈 집(HTML)에 들어간 뒤, 가구(JavaScript)를 배송받아 직접 조립하는 방식
- 브라우저는 거의 텅 빈 HTML과 JavaScript 파일을 받습니다
- 그 후 JavaScript가 실행되어 데이터를 요청하고 화면을 동적으로 완성합니다

### 작동 원리

1. 사용자가 웹사이트에 요청을 보냄
2. 서버는 최소한의 HTML과 JavaScript 파일을 클라이언트로 전송
3. 클라이언트는 HTML과 JavaScript를 다운로드 받음
4. 브라우저가 JavaScript를 실행하여 동적으로 페이지 콘텐츠를 생성
5. 필요한 데이터는 API를 통해 서버로부터 **비동기적**으로 가져옴

> **비동기**: 하나의 작업이 끝날 때까지 기다리지 않고 다른 작업을 실행

### CSR 작동 예시

**1단계: 사용자 요청 및 서버 응답**
```
브라우저 → 서버: 페이지 요청
서버 → 브라우저: 빈 HTML + JS 파일 전송
```

**2단계: 브라우저에서 JS 실행**
```html
<!-- 서버가 보낸 최소한의 HTML -->
<!DOCTYPE html>
<html>
  <head>
    <title>My App</title>
  </head>
  <body>
    <div id="app"></div>
    <script src="app.js"></script>
  </body>
</html>
```

**3단계: API 요청 및 렌더링**
```javascript
// app.js가 실행되며 데이터 요청
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    // 받은 데이터로 화면 구성
    document.getElementById('app').innerHTML = `
      <h1>${data.title}</h1>
      <p>${data.content}</p>
    `;
  });
```

### CSR의 장점
1. **빠른 페이지 전환**
   - 페이지 이동 시 새로고침 없이 필요한 부분만 갱신
2. **서버 부하 감소**
   - 서버는 데이터만 전송, 렌더링은 클라이언트에서 처리
3. **풍부한 상호작용**
   - JavaScript로 복잡한 UI/UX 구현 가능

### CSR의 단점
1. **느린 초기 로드**
   - 모든 JavaScript 파일을 다운로드하고 실행해야 함
2. **SEO(검색 엔진 최적화) 문제**
   - 초기 HTML이 비어있어 검색 엔진이 콘텐츠를 인식하기 어려움
3. **JavaScript 실행 전까지 빈 페이지**

---

## 5️⃣ Vue

### 정의
사용자 인터페이스를 구축하기 위한 **JavaScript 프레임워크**

### Vue의 핵심 기능

#### 1) 선언적 렌더링 (Declarative Rendering)
- JavaScript의 데이터(상태)를 기반으로 화면에 출력할 HTML을 템플릿 문법을 통해 선언적으로 작성
- "데이터가 바뀌면 화면은 이런 모습이어야 한다"고 선언하는 방식

#### 2) 반응성 (Reactivity)
- JavaScript 데이터(상태)가 변경되면 Vue가 이를 감지하여 화면(DOM)을 자동으로 업데이트
- 데이터가 바뀌면 화면이 '알아서' 바뀜
- 더 이상 번거로운 DOM 조작에 신경 쓸 필요가 없음

### Vue의 2가지 핵심 API 스타일

#### 1) Options API
```javascript
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
    console.log(`초기 카운트: ${this.count}`)
  }
}
```

#### 2) Composition API (권장)
```javascript
import { ref, onMounted } from 'vue'

export default {
  setup() {
    const count = ref(0)
    
    function increment() {
      count.value++
    }
    
    onMounted(() => {
      console.log(`초기 카운트: ${count.value}`)
    })
    
    return {
      count,
      increment
    }
  }
}
```

---

## 6️⃣ Component (컴포넌트)

### 정의
UI를 **독립적이고 재사용 가능한 조각**으로 나눈 코드 블록

### 특징
- Vue 앱은 컴포넌트들의 트리 구조로 구성됨
- 재사용성과 관리 효율성을 높이는 핵심 개념

### 컴포넌트 구조 예시
```
App (최상위 컴포넌트)
├── Header
│   ├── Logo
│   └── Navigation
├── Main
│   ├── Sidebar
│   └── Content
│       ├── Article
│       └── Comments
└── Footer
```

### 컴포넌트 예제
```javascript
// 버튼 카운터 컴포넌트
import { ref } from 'vue'

export default {
  setup() {
    const count = ref(0)
    return { count }
  },
  template: `
    <button @click="count++">
      카운트: {{ count }}
    </button>
  `
}
```

---

## 7️⃣ Vue Tutorial

### Vue Application 생성

#### 기본 구조
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Vue App</title>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
</head>
<body>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>

  <script>
    const { createApp, ref } = Vue;

    createApp({
      setup() {
        const message = ref('Hello Vue!');
        return { message };
      }
    }).mount('#app');
  </script>
</body>
</html>
```

#### 핵심 단계

**1단계: createApp()으로 Vue 앱 인스턴스 생성**
```javascript
const { createApp } = Vue;

const app = createApp({
  setup() {
    // 반응형 상태와 함수 정의
    return {
      // 템플릿에서 사용할 데이터와 메서드
    }
  }
});
```

**2단계: mount()로 특정 HTML 요소에 연결**
```javascript
app.mount('#app');
```

### 반응형 상태 (Reactive State)

#### ref() 함수
변화를 감지할 수 있는 **반응형 변수**를 선언

```javascript
import { ref } from 'vue'

const count = ref(0)
console.log(count.value) // 0

count.value++
console.log(count.value) // 1
```

**중요 규칙:**
- `ref()`로 만든 변수는 `.value` 속성을 가진 객체
- **JavaScript에서는** `.value`로 접근
- **템플릿에서는** `.value` 없이 변수 이름만으로 접근

#### 기본 예제
```html
<div id="app">
  <p>{{ message }}</p>
  <button @click="updateMessage">메시지 변경</button>
</div>

<script>
const { createApp, ref } = Vue;

createApp({
  setup() {
    const message = ref('안녕하세요!');
    
    function updateMessage() {
      message.value = '새로운 메시지!';  // .value로 접근
    }
    
    return {
      message,
      updateMessage
    };
  }
}).mount('#app');
</script>
```

### 템플릿 문법

#### 1) 콧수염 구문 (Mustache Syntax)
```html
<h1>{{ message }}</h1>
<p>{{ count + 1 }}</p>
<div>{{ isActive ? '활성' : '비활성' }}</div>
```

#### 2) v-on 디렉티브 (이벤트 처리)
```html
<!-- 전체 문법 -->
<button v-on:click="increment">증가</button>

<!-- 단축 문법 -->
<button @click="increment">증가</button>

<!-- 인라인 핸들러 -->
<button @click="count++">증가</button>
```

#### 전체 예제: 카운터 앱
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Counter App</title>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
</head>
<body>
  <div id="app">
    <h1>카운터: {{ count }}</h1>
    <button @click="increment">증가</button>
    <button @click="decrement">감소</button>
  </div>

  <script>
    const { createApp, ref } = Vue;

    createApp({
      setup() {
        const count = ref(0);
        
        function increment() {
          count.value++;
        }
        
        function decrement() {
          count.value--;
        }
        
        return {
          count,
          increment,
          decrement
        };
      }
    }).mount('#app');
  </script>
</body>
</html>
```

---

## 8️⃣ 참고사항

### ref 객체

#### ref 특징
```javascript
const count = ref(0)

// ref 객체는 .value 속성을 가짐
console.log(count)        // {value: 0}
console.log(count.value)  // 0
```

#### Ref Unwrap 주의사항

**템플릿에서의 자동 언래핑**
```html
<template>
  <!-- 템플릿에서는 .value 생략 가능 -->
  <p>{{ count }}</p>
</template>

<script>
const count = ref(0)
// JavaScript에서는 .value 필수
count.value++
</script>
```

**객체 내부에서의 unwrap**
```javascript
const object = { id: ref(0) }

// 객체 속성일 때는 자동 unwrap 안됨
console.log(object.id)        // {value: 0}
console.log(object.id.value)  // 0 (올바른 접근)
```

**reactive 객체 내에서의 unwrap**
```javascript
import { ref, reactive } from 'vue'

const count = ref(0)
const state = reactive({ count })

// reactive 내부에서는 자동 unwrap됨
console.log(state.count)  // 0 (.value 없이 접근 가능)
state.count++
console.log(count.value)  // 1 (원본도 변경됨)
```

### SEO (Search Engine Optimization)

#### 정의
**검색 엔진 최적화** - 검색 엔진에 내 서비스나 제품이 효율적으로 노출되도록 개선하는 과정

#### 검색 엔진의 동작 방식
- Google, Bing과 같은 검색 엔진은 웹상에 존재하는 가능한 모든 정보를 긁어 모으는 방식으로 동작
- 정보의 대상은 주로 **HTML에 작성된 내용**

#### SPA/CSR과 SEO 문제

**문제점:**
- SPA는 하나의 페이지 안에서 내용만 바뀌어 보여줌
- CSR은 서버가 뼈대만 주고 브라우저가 직접 페이지를 그리는 방식
- 초기 HTML이 비어있어 검색 엔진이 콘텐츠를 인식하기 어려움

**해결 방안:**
- 최근에는 SPA/CSR로 구성된 서비스의 비중이 증가하면서
- SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전 중

### CSR과 SSR

#### SSR (Server-Side Rendering)
- 서버에서 완성된 HTML을 만들어 클라이언트에 전송
- 초기 로딩 속도가 빠르고 SEO에 유리
- 서버 부하가 높음

#### CSR vs SSR
CSR과 SSR은 흑과 백이 아님:
- 애플리케이션의 목적, 규모, 성능 및 SEO 요구 사항에 따라 달라질 수 있음
- 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함

#### SSR을 지원하는 프레임워크
- **Vue의 Nuxt.js**
- **React의 Next.js**

---

## 📝 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **Vue** | 사용자 인터페이스를 구축하는 JS 프레임워크 | `<div id="app">` |
| **SPA** | 단일 페이지에서 동작하는 웹 앱 | 페이지 이동 시 새로고침 없음 |
| **CSR** | 클라이언트에서 페이지를 렌더링 | 빈 HTML을 받고 JS로 화면 구성 |
| **선언적 렌더링** | JS 상태 기반으로 HTML을 선언 | `<h1>{{ message }}</h1>` |
| **반응성** | 데이터 변경 시 DOM 자동 업데이트 | `count.value++` |
| **ref()** | 반응형 상태(데이터)를 선언하는 함수 | `const count = ref(0)` |
| **컴포넌트** | 재사용 가능한 독립적인 UI 조각 | `<Header />`, `<Article />` |

---

## 🎯 학습 목표 요약

1. ✅ SPA와 CSR의 개념과 현대 웹 개발에서의 역할을 설명한다
2. ✅ Vue의 핵심 기능인 선언적 렌더링과 반응성을 이해한다
3. ✅ `createApp`과 `mount`를 사용해 Vue 앱 인스턴스를 생성한다
4. ✅ `ref` 함수를 사용해 반응형 상태를 선언하고 사용할 수 있다
5. ✅ 콧수염 구문(`{{ }}`)을 사용해 데이터를 템플릿에 연결한다
6. ✅ `v-on` 디렉티브로 DOM 이벤트를 처리하고 상태를 변경한다
7. ✅ 컴포넌트 기반 아키텍처의 개념과 장점을 설명할 수 있다

---

## 💡 핵심 개념 비교

### 명령형 방식 (Vanilla JS) vs 선언형 방식 (Vue)

**명령형 (Vanilla JS):**
```javascript
// 1. 요소를 찾고
const element = document.querySelector('#message');
// 2. 내용을 직접 변경
element.textContent = '새로운 메시지';
```

**선언형 (Vue):**
```javascript
// 데이터만 변경하면 화면이 자동으로 갱신됨
const message = ref('기존 메시지');

function updateMessage() {
  message.value = '새로운 메시지!';  // 이것만으로 화면이 바뀜!
}
```

Vue는 `querySelector`로 요소를 찾아 `textContent`를 직접 바꾸는 명령형 방식에서,
`ref()`로 선언한 데이터만 바꾸면 화면이 저절로 갱신되는 선언형 방식으로 전환됩니다.

**더 이상 DOM을 조작하지 않고 데이터만 관리하면 되는, 더 효율적인 개발 방식입니다!**
