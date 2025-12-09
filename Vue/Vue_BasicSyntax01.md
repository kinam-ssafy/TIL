# Vue Basic Syntax 1

## 📚 목차
1. Template Syntax
2. Directive
3. Dynamically data binding
4. v-bind (Attribute Bindings)
5. Class and Style Bindings
6. Event Handling
7. v-on
8. Modifiers
9. Form Input Bindings
10. v-model
11. 참고사항 (접두어 $, IME)

---

## 🎯 학습 목표

1. ✅ `v-` 접두사를 가진 디렉티브의 개념과 역할을 이해한다
2. ✅ `v-bind` 디렉티브를 사용해 HTML 속성을 동적으로 바인딩한다
3. ✅ 객체나 배열을 이용해 class와 style을 동적으로 바인딩한다
4. ✅ `v-on` 디렉티브로 DOM 이벤트를 수신하고 메서드를 실행한다
5. ✅ `.prevent`와 같은 이벤트 수식어로 이벤트 동작을 제어한다
6. ✅ `v-model` 디렉티브로 폼 요소에 양방향 바인딩을 한다
7. ✅ `v-model`이 `v-bind`와 `v-on`의 조합임을 이해한다

---

## 🧩 퀴즈

HTML 속성 앞에 붙는 `v-` 라는 접두사는 무엇을 의미할까요?

1. HTML 태그의 속성 값을 Vue의 데이터와 동적으로 연결 → **`v-bind`**
2. 버튼 클릭과 같은 사용자의 이벤트를 감지하고 지정된 함수를 실행 → **`v-on`**
3. `<input>`과 같은 폼(Form) 요소의 값과 데이터를 실시간으로 동기화 → **`v-model`**

---

## 1️⃣ Template Syntax

### 정의
Vue는 DOM을 컴포넌트 인스턴스의 데이터에 **선언적으로 바인딩**할 수 있는, **HTML 기반 템플릿 구문**을 사용

### 핵심 개념

**선언적 바인딩**
- JavaScript 데이터(상태)가 바뀌면 DOM(화면)이 알아서 업데이트되는 것을 의미

**템플릿 구문**
- HTML에 Vue만의 특별한 문법을 추가해서 사용하는 것을 의미

---

### Template Syntax 종류

#### 1) Text Interpolation (텍스트 보간)

**정의**: 데이터 바인딩의 가장 기본적인 형태

**이중 중괄호 구문 (콧수염 구문)** 사용

```html
<p>Message: {{ msg }}</p>
```

```javascript
const msg = ref('Hello Vue!')
```

- 콧수염 구문은 해당 컴포넌트 인스턴스의 `msg` 속성 값으로 대체
- `msg` 속성이 변경될 때마다 업데이트됨

> **데이터 바인딩**: 자바스크립트 데이터와 HTML 화면을 동기화하여 연결하는 것

---

#### 2) Raw HTML

콧수염 구문은 데이터를 **일반 텍스트**로 해석하기 때문에 실제 HTML을 출력하려면 `v-html`을 사용해야 함

```html
<div v-html="rawHtml"></div>
```

```javascript
const rawHtml = ref('<span style="color:red">This should be red.</span>')
```

**렌더링 결과:**
```html
<div>
  <span style="color: red">This should be red</span>
</div>
```

---

#### 3) Attribute Bindings

콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 **`v-bind`를 사용**

```html
<div v-bind:id="dynamicId"></div>
```

```javascript
const dynamicId = ref('my-id')
```

**렌더링 결과:**
```html
<div id="my-id"></div>
```

**중요 규칙:**
- 바인딩 값이 `null`이나 `undefined`인 경우 해당 속성은 렌더링 요소에서 제거됨

---

#### 4) JavaScript Expressions

Vue는 모든 데이터 바인딩 내에서 **JavaScript 표현식**의 모든 기능을 지원

> **JavaScript 표현식**: 하나의 값으로 평가(계산)될 수 있는 모든 코드 조각

**JavaScript 표현식을 사용할 수 있는 위치:**

**1. 콧수염 구문 내부**
```html
{{ number + 1 }}
{{ ok ? 'YES' : 'NO' }}
{{ message.split('').reverse().join('') }}
```

**2. 모든 디렉티브의 속성 값** (`v-`로 시작하는 특수 속성)
```html
<div v-bind:id="`list-${id}`"></div>
```

---

### Expressions 주의사항

**각 바인딩에는 하나의 단일 표현식만 포함될 수 있음**
- 표현식은 값으로 평가할 수 있는 코드 조각 (return 뒤에 사용할 수 있는 코드여야 함)

**❌ 작동하지 않는 경우**

```html
<!-- 표현식이 아닌 선언식 -->
{{ const number = 1 }}

<!-- 제어문은 삼항 표현식을 사용해야 함 -->
{{ if (ok) { return message } }}
```

**✅ 올바른 사용**

```html
<!-- 삼항 연산자 사용 -->
{{ ok ? message : '' }}
```

---

## 2️⃣ Directive

### 정의
**`v-` 접두사가 있는 특수 속성**

Directive는 `v-` 접두사를 가진 특수 속성으로 **DOM 요소에 특정 반응형 동작을 적용하는 명령어**입니다.

### 역할
- `v-if`는 조건에 따라 렌더링하고, `v-for`는 배열을 반복 출력하는 등 다양한 반응형 동작을 연결
- JavaScript 로직을 HTML 템플릿 안에서 선언적으로 사용하여, 코드를 깔끔하고 직관적으로 유지하는 데 도움을 주는 Vue의 강력한 도구

---

### Directive 특징

**Directive의 속성 값은 단일 JavaScript 표현식이어야 함** (`v-for`, `v-on` 제외)

```html
<p v-if="seen">Hi There</p>
```

- 표현식 값(ex: `seen`)이 변경될 때 DOM에 반응적으로 업데이트를 적용

**⚠️ TIP**
- 디렉티브 안에는 if문 같은 문장을 쓸 수 없습니다. 하나의 값으로 귀결되는 표현식만 가능합니다.
- 문자열 리터럴을 값으로 주려면 `'문자열'"`처럼, 따옴표로 한 번 더 감싸야 합니다.

---

### Directive 전체 구문

```html
v-on:submit.prevent="onSubmit"
```

| 구성 요소 | 설명 | 예시 |
|---------|------|------|
| **Name (이름)** | Directive의 핵심 이름으로 어떤 종류의 기능을 수행할지를 의미 | `v-on` |
| **Argument (전달 인자)** | Directive가 '무엇에 대해' 동작할지 알려주는 구체적인 대상 | `:submit` |
| **Modifiers (수식어)** | 점으로 표시되는 특별한 접미사로 Directive의 기본 동작을 수정 | `.prevent` |
| **Value (값)** | Directive에 연결될 JavaScript 표현식 | `"onSubmit"` |

```
v-on:submit.prevent="onSubmit"
└─┬─┘└──┬──┘└──┬───┘ └───┬───┘
Name  Arg   Mod     Value

Starts with v-
Follows the colon
Denoted by the leading dot
Interpreted as JavaScript expressions
```

---

### Directive: Arguments

일부 directive는 directive 뒤에 콜론(`:`)으로 표시되는 **인자를 사용**할 수 있음

**예시 1: v-bind의 인자**
```html
<a v-bind:href="myUrl">Link</a>
```
- `href`는 HTML `<a>` 요소의 href 속성 값을 `myUrl` 값에 바인딩 하도록 하는 `v-bind`의 인자

**예시 2: v-on의 인자**
```html
<button v-on:click="doSomething">Button</button>
```
- `click`은 이벤트를 수신할 이벤트 이름을 작성하는 `v-on`의 인자

---

### Directive: Modifiers

점(`.`)으로 표시되는 특수 접미사로 directive가 특별한 방식으로 바인딩되어야 함을 나타냄

**예시: .prevent 수식어**
```html
<form v-on:submit.prevent="onSubmit">
  <input type="submit">
</form>
```

- `.prevent`는 발생한 이벤트에서 `event.preventDefault()`를 호출하도록 `v-on`에 지시하는 modifier

**⚠️ TIP**
- 하나의 디렉티브에 여러 수식어를 이어서 붙일 수 있습니다. (예: `@click.stop.prevent`)

---

## 3️⃣ Dynamically data binding

### v-bind

**역할**: HTML 태그의 속성(attribute) 값을 Vue의 데이터와 **동적으로 연결(바인딩)**하는 디렉티브

하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 **동적으로 바인딩**

---

### v-bind 사용처

#### 1) Attribute Bindings (속성 바인딩)
#### 2) Class and Style Bindings (클래스 및 스타일 바인딩)

---

## 4️⃣ v-bind (Attribute Bindings)

### 기본 사용법

```html
<img v-bind:src="imageSrc">
<a v-bind:href="myUrl">Link</a>
```

### 약어 (Shorthand)

`v-bind:` → `:`

```html
<img :src="imageSrc">
<a :href="myUrl">Link</a>
```

---

### Dynamic attribute name (동적 인자 이름)

대괄호(`[]`)로 감싸서 directive argument에 JavaScript 표현식을 사용할 수도 있음

**표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨**

```html
<button v-bind:[key]="myValue"></button>
```

```javascript
const key = ref('id')
const myValue = ref('button-1')
```

**렌더링 결과:**
```html
<button id="button-1"></button>
```

**대괄호 안에 작성하는 이름은 반드시 소문자로만 구성 가능** (브라우저가 속성 이름을 소문자로 강제 변환하기 때문)

---

## 5️⃣ Class and Style Bindings

### Class Bindings

`class`와 `style`은 모두 HTML 속성이므로 다른 속성과 마찬가지로 `v-bind`를 사용하여 동적으로 문자열 값을 할당할 수 있음

**단순히 문자열 연결을 사용하여 이러한 값을 생성하는 것은 번거롭고 오류가 발생하기 쉬운 작업**

Vue는 `class` 및 `style` 속성 값을 `v-bind`로 사용할 때 **객체** 또는 **배열**을 활용한 개선 사항을 제공

---

### Binding HTML Classes

#### 1) Binding to Objects (객체 바인딩)

`:class`(v-bind:class의 약어)를 사용하여 클래스를 동적으로 전환

```html
<div :class="{ active: isActive }">Text</div>
```

```javascript
const isActive = ref(true)
```

**렌더링 결과:**
```html
<div class="active">Text</div>
```

**객체에 더 많은 필드를 포함하여 여러 클래스를 전환 가능**

```html
<div class="static" :class="{ active: isActive, 'text-danger': hasError }">
  Text
</div>
```

```javascript
const isActive = ref(true)
const hasError = ref(false)
```

**렌더링 결과:**
```html
<div class="static active">Text</div>
```

---

**반드시 inline 방식으로 작성하지 않아도 됨**

```html
<div :class="classObj">Text</div>
```

```javascript
const isActive = ref(true)
const hasError = ref(false)

const classObj = ref({
  active: isActive,
  'text-danger': hasError
})
```

---

#### 2) Binding to Arrays (배열 바인딩)

`:class`를 배열에 바인딩하여 클래스 목록을 적용

```html
<div :class="[activeClass, errorClass]">Text</div>
```

```javascript
const activeClass = ref('active')
const errorClass = ref('text-danger')
```

**렌더링 결과:**
```html
<div class="active text-danger">Text</div>
```

---

**배열 구문 내에서 객체 구문 사용 가능**

```html
<div :class="[{ active: isActive }, errorClass]">Text</div>
```

```javascript
const isActive = ref(true)
const errorClass = ref('text-danger')
```

**렌더링 결과:**
```html
<div class="active text-danger">Text</div>
```

---

### Binding Inline Styles

#### 1) Binding to Objects (객체 바인딩)

`:style`은 JavaScript 객체 값에 대한 바인딩을 지원 (HTML style 속성에 해당)

```html
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }">Text</div>
```

```javascript
const activeColor = ref('crimson')
const fontSize = ref(30)
```

**렌더링 결과:**
```html
<div style="color: crimson; font-size: 30px;">Text</div>
```

---

**템플릿을 더 깔끔하게 작성하려면 스타일 객체에 직접 바인딩하는 것이 권장됨**

```html
<div :style="styleObj">Text</div>
```

```javascript
const styleObj = ref({
  color: 'crimson',
  fontSize: '30px'
})
```

---

#### 2) Binding to Arrays (배열 바인딩)

여러 스타일 객체를 배열에 작성해서 `:style`을 바인딩하면 작성한 객체들이 병합되어 동일한 요소에 적용

```html
<div :style="[styleObj1, styleObj2]">Text</div>
```

```javascript
const styleObj1 = ref({
  color: 'crimson',
  fontSize: '30px'
})

const styleObj2 = ref({
  backgroundColor: 'lightgray'
})
```

**렌더링 결과:**
```html
<div style="color: crimson; font-size: 30px; background-color: lightgray;">Text</div>
```

---

## 6️⃣ Event Handling

### v-on

**역할**: DOM 요소에 이벤트 리스너를 연결 및 수신

---

### v-on 구성

```html
v-on:event="handler"
```

- **event**: 수신할 이벤트 이름
  - 클릭, 입력, 키보드 입력 등 다양한 DOM 이벤트를 청취할 수 있음
  
- **handler**: 이벤트가 발생했을 때 실행할 JavaScript 코드
  - 2가지 작성 방식 존재
    1. **Inline handlers**: 이벤트가 트리거 될 때 실행될 JavaScript 코드
    2. **Method handlers**: 컴포넌트에 정의된 메서드 이름

---

### 약어 (Shorthand)

`v-on:` → `@`

```html
<button @click="doSomething">Click</button>
```

---

### 1) Inline handlers

이벤트가 트리거 될 때 실행될 JavaScript 코드

주로 간단한 상황에 사용

```html
<button @click="count++">Add 1</button>
<p>Count: {{ count }}</p>
```

```javascript
const count = ref(0)
```

---

### 2) Method handlers

컴포넌트에 정의된 메서드를 가리키는 속성 이름 또는 경로

```html
<button @click="myFunc">Hello</button>
```

```javascript
const name = ref('Alice')

const myFunc = function() {
  console.log(`Hello, ${name.value}!`)
}
```

**Method handler는 이를 트리거 한 기본 DOM Event 객체를 자동으로 수신**

```javascript
const myFunc = function(event) {
  console.log(event)        // 이벤트 객체
  console.log(event.target) // 이벤트가 발생한 요소
}
```

---

### Inline Handlers에서의 메서드 호출

메서드 이름에 직접 바인딩하는 대신 inline handlers에서 메서드를 호출할 수도 있음

**이를 통해 기본 이벤트 대신 사용자 지정 인자를 전달할 수 있음**

```html
<button @click="greeting('hello')">Say hello</button>
<button @click="greeting('bye')">Say bye</button>
```

```javascript
const greeting = function(message) {
  console.log(message)
}
```

---

### Inline Handlers에서의 event 객체 접근

inline handlers에서 원본 DOM 이벤트에 접근하기

**특별한 `$event` 변수를 사용하여 메서드에 전달**

```html
<button @click="warning('경고입니다', $event)">Submit</button>
```

```javascript
const warning = function(message, event) {
  console.log(message)     // '경고입니다'
  console.log(event)       // 이벤트 객체
  console.log(event.target) // 이벤트가 발생한 요소
}
```

---

## 7️⃣ Event Modifiers

### 이벤트 수식어 (Modifiers)

Vue는 `v-on`에 대한 **Event Modifiers**를 제공해 `event.preventDefault()`와 같은 구문을 메서드에서 작성하지 않도록 함

```html
<form @submit.prevent="onSubmit">
  <input type="submit">
</form>
```

```javascript
const onSubmit = function() {
  console.log('Form submitted!')
  // event.preventDefault() 불필요!
}
```

---

### 주요 Event Modifiers

| 수식어 | 설명 |
|--------|------|
| `.stop` | 이벤트 전파 중단 (`event.stopPropagation()`) |
| `.prevent` | 기본 동작 방지 (`event.preventDefault()`) |
| `.self` | 이벤트가 해당 요소 자체에서 발생한 경우에만 핸들러 실행 |
| `.capture` | 캡처 모드에서 이벤트 수신 |
| `.once` | 이벤트를 한 번만 트리거 |
| `.passive` | 이벤트의 기본 동작을 취소할 수 없도록 설정 |

---

### Modifiers 예시

#### .prevent
폼 제출 시 페이지 새로고침 방지

```html
<form @submit.prevent="onSubmit">
  <input type="submit">
</form>
```

#### .stop
클릭 이벤트 전파 중단

```html
<div @click="parentClick">
  <button @click.stop="childClick">클릭</button>
</div>
```

```javascript
const parentClick = function() {
  console.log('Parent clicked')
}

const childClick = function() {
  console.log('Child clicked')
  // 부모의 parentClick은 실행되지 않음
}
```

---

### Key Modifiers

Vue는 키보드 이벤트를 수신할 때 특정 키에 대한 Modifiers를 사용할 수 있음

```html
<!-- key가 Enter일 때만 submit 함수 호출 -->
<input @keyup.enter="submit">
```

```html
<!-- key가 Delete 또는 Backspace일 때만 remove 함수 호출 -->
<input @keyup.delete="remove">
```

---

### Key Modifiers 종류

**주요 Key Modifiers:**
- `.enter`
- `.tab`
- `.delete` (Delete와 Backspace 모두 캡처)
- `.esc`
- `.space`
- `.up`
- `.down`
- `.left`
- `.right`
- `.ctrl`
- `.alt`
- `.shift`
- `.meta` (Mac: Command, Windows: Windows 키)

---

## 8️⃣ Form Input Bindings

### v-bind와 v-on을 함께 사용

**form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScript 상태에 동기화해야 하는 경우**

```html
<p>{{ inputText }}</p>
<input :value="inputText" @input="onInput">
```

```javascript
const inputText = ref('')

const onInput = function(event) {
  inputText.value = event.target.value
}
```

**동작 흐름:**
1. `v-bind`를 사용하여 input 요소의 `value` 속성 값을 `inputText` 값과 동기화
2. `v-on`을 사용하여 input 이벤트가 발생할 때마다 `inputText` 값을 업데이트

---

## 9️⃣ v-model

### 정의

**form input 요소** 또는 **컴포넌트**에서 **양방향 바인딩**을 만듦

---

### v-model의 역할

`v-model`을 사용하여 위 예시 코드를 간결하게 작성 가능

```html
<p>{{ inputText }}</p>
<input v-model="inputText">
```

```javascript
const inputText = ref('')
```

---

### v-model의 본질

**`v-model`은 사용자 입력 데이터와 JavaScript 데이터 간의 양방향 바인딩을 만듦**

**내부적으로는 다음 두 가지의 조합:**

1. **`v-bind`**: 데이터를 input의 value에 연결
2. **`v-on`**: input 이벤트를 감지해 데이터 업데이트

```html
<!-- 이 두 코드는 동일한 동작을 수행 -->

<!-- v-model 사용 -->
<input v-model="inputText">

<!-- v-bind + v-on 조합 -->
<input :value="inputText" @input="inputText = $event.target.value">
```

---

### v-model 활용

**1) 단일행 입력 (text input)**

```html
<p>Message: {{ message }}</p>
<input v-model="message" placeholder="메시지 입력">
```

```javascript
const message = ref('')
```

---

**2) 여러 줄 입력 (textarea)**

```html
<p style="white-space: pre-line;">{{ text }}</p>
<textarea v-model="text" placeholder="여러 줄을 입력하세요"></textarea>
```

```javascript
const text = ref('')
```

> **주의**: `<textarea>{{ text }}</textarea>`는 작동하지 않음. `v-model`을 사용해야 함

---

**3) 체크박스 (checkbox)**

**단일 체크박스:**
```html
<input type="checkbox" id="checkbox" v-model="checked">
<label for="checkbox">{{ checked }}</label>
```

```javascript
const checked = ref(false)
```

---

**여러 체크박스:**
배열을 사용하여 여러 체크박스의 선택 값을 관리

```html
<div>Checked names: {{ checkedNames }}</div>

<input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
<label for="alice">Alice</label>

<input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
<label for="bella">Bella</label>

<input type="checkbox" id="cathy" value="Cathy" v-model="checkedNames">
<label for="cathy">Cathy</label>
```

```javascript
const checkedNames = ref([])
```

**결과**: `checkedNames` 배열에 선택된 값들이 추가됨
- 예: `['Alice', 'Cathy']`

---

**4) 라디오 (radio)**

```html
<div>Picked: {{ picked }}</div>

<input type="radio" id="one" value="One" v-model="picked">
<label for="one">One</label>

<input type="radio" id="two" value="Two" v-model="picked">
<label for="two">Two</label>
```

```javascript
const picked = ref('')
```

---

**5) 드롭다운 (select)**

**단일 선택:**
```html
<div>Selected: {{ selected }}</div>

<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>Alice</option>
  <option>Bella</option>
  <option>Cathy</option>
</select>
```

```javascript
const selected = ref('')
```

---

**다중 선택:**
```html
<div>Selected: {{ selected }}</div>

<select v-model="selected" multiple>
  <option>Alice</option>
  <option>Bella</option>
  <option>Cathy</option>
</select>
```

```javascript
const selected = ref([])
```

**결과**: `selected` 배열에 선택된 옵션들이 추가됨

---

### v-model Modifiers

#### .lazy
`input` 대신 `change` 이벤트 이후에 동기화

```html
<!-- input 이벤트마다 업데이트되지 않고 -->
<!-- change 이벤트(포커스를 잃을 때) 이후에 업데이트 -->
<input v-model.lazy="msg">
```

```javascript
const msg = ref('')
```

---

#### .number
사용자 입력을 자동으로 숫자로 형변환

```html
<input v-model.number="age" type="number">
```

```javascript
const age = ref(0)
```

> `type="number"`를 사용하는 경우에도 값은 문자열로 반환됨. `.number` 수식어를 사용하면 자동으로 숫자 타입으로 변환

---

#### .trim
사용자 입력의 앞뒤 공백을 자동으로 제거

```html
<input v-model.trim="msg">
```

```javascript
const msg = ref('')
```

---

## 🔟 참고사항

### 접두어 `$`

#### `$` 접두어가 붙은 변수

**Vue 인스턴스 내에서 사용할 수 있도록 Vue가 제공하는 공용 프로퍼티**

- 사용자가 지정한 반응형 변수나 메서드와 구분하기 위함
- 주로 Vue 인스턴스 내부 상태를 다룰 때 사용

**예시:**
- `$event`: 이벤트 객체
- `$el`: 컴포넌트의 루트 DOM 요소
- `$data`: 컴포넌트의 data 객체
- `$props`: 컴포넌트의 props 객체

**⚠️ TIP**
- 내가 만드는 데이터와 메서드 이름에 `$`나 `_` 접두사를 사용하지 않는 것이 좋습니다
- `_`로 시작하는 속성은 내부용이므로 직접 사용하면 안 됩니다. 예고 없이 변경될 수 있습니다

---

### IME (Input Method Editor)

#### 정의
사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 **운영 체제 구성 프로그램**

- 일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함

#### 문제점
IME가 활성화된 상태(예: 한글 조합 중)에서 input 이벤트가 발생하는 방식과 `v-model`의 업데이트 방식이 충돌하여 **의도치 않은 동작이 발생**할 수 있음

**예시:**
- 한글로 "안녕"을 입력하는 경우
- "ㅇ" → "아" → "안" → "안ㄴ" → "안녀" → "안녕" 각 단계마다 input 이벤트가 발생
- 조합이 완성되기 전에도 데이터가 업데이트되어 의도치 않은 동작 발생 가능

#### 해결 방법
**`.lazy` 수식어 사용**

```html
<input v-model.lazy="text">
```

```javascript
const text = ref('')
```

**⚠️ 주의점**
- 데이터가 실시간으로 반영되지 않고, 사용자가 입력을 마친 후 다른 곳을 클릭하는 등 **포커스를 잃었을 때** 한 번에 반영됩니다

---

## 📝 핵심 키워드 정리

| 개념 | 설명 | 예시 |
|------|------|------|
| **템플릿 구문** | HTML 기반의 Vue 전용 구문 | `{{ msg }}` `<div v-if>` |
| **디렉티브 (Directive)** | `v-` 접두사가 있는 특수 속성 | `<p v-if="seen">` |
| **v-bind** | HTML 속성을 동적으로 바인딩 | `<img :src="imageSrc">` |
| **v-on** | DOM 이벤트 수신 및 핸들러 연결 | `<button @click="myFunc">` |
| **이벤트 수식어** | 이벤트 동작을 제어하는 특별 접미사 | `@submit.prevent="onSubmit"` |
| **v-model** | 폼 요소에 양방향 바인딩 설정 | `<input v-model="message">` |
| **데이터 바인딩** | JS 데이터와 HTML 화면을 동기화 | `{{ msg }}` |

---

## 📋 요약 정리

### Template Syntax (템플릿 구문)
Vue가 HTML을 기반으로 사용하는 특별한 문법으로, 이를 통해 DOM과 Vue 인스턴스의 데이터를 선언적으로 연결(바인딩) 가능

---

### Directive (디렉티브)
`v-` 접두사가 붙는 특수 속성으로 DOM에 특정 반응형 동작을 적용하는 명령어

**디렉티브의 값으로는 단일 JavaScript 표현식만 사용 가능**

---

### v-bind (데이터 바인딩)
`v-bind`는 HTML 태그의 속성 값을 Vue의 데이터와 동적으로 연결하는 디렉티브

**약어(shorthand)는 콜론(`:`)을 사용**

`v-bind`를 사용하면 데이터 값의 변경에 따라 `src`, `href` 같은 HTML 속성을 실시간으로 업데이트 가능

---

### 클래스와 스타일 바인딩
Class와 style 속성에 `v-bind`를 사용하면 **객체나 배열**을 활용해 여러 클래스와 스타일을 조건부로 동적 적용할 수 있어 편리

---

### v-on (이벤트 핸들링)
`v-on`은 `click`, `submit`과 같은 DOM 이벤트가 발생했을 때 지정된 JavaScript 코드를 실행하는 디렉티브

**약어(shorthand)는 `@` 기호를 사용**

---

### 이벤트 수식어 (Modifiers)
`.prevent` (기본 동작 방지), `.stop` (이벤트 전파 중단)과 같이 디렉티브 뒤에 점(`.`)으로 붙여 이벤트의 동작을 제어하는 특별한 접미사

---

### v-model (폼 입력 양방향 바인딩)
`v-model`은 `<input>`, `<textarea>`, `<select>` 같은 폼 요소에서 사용하며, 사용자의 입력과 Vue 데이터를 실시간으로 동기화하는 **양방향 바인딩**을 생성

**특징:**
- 사용자가 입력 필드에 값을 입력하면 연결된 데이터가 즉시 업데이트
- 데이터 값이 변경되면 입력 필드의 값도 자동으로 변경

**본질:**
사실 `v-model`은 `v-bind`로 값을 연결하고 `v-on`으로 입력 이벤트를 감지하여 값을 변경하는 두 동작을 합친 축약형

```html
<!-- 동일한 동작 -->
<input v-model="text">
<input :value="text" @input="text = $event.target.value">
```

---

## ✅ 확인 문제 정답

1. **c) 디렉티브** - `v-` 접두사가 붙는 Vue의 특수 속성
2. **d) v-bind** - HTML 속성을 데이터에 동적으로 연결
3. **d) :** - v-bind 디렉티브의 약어(shorthand)
4. **b) :class="{ active: isActive }"** - 클래스를 동적으로 적용하는 방법
5. **a) v-on** - DOM 이벤트를 수신하는 디렉티브
6. **b) @** - v-on 디렉티브의 약어(shorthand)
7. **c) .prevent** - 이벤트의 기본 동작을 막는 수식어(modifier)
8. **c) $event** - 인라인 핸들러에서 event 객체에 접근하는 방법
9. **d) v-model** - 폼 요소에 양방향 바인딩을 만드는 디렉티브
10. **c) v-bind와 v-on** - v-model은 내부적으로 이 두 디렉티브의 조합
11. **b) {{ }}** - HTML 속성이 아닌 곳에서 데이터를 표시하는 구문
12. **a) :[dynamicArg]="value"** - 디렉티브의 인자를 동적으로 지정하는 방법

---

## 🎯 최종 정리

### 디렉티브 비교표

| 디렉티브 | 역할 | 약어 | 예시 |
|---------|------|------|------|
| `v-bind` | 속성을 데이터에 바인딩 | `:` | `:src="url"` |
| `v-on` | 이벤트를 수신하고 처리 | `@` | `@click="handler"` |
| `v-model` | 양방향 바인딩 (v-bind + v-on) | 없음 | `v-model="text"` |
| `v-if` | 조건부 렌더링 | 없음 | `v-if="show"` |
| `v-for` | 리스트 렌더링 | 없음 | `v-for="item in items"` |
| `v-show` | 조건부 표시 (display 토글) | 없음 | `v-show="visible"` |

---

### 바인딩 방식 비교

```html
<!-- 1. 단방향 바인딩 (v-bind) -->
<input :value="message">
<!-- 데이터 → 화면 (한 방향) -->

<!-- 2. 이벤트 처리 (v-on) -->
<input @input="updateMessage">
<!-- 화면 → 데이터 (한 방향) -->

<!-- 3. 양방향 바인딩 (v-model) -->
<input v-model="message">
<!-- 데이터 ↔ 화면 (양 방향) -->
```

---

## 🚀 실전 활용 팁

### 1. 클래스 바인딩 실전 예제

```html
<template>
  <button 
    :class="{ 
      'btn': true,
      'btn-primary': isPrimary,
      'btn-large': isLarge,
      'disabled': isDisabled 
    }"
    @click="handleClick"
  >
    {{ buttonText }}
  </button>
</template>

<script setup>
import { ref } from 'vue'

const isPrimary = ref(true)
const isLarge = ref(false)
const isDisabled = ref(false)
const buttonText = ref('클릭하세요')

const handleClick = () => {
  if (!isDisabled.value) {
    console.log('버튼 클릭됨!')
  }
}
</script>
```

---

### 2. 폼 유효성 검사 예제

```html
<template>
  <form @submit.prevent="onSubmit">
    <input 
      v-model.trim="username" 
      @input="validateUsername"
      :class="{ 'error': usernameError }"
      placeholder="사용자명"
    >
    <p v-if="usernameError" class="error-message">
      {{ usernameError }}
    </p>
    
    <input 
      v-model.number="age" 
      type="number"
      placeholder="나이"
    >
    
    <button type="submit" :disabled="!isValid">
      제출
    </button>
  </form>
</template>

<script setup>
import { ref, computed } from 'vue'

const username = ref('')
const age = ref(0)
const usernameError = ref('')

const validateUsername = () => {
  if (username.value.length < 3) {
    usernameError.value = '사용자명은 3자 이상이어야 합니다'
  } else {
    usernameError.value = ''
  }
}

const isValid = computed(() => {
  return username.value.length >= 3 && age.value > 0
})

const onSubmit = () => {
  if (isValid.value) {
    console.log('제출:', { username: username.value, age: age.value })
  }
}
</script>
```
