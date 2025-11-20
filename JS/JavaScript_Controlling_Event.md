# JavaScript Controlling Event

## 📚 목차

1. [이벤트](#이벤트)
2. [event](#event)
3. [event object](#event-object)
4. [event handler](#event-handler)
5. [버블링](#버블링)
6. [캡처링과 버블링](#캡처링과-버블링)
7. [버블링의 필요성](#버블링의-필요성)
8. [event handler 활용](#event-handler-활용)
9. [이벤트 기본 동작 취소하기](#이벤트-기본-동작-취소하기)
10. [참고](#참고)
11. [실습 예제](#실습-예제)
12. [핵심 정리](#핵심-정리)

---

## 🎯 학습 목표

- `addEventListener`를 사용해 이벤트 핸들러를 등록할 수 있다.
- 이벤트 핸들러의 event 객체를 활용해 정보를 얻을 수 있다.
- 이벤트 버블링의 개념과 전파 과정을 설명할 수 있다.
- `event.target`과 `event.currentTarget`의 차이점을 이해한다.
- 이벤트 버블링을 활용하여 상위 요소에 이벤트를 위임한다.
- `event.preventDefault()`로 요소의 기본 동작을 취소한다.
- DOM 조작과 이벤트를 결합하여 동적인 웹을 구현한다.

---

## 🌟 시작하기

웹 페이지를 하나의 **'카페'**라고 상상해봅시다. 손님의 주문은 어떻게 처리될까요?

카페에서 손님이 주문하는 과정을 살펴봅시다.

1. 손님이 키오스크에서 하는 **'주문'** (클릭, 입력 등)이 바로 **이벤트**입니다.

2. 이 주문을 받는 키오스크가 **이벤트 리스너**입니다.

3. 주문에 맞춰 커피를 만드는 바리스타의 행동이 **이벤트 핸들러**입니다.

웹 페이지에서 다양한 클릭, 입력을 받아 처리하는 방식을 학습합니다.

학습 후 카페에서 손님이 주문하는 과정과 웹에서의 이벤트 처리 방식을 비교하면서 학습을 마무리합니다.

---

## 이벤트

### 일상 속의 이벤트

- 컴퓨터 키보드를 눌러 텍스트를 입력하는 것
- 전화벨이 울려 전화가 왔음을 알리는 것
- 손을 흔들어 인사하는 것
- 전화기의 버튼을 눌러서 통화를 시작하는 것
- 리모컨을 사용하여 채널을 변경하는 것

### 웹에서의 이벤트

- 화면을 스크롤하는 것
- 버튼을 클릭했을 때 팝업 창이 출력되는 것
- 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
- 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것

> **💡 중요**: 웹에서의 거의 모든 상호작용은 이벤트와 함께 합니다.

---

## event

### event란?

**event**
- 웹 페이지 상에서 **'무언가 일어났다는 신호 또는 사건'**

JS 이벤트는 **'영화 서비스'**와 같습니다.

우리가 보고 싶은 영화 포스터에 마우스를 올리면(이벤트) 시스템은 마우스의 움직임을 감지(리스너)하고 작은 미리보기 영상이나 설명을 보여주는(핸들러) 반응을 보입니다.

마우스 움직임 하나하나가 이벤트가 될 수 있고 이러한 다양한 클릭, 입력, 변경하는 행위가 이벤트에 해당합니다.

### DOM 요소와 이벤트

**DOM 요소**
- HTML 문서의 각 태그를 하나의 객체로 변환한 것
- 모든 DOM 요소는 다양한 형태의 이벤트를 발생시킬 수 있음

**예시**
- `button`을 클릭하면 `click` 이벤트
- `input` 값 변경 시 `input` 이벤트

```
document
  └─ Root element: <html>
      ├─ Element: <head>
      │   └─ Element: <title>
      │       └─ Text: "My title"
      └─ Element: <body>
          ├─ Element: <h1>
          │   └─ Text: "heading"
          └─ Element: <a>
              ├─ Attribute: href
              └─ Text: "Link text"
```

---

## event object

### event object란?

DOM에서 이벤트가 발생하면 브라우저는 해당 이벤트에 관한 정보를 담은 **'event object'**를 자동으로 생성합니다.

### 이벤트 종류

- **mouse**: 마우스 관련 이벤트
- **input**: 입력 관련 이벤트
- **keyboard**: 키보드 관련 이벤트
- 기타 다양한 이벤트들

> **💡 참고**: [MDN Event 문서](https://developer.mozilla.org/en-US/docs/Web/API/Event)

이벤트 객체는 이벤트 발생 순간의 상황(어떤 요소에서 이벤트가 발생했는지, 마우스 좌표는 어디인지, 눌린 키는 무엇인지 등)과 관련된 상세 정보를 담고 있습니다.

이를 통해 이벤트와 관련된 구체적인 정보를 참조할 수 있습니다.

### event handler

DOM 요소에서 event가 발생하면 해당 event는 연결된 이벤트 처리기(event handler)에 의해 처리됩니다.

```
Event (Order)  →  Event Handler (Barista)  →  Preparing coffee
```

---

## event handler

### event handler란?

**event handler**
- 특정 이벤트가 발생했을 때 실행되는 **(콜백)함수**

보통 `addEventListener`를 통해 DOM 요소에 event handler를 등록합니다.

### addEventListener()

**addEventListener()**
- 특정 DOM 요소에, 지정한 이벤트가 발생했을 때 실행할 이벤트 핸들러를 등록하는 메서드
- 이벤트 핸들러(콜백 함수)를 DOM 요소에 연결하는 역할을 담당

### addEventListener() 예시

```javascript
const button = document.querySelector('button')

// 이벤트 핸들러
const handleClick = function () {
  window.alert('버튼이 클릭 되었습니다!')
}

// addEventListener 메서드를 이용해 버튼에 이벤트 핸들러를 등록
button.addEventListener('click', handleClick)
```

`handleClick` 함수가 이벤트 핸들러이고, `button.addEventListener()`는 그 핸들러를 click 이벤트에 연결해주는 역할을 합니다.

### 이벤트 등록 (addEventListener)

**구조**: `EventTarget.addEventListener(type, handler)`

- **DOM 요소**: HTML 문서의 각 태그를 하나의 객체로 변환한 것
- **수신할 이벤트**: 무언가 일어났다는 신호 또는 사건
- **핸들러**: 특정 이벤트가 발생했을 때 실행되는 (콜백)함수

```javascript
// DOM 요소     리스너           핸들러
button.addEventListener('click', handleClick)
```

### addEventListener 구조

**메서드 구문**

```javascript
element.addEventListener('click', function (event) {
  // 이벤트 처리 로직
})
```

#### type
- 수신할 이벤트 유형
- 문자열로 작성 (예: `'click'`, `'mouseover'` 등)

#### handler
- 이벤트 발생 시 호출되는 콜백 함수
- 자동으로 event 객체를 첫 번째 매개변수로 받음
- 반환 값 없음

### 이벤트 객체 전달

```javascript
const btn = document.querySelector('button')

// 1. 이벤트 핸들러에서 event 객체를 매개변수로 받음
btn.addEventListener('click', function (event) {
  // 2. event 객체 출력
  console.log(event)
})
```

이벤트가 발생하면 브라우저는 자동으로 event 객체를 생성하고, 이를 이벤트 핸들러의 첫 번째 인자로 전달합니다.

### 이벤트 객체가 필요한 이유

**1. 이벤트 발생 요소 파악**

```javascript
const divTag = document.querySelector('div')

divTag.addEventListener('click', function (event) {
  console.log(event.target)
})
```

**2. 이벤트 타입 파악**

```javascript
const divTag = document.querySelector('div')

divTag.addEventListener('click', function (event) {
  console.log(event.type)  // 'click'
})
```

**3. 키보드 이벤트에서 입력한 키 확인**

```javascript
const inputTag = document.querySelector('input')

inputTag.addEventListener('keydown', function (event) {
  console.log(event.key)
})
```

---

## 버블링

### 이벤트 버블링 (Event Bubbling)

**버블링**
- 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상
- 가장 최상단의 조상 요소(`document`)를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작

> **비유**: 물속에서 공기 방울이 위로 올라가는 것처럼, 이벤트가 자식 요소에서 부모 요소로 전파되는 현상

### 버블링 예시

```html
<div class="outer">
  outer
  <div class="middle">
    middle
    <div class="inner">inner</div>
  </div>
</div>
```

```javascript
const divTags = document.querySelectorAll('div')

divTags.forEach(function (divTag) {
  divTag.addEventListener('click', function (event) {
    console.log(event.currentTarget.className)
  })
})
```

**inner를 클릭했을 때 출력 결과:**
```
inner
middle
outer
```

inner를 클릭하면 inner → middle → outer 순서로 핸들러가 실행됩니다.

### 버블링이 필요한 이유

**상황**: 각기 다른 동작을 수행하는 버튼이 여러 개 있을 때

```html
<div id="container">
  <button id="btn1">버튼1</button>
  <button id="btn2">버튼2</button>
  <button id="btn3">버튼3</button>
</div>
```

**버블링을 사용하지 않을 경우**

```javascript
const btn1 = document.querySelector('#btn1')
const btn2 = document.querySelector('#btn2')
const btn3 = document.querySelector('#btn3')

btn1.addEventListener('click', function (event) {
  console.log('버튼1 클릭')
})

btn2.addEventListener('click', function (event) {
  console.log('버튼2 클릭')
})

btn3.addEventListener('click', function (event) {
  console.log('버튼3 클릭')
})
```

각 버튼마다 이벤트 핸들러를 등록해야 하므로:
- 코드의 중복이 발생
- 버튼이 늘어날수록 핸들러 등록 코드도 늘어남

### 이벤트 위임 (Event Delegation)

**버블링을 활용한 해결 방법**

```javascript
const container = document.querySelector('#container')

container.addEventListener('click', function (event) {
  if (event.target.tagName === 'BUTTON') {
    console.log(`${event.target.id} 클릭`)
  }
})
```

**장점:**
- 하나의 핸들러로 여러 요소를 관리
- 동적으로 추가되는 요소에도 자동으로 적용
- 메모리 효율적

---

## 캡처링과 버블링

### 이벤트 전파 단계

이벤트는 3가지 단계로 전파됩니다:

1. **캡처링 단계 (Capturing phase)**: 이벤트가 최상위 요소에서 타겟 요소로 전파
2. **타겟 단계 (Target phase)**: 이벤트가 실제 타겟 요소에 도달
3. **버블링 단계 (Bubbling phase)**: 이벤트가 타겟 요소에서 최상위 요소로 전파

```
document (캡처링 시작)
   ↓
 html
   ↓
 body
   ↓
 div (타겟)
   ↑
 body
   ↑
 html
   ↑
document (버블링 끝)
```

### 캡처링 단계에서 이벤트 감지

기본적으로 `addEventListener`는 버블링 단계에서 이벤트를 감지하지만, 세 번째 인자로 `true`를 전달하면 캡처링 단계에서 이벤트를 감지할 수 있습니다.

```javascript
element.addEventListener('click', handler, true)
```

### target과 currentTarget

**event.target**
- 이벤트가 실제로 발생한 요소 (가장 안쪽 요소)
- 버블링이 진행되어도 변하지 않음

**event.currentTarget**
- 현재 이벤트 핸들러가 연결된 요소
- 일반 함수에서 `this`와 동일

```javascript
const outer = document.querySelector('.outer')

outer.addEventListener('click', function (event) {
  console.log('target:', event.target)           // 실제 클릭한 요소
  console.log('currentTarget:', event.currentTarget)  // outer (핸들러가 등록된 요소)
  console.log('this:', this)                     // outer (currentTarget과 동일)
})
```

### 버블링 중단

**stopPropagation()**
- 이벤트의 전파를 중단하는 메서드
- 현재 요소에서 이벤트 처리를 마친 후 상위 요소로의 전파를 막음

```javascript
const inner = document.querySelector('.inner')

inner.addEventListener('click', function (event) {
  console.log('inner 클릭')
  event.stopPropagation()  // 여기서 버블링 중단
})
```

> **⚠️ 주의**: 필요한 경우가 아니라면 버블링을 중단하지 않는 것이 좋습니다. 상위 요소의 이벤트 처리가 의도치 않게 차단될 수 있습니다.

---

## event handler 활용

### 1. click 이벤트

**버튼 클릭 이벤트 실습**

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .clicked {
      background-color: crimson;
      color: white;
    }
  </style>
</head>
<body>
  <button id="btn">버튼</button>

  <script>
    // 1. 버튼 선택
    const btn = document.querySelector('#btn')

    // 2. 버튼에 이벤트 핸들러를 부착
    // 버튼을 클릭하면 함수가 실행됨
    btn.addEventListener('click', function (event) {
      console.log(event)
      console.log(event.currentTarget)

      // 3. 버튼에 clicked 클래스 토글
      event.currentTarget.classList.toggle('clicked')
    })
  </script>
</body>
</html>
```

### 2. input 이벤트

**실시간 입력 값 감지**

```html
<!DOCTYPE html>
<html>
<body>
  <input type="text" id="text-input">
  <p id="output"></p>

  <script>
    // 1. input 요소 선택
    const inputTag = document.querySelector('#text-input')
    const outputTag = document.querySelector('#output')

    // 2. input 이벤트 핸들러 부착
    inputTag.addEventListener('input', function (event) {
      // 3. 입력된 값을 실시간으로 출력
      outputTag.textContent = event.currentTarget.value
    })
  </script>
</body>
</html>
```

### 3. click & input 이벤트 종합

**할 일 관리 실습**

```html
<!DOCTYPE html>
<html>
<body>
  <input type="text" class="input-text">
  <button id="btn">버튼</button>
  <ul></ul>

  <script>
    // 1. 필요한 요소 선택
    const inputTag = document.querySelector('.input-text')
    const btn = document.querySelector('#btn')
    const ulTag = document.querySelector('ul')

    // 2. 버튼에 이벤트 핸들러를 부착
    const addTodo = function (event) {
      // 2-1. 사용자 입력 데이터 가져오기
      const inputData = inputTag.value

      // 2-2. 입력 데이터가 공백이 아닐 경우에만 진행
      if (inputData.trim()) {
        // 2-3. 데이터를 저장할 li 요소를 생성
        const liTag = document.createElement('li')

        // 2-4. li 요소 컨텐츠에 데이터 입력
        liTag.textContent = inputData

        // 2-5. li 요소를 부모 ul 요소의 자식 요소로 추가
        ulTag.appendChild(liTag)

        // 2-6. 입력 필드 초기화
        inputTag.value = ''
      } else {
        alert('할 일을 입력하세요!')
      }
    }

    btn.addEventListener('click', addTodo)
  </script>
</body>
</html>
```

### 4. change 이벤트

**입력이 끝난 후 발생하는 이벤트**

```javascript
const inputTag = document.querySelector('#text-input')

inputTag.addEventListener('change', function (event) {
  console.log('입력이 끝났습니다:', event.currentTarget.value)
})
```

**input vs change**
- `input`: 입력 값이 변경될 때마다 실시간으로 발생
- `change`: 입력이 완료되고 포커스를 잃었을 때 발생

### 5. submit 이벤트

**form 제출 이벤트**

```html
<!DOCTYPE html>
<html>
<body>
  <form id="my-form">
    <input type="text" name="username">
    <button type="submit">제출</button>
  </form>

  <script>
    const formTag = document.querySelector('#my-form')

    formTag.addEventListener('submit', function (event) {
      // 기본 동작(페이지 새로고침) 방지
      event.preventDefault()
      
      console.log('form이 제출되었습니다')
    })
  </script>
</body>
</html>
```

---

## 이벤트 기본 동작 취소하기

### preventDefault()

**event.preventDefault()**
- 이벤트의 기본 동작을 취소하는 메서드
- 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

### 1. copy 이벤트 동작 취소

복사 이벤트를 실행하지 못하도록 하기 (콘텐츠를 복사하는 것을 방지)

```html
<!DOCTYPE html>
<html>
<body>
  <h1>중요한 내용</h1>

  <script>
    const h1Tag = document.querySelector('h1')

    h1Tag.addEventListener('copy', function (event) {
      console.log(event)
      event.preventDefault()
      alert('복사 할 수 없습니다.')
    })
  </script>
</body>
</html>
```

### 2. form 제출 시 페이지 새로고침 동작 취소

form 요소의 submit 동작(action 값으로 요청)을 취소 시킴

```html
<!DOCTYPE html>
<html>
<body>
  <form id="my-form">
    <input type="text" name="username">
    <button type="submit">Submit</button>
  </form>

  <script>
    const formTag = document.querySelector('#my-form')

    const handleSubmit = function (event) {
      event.preventDefault()
      console.log('form 제출 완료')
    }

    formTag.addEventListener('submit', handleSubmit)
  </script>
</body>
</html>
```

실습 시 submit 버튼을 눌러도 새로고침이 안되는 것을 확인할 수 있습니다.

---

## 참고

### addEventListener와 화살표 함수 관계

#### 화살표 함수 특징

**화살표 함수**
- `function` 키워드 대신 `=>`를 사용해 함수를 간결하게 표현하는 문법
- 화살표 함수는 자신만의 `this`를 가지지 않음
- 대신, 자신이 선언된 상위 스코프의 `this`를 그대로 물려받아 사용

따라서 이벤트 핸들러로 화살표 함수를 사용하면 `this`는 대부분 전역 객체(`window`)를 가리키게 됩니다.

#### 해결책

**1. 일반 함수로 사용하기**

```javascript
const element = document.querySelector('#function')

element.addEventListener('click', function () {
  console.log(this)  // <button id="function">
})
```

**2. 화살표 함수일 경우 event.currentTarget을 사용하기**

```javascript
const element = document.querySelector('#arrow')

element.addEventListener('click', (event) => {
  console.log(this)  // window
  console.log(event.currentTarget)  // <button id="arrow">
})
```

---

## 실습 예제

### 예제 1: 버튼 클릭 카운터

```html
<!DOCTYPE html>
<html>
<body>
  <button id="counter-btn">클릭 횟수: 0</button>

  <script>
    const btn = document.querySelector('#counter-btn')
    let count = 0

    btn.addEventListener('click', function () {
      count++
      this.textContent = `클릭 횟수: ${count}`
    })
  </script>
</body>
</html>
```

### 예제 2: 테마 전환 버튼

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      transition: background-color 0.3s;
    }
    body.dark-mode {
      background-color: #1a1a1a;
      color: white;
    }
  </style>
</head>
<body>
  <button id="theme-btn">다크 모드</button>

  <script>
    const themeBtn = document.querySelector('#theme-btn')

    themeBtn.addEventListener('click', function () {
      document.body.classList.toggle('dark-mode')
      
      if (document.body.classList.contains('dark-mode')) {
        this.textContent = '라이트 모드'
      } else {
        this.textContent = '다크 모드'
      }
    })
  </script>
</body>
</html>
```

### 예제 3: 욕설 필터링

```html
<!DOCTYPE html>
<html>
<body>
  <input type="text" id="text-input">
  <p id="output"></p>

  <script>
    const inputTag = document.querySelector('#text-input')
    const outputTag = document.querySelector('#output')
    const badWords = ['바보', '멍청이']

    inputTag.addEventListener('input', function (event) {
      let text = event.currentTarget.value

      badWords.forEach(word => {
        text = text.replaceAll(word, '***')
      })

      outputTag.textContent = text
    })
  </script>
</body>
</html>
```

---

## 확인 문제

### 문제

**1. 특정 이벤트가 발생했을 때 실행되는 함수는?**
- a) 이벤트 리스너
- b) 이벤트 객체
- c) 이벤트 핸들러 ✅
- d) 이벤트 타입

**2. DOM 요소에 이벤트 핸들러를 등록하는 메서드는?**
- a) setEvent()
- b) handleEvent()
- c) onEvent()
- d) addEventListener() ✅

**3. 한 요소의 이벤트가 부모 요소로 전파되는 현상은?**
- a) 캡처링 (Capturing)
- b) 버블링 (Bubbling) ✅
- c) 위임 (Delegation)
- d) 호이스팅 (Hoisting)

**4. 이벤트 핸들러에 자동으로 전달되는 첫 번째 인자는?**
- a) this
- b) event 객체 ✅
- c) target 요소
- d) currentTarget 요소

**5. event.target이 가리키는 대상은?**
- a) 이벤트가 처음 발생한 요소 ✅
- b) 이벤트 핸들러가 연결된 요소
- c) 부모 요소
- d) 최상위 document 객체

**6. event.currentTarget이 가리키는 대상은?**
- a) 이벤트가 처음 발생한 요소
- b) 이벤트 핸들러가 연결된 요소 ✅
- c) 자식 요소
- d) 최상위 window 객체

**7. 요소의 기본 동작을 막는 메서드는?**
- a) stopAction()
- b) cancelEvent()
- c) preventDefault() ✅
- d) stopPropagation()

**8. 버블링의 이점을 활용하는 주요 패턴은 무엇인가요?**
- a) 여러 요소에 각각 핸들러 등록
- b) 상위 요소에 핸들러 하나만 등록 ✅
- c) 모든 요소에 preventDefault() 사용
- d) 캡처링 단계에서 이벤트 처리

**9. 버블링과 캡처링의 차이를 올바르게 설명한 것은?**
- a) 캡처링은 하향 전파, 버블링은 상향 전파 ✅
- b) 캡처링은 상향 전파, 버블링은 하향 전파
- c) 버블링은 기본 동작을, 캡처링은 전파를 막음
- d) 두 용어는 동일하여 실제 동작에 차이가 없음

**10. event.target과 event.currentTarget의 차이를 올바르게 설명한 것은?**
- a) target은 리스너 부착 요소, currentTarget은 이벤트 발생 요소
- b) target은 이벤트 발생 요소, currentTarget은 리스너 부착 요소 ✅
- c) target은 항상 부모 요소, currentTarget은 항상 자식 요소
- d) 두 속성은 모든 상황에서 항상 동일한 요소를 가리킴

### 정답 해설

**1. 이벤트 핸들러**
- 이벤트 핸들러는 특정 이벤트 발생 시 호출되도록 작성된 콜백 함수입니다.

**2. addEventListener()**
- `addEventListener()`는 특정 DOM 요소에 지정된 타입의 이벤트를 처리할 함수(핸들러)를 등록합니다.

**3. 버블링 (Bubbling)**
- 이벤트가 가장 안쪽 요소에서 시작해 바깥쪽 부모 요소로 거슬러 올라가며 전파되는 현상입니다.

**4. event 객체**
- 이벤트 발생 시, 해당 이벤트에 대한 상세 정보를 담은 event 객체가 핸들러에 자동으로 전달됩니다.

**5. 이벤트가 처음 발생한 요소**
- `event.target`은 이벤트가 최초로 발생한 요소, 즉 이벤트의 실제 시작이 된 요소를 가리킵니다.

**6. 이벤트 핸들러가 연결된 요소**
- `event.currentTarget`은 이벤트 리스너가 실제로 연결되어 있는 요소, 즉 `this`와 동일한 대상을 가리킵니다.

**7. preventDefault()**
- `event.preventDefault()`는 a 태그의 링크 이동이나 form의 제출과 같은 기본 동작을 취소합니다.

**8. 상위 요소에 핸들러 하나만 등록**
- 여러 하위 요소의 이벤트를 공통 상위 요소에서 한 번에 처리하여 효율성을 높일 수 있습니다.

**9. 캡처링은 하향 전파, 버블링은 상향 전파**
- 캡처링은 부모에서 자식으로 하향식, 버블링은 자식에서 부모로 상향식으로 이벤트를 전달합니다.

**10. target은 이벤트 발생 요소, currentTarget은 리스너 부착 요소**
- target은 실제 이벤트 발생 요소를 의미하고, currentTarget은 리스너가 달린 요소(this와 동일한 대상)를 의미합니다.

---

## 핵심 정리

### 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| **이벤트 (event)** | 웹페이지에서 일어나는 신호 또는 사건 | click, input 등 |
| **이벤트 핸들러** | 이벤트 발생 시 실행되는 콜백 함수 | `btn.addEventListener('click', func)` |
| **addEventListener** | DOM 요소에 이벤트 핸들러를 등록 | `btn.addEventListener('click', func)` |
| **이벤트 버블링** | 이벤트가 부모 요소로 전파되는 현상 | 하위 요소 클릭 시 상위 핸들러 동작 |
| **event.target** | 실제 이벤트가 시작된 요소를 참조 | `console.log(event.target)` |
| **event.currentTarget** | 핸들러가 연결된 요소를 참조 | `console.log(event.currentTarget)` |
| **preventDefault** | 이벤트의 기본 동작을 취소 | `event.preventDefault()` |

### 요약 및 정리

#### 이벤트 기본 개념

**이벤트 (event)**
- 웹 페이지에서 사용자의 클릭, 키보드 입력, 마우스 움직임 등 '무언가 일어났다는 신호 또는 사건'을 의미

**이벤트 객체 (event object)**
- 이벤트가 발생하면, 해당 이벤트에 대한 상세 정보(발생 위치, 마우스 좌표 등)를 담은 객체가 자동으로 생성

**이벤트 핸들러 (event handler)**
- 특정 이벤트가 발생했을 때 실행되도록 등록된 콜백 함수

**addEventListener(type, handler)**
- DOM 요소에 특정 이벤트(type)가 발생했을 때 실행할 이벤트 핸들러(handler)를 등록하는 메서드

#### 이벤트 버블링 (Event Bubbling)

한 요소에 이벤트가 발생하면 그 요소의 핸들러가 동작한 후, 부모 요소의 핸들러, 그 부모의 부모 핸들러 순으로 최상단까지 이벤트가 전파되는 현상

**target vs currentTarget**

이벤트 객체 내에서 두 속성은 이벤트 전파 과정 중 요소를 참조하는 데 사용됩니다.

- `event.target`: 이벤트가 처음 발생한 가장 안쪽의 요소이며, 버블링이 진행되어도 이 값은 변하지 않음
- `event.currentTarget`: 이벤트 핸들러가 연결된 현재 요소를 가리키고, 일반 함수 핸들러 내에서 `this`와 같은 값을 가짐

버블링의 이런 특징을 이용하면 여러 자식 요소의 이벤트를 부모 요소 하나에서 관리할 수 있습니다.

---

## 마무리 예제

웹 페이지를 하나의 **'카페'**에 비유한 코드 예제:

```javascript
// 1. '주문'을 받을 키오스크(버튼) 선택
const button = document.querySelector('#order-btn')

// 2. '바리스타'의 행동(핸들러) 정의
const makeCoffee = function (event) {
  console.log('커피 제조 중...', event)
  // event 객체를 통해 '주문 정보' 확인 가능
}

// 3. 키오스크에 '주문'이 들어오면 '바리스타'가 행동하도록 연결
button.addEventListener('click', makeCoffee)
```

---

JavaScript Controlling Event 학습을 완료하신 것을 축하합니다! 🎉

이제 여러분은:
- 이벤트의 개념과 종류를 이해하고
- 이벤트 핸들러를 등록하여 사용자 상호작용을 처리하며
- 버블링과 캡처링을 활용하여 효율적으로 이벤트를 관리하고
- 기본 동작을 취소하여 커스텀 동작을 구현할 수 있습니다

계속해서 실습하면서 더 복잡한 웹 애플리케이션을 만들어보세요!

---

**작성일**: 2024  
**과정**: SSAFY JavaScript Controlling Event
