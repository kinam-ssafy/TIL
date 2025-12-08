# Vue State Management

## 📚 목차
1. State Management 개념
2. Vue 컴포넌트 구조
3. 상태 관리의 한계
4. Pinia (Vue 공식 상태 관리 라이브러리)
5. Pinia 구성요소
6. Pinia 설치 및 설정
7. Store 정의 및 활용
8. Local Storage (상태 지속성)
9. Pinia 활용 시점
10. 참고사항

---

## 🎯 학습 목표

1. ✅ Vue 컴포넌트의 단방향 데이터 흐름을 이해한다
2. ✅ Props와 Emit만으로 상태 관리 시 한계를 파악한다
3. ✅ Pinia가 제공하는 중앙 저장소의 개념을 이해한다
4. ✅ `defineStore()`로 store를 정의하고 활용할 수 있다
5. ✅ `state`, `getters`, `actions`의 역할과 차이를 안다
6. ✅ 컴포넌트에서 store의 상태와 메서드에 접근할 수 있다
7. ✅ `pinia-plugin-persistedstate`로 상태를 영구 저장한다

---

## 🏠 학습 시작

**"여러 컴포넌트가 같은 데이터를 공유해야 한다면 어떻게 해야 할까요?"**

### 문제 상황

부모 → 자식 → 손자 → 증손자...로 이어지는 깊은 컴포넌트 구조에서:
- Props로 데이터를 5단계 아래로 전달하려면?
- 자식 컴포넌트에서 부모의 상태를 변경하려면?

**Props와 Emit만으로는 관리가 너무 복잡해집니다!**

### 해결책: Pinia

**중앙 저장소(Store)에 공통 데이터를 보관하고, 모든 컴포넌트가 직접 접근!**

```
Props/Emit 방식:
Parent → Child → GrandChild → GreatGrandChild

Pinia 방식:
Store ←→ Parent
      ←→ Child
      ←→ GrandChild
      ←→ GreatGrandChild
```

**이제 Pinia를 통해 체계적인 상태 관리를 학습해봅시다!**

---

## 1️⃣ State Management

### State Management란?

**정의**: 여러 컴포넌트가 공유하는 상태(데이터)를 효율적으로 관리하는 것

**상태(State)**: 애플리케이션 구동에 필요한 기본 데이터

---

## 2️⃣ Vue 컴포넌트 구조

### Vue의 단방향 데이터 흐름

**상태(State), 뷰(View), 기능(Actions)은 '단방향 데이터 흐름'으로 상호작용**

```
┌─────────────┐
│   Actions   │ (기능)
│             │
└──────┬──────┘
       │
       ↓
┌─────────────┐
│    State    │ (상태)
│             │
└──────┬──────┘
       │
       ↓
┌─────────────┐
│    View     │ (뷰)
│             │
└─────────────┘
```

---

### 컴포넌트 구성요소

**1. 상태(State)**
- 앱 구동에 필요한 기본 데이터

**2. 뷰(View)**
- 상태를 선언적으로 매핑하여 시각화

**3. 기능(Actions)**
- 뷰에서 사용자 입력에 대해 반응적으로
- 상태를 변경할 수 있게 정의된 동작

---

### 코드 예시

```vue
<template>
  <!-- 뷰(View) -->
  <div>{{ count }}</div>
  <button @click="increment">증가</button>
</template>

<script setup>
import { ref } from 'vue'

// 상태(State)
const count = ref(0)

// 기능(Actions)
const increment = function() {
  count.value++
}
</script>
```

---

## 3️⃣ 상태 관리의 한계

### 단방향 데이터 흐름이 무너지는 시점

#### 1) 여러 뷰가 동일한 상태에 종속되는 경우

**문제:**
- 공유 상태를 공통 조상 컴포넌트로 '끌어올린' 다음
- Props로 여러 컴포넌트에 전달하는 방법

**한계:**
- 컴포넌트 계층 구조가 깊어질수록 비효율적
- 관리가 어려워짐

```
Parent (공통 데이터 보관)
  │
  ├─ props ─→ Child1
  │
  ├─ props ─→ Child2
  │              │
  │              └─ props ─→ GrandChild1
  │
  └─ props ─→ Child3
                 │
                 └─ props ─→ GrandChild2
                               │
                               └─ props ─→ GreatGrandChild
```

---

#### 2) 서로 다른 뷰의 기능이 동일한 상태를 변경시켜야 하는 경우

**문제:**
- Emit된 이벤트를 통해 상태의 여러 복사본을 변경 및 동기화

**한계:**
- 관리의 패턴이 깨지기 쉬움
- 유지 관리할 수 없는 코드가 됨

```
                Parent (상태 보관)
                  ↑
         ┌────────┼────────┐
      emit      emit      emit
         │        │        │
      Child1   Child2   Child3
         ↑        ↑        ↑
      emit      emit      emit
         │        │        │
   GrandChild GrandChild GrandChild
```

---

## 4️⃣ Pinia

### Pinia란?

**정의**: Vue의 공식 상태 관리 라이브러리

**Pinia는 여러 컴포넌트가 함께 사용해야 하는 공통 데이터를 중앙 저장소에서 통합 관리를 도와주는 Vue의 공식 상태 관리 라이브러리입니다.**

**Props나 Emit으로 복잡하게 데이터를 전달할 필요 없이, 어떤 컴포넌트든 이 중앙 저장소에 직접 접근하여 데이터를 읽거나 수정할 수 있습니다.**

---

### Pinia의 해결책

**각 컴포넌트의 공유 상태를 추출하여 전역에서 참조할 수 있는 저장소에서 관리**

```
┌──────────────────────┐
│   Pinia Store        │
│   (중앙 저장소)        │
│                      │
│   - state            │
│   - getters          │
│   - actions          │
└──────────────────────┘
         ↕
    ┌────┼────┐
    ↕    ↕    ↕
  Comp1 Comp2 Comp3
```

**컴포넌트 트리는 하나의 큰 View가 되고, 모든 컴포넌트는 트리 계층 구조에 관계 없이 상태에 접근하거나 기능을 사용할 수 있음**

---

## 5️⃣ Pinia 설치

### Vite 프로젝트 생성 시 Pinia 추가

```bash
npm create vue@latest
```

**실행 시 나타나는 옵션:**

```
✔ Project name: … vue-project
✔ Add TypeScript? … No / Yes
✔ Add JSX Support? … No / Yes
✔ Add Vue Router for Single Page Application development? … No / Yes
✔ Add Pinia for state management? … No / Yes  ← Yes 선택!
✔ Add Vitest for Unit Testing? … No / Yes
✔ Add an End-to-End Testing Solution? › No
✔ Add ESLint for code quality? … No / Yes
✔ Add Prettier for code formatting? … No / Yes
```

---

### 프로젝트 구조 변화

**Pinia 설치 후 생성되는 폴더:**

```
vue-project/
├── src/
│   ├── assets/
│   ├── components/
│   ├── stores/          ← 새로 생성!
│   │   └── counter.js   ← 예제 store
│   ├── App.vue
│   └── main.js
├── index.html
└── package.json
```

---

## 6️⃣ Pinia 구성요소

### Pinia의 핵심 구성 요소

1. **store** - 중앙 저장소
2. **state** - 반응형 상태(데이터)
3. **getters** - 계산된 값
4. **actions** - 상태 변경 메서드
5. **반환 값** - store에서 사용할 수 있도록 반환
6. **plugin** - 추가 기능 (선택사항)

---

## 7️⃣ Store 정의

### 1) Store

**정의**: 공통 데이터를 관리하는 중앙 저장소

모든 컴포넌트가 공유하는 상태, 기능이 작성됨

**stores/counter.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  
  function increment() {
    count.value++
  }
  
  return { count, doubleCount, increment }
})
```

**중요:**
- `defineStore()`의 반환 값(store)을 담는 변수의 이름은 **`use...Store` 패턴**을 사용하는 것을 권장합니다 (예: `useCounterStore`)
- `defineStore()`의 첫 번째 인자는 애플리케이션 전체에 걸쳐 사용하는 **store의 고유 ID**

---

### 2) State

**정의**: 중앙 저장소에 저장되는 반응형 상태(데이터)

**`ref()`와 같은 역할을 함**

해당 값(count)을 변경하면 이 데이터를 사용하고 있는 모든 컴포넌트의 화면은 알아서 업데이트됨

**stores/counter.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // state
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  
  function increment() {
    count.value++
  }
  
  return { count, doubleCount, increment }
})
```

---

### 3) Getters

**정의**: State를 기반으로 계산된 값

**`computed()`와 같은 역할을 함**

Getters는 State 값을 읽기만 하고 변경하지 않으며, State가 바뀔 때만 재계산됨

**stores/counter.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  
  // getters
  const doubleCount = computed(() => count.value * 2)
  
  function increment() {
    count.value++
  }
  
  return { count, doubleCount, increment }
})
```

---

### 4) Actions

**정의**: State를 변경하는 메서드

**`function()`으로 정의함**

Actions는 비동기 로직도 포함 가능

**stores/counter.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  
  // actions
  function increment() {
    count.value++
  }
  
  return { count, doubleCount, increment }
})
```

---

### 5) 반환 값 (return)

**정의**: Store에서 사용할 수 있도록 state, getters, actions를 반환

**stores/counter.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  
  function increment() {
    count.value++
  }
  
  // 반환 값
  return {
    count,        // state
    doubleCount,  // getters
    increment     // actions
  }
})
```

**중요**: 반환하지 않은 값은 컴포넌트에서 사용할 수 없음

---

## 8️⃣ Store 활용

### 컴포넌트에서 Store 사용하기

#### 1단계: Store import 및 인스턴스 생성

**App.vue**
```vue
<template>
  <div>
    <p>{{ store.count }}</p>
    <p>{{ store.doubleCount }}</p>
    <button @click="store.increment()">증가</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
```

---

#### 2단계: State 접근

**State에 직접 접근 가능**

```vue
<template>
  <p>{{ store.count }}</p>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
```

---

#### 3단계: Getters 접근

**Getters에 직접 접근 가능**

```vue
<template>
  <p>{{ store.doubleCount }}</p>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
```

---

#### 4단계: Actions 호출

**Actions는 메서드처럼 호출**

```vue
<template>
  <button @click="store.increment()">증가</button>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
```

---

### storeToRefs()

**문제**: 구조 분해 할당 시 반응성이 사라짐

```vue
<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

// ❌ 반응성 상실
const { count, doubleCount } = store

// count와 doubleCount는 더 이상 반응형이 아님
</script>
```

---

**해결**: `storeToRefs()` 사용

```vue
<template>
  <div>
    <p>{{ count }}</p>
    <p>{{ doubleCount }}</p>
    <button @click="store.increment()">증가</button>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

// ✅ 반응성 유지
const { count, doubleCount } = storeToRefs(store)

// actions는 반응성이 필요 없으므로 일반 구조 분해
const { increment } = store
</script>
```

**중요:**
- `storeToRefs()`는 **state와 getters만** 반응성을 유지
- **actions는** 일반 구조 분해 할당 사용

---

### 완전한 예시

**stores/counter.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // state
  const count = ref(0)
  
  // getters
  const doubleCount = computed(() => count.value * 2)
  const isEven = computed(() => count.value % 2 === 0)
  
  // actions
  function increment() {
    count.value++
  }
  
  function decrement() {
    count.value--
  }
  
  function reset() {
    count.value = 0
  }
  
  return {
    count,
    doubleCount,
    isEven,
    increment,
    decrement,
    reset
  }
})
```

---

**App.vue**
```vue
<template>
  <div>
    <h1>Counter: {{ count }}</h1>
    <p>Double: {{ doubleCount }}</p>
    <p>{{ isEven ? '짝수' : '홀수' }}</p>
    
    <button @click="increment">+1</button>
    <button @click="decrement">-1</button>
    <button @click="reset">Reset</button>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

// state와 getters는 storeToRefs로 반응성 유지
const { count, doubleCount, isEven } = storeToRefs(store)

// actions는 일반 구조 분해
const { increment, decrement, reset } = store
</script>
```

---

## 9️⃣ Local Storage (상태 지속성)

### 문제 상황

**Pinia의 상태는 기본적으로 메모리에 저장**

→ 페이지를 새로고침하면 **모든 상태가 초기화됨**

```
사용자가 카운트를 10까지 증가
   ↓
페이지 새로고침 (F5)
   ↓
카운트가 0으로 초기화 😢
```

---

### 해결책: pinia-plugin-persistedstate

**Pinia의 상태를 브라우저의 Local Storage에 자동으로 저장하여 새로고침해도 데이터가 유지되도록 하는 플러그인**

---

### Local Storage란?

**정의**: 브라우저가 닫혔다 열어도 데이터가 사라지지 않는 영구적인 웹 스토리지 객체

**특징:**
- 도메인별로 데이터 저장
- 용량: 약 5~10MB
- 문자열만 저장 가능 (객체는 JSON.stringify 필요)
- 개발자 도구 → Application → Local Storage에서 확인 가능

---

### pinia-plugin-persistedstate 설치

#### 1단계: 패키지 설치

```bash
npm install pinia-plugin-persistedstate
```

---

#### 2단계: main.js에 플러그인 등록

**src/main.js**
```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

// Pinia에 플러그인 등록
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.mount('#app')
```

---

#### 3단계: Store에 persist 옵션 추가

**stores/counter.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore(
  'counter',
  () => {
    const count = ref(0)
    const doubleCount = computed(() => count.value * 2)
    
    function increment() {
      count.value++
    }
    
    return { count, doubleCount, increment }
  },
  {
    persist: true  // ← Local Storage에 저장!
  }
)
```

**중요**: `defineStore()`의 **세 번째 인자**로 `{ persist: true }` 옵션 전달

---

### 작동 확인

#### 1) 개발자 도구에서 확인

**브라우저 개발자 도구 → Application → Local Storage → http://localhost:5173**

```
Key: counter
Value: {"count":5}
```

---

#### 2) 동작 테스트

```
1. 카운터를 5까지 증가
2. 페이지 새로고침 (F5)
3. 카운터가 여전히 5로 유지됨! ✅
```

---

### persist 옵션 커스터마이징

**기본 설정 외에 다양한 옵션 지정 가능**

```javascript
export const useCounterStore = defineStore(
  'counter',
  () => {
    const count = ref(0)
    const name = ref('Alice')
    
    return { count, name }
  },
  {
    persist: {
      // 저장할 데이터 선택
      paths: ['count'],  // name은 저장 안 함
      
      // 저장 위치 변경 (기본: localStorage)
      storage: sessionStorage,  // 브라우저 닫으면 삭제됨
      
      // 저장 키 이름 변경
      key: 'my-custom-counter'
    }
  }
)
```

---

### 실전 예시: Todo Store

**stores/todo.js**
```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useTodoStore = defineStore(
  'todo',
  () => {
    const todos = ref([])
    
    const doneTodosCount = computed(() => {
      return todos.value.filter(todo => todo.isDone).length
    })
    
    function addTodo(text) {
      todos.value.push({
        id: Date.now(),
        text,
        isDone: false
      })
    }
    
    function deleteTodo(id) {
      const index = todos.value.findIndex(todo => todo.id === id)
      if (index !== -1) {
        todos.value.splice(index, 1)
      }
    }
    
    function updateTodo(id) {
      const todo = todos.value.find(todo => todo.id === id)
      if (todo) {
        todo.isDone = !todo.isDone
      }
    }
    
    return {
      todos,
      doneTodosCount,
      addTodo,
      deleteTodo,
      updateTodo
    }
  },
  {
    persist: true  // Local Storage에 저장
  }
)
```

---

**TodoApp.vue**
```vue
<template>
  <div>
    <h1>Todo List</h1>
    <p>완료된 Todo 개수: {{ doneTodosCount }}</p>
    
    <form @submit.prevent="handleAddTodo">
      <input v-model="newTodo" placeholder="할 일을 입력하세요" />
      <button type="submit">추가</button>
    </form>
    
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input
          type="checkbox"
          :checked="todo.isDone"
          @change="updateTodo(todo.id)"
        />
        <span :class="{ done: todo.isDone }">{{ todo.text }}</span>
        <button @click="deleteTodo(todo.id)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useTodoStore } from '@/stores/todo'

const store = useTodoStore()
const { todos, doneTodosCount } = storeToRefs(store)
const { addTodo, deleteTodo, updateTodo } = store

const newTodo = ref('')

function handleAddTodo() {
  if (newTodo.value.trim()) {
    addTodo(newTodo.value)
    newTodo.value = ''
  }
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
  color: gray;
}
</style>
```

---

## 🔟 Pinia 활용 시점

### 이제 모든 데이터를 Store에서 관리해야 할까?

**아닙니다!**

Pinia를 사용한다고 해서 모든 데이터를 state에 넣어야 하는 것은 아님

**컴포넌트 내부에서만 사용하는 데이터까지 Pinia로 관리하면 코드가 불필요하게 복잡해짐**

**Pass Props, Emit Event를 함께 사용하여 애플리케이션을 구성해야 함**

---

### Props vs Pinia

#### Props 사용 (권장)

**간단한 부모-자식 데이터 전달**

```vue
<!-- Parent.vue -->
<template>
  <Child :message="message" />
</template>

<script setup>
import { ref } from 'vue'
import Child from './Child.vue'

const message = ref('Hello')
</script>
```

**장점:**
- 간단하고 직관적
- 데이터 흐름이 명확
- 디버깅 용이

---

#### Pinia 사용 (권장)

**여러 컴포넌트가 공유하는 데이터**

```javascript
// stores/user.js
export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const isLoggedIn = computed(() => !!user.value)
  
  function login(userData) {
    user.value = userData
  }
  
  function logout() {
    user.value = null
  }
  
  return { user, isLoggedIn, login, logout }
})
```

**장점:**
- 어디서든 접근 가능
- 중복 코드 감소
- 데이터 일관성 유지

---

### Pinia를 사용하면 좋은 경우

#### 1) 여러 컴포넌트가 공유하는 데이터

```
사용자 정보, 인증 상태, 테마 설정 등
```

**예시:**
```javascript
// stores/user.js
const user = ref({
  id: 1,
  name: 'Alice',
  email: 'alice@example.com'
})
```

**사용 컴포넌트:**
- Header (사용자 이름 표시)
- Profile (프로필 정보)
- Settings (설정 페이지)

---

#### 2) 깊은 컴포넌트 계층 구조

```
Parent → Child → GrandChild → GreatGrandChild
```

**Props 드릴링 방지**

---

#### 3) 여러 페이지에서 필요한 데이터

```
장바구니, 알림, 검색 히스토리 등
```

---

#### 4) 복잡한 상태 관리가 필요한 경우

```
Todo 목록, 게시글 관리, 쇼핑 카트 등
```

---

### Pinia를 사용하지 않아도 되는 경우

#### 1) 단순한 부모-자식 관계

```vue
<!-- Props 사용 -->
<Child :message="message" />
```

---

#### 2) 컴포넌트 내부에서만 사용하는 데이터

```vue
<script setup>
import { ref } from 'vue'

// 이 데이터는 Pinia가 필요 없음
const isModalOpen = ref(false)
const searchQuery = ref('')
</script>
```

---

#### 3) 폼 입력 데이터

```vue
<script setup>
import { ref } from 'vue'

// 제출 전까지는 로컬 상태로 관리
const email = ref('')
const password = ref('')

function handleSubmit() {
  // 제출 시에만 store에 저장
  userStore.login({ email: email.value, password: password.value })
}
</script>
```

---

### 판단 기준

**"이 데이터를 여러 컴포넌트에서 사용하나요?"**

| 질문 | Pinia | Props/Local |
|------|-------|-------------|
| 한 컴포넌트에서만 사용? | ❌ | ✅ |
| 부모-자식 관계만? | ❌ | ✅ |
| 여러 컴포넌트에서 공유? | ✅ | ❌ |
| 깊은 계층 구조? | ✅ | ❌ |
| 페이지 이동 후에도 유지? | ✅ | ❌ |

---

### 중대형 규모의 SPA

**Pinia는 공유된 상태를 관리하는 데 유용하지만, 구조적인 개념을 이해하고 시작하는 비용이 큼**

**애플리케이션이 단순하다면 Pinia가 없는 것이 더 효율적일 수 있음**

**그러나 중대형 규모의 SPA를 구축하는 경우 Pinia는 자연스럽게 선택할 수 있는 단계가 오게 됨**

**결과적으로 적절한 상황에서 활용했을 때 Pinia 효용을 극대화할 수 있음**

---

## 1️⃣1️⃣ 참고사항

### Pinia vs Vuex

**Vuex**: Vue 2 시대의 공식 상태 관리 라이브러리

**Pinia**: Vue 3의 공식 상태 관리 라이브러리 (권장)

| 특징 | Vuex | Pinia |
|------|------|-------|
| **문법** | Options API 스타일 | Composition API 스타일 |
| **mutations** | 필요 | 없음 (actions만 사용) |
| **모듈 구조** | 복잡 | 간단 |
| **TypeScript** | 제한적 | 우수 |
| **크기** | 큼 | 작음 |

**결론**: Vue 3 프로젝트에서는 **Pinia 사용을 권장**

---

### Store 네이밍 컨벤션

**권장 패턴:**

```javascript
// ✅ 좋은 예
export const useUserStore = defineStore('user', ...)
export const useTodoStore = defineStore('todo', ...)
export const useCartStore = defineStore('cart', ...)

// ❌ 나쁜 예
export const userStore = defineStore('user', ...)
export const UserStore = defineStore('user', ...)
```

---

### Store 파일 구조

**프로젝트 규모에 따라 선택**

#### 소규모 프로젝트
```
src/
  stores/
    counter.js
    user.js
    todo.js
```

#### 중대형 프로젝트
```
src/
  stores/
    modules/
      user/
        index.js
        types.js
      product/
        index.js
        types.js
    index.js
```

---

## 📝 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **상태 관리** | 여러 컴포넌트의 공유 상태를 관리 | Props, Emit 혹은 중앙 저장소 사용 |
| **Pinia** | Vue의 공식 상태 관리 라이브러리 | 중앙 저장소(store)를 제공 |
| **defineStore** | 중앙 저장소(store)를 정의하는 함수 | `defineStore('counter', () => {})` |
| **state** | 중앙 저장소의 반응형 데이터 | `const count = ref(0)` |
| **getters** | state를 기반으로 한 계산된 속성 | `const double = computed(() => {})` |
| **actions** | state를 변경하는 메서드 | `function increment() {}` |
| **상태 유지 (Pinia)** | Pinia 상태를 Local Storage에 저장 | `{ persist: true }` 옵션 사용 |

---

## 📋 요약 정리

### Pinia

**Vue의 공식 상태 관리 라이브러리로 컴포넌트들이 공유하는 상태를 관리하기 위한 중앙 저장소(store)를 제공**

**Pinia를 사용하면 어떤 컴포넌트든 props나 emit 없이 중앙 저장소에 직접 접근하여 상태를 읽거나 변경 가능**

**`defineStore()` 함수를 사용해 store를 정의하며, store는 세 가지 핵심 요소로 구성:**

---

### state

**`ref()`로 정의된 반응형 데이터로 여러 컴포넌트가 공유하는 상태의 원본**

```javascript
const count = ref(0)
```

---

### getters

**`computed()`로 정의되며, state를 기반으로 하는 계산된 값으로 state 원본에 의존하기 때문에 캐싱(caching) 기능이 존재**

```javascript
const doubleCount = computed(() => count.value * 2)
```

---

### actions

**`function()`으로 정의되며 state를 변경하는 메서드임. 비동기 로직을 포함 가능**

```javascript
function increment() {
  count.value++
}
```

---

### State Persistence

**Pinia의 상태는 기본적으로 메모리에 저장되므로 페이지를 새로고침하면 초기화**

**`pinia-plugin-persistedstate`:**
- Pinia의 상태를 브라우저의 Local Storage에 자동으로 저장하여 새로고침해도 데이터가 유지되도록 하는 플러그인

**Local Storage:**
- 브라우저가 닫혔다 열어도 데이터가 사라지지 않는 영구적인 웹 스토리지 객체

**플러그인을 설치하고 main.js에 등록한 후 `defineStore()`의 세 번째 인자로 `{ persist: true }` 옵션을 추가하면 해당 store의 상태가 자동으로 Local Storage에 저장**

---

## ✅ 확인 문제 정답

1. **c) 구조가 깊어지면 관리가 복잡함** - 여러 컴포넌트를 거쳐 데이터를 전달(prop drilling)하는 것은 비효율적이고 코드를 복잡하게 만듭니다.

2. **b) Pinia** - Pinia는 Vue 팀에서 공식적으로 권장하는 상태 관리 라이브러리로 여러 컴포넌트의 상태를 중앙에서 관리합니다.

3. **c) defineStore()** - `defineStore()` 함수를 사용하여 고유 ID와 함께 새로운 중앙 저장소(store)를 정의합니다.

4. **a) state** - state는 `ref()`로 정의되며, 여러 컴포넌트가 공유하는 핵심 원본 데이터입니다.

5. **b) getters** - getters는 `computed()`와 같이 state 값에 의존하여 계산된 값을 반환하여 캐싱 기능을 가집니다.

6. **c) actions** - actions는 state를 변경하는 로직을 함수 형태로 정의하며, 비동기 로직도 포함할 수 있습니다.

7. **b) store.count** - `useStore()`로 가져온 store 인스턴스를 통해 state, getters, actions에 직접 접근할 수 있습니다.

8. **b) store.increment()** - actions에 정의된 함수는 store 인스턴스의 메서드처럼 직접 호출하여 사용합니다.

9. **c) 로컬 스토리지(Local Storage)에 저장** - `pinia-plugin-persistedstate` 플러그인을 사용하여 Pinia 상태를 로컬 스토리지에 영구적으로 저장할 수 있습니다.

10. **a) defineStore의 옵션으로 persist: true 추가** - 플러그인 설치 후 상태를 유지하고 싶은 `defineStore()`의 세 번째 인자로 `{ persist: true }`를 전달합니다.

---

## 🎯 최종 정리

**"여러 컴포넌트가 같은 데이터를 공유해야 한다면 어떻게 해야 할까요?"**

### Props는 훌륭한 도구지만, 컴포넌트 구조가 5단계 이상 깊어진다면?

**데이터를 전달하기 위해 모든 중간 컴포넌트를 거쳐야 하는 건 너무나 복잡합니다.**

### Pinia라는 중앙 저장소를 활용해 문제 해결!

```javascript
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

// 이제 store.count, store.increment() 등으로 직접 접근!
```

**이로써 우리는 컴포넌트 구조에 얽매이지 않고 앱 전체의 상태를 일관되고 효율적으로 관리하는 방법을 배웠습니다.**

---

**핵심 포인트:**
1. **Pinia**: Vue 공식 상태 관리 라이브러리
2. **Store**: 중앙 저장소 (state + getters + actions)
3. **State**: `ref()`로 정의된 반응형 데이터
4. **Getters**: `computed()`로 정의된 계산된 값
5. **Actions**: state를 변경하는 메서드
6. **storeToRefs**: 구조 분해 시 반응성 유지
7. **Persistence**: Local Storage에 상태 저장
8. **적절한 사용**: Props vs Pinia 상황에 맞게 선택

