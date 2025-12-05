# Vue Component State Flow 교안 정리

## 📚 목차
1. Passing Props
   - Props
   - Props 선언
   - Props 세부사항
   - Props 활용
2. Component Events
   - Emit
   - 이벤트 발신 및 수신
   - emit 이벤트 선언
   - 이벤트 전달
   - 이벤트 세부사항
   - emit 이벤트 활용
3. 참고
   - 정적 & 동적 props 주의사항
   - Props & Emit 객체 선언 문법

---

## 🎯 학습 목표

1. ✅ Props를 통해 부모에서 자식으로 데이터를 전달할 수 있다
2. ✅ 자식 컴포넌트에서 `defineProps`를 사용하여 props를 선언한다
3. ✅ `v-bind`를 사용해 부모의 동적 데이터를 props로 전달한다
4. ✅ 자식에서 부모로 이벤트를 보내기 위해 emit을 사용한다
5. ✅ `defineEmits`로 이벤트를 선언하고 emit 함수로 발신한다
6. ✅ 부모 컴포넌트에서 `v-on`을 사용해 자식 이벤트를 수신한다
7. ✅ emit 이벤트 발신 시 부모 컴포넌트로 데이터를 전달한다

---

## 🏠 학습 시작: Todo List 비유

**"Todo List를 만든다고 상상해봅시다. 전체 목록은 부모가, 각 항목은 자식이 보여줍니다. 이 둘은 어떻게 협력할까요?"**

### 1. 부모는 자식에게 '오늘 할 일'의 내용이 무엇인지 **Props**로 알려줍니다.

### 2. 자식 내의 '삭제' 버튼이 클릭되면, 그 사실을 부모에게 **Emit**으로 알려주고, 실제 목록에서 해당 항목을 지우도록 요청해야 합니다.

**이번 시간에는 이처럼 컴포넌트 협업의 기본기를 학습해봅시다.**

---

## 1️⃣ Passing Props

### Props

#### 정의

**Props**: 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 사용자 지정 특성

**Props는 부모 컴포넌트가 자식 컴포넌트에게 데이터를 전달할 때 사용하는 특별한 속성입니다:**
- 데이터는 부모에서 자식으로 한 방향으로만 흐르며
- 자식 컴포넌트는 전달받은 props를 직접 수정해서는 안 됩니다 (읽기 전용)
- 이 방식을 통해 재사용 가능한 컴포넌트를 만들고
- 부모가 어떤 데이터를 전달하느냐에 따라 자식의 내용과 모습을 다르게 설정할 수 있습니다

---

#### 동일한 데이터, 하지만 다른 컴포넌트

**상황:**
- 동일한 사진 데이터가 한 화면에 다양한 위치에서 여러 번 출력되고 있음
- 해당 페이지를 구성하는 컴포넌트가 여러 개라면?

**질문:**
- 각 컴포넌트가 개별적으로 동일한 데이터를 관리해야 할까?
- 그렇다면 사진을 변경해야 할 때 모든 컴포넌트에 대해 변경 요청을 해야 함

**해결책:**
**→ 공통된 부모 컴포넌트에서 관리하자!**

---

#### Props와 Emit의 관계

```
Parent
  ↓ Pass Props (데이터 전달)
Child
  ↑ Emit Events (이벤트 발신)
```

**부모는 자식에게 데이터를 전달 (Pass Props)**
**자식은 자신에게 일어난 일을 부모에게 알림 (Emit event)**

---

#### Props 특징

**1) 단방향 데이터 흐름**

부모의 데이터가 업데이트되면 자식에게 전달되지만, 그 반대는 불가능

- 즉, 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안 되며 불가능
- 또한 부모 컴포넌트가 업데이트될 때마다 이를 사용하는 자식 컴포넌트의 모든 props가 최신 값으로 업데이트됨
- 부모 컴포넌트에서만 변경하고 이를 내려받는 자식 컴포넌트는 자연스럽게 갱신

> **⚠️ TIP**
> - 자식이 부모 속성을 바꾸려면 props를 수정하지 말고 이후 배울 emit을 이용해서 부모에게 알려야 합니다
> - 객체/배열 props는 자식에서 내부 값을 바꾸면 부모의 원본도 바뀌니, 매우 주의해야 합니다

---

#### One-Way Data Flow

**모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성 (one-way-down binding)**

**단방향인 이유:**
- 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여
- 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함
- (무한 루프, 디버깅 난이도 상승 등)

**목표:**
- 데이터 흐름의 **'일관성'** 및 **'예측 가능성'**을 높이는 것

---

## 2️⃣ Props 선언

### 사전 준비

#### 1단계: Vue 프로젝트 생성
```bash
npm create vue@latest
```

#### 2단계: 초기 설정
- 초기 생성된 컴포넌트 모두 삭제 (App.vue 제외)
- `src/assets` 내부 파일 모두 삭제
- `main.js`에서 아래 코드 삭제:
  ```javascript
  import './assets/main.css'
  ```

#### 3단계: 컴포넌트 관계 작성
**App > Parent > ParentChild** 컴포넌트 관계 작성

---

### App 컴포넌트 작성

**App.vue**
```vue
<template>
  <div>
    <Parent />
  </div>
</template>

<script setup>
import Parent from '@/components/Parent.vue'
</script>
```

---

### Parent 컴포넌트 작성

**Parent.vue**
```vue
<template>
  <div>
    <ParentChild />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
</script>
```

---

### ParentChild 컴포넌트 작성

**ParentChild.vue**
```vue
<template>
  <div></div>
</template>

<script setup>
</script>
```

---

## 3️⃣ Props 작성

### 부모에서 자식으로 Props 전달

**Parent.vue**
```vue
<template>
  <div>
    <ParentChild my-msg="message" />
  </div>
</template>
```

**구조:**
```
<ParentChild my-msg="message" />
             ↑      ↑
         props 이름  props 값
```

---

## 4️⃣ Props 선언

### defineProps()

**부모 컴포넌트에서 내려 보낸 props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요**

**`defineProps()`를 사용하여 props를 선언**

```vue
<script setup>
defineProps()
</script>
```

**`defineProps()`에 전달하는 인자의 형태에 따라 선언 방식이 나뉨:**

1. **'문자열 배열'**을 사용한 선언
2. **'객체'**를 사용한 선언

---

### 1) 문자열 배열을 사용한 선언

**배열의 문자열 요소로 props 선언**
- 문자열 요소의 이름은 전달된 props의 이름

**ParentChild.vue**
```vue
<script setup>
defineProps(['myMsg'])
</script>
```

---

### 2) 객체를 사용한 선언 (권장)

**각 객체 속성의 키가 전달받은 props 이름이 됨**
- 객체 속성의 값은 해당 데이터의 타입에 맞는 생성자 함수 (String, Number 등)여야 함

**ParentChild.vue**
```vue
<script setup>
defineProps({
  myMsg: String
})
</script>
```

> **⚠️ TIP**
> **가급적 "객체를 사용한 선언"을 사용하는 것을 권장합니다.**
> - 각 prop에 대해 상세한 규칙(유효성 검사)을 설정하여 컴포넌트의 안정성을 높여줍니다
> - 객체 구문은 그 자체로 컴포넌트의 설명서 역할을 하므로 코드를 통해 명확하게 의사소통이 가능합니다

---

## 5️⃣ Props 데이터 사용

### 템플릿에서 반응형 변수와 같은 방식으로 활용

**ParentChild.vue**
```vue
<template>
  <div>
    <p>{{ myMsg }}</p>
  </div>
</template>

<script setup>
defineProps({
  myMsg: String
})
</script>
```

**브라우저 출력:**
```
message
```

---

### Props를 객체로 반환받아 사용

**ParentChild.vue**
```vue
<template>
  <div>
    <p>{{ props.myMsg }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  myMsg: String
})

console.log(props)      // {myMsg: 'message'}
console.log(props.myMsg) // 'message'
</script>
```

---

## 6️⃣ Props 세부사항

### 1) Props Name Casing (Props 이름 컨벤션)

**자식 컴포넌트로 전달 시:**
- kebab-case (HTML 속성 표기법)

**자식 컴포넌트에서 선언 및 템플릿 참조 시:**
- camelCase (JavaScript 표기법)

**예시:**

**부모 컴포넌트 (Parent.vue):**
```vue
<template>
  <ParentChild my-msg="message" />
</template>
```

**자식 컴포넌트 (ParentChild.vue):**
```vue
<template>
  <p>{{ myMsg }}</p>
</template>

<script setup>
defineProps({
  myMsg: String
})
</script>
```

---

### 2) Static Props & Dynamic Props

#### Static Props (정적 props)
**고정된 문자열 값을 전달**

```vue
<template>
  <ParentChild my-msg="message" />
</template>
```

---

#### Dynamic Props (동적 props)
**`v-bind`를 사용하여 동적으로 할당된 props를 사용**

부모 컴포넌트의 데이터가 업데이트되면 자식 컴포넌트로 전달된 값도 업데이트됨

**Parent.vue**
```vue
<template>
  <ParentChild :my-msg="dynamicProps" />
</template>

<script setup>
import { ref } from 'vue'
import ParentChild from '@/components/ParentChild.vue'

const dynamicProps = ref('Dynamic Props!')
</script>
```

**ParentChild.vue**
```vue
<template>
  <p>{{ myMsg }}</p>
</template>

<script setup>
defineProps({
  myMsg: String
})
</script>
```

**브라우저 출력:**
```
Dynamic Props!
```

---

## 7️⃣ Component Events

### Emit

#### 정의

**Emit**: 자식 컴포넌트가 부모 컴포넌트에게 특정 이벤트가 발생했음을 알리는 역할

부모는 자식에게 데이터를 전달 (Pass Props) → **하향식**
자식은 자신에게 일어난 일을 부모에게 알림 (Emit event) → **상향식**

---

### 이벤트 발신 및 수신

#### 1단계: `$emit()`을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신

**ParentChild.vue**
```vue
<template>
  <button @click="$emit('someEvent')">클릭</button>
</template>
```

**설명:**
- `$emit('someEvent')`
- 첫 번째 인자: 이벤트 이름
- 이벤트 이름은 camelCase로 작성하는 것을 권장

---

#### 2단계: 부모는 `v-on`을 사용하여 수신

**Parent.vue**
```vue
<template>
  <ParentChild @some-event="someCallback" />
</template>

<script setup>
const someCallback = function() {
  console.log('ParentChild가 발신한 이벤트를 수신했습니다.')
}
</script>
```

**설명:**
- `@some-event="someCallback"`
- 수신 후 처리할 콜백 함수 호출
- HTML 속성 표기법이므로 kebab-case로 작성

---

### emit 이벤트 선언

**`defineEmits()`를 사용하여 발신할 이벤트를 선언**

**props와 마찬가지로:**
- `defineEmits()`에 작성하는 인자의 형태에 따라 선언 방식이 나뉨 (배열, 객체)
- `defineEmits()`는 `$emit` 대신 사용할 수 있는 동등한 함수를 반환 (명시적 선언 권장)

---

#### 1) 배열 구문

**ParentChild.vue**
```vue
<template>
  <button @click="buttonClick">클릭</button>
</template>

<script setup>
const emit = defineEmits(['someEvent'])

const buttonClick = function() {
  emit('someEvent')
}
</script>
```

---

#### 2) 객체 구문

**ParentChild.vue**
```vue
<template>
  <button @click="buttonClick">클릭</button>
</template>

<script setup>
const emit = defineEmits({
  someEvent: null
})

const buttonClick = function() {
  emit('someEvent')
}
</script>
```

---

### 이벤트 전달

#### emit 이벤트는 추가 인자를 전달할 수 있음

**ParentChild.vue**
```vue
<template>
  <button @click="emitArgs">추가 인자 전달</button>
</template>

<script setup>
const emit = defineEmits(['someEvent'])

const emitArgs = function() {
  emit('someEvent', 1, 2, 3)
}
</script>
```

---

#### 부모 컴포넌트에서 추가 인자 수신

**Parent.vue**
```vue
<template>
  <ParentChild @some-event="getNumbers" />
</template>

<script setup>
const getNumbers = function(...args) {
  console.log(args)        // [1, 2, 3]
  console.log(`전달받은 값: ${args}`)
}
</script>
```

**설명:**
- `emit`이 전달한 추가 인자는 `getNumbers`의 매개변수로 전달됨
- `...args` 스프레드 연산자를 사용하여 여러 인자를 배열로 받을 수 있음

---

### 이벤트 세부사항

#### Event Name Casing

**선언 및 발신 시:**
- camelCase

**부모 컴포넌트에서 수신 시:**
- kebab-case

**ParentChild.vue**
```vue
<script setup>
const emit = defineEmits(['someEvent'])  // camelCase

const buttonClick = function() {
  emit('someEvent')  // camelCase
}
</script>
```

**Parent.vue**
```vue
<template>
  <ParentChild @some-event="..." />  <!-- kebab-case -->
</template>
```

---

## 8️⃣ emit 이벤트 실습

### emit 이벤트 활용

#### 최하단 컴포넌트 ParentGrandChild에서 Parent 컴포넌트의 name 변수 변경 요청하기

```
App
 └─ Parent
     └─ ParentChild
         └─ ParentGrandChild
```

**구조:**
- ParentGrandChild에서 이벤트 발신
- ParentChild에서 이벤트 수신 및 재발신
- Parent에서 최종 수신 및 데이터 변경

---

### 1단계: ParentGrandChild에서 이벤트 발신

**ParentGrandChild.vue**
```vue
<template>
  <button @click="updateName">이름 변경</button>
</template>

<script setup>
const emit = defineEmits(['updateName'])

const updateName = function() {
  emit('updateName')
}
</script>
```

---

### 2단계: ParentChild에서 수신 및 재발신

**ParentChild.vue**
```vue
<template>
  <ParentGrandChild @update-name="updateName" />
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

const emit = defineEmits(['updateName'])

const updateName = function() {
  emit('updateName')
}
</script>
```

---

### 3단계: Parent에서 최종 수신

**Parent.vue**
```vue
<template>
  <div>
    <p>{{ name }}</p>
    <ParentChild @update-name="updateName" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ParentChild from '@/components/ParentChild.vue'

const name = ref('Alice')

const updateName = function() {
  name.value = 'Bella'
}
</script>
```

---

## 9️⃣ 참고사항

### 정적 & 동적 props 주의사항

**첫 번째는 정적 props로 문자열 "1"을 전달**
```vue
<SomeComponent num-props="1" />
```

**두 번째는 동적 props로 숫자 1을 전달**
```vue
<SomeComponent :num-props="1" />
```

**차이점:**
- 정적: `"1"` (문자열)
- 동적: `1` (숫자)

---

### Props & Emit 객체 선언 문법

#### Props 선언 시 '객체 선언 문법'을 권장하는 이유

**컴포넌트의 의도를 명확히 하여:**
- 가독성을 높이고
- 다른 개발자가 잘못된 타입의 데이터를 전달했을 때
- 콘솔에 경고를 출력하여 실수를 방지
- 추가로 props에 대한 유효성 검사로써 활용 가능

---

#### Props 유효성 검사 예시

```javascript
defineProps({
  // 여러 타입 허용
  propB: [String, Number],
  
  // 문자열 필수
  propC: {
    type: String,
    required: true
  },
  
  // 기본 값을 가지는 숫자형
  propD: {
    type: Number,
    default: 10
  },
})
```

**참고:** https://vuejs.org/guide/components/props.html#prop-validation

---

#### emit 이벤트도 '객체 선언 문법'으로 작성 가능

**emit 이벤트 또한 객체 구문으로 선언된 경우 유효성을 검사할 수 있음**

```javascript
const emit = defineEmits({
  // 유효성 검사 없음
  click: null,
  
  // submit 이벤트 유효성 검사
  submit: ({ email, password }) => {
    if (email && password) {
      return true
    } else {
      console.warn('submit 이벤트가 올바르지 않음')
      return false
    }
  }
})

const submitForm = function(email, password) {
  emit('submit', { email, password })
}
```

**참고:** https://vuejs.org/guide/components/events.html#events-validation

---

## 📝 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **props** | 부모가 자식에게 데이터를 전달하는 속성 | `<Child :props-data="parentData">` |
| **단방향 데이터 흐름** | 데이터는 부모에서 자식으로만 흐름 | Props는 자식에게 읽기 전용으로 전달됨 |
| **defineProps** | 자식에서 전달받을 props를 선언 | `defineProps({ myMsg: String })` |
| **동적 props** | v-bind로 반응형 데이터를 전달 | `<Child :my-prop="item">` |
| **$emit** | 자식이 부모에게 이벤트를 발신 | `<button @click="$emit('event')">` |
| **defineEmits** | 발신할 이벤트를 script에서 선언 | `const emit = defineEmits(['myEvent'])` |
| **이벤트 전달** | emit으로 부모에게 데이터를 전달 | `emit('myEvent', data)` |

---

## 📋 요약 정리

### Props (1/2)

**부모 컴포넌트가 자식 컴포넌트에게 데이터를 전달할 때 사용하는 특별한 속성**

- 자식 컴포넌트는 전달받은 props를 직접 수정할 수 없으며, 읽기 전용으로 사용하는 것을 권장

**자식 컴포넌트:**
- `defineProps()` 매크로를 사용해 전달받을 props를 선언
- 문자열 배열 `['myMsg']` 또는 객체 `{ myMsg: String }` 형태로 선언
- 유효성 검사를 위해 객체 형식이 권장

---

### Props (2/2)

**부모 컴포넌트:**
- 자식 컴포넌트 태그에 속성처럼 props를 전달

**Props 이름 컨벤션:**
- HTML 템플릿에서는 kebab-case (`my-msg`)로
- JavaScript 스크립트에서는 camelCase (`myMsg`)로 작성

**정적 vs 동적 Props:**
- **정적 Props**: 고정된 문자열 값을 전달 (`my-msg="hello"`)
- **동적 Props**: v-bind (또는 약어 `:`)를 사용하여 부모의 반응형 데이터를 전달 (`:my-msg="parentData"`)

---

### Emit

**자식 컴포넌트가 부모 컴포넌트에게 특정 이벤트가 발생했음을 알리고 데이터를 함께 전달하는 기능**

**자식 컴포넌트:**
- `<script setup>` 안에서 `defineEmits()` 매크로를 사용해 발신할 이벤트를 선언
- `defineEmits()`는 emit 함수를 반환하고, 이 함수를 호출해 이벤트를 발신 (`emit('eventName', data)`)

**부모 컴포넌트:**
- v-on (또는 약어 `@`) 디렉티브를 사용해 자식이 발신한 이벤트를 수신 (`@event-name="handlerMethod"`)
- 자식이 emit으로 전달한 데이터는 부모의 핸들러 메서드에서 매개변수로 받을 수 있음

---

## ✅ 확인 문제 정답

1. **b) 부모에서 자식으로 데이터를 전달하는 속성** - Props는 부모 컴포넌트가 자식에게 데이터를 전달하는 단방향 데이터 흐름의 핵심입니다.

2. **a) defineProps()** - defineProps() 매크로를 사용하여 부모로부터 전달받을 props를 명시적으로 선언해야 합니다.

3. **c) v-bind:prop="data"** - v-bind (또는 약어 `:`)를 사용해야 부모의 동적인 데이터를 props로 전달할 수 있습니다.

4. **d) 전달(kebab-case), 선언(camelCase)** - HTML 속성에서는 kebab-case(my-msg), JavaScript에서는 camelCase(myMsg)로 작성합니다.

5. **b) 단방향 데이터 흐름 원칙에 위배되기 때문에** - 데이터 흐름을 예측하기 어렵게 만드는 것을 방지하기 위해 props는 읽기 전용으로 사용해야 합니다.

6. **b) Emit** - 자식은 emit을 통해 특정 이벤트가 발생했음을 부모에게 알리고 데이터를 전달할 수 있습니다.

7. **c) defineEmits()** - defineEmits()는 컴포넌트가 발신할 이벤트를 명시적으로 선언하고 emit 함수를 반환합니다.

8. **b) v-on** - v-on (또는 약어 `@`) 디렉티브를 사용하여 자식 컴포넌트가 발신한 이벤트를 수신하고 처리합니다.

9. **a) emit('myEvent', data)** - emit 함수의 첫 번째 인자는 이벤트 이름, 두 번째부터는 전달할 데이터를 순서대로 작성합니다.

10. **b) 동적 props를 사용한다** - v-for의 각 반복 아이템을 `:my-prop="item"`과 같이 동적 props로 전달해야 합니다.

---

## 🎯 최종 정리

**"Todo List를 만든다고 상상해봅시다. 전체 목록은 부모가, 각 항목은 자식이 보여줍니다. 이 둘은 어떻게 협력할까요?"**

### 1. 부모는 자식에게 '오늘 할 일'의 내용이 무엇인지 **Props**로 알려줍니다.

### 2. 자식 내의 '삭제' 버튼이 클릭되면, 그 사실을 부모에게 **Emit**으로 알려주고, 실제 목록에서 해당 항목을 지우도록 요청해야 합니다.

**이처럼 Props는 위에서 아래로, Emit은 아래에서 위로 흐르는 '단방향 데이터 흐름'은 Vue를 예측 가능하고 안정적으로 만드는 핵심 원칙입니다.**

**이제 우리는 이 원칙을 사용해 컴포넌트들을 체계적으로 조립할 수 있습니다.**

---



**핵심 포인트:**
1. **Props**: 부모 → 자식 (데이터 전달, 읽기 전용)
2. **Emit**: 자식 → 부모 (이벤트 발신, 데이터 전달 가능)
3. **단방향 데이터 흐름**: 예측 가능하고 안정적인 앱 구조
4. **명명 규칙**: HTML(kebab-case), JS(camelCase)
5. **객체 선언 문법**: 유효성 검사와 명확한 의도 전달

