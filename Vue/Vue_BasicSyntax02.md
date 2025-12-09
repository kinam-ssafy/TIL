# Vue Basic Syntax 02
## 📚 목차
1. Computed Property
2. Computed vs. Methods
3. Conditional Rendering (v-if)
4. v-if vs. v-show
5. List Rendering (v-for)
6. v-for with key
7. v-for with v-if
8. Watchers
9. computed vs. watch
10. Lifecycle Hooks
11. Vue Style Guide
12. 참고사항 (computed 주의사항, 배열 메서드, Todo 앱 구현)

---

## 🎯 학습 목표

1. ✅ `computed`를 사용해 캐싱되는 계산된 속성을 만들 수 있다
2. ✅ `v-if`와 `v-show`의 차이를 알고 조건부 렌더링을 구현한다
3. ✅ `v-for` 디렉티브를 `key`와 함께 사용해 목록을 렌더링한다
4. ✅ `computed` 속성을 활용하여 v-for 렌더링 목록을 필터링한다
5. ✅ `watch`를 사용해 데이터 변경을 감지하고 특정 작업을 수행한다
6. ✅ `computed`와 `watch`의 차이점을 알고 상황에 맞게 사용한다
7. ✅ `onMounted` 같은 라이프사이클 훅을 사용해 코드를 실행한다

---

## 🧩 퀴즈

Vue의 다양한 기능들은 어떤 역할을 할까요?

1. 조건에 따라 요소를 DOM에서 완전히 제거 → **`v-if`**
2. 조건에 따라 요소를 보이거나 숨기기만 함 → **`v-show`**
3. 배열 데이터를 기반으로 목록을 반복하여 렌더링 → **`v-for`**
4. 데이터가 바뀔 때마다 새로운 값을 계산하고 결과를 기억(캐싱) → **`computed`**
5. 데이터가 바뀔 때마다 특정 행동(Side Effect)을 수행 → **`watch`**

---

## 1️⃣ Computed Property

### computed()

**정의**: "계산된 속성"을 정의하는 함수

### 핵심 개념

**미리 계산된 속성을 만들어:**
- 템플릿의 표현식을 단순하게 하고
- 불필요한 반복 연산을 줄입니다

**한 번 계산된 값은 캐싱(임시 저장)되어:**
- 의존하는 데이터가 바뀌기 전까지는 다시 계산하지 않으므로
- 성능에 매우 유리합니다

---

### Computed가 없는 경우

할 일이 남았는지 여부에 따라 다른 메시지 출력하기

```html
<h2>남은 할 일</h2>
<p>{{ todos.length > 0 ? '아직 남았다' : '퇴근!' }}</p>
```

```javascript
const todos = ref([
  { text: 'Vue 실습' },
  { text: '자격증 공부' },
  { text: 'TIL 작성' }
])
```

**문제점:**
- 템플릿이 복잡해지며 `todos`에 따라 계산을 수행하게 됨
- 만약 이 계산을 템플릿에 여러 번 사용하는 경우에는 매번 계산이 발생

---

### Computed를 사용하는 경우

반응형 데이터를 포함하는 복잡한 로직의 경우 `computed`를 활용하여 미리 값을 계산

**여러 곳에서 사용해야 한다면, `computed`로 정의한 `restOfTodos`를 필요한 곳마다 재사용하면 됨**

```html
<h2>남은 할 일</h2>
<p>{{ restOfTodos }}</p>
```

```javascript
import { createApp, ref, computed } from 'vue'

const todos = ref([
  { text: 'Vue 실습' },
  { text: '자격증 공부' },
  { text: 'TIL 작성' }
])

const restOfTodos = computed(() => {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
})
```

---

### computed 특징

#### 1) computed ref
**반환되는 값은 계산된 ref (computed ref)**
- 일반 ref와 유사하게 계산된 결과를 `.value`로 참조 가능 (템플릿에서는 `.value` 생략 가능)

> **ref**: 기본형 데이터를 반응형으로 만드는 Vue 함수

> **computed ref**: 원본 데이터가 바뀔 때만 값을 알아서 다시 계산하는 ref

---

#### 2) 자동 의존성 추적
**computed 속성은 의존된 반응형 데이터를 자동으로 추적**
- 의존하는 반응형 데이터가 변경될 때만 재평가

```javascript
const restOfTodos = computed(() => {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
})
```

- `restOfTodos`의 계산은 `todos`에 의존하고 있음
- 따라서 `todos`가 변경될 때만 `restOfTodos`가 업데이트됨

---

## 2️⃣ Computed vs. Methods

### computed와 동일한 로직을 처리할 수 있는 method

`computed` 속성 대신 `method`로도 동일한 기능을 정의할 수 있음

#### computed 예시
```html
<h2>남은 할 일</h2>
<p>{{ restOfTodos }}</p>
```

```javascript
import { createApp, ref, computed } from 'vue'

const restOfTodos = computed(() => {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
})
```

---

#### method 예시
```html
<h2>남은 할 일</h2>
<p>{{ getRestOfTodos() }}</p>
```

```javascript
const getRestOfTodos = function() {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
}
```

---

### computed와 method 차이

#### 핵심 차이: 캐시 (Cache)

**computed 속성:**
- 의존하는 반응형 데이터를 기반으로 그 결과를 **캐시(cached)**
- 의존하는 데이터가 변경된 경우에만 재평가됨
- 의존하는 데이터가 변경되지 않으면, 해당 computed 속성에 여러 번 접근해도 함수를 다시 실행하지 않고 **캐시된 결과를 즉시 반환**

**method 호출:**
- 다시 렌더링이 발생할 때마다 **항상 함수를 실행**

> **캐시(cached)**: 데이터를 임시로 저장하여 다음에 같은 데이터를 요청할 때 더 빠르게 접근할 수 있도록 하는 기술이나 저장 공간

---

**⚠️ TIP**
- 템플릿에서 `computed`는 괄호 없이, `method`는 괄호를 붙여 호출합니다
- 계산에 인자가 필요하다면 `computed`가 아닌 `method`를 사용해야 합니다 (계산에 외부의 값이 필요한지 여부를 판단)

---

### 캐시 (Cache)

**정의**: 데이터나 결과를 일시적으로 저장해두는 임시 저장소

**비유:**
캐시는 자주 꺼내 먹는 식재료를 넣어두는 **'냉장고'**와 같은 임시 저장 공간입니다.

- 요리할 때마다 매번 마트(원본 데이터)에 갈 필요 없이
- 냉장고에서 바로 재료를 꺼내 쓰니 시간을 크게 절약할 수 있습니다

마찬가지로:
- 데이터를 요청할 때 먼저 캐시를 확인하고
- 없을 경우에만 원본 데이터에 접근하여 가져온 뒤
- 캐시에 저장합니다

---

### Cache 예시: 웹 페이지의 캐시 데이터

과거 방문한 적이 있는 페이지에 다시 접속할 경우:
- 페이지 일부 데이터가 브라우저 캐시에 저장 후
- 같은 페이지에 다시 요청 시 모든 데이터를 다시 응답받는 것이 아니라
- 일부 캐시된 데이터를 사용하여 더 빠르게 웹 페이지를 렌더링

**브라우저 개발자 도구 Network 탭:**
```
Name                Status   Type   Size
image.png           200      png    (memory cache)
style.css           200      css    (disk cache)
```

---

## 3️⃣ Conditional Rendering

### v-if

**역할**: 표현식 값의 true/false를 기반으로 요소를 조건부로 렌더링

---

### v-if 기본 사용

```html
<p v-if="isSeen">Hi There</p>
```

```javascript
const isSeen = ref(true)
```

---

### v-else
`v-if`가 false일 때 렌더링할 블록을 나타냄

```html
<p v-if="isSeen">Yes</p>
<p v-else>No</p>
```

```javascript
const isSeen = ref(false)
```

**렌더링 결과:**
```html
<p>No</p>
```

---

### v-else-if
여러 조건을 연결할 때 사용

```html
<div v-if="name === 'Alice'">Alice</div>
<div v-else-if="name === 'Bella'">Bella</div>
<div v-else-if="name === 'Cathy'">Cathy</div>
<div v-else>Unknown</div>
```

```javascript
const name = ref('Bella')
```

**렌더링 결과:**
```html
<div>Bella</div>
```

---

### 여러 요소에 대한 v-if 적용

HTML `<template>` 요소에 `v-if`를 사용하여 하나 이상의 요소에 대해 적용

```html
<template v-if="name === 'Cathy'">
  <div>Cathy</div>
  <div>나이: 30</div>
  <div>직업: 개발자</div>
</template>
```

```javascript
const name = ref('Cathy')
```

**렌더링 결과:**
```html
<div>Cathy</div>
<div>나이: 30</div>
<div>직업: 개발자</div>
```

> `<template>`은 페이지에 렌더링되지 않지만, 하나의 블록으로 여러 요소를 그룹화할 수 있음

---

## 4️⃣ v-if vs. v-show

### v-show

**역할**: 표현식 값의 true/false를 기반으로 요소의 가시성(visibility)을 전환

```html
<div v-show="isShow">Hello</div>
```

```javascript
const isShow = ref(false)
```

---

### v-show 특징

**1) 항상 DOM에 렌더링**
- `v-show`는 항상 렌더링되어 DOM에 남아있음
- CSS `display` 속성만 전환

```html
<!-- isShow가 false일 때 -->
<div style="display: none;">Hello</div>
```

**2) `<template>` 태그 지원 안 함**

**3) `v-else` 지원 안 함**

---

### v-if vs. v-show 비교

| 특징 | v-if | v-show |
|------|------|--------|
| **렌더링 방식** | 조건이 false면 DOM에서 제거 | 항상 DOM에 렌더링, CSS로 숨김 |
| **초기 렌더링 비용** | 조건이 false면 렌더링 안 함 (비용 낮음) | 항상 렌더링 (비용 높음) |
| **토글 비용** | 높음 (DOM 추가/제거) | 낮음 (CSS만 변경) |
| **사용 권장 시기** | 런타임 중 조건이 변경되지 않을 때 | 자주 전환해야 할 때 |

---

### 사용 권장 상황

**v-if:**
- 초기 조건이 false인 경우 (초기 렌더링 비용 절감)
- 런타임 중에 조건이 거의 바뀌지 않을 때

**v-show:**
- 자주 전환해야 하는 요소
- 초기 렌더링 비용보다 토글 비용이 중요한 경우

---

## 5️⃣ List Rendering

### v-for

**역할**: 소스 데이터(Array, Object, Number, String, Iterable)를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링

---

### v-for 구조

```
v-for="item in items"
```

- `items`: 반복할 데이터 (원본 배열)
- `item`: 반복되는 현재 요소의 별칭 (alias)

---

### v-for 기본 사용

#### 1) 배열 반복
```html
<div v-for="item in items">
  {{ item.text }}
</div>
```

```javascript
const items = ref([
  { id: 1, text: 'Vue' },
  { id: 2, text: 'React' },
  { id: 3, text: 'Angular' }
])
```

**렌더링 결과:**
```html
<div>Vue</div>
<div>React</div>
<div>Angular</div>
```

---

#### 2) 인덱스 활용
`v-for`는 두 번째 인자로 현재 항목의 인덱스를 제공

```html
<div v-for="(item, index) in items">
  {{ index }} - {{ item.text }}
</div>
```

**렌더링 결과:**
```html
<div>0 - Vue</div>
<div>1 - React</div>
<div>2 - Angular</div>
```

---

#### 3) 객체 반복
객체의 각 속성을 반복할 수도 있음

```html
<div v-for="(value, key) in myObj">
  {{ key }}: {{ value }}
</div>
```

```javascript
const myObj = ref({
  name: 'Cathy',
  age: 30,
  job: '개발자'
})
```

**렌더링 결과:**
```html
<div>name: Cathy</div>
<div>age: 30</div>
<div>job: 개발자</div>
```

---

#### 4) 객체 반복 (인덱스 포함)
세 번째 인자로 인덱스를 제공

```html
<div v-for="(value, key, index) in myObj">
  {{ index }} / {{ key }}: {{ value }}
</div>
```

**렌더링 결과:**
```html
<div>0 / name: Cathy</div>
<div>1 / age: 30</div>
<div>2 / job: 개발자</div>
```

---

#### 5) 중첩된 v-for
```html
<ul v-for="item in myInfo">
  <li v-for="friend in item.friends">
    {{ item.name }} - {{ friend }}
  </li>
</ul>
```

```javascript
const myInfo = ref([
  { name: 'Alice', friends: ['Bella', 'Cathy'] },
  { name: 'Bella', friends: ['Alice', 'Cathy'] }
])
```

**렌더링 결과:**
```html
<ul>
  <li>Alice - Bella</li>
  <li>Alice - Cathy</li>
</ul>
<ul>
  <li>Bella - Alice</li>
  <li>Bella - Cathy</li>
</ul>
```

---

## 6️⃣ v-for with key

### key 속성의 필요성

**내부 컴포넌트의 상태를 일관되게 유지**
- 데이터의 식별자 역할을 하는 `key` 속성을 사용하여 Vue가 각 노드를 추적하고
- 기존 요소를 재사용, 재정렬할 수 있도록 힌트를 제공

---

### key 사용법

**반드시 `v-for`와 함께 `key`를 사용해야 함**

```html
<div v-for="item in items" :key="item.id">
  {{ item.text }}
</div>
```

```javascript
const items = ref([
  { id: 1, text: 'Vue' },
  { id: 2, text: 'React' },
  { id: 3, text: 'Angular' }
])
```

---

### key 특징

**1) 고유한 값**
- `key`는 반드시 각 요소에 대한 고유한 값을 사용해야 함
- 문자열 또는 숫자 타입만 사용 가능

**2) 내장 특수 속성**
- `key`는 Vue의 내부 가상 DOM 알고리즘이 이전 목록과 새 노드 목록을 비교할 때 각 노드를 식별하는 데 사용

---

### key가 없을 때의 문제

**예시: 항목 추가 시**

```html
<!-- key 없이 사용 -->
<div v-for="item in items">
  <input type="checkbox">
  {{ item.text }}
</div>
```

- 새로운 항목이 배열 중간에 추가되면
- Vue는 기존 DOM 요소를 재사용하려고 시도
- 체크박스 상태가 잘못된 항목과 연결될 수 있음

**해결: key 사용**

```html
<div v-for="item in items" :key="item.id">
  <input type="checkbox">
  {{ item.text }}
</div>
```

- 각 항목이 고유한 `key`를 가지므로
- Vue가 정확히 어떤 항목이 추가/삭제/이동되었는지 추적 가능
- 체크박스 상태가 올바르게 유지됨

---

## 7️⃣ v-for with v-if

### 동일 요소에 v-for와 v-if를 함께 사용하지 않기

**❌ 나쁜 예:**

```html
<ul>
  <li v-for="todo in todos" v-if="!todo.isComplete" :key="todo.id">
    {{ todo.text }}
  </li>
</ul>
```

---

### 문제점

**v-if가 v-for보다 우선순위가 높음**
- `v-if`에서 `v-for` 변수에 접근할 수 없음

```html
<!-- v-if가 먼저 평가되므로 todo 변수를 알 수 없음 -->
<li v-for="todo in todos" v-if="!todo.isComplete">
```

---

### 해결 방법 1: computed 사용

**✅ 좋은 예:**

```html
<ul>
  <li v-for="todo in completeTodos" :key="todo.id">
    {{ todo.text }}
  </li>
</ul>
```

```javascript
const todos = ref([
  { id: 1, text: 'Vue 학습', isComplete: false },
  { id: 2, text: 'React 학습', isComplete: true },
  { id: 3, text: 'Angular 학습', isComplete: false }
])

const completeTodos = computed(() => {
  return todos.value.filter(todo => !todo.isComplete)
})
```

---

### 해결 방법 2: template 태그 사용

**`<template>` 태그를 사용해 `v-if`의 위치를 조정**

```html
<ul>
  <template v-for="todo in todos" :key="todo.id">
    <li v-if="!todo.isComplete">
      {{ todo.text }}
    </li>
  </template>
</ul>
```

---

## 8️⃣ Watchers

### watch()

**정의**: 하나 이상의 반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수를 호출

**주요 용도**: 데이터 변경에 대한 반응으로 비동기 작업이나 다른 부수 효과(side effect)를 수행할 때

---

### watch 구조

```javascript
watch(source, callback)
```

- **source**: 감시할 반응형 데이터
- **callback**: 데이터가 변경될 때 실행할 함수

---

### watch 기본 사용

#### 1) 단일 ref 감시

```javascript
const count = ref(0)

watch(count, (newValue, oldValue) => {
  console.log(`count가 ${oldValue}에서 ${newValue}로 변경됨`)
})

count.value++ // 콘솔: "count가 0에서 1로 변경됨"
```

---

#### 2) 여러 source를 감시

배열을 사용하여 여러 데이터를 동시에 감시

```javascript
const firstName = ref('Alice')
const lastName = ref('Kim')

watch([firstName, lastName], ([newFirst, newLast], [oldFirst, oldLast]) => {
  console.log(`이름이 변경됨: ${oldFirst} ${oldLast} → ${newFirst} ${newLast}`)
})

firstName.value = 'Bella'
// 콘솔: "이름이 변경됨: Alice Kim → Bella Kim"
```

---

### watch 실전 예시

#### API 호출 예시

사용자 ID가 변경될 때마다 새로운 데이터를 서버에서 가져오기

```javascript
const userId = ref(1)
const userData = ref(null)

watch(userId, async (newId) => {
  const response = await fetch(`https://api.example.com/users/${newId}`)
  userData.value = await response.json()
})

// userId가 변경되면 자동으로 API 호출
userId.value = 2
```

---

#### 검색어 입력 감시

```javascript
const searchQuery = ref('')
const searchResults = ref([])

watch(searchQuery, async (newQuery) => {
  if (newQuery.length > 2) {
    const response = await fetch(`/api/search?q=${newQuery}`)
    searchResults.value = await response.json()
  } else {
    searchResults.value = []
  }
})
```

---

### watch의 다양한 옵션

#### immediate
컴포넌트가 생성될 때 즉시 콜백 실행

```javascript
watch(
  count,
  (newValue) => {
    console.log(`현재 count: ${newValue}`)
  },
  { immediate: true }
)
// 컴포넌트 생성 시 즉시 콘솔: "현재 count: 0"
```

---

#### deep
객체 내부의 중첩된 값 변경도 감지

```javascript
const user = ref({
  name: 'Alice',
  profile: {
    age: 30
  }
})

watch(
  user,
  (newValue) => {
    console.log('사용자 정보 변경됨', newValue)
  },
  { deep: true }
)

user.value.profile.age = 31 // deep 옵션으로 인해 감지됨
```

---

## 9️⃣ computed vs. watch

### 공통점
둘 다 데이터의 변화를 감지하고 처리

### 차이점

| 구분 | computed | watch |
|------|----------|-------|
| **목적** | 새로운 값을 계산하여 반환 | 특정 작업(side effect) 수행 |
| **반환값** | 있음 (계산된 값) | 없음 |
| **캐싱** | 의존 데이터 변경 시에만 재계산 | 매번 실행 |
| **사용 시기** | 템플릿에 표시할 값 계산 | API 호출, 로깅 등의 작업 |
| **인자 전달** | 불가능 | 가능 (newValue, oldValue) |

---

### 사용 시기 가이드

#### computed 사용:
```javascript
// ✅ 계산된 값을 반환하여 템플릿에 표시
const fullName = computed(() => {
  return `${firstName.value} ${lastName.value}`
})
```

```html
<p>{{ fullName }}</p>
```

---

#### watch 사용:
```javascript
// ✅ 데이터 변경 시 API 호출 등의 부수 효과 수행
watch(searchQuery, async (newQuery) => {
  // API 호출
  const response = await fetch(`/api/search?q=${newQuery}`)
  searchResults.value = await response.json()
})
```

---

### 비교 예시

#### 시나리오: 할 일 목록에서 완료되지 않은 항목만 표시

**computed 사용 (권장):**
```javascript
const todos = ref([
  { id: 1, text: 'Vue 학습', done: false },
  { id: 2, text: 'React 학습', done: true },
  { id: 3, text: 'Angular 학습', done: false }
])

// ✅ 계산된 값을 반환
const incompleteTodos = computed(() => {
  return todos.value.filter(todo => !todo.done)
})
```

```html
<li v-for="todo in incompleteTodos" :key="todo.id">
  {{ todo.text }}
</li>
```

---

**watch 사용 (비권장):**
```javascript
// ❌ 불필요하게 복잡
const incompleteTodos = ref([])

watch(todos, (newTodos) => {
  incompleteTodos.value = newTodos.filter(todo => !todo.done)
}, { deep: true, immediate: true })
```

---

## 🔟 Lifecycle Hooks

### 정의

**Lifecycle Hooks**: Vue 컴포넌트가 생성되고 DOM에 추가되고 업데이트되고 제거되는 각 생애 주기 단계에서 특정 로직을 실행할 수 있도록 제공되는 함수들

---

### Lifecycle Diagram

```
setup()
   ↓
onBeforeMount()
   ↓
onMounted() ← 컴포넌트가 DOM에 마운트됨
   ↓
   ↓ (데이터 변경 시)
   ↓
onBeforeUpdate()
   ↓
onUpdated() ← DOM이 업데이트됨
   ↓
   ↓ (컴포넌트 제거 시)
   ↓
onBeforeUnmount()
   ↓
onUnmounted() ← 컴포넌트가 제거됨
```

---

### 주요 Lifecycle Hooks

#### 1) onMounted()
**컴포넌트가 DOM에 마운트된 직후에 호출**

**사용 예시:**
- 초기 데이터 로드
- DOM 조작
- 외부 라이브러리 초기화

```javascript
import { onMounted, ref } from 'vue'

const items = ref([])

onMounted(async () => {
  // 서버에서 초기 데이터 가져오기
  const response = await fetch('/api/items')
  items.value = await response.json()
  
  console.log('컴포넌트가 마운트되었습니다!')
})
```

---

#### 2) onUpdated()
**반응형 데이터의 변경으로 인해 컴포넌트의 DOM이 업데이트된 후 호출**

```javascript
import { onUpdated, ref } from 'vue'

const count = ref(0)

onUpdated(() => {
  console.log('DOM이 업데이트되었습니다!')
  console.log(`현재 count: ${count.value}`)
})
```

---

#### 3) onUnmounted()
**컴포넌트가 DOM에서 제거된 후 호출**

**사용 예시:**
- 타이머 정리
- 이벤트 리스너 제거
- 외부 라이브러리 정리

```javascript
import { onMounted, onUnmounted } from 'vue'

let timer

onMounted(() => {
  timer = setInterval(() => {
    console.log('타이머 실행 중')
  }, 1000)
})

onUnmounted(() => {
  // 컴포넌트 제거 시 타이머 정리
  clearInterval(timer)
  console.log('타이머가 정리되었습니다')
})
```

---

### Lifecycle Hooks 활용 예시

#### 실전 예시: 데이터 로드 및 정리

```javascript
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  setup() {
    const posts = ref([])
    const loading = ref(true)
    let intervalId

    onMounted(async () => {
      // 1. 초기 데이터 로드
      try {
        const response = await fetch('/api/posts')
        posts.value = await response.json()
      } catch (error) {
        console.error('데이터 로드 실패:', error)
      } finally {
        loading.value = false
      }

      // 2. 자동 새로고침 설정 (30초마다)
      intervalId = setInterval(async () => {
        const response = await fetch('/api/posts')
        posts.value = await response.json()
      }, 30000)
    })

    onUnmounted(() => {
      // 3. 컴포넌트 제거 시 인터벌 정리
      if (intervalId) {
        clearInterval(intervalId)
      }
    })

    return {
      posts,
      loading
    }
  }
}
```

---

## 1️⃣1️⃣ Vue Style Guide

### Vue의 스타일 가이드 규칙

Vue의 스타일 가이드는 **우선순위**에 따라 4가지 범주로 나뉨

---

### 우선순위별 규칙

#### Priority A: Essential (필수)
**오류를 방지하는 데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수**

**예시:**
- `v-for`에 `key` 작성하기
- 동일 요소에 `v-if`와 `v-for` 함께 사용하지 않기

---

#### Priority B: Strongly Recommended (적극 권장)
**가독성 및/또는 개발자 경험을 향상시킴**

**예시:**
- 컴포넌트 파일명은 항상 PascalCase 또는 kebab-case
  - `MyComponent.vue` 또는 `my-component.vue`

---

#### Priority C: Recommended (권장)
**일관성을 보장하도록 임의의 선택을 할 수 있음**

**예시:**
- 컴포넌트/인스턴스 옵션 순서
  1. `name`
  2. `components`
  3. `props`
  4. `emits`
  5. `setup`
  6. ...

---

#### Priority D: Use with Caution (주의 필요)
**잠재적 위험 특성을 고려함**

**예시:**
- `<template>` 내에서 복잡한 표현식 피하기
- 간단한 computed 속성 사용 권장

---

### Vue Style Guide 참고 링크

**공식 문서:** https://vuejs.org/style-guide/

---

## 1️⃣2️⃣ 참고사항

### computed 주의사항

#### 1) computed의 반환 값은 변경하지 말 것

**❌ 나쁜 예:**
```javascript
const fullName = computed(() => {
  return `${firstName.value} ${lastName.value}`
})

// ❌ computed 값을 직접 수정하지 말 것
fullName.value = 'New Name' // 에러 발생!
```

**computed는 읽기 전용(read-only)**

---

#### 2) computed 사용 시 원본 배열 변경 금지

**❌ 나쁜 예:**
```javascript
const sortedTodos = computed(() => {
  // ❌ 원본 배열을 직접 수정
  return todos.value.sort((a, b) => a.id - b.id)
})
```

**✅ 좋은 예:**
```javascript
const sortedTodos = computed(() => {
  // ✅ 복사본을 만들어서 수정
  return [...todos.value].sort((a, b) => a.id - b.id)
})
```

**이유:**
- `sort()`, `reverse()` 등은 원본 배열을 변경하는 메서드
- computed 내부에서 원본 데이터를 변경하면 예기치 않은 부수 효과 발생

---

### Lifecycle Hooks 주의사항

#### Lifecycle Hooks는 동기적으로 작성

**✅ 좋은 예:**
```javascript
onMounted(() => {
  console.log('마운트 완료')
})
```

**❌ 나쁜 예:**
```javascript
setTimeout(() => {
  onMounted(() => {
    console.log('마운트 완료')
  })
}, 100)
// ❌ 비동기 콜백 안에서 호출하면 작동하지 않음
```

**이유:**
- Lifecycle Hooks는 컴포넌트 설정 단계에서 등록되어야 함
- 비동기 함수 내부에서는 제대로 등록되지 않음

---

### v-for와 배열을 활용한 필터링/정렬

#### computed 활용 필터링

```javascript
const todos = ref([
  { id: 1, text: 'Vue 학습', done: false },
  { id: 2, text: 'React 학습', done: true },
  { id: 3, text: 'Angular 학습', done: false }
])

// 완료되지 않은 할 일만 필터링
const activeTodos = computed(() => {
  return todos.value.filter(todo => !todo.done)
})

// 완료된 할 일만 필터링
const completedTodos = computed(() => {
  return todos.value.filter(todo => todo.done)
})
```

```html
<ul>
  <li v-for="todo in activeTodos" :key="todo.id">
    {{ todo.text }}
  </li>
</ul>
```

---

#### computed 활용 정렬

```javascript
const numbers = ref([3, 1, 4, 1, 5, 9, 2, 6])

// 오름차순 정렬 (복사본 생성)
const sortedNumbers = computed(() => {
  return [...numbers.value].sort((a, b) => a - b)
})

// 내림차순 정렬
const reversedNumbers = computed(() => {
  return [...numbers.value].sort((a, b) => b - a)
})
```

---

### 배열 변경 관련 메서드

#### 1) 배열 변경 메서드 (Mutating Methods)
**원본 배열을 직접 수정**

- `push()` - 배열 끝에 요소 추가
- `pop()` - 배열 끝 요소 제거
- `shift()` - 배열 첫 요소 제거
- `unshift()` - 배열 앞에 요소 추가
- `splice()` - 배열의 일부를 삭제/교체/추가
- `sort()` - 배열 정렬
- `reverse()` - 배열 순서 뒤집기

```javascript
const items = ref([1, 2, 3])

items.value.push(4)    // items: [1, 2, 3, 4]
items.value.pop()      // items: [1, 2, 3]
items.value.reverse()  // items: [3, 2, 1]
```

---

#### 2) 배열 교체 메서드 (Non-Mutating Methods)
**원본 배열을 수정하지 않고 항상 새 배열을 반환**

- `filter()` - 조건에 맞는 요소로 새 배열 생성
- `concat()` - 배열 합치기
- `slice()` - 배열의 일부를 복사

```javascript
const items = ref([1, 2, 3, 4, 5])

// 원본은 그대로, 새 배열 반환
const evenNumbers = items.value.filter(n => n % 2 === 0)  // [2, 4]
const firstThree = items.value.slice(0, 3)  // [1, 2, 3]

console.log(items.value)  // [1, 2, 3, 4, 5] (원본 유지)
```

---

## 1️⃣3️⃣ Todo 애플리케이션 구현

### 전체 코드

`v-model`, `v-on`, `v-bind`, `v-for`를 활용한 Todo 앱

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Todo App</title>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
</head>
<body>
  <div id="app">
    <h1>Todo App</h1>
    
    <!-- 새로운 Todo 추가 폼 -->
    <form @submit.prevent="addTodo">
      <input v-model="newTodo" placeholder="할 일을 입력하세요">
      <button>Add Todo</button>
    </form>
    
    <!-- Todo 목록 -->
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.text }}
        <button @click="removeTodo(todo)">X</button>
      </li>
    </ul>
  </div>

  <script>
    const { createApp, ref } = Vue;

    createApp({
      setup() {
        let id = 0;
        const newTodo = ref('');
        const todos = ref([
          { id: id++, text: 'Learn HTML' },
          { id: id++, text: 'Learn JS' },
          { id: id++, text: 'Learn Vue' }
        ]);

        // 새로운 Todo 항목을 추가하는 함수
        const addTodo = function() {
          // todos 배열에 새로운 Todo 객체 추가
          todos.value.push({ 
            id: id++, 
            text: newTodo.value 
          });
          // 입력 필드 초기화
          newTodo.value = '';
        };

        // 선택한 Todo 항목을 삭제하는 함수
        const removeTodo = function(selectedTodo) {
          // filter를 사용하여 선택한 Todo를 제외한 새로운 배열 생성
          todos.value = todos.value.filter((todo) => {
            return todo !== selectedTodo;
          });
        };

        return {
          newTodo,
          todos,
          addTodo,
          removeTodo
        };
      }
    }).mount('#app');
  </script>
</body>
</html>
```

---

### 코드 설명

#### 1) 데이터 정의
```javascript
let id = 0;  // Todo의 고유 ID
const newTodo = ref('');  // 입력 필드의 값
const todos = ref([
  { id: id++, text: 'Learn HTML' },
  { id: id++, text: 'Learn JS' },
  { id: id++, text: 'Learn Vue' }
]);
```

---

#### 2) Todo 추가 함수
```javascript
const addTodo = function() {
  // todos 배열에 새로운 Todo 객체 추가
  todos.value.push({ 
    id: id++, 
    text: newTodo.value 
  });
  // 입력 필드 초기화
  newTodo.value = '';
};
```

---

#### 3) Todo 삭제 함수
```javascript
const removeTodo = function(selectedTodo) {
  // filter를 사용하여 선택한 Todo를 제외한 새로운 배열 생성
  todos.value = todos.value.filter((todo) => {
    return todo !== selectedTodo;
  });
};
```

---

#### 4) 템플릿
```html
<!-- v-model로 양방향 바인딩 -->
<input v-model="newTodo">

<!-- v-on으로 이벤트 처리 -->
<form @submit.prevent="addTodo">
  <button>Add Todo</button>
</form>

<!-- v-for로 목록 렌더링, :key로 고유 식별 -->
<ul>
  <li v-for="todo in todos" :key="todo.id">
    {{ todo.text }}
    <button @click="removeTodo(todo)">X</button>
  </li>
</ul>
```

---

## 📝 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **computed 속성** | 의존 데이터를 기반으로 캐싱되는 값 | `const c = computed(() => {})` |
| **v-if 디렉티브** | 조건에 따라 요소를 렌더링/제거 | `<p v-if="isSeen">Hi</p>` |
| **v-show 디렉티브** | 조건에 따라 CSS display 전환 | `<p v-show="isShow">Hi</p>` |
| **v-for 디렉티브** | 데이터를 기반으로 목록을 렌더링 | `<li v-for="i in items">` |
| **key 속성** | v-for 각 노드를 식별하는 고유 값 | `<li :key="item.id">` |
| **watch 함수** | 데이터 변경을 감지하고 콜백 실행 | `watch(count, (newV) => {})` |
| **라이프사이클 훅** | 컴포넌트 생애 주기 특정 시점 함수 | `onMounted(() => {})` |

---

## 📋 요약 정리

### computed()
- 반응형 데이터를 기반으로 하는 **계산된 속성**을 만드는 함수
- 템플릿 안의 표현식이 너무 복잡해지는 것을 방지하고 재사용성을 높임
- 가장 큰 특징은 **캐싱(caching)**
- 의존하는 반응형 데이터가 변경될 때만 값을 다시 계산하고, 그렇지 않으면 이전에 계산된 값을 즉시 반환하여 성능을 향상
- 메서드(Methods)는 호출될 때마다 항상 함수를 실행하지만, `computed`는 의존 데이터가 바뀔 때만 실행된다는 점에서 차이

---

### v-if
- 조건이 `true`일 때만 블록을 렌더링하고, 조건이 `false`이면 해당 요소는 **DOM에서 완전히 제거**
- `v-else`, `v-else-if`와 함께 사용 가능

### v-show
- 조건에 따라 요소의 가시성을 전환하지만 항상 **DOM에 렌더링된 상태를 유지**
- 단순히 CSS `display` 속성을 `none`으로 변경하여 숨김

### v-if vs. v-show
- 자주 토글해야 하는 요소에는 `v-show`가 더 효율적
- 런타임 중에 조건이 거의 바뀌지 않는다면 `v-if`가 더 적합함

---

### v-for
- 배열이나 객체를 기반으로 목록을 반복해서 렌더링하는 디렉티브

### key 속성
- `v-for`를 사용할 때는 각 항목을 고유하게 식별할 수 있는 `key`를 반드시 함께 제공해야 함
- Vue는 이 `key`를 사용해 변경된 항목을 효율적으로 추적하고 업데이트

### v-for와 v-if
- `v-if`의 우선순위가 더 높기 때문에 두 디렉티브를 같은 요소에 함께 사용하면 안 됨

**해결책:**
- `computed` 속성으로 미리 필터링된 배열을 생성
- `<template>` 태그를 사용해 `v-if`의 위치를 조정

---

### watch
- 특정 반응형 데이터를 감시하고, 데이터가 변경될 때마다 지정된 콜백 함수를 실행하는 기능
- `computed`가 데이터 변경에 따라 새로운 값을 계산하는 데 사용되지만
- `watch`는 데이터 변경에 대한 반응으로 **비동기 요청이나 다른 특정 작업(side effect)**을 수행할 때 주로 사용

---

### Lifecycle Hooks
- Vue 컴포넌트가 생성되고 DOM에 추가되고 업데이트되고 제거되는 각 생애 주기 단계에서 특정 로직을 실행할 수 있도록 제공되는 함수들

**onMounted:**
- 컴포넌트가 DOM에 마운트된 직후에 호출되는 훅으로, 보통 서버에서 초기 데이터를 가져오는 등의 작업에 사용

**onUpdated:**
- 반응형 데이터의 변경으로 인해 컴포넌트의 DOM이 업데이트된 후 특정 로직을 수행

---

## ✅ 확인 문제 정답

1. **c) 의존된 데이터를 캐싱함** - computed 속성의 가장 큰 특징
2. **c) 계산에 인자가 필요할 때** - computed 대신 메서드를 사용해야 하는 경우
3. **b) 조건이 거짓이면 DOM에서 제거된다** - v-if 디렉티브의 설명
4. **b) v-show** - 자주 토글할 때 더 효율적
5. **c) key** - v-for 사용 시 함께 작성해야 하는 속성
6. **b) v-if의 우선순위가 더 높아서** - v-for와 v-if를 같은 요소에 쓰면 안 되는 이유
7. **b) computed 속성 사용** - v-for로 렌더링할 목록을 필터링하는 가장 좋은 방법
8. **b) 데이터 변경 시 특정 작업 수행** - watch 함수의 주된 용도
9. **b) 반환 값 유무** - computed와 watch의 가장 큰 차이점
10. **c) onMounted** - 컴포넌트가 DOM에 마운트된 후 호출되는 훅
11. **b) 동기적으로 작성** - 라이프사이클 훅은 어떻게 작성해야 하는지
12. **b) 복사본을 만들어 수정해야 함** - computed에서 원본 배열을 정렬할 때 주의할 점

---

## 🚀 실전 활용 팁

### 1. 검색 기능 구현

```javascript
import { ref, computed } from 'vue'

const searchQuery = ref('')
const items = ref([
  { id: 1, name: 'Vue.js' },
  { id: 2, name: 'React' },
  { id: 3, name: 'Angular' }
])

// computed로 필터링된 결과 제공
const filteredItems = computed(() => {
  return items.value.filter(item => 
    item.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})
```

```html
<input v-model="searchQuery" placeholder="검색...">
<ul>
  <li v-for="item in filteredItems" :key="item.id">
    {{ item.name }}
  </li>
</ul>
```

---

### 2. 정렬 기능 구현

```javascript
import { ref, computed } from 'vue'

const sortOrder = ref('asc')
const products = ref([
  { id: 1, name: '상품A', price: 3000 },
  { id: 2, name: '상품B', price: 1000 },
  { id: 3, name: '상품C', price: 2000 }
])

const sortedProducts = computed(() => {
  return [...products.value].sort((a, b) => {
    if (sortOrder.value === 'asc') {
      return a.price - b.price
    } else {
      return b.price - a.price
    }
  })
})
```

```html
<button @click="sortOrder = sortOrder === 'asc' ? 'desc' : 'asc'">
  정렬 전환 ({{ sortOrder === 'asc' ? '오름차순' : '내림차순' }})
</button>

<ul>
  <li v-for="product in sortedProducts" :key="product.id">
    {{ product.name }} - {{ product.price }}원
  </li>
</ul>
```

---

### 3. API 데이터 로드 (watch + lifecycle)

```javascript
import { ref, watch, onMounted } from 'vue'

const userId = ref(1)
const userData = ref(null)
const loading = ref(false)
const error = ref(null)

const fetchUserData = async (id) => {
  loading.value = true
  error.value = null
  
  try {
    const response = await fetch(`/api/users/${id}`)
    if (!response.ok) throw new Error('데이터 로드 실패')
    userData.value = await response.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

// 컴포넌트 마운트 시 초기 데이터 로드
onMounted(() => {
  fetchUserData(userId.value)
})

// userId 변경 감지
watch(userId, (newId) => {
  fetchUserData(newId)
})
```

```html
<div v-if="loading">로딩 중...</div>
<div v-else-if="error">에러: {{ error }}</div>
<div v-else-if="userData">
  <h2>{{ userData.name }}</h2>
  <p>{{ userData.email }}</p>
</div>
```

---

## 🎓 학습 완료!

이제 Vue의 핵심 기능들을 모두 학습했습니다:
- ✅ `computed`로 효율적인 계산된 속성 만들기
- ✅ `v-if`/`v-show`로 조건부 렌더링
- ✅ `v-for`로 리스트 렌더링
- ✅ `watch`로 데이터 변경 감지
- ✅ Lifecycle Hooks로 컴포넌트 생명주기 관리

이 기능들을 조합하면 강력한 Vue 애플리케이션을 만들 수 있습니다! 🎉
