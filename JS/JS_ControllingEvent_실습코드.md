# JavaScript Controlling Event 실습 코드 정리

## 📚 목차

1. [addEventListener](#1-addeventlistener)
2. [Event 객체](#2-event-객체)
3. [이벤트 버블링](#3-이벤트-버블링)
4. [target vs currentTarget](#4-target-vs-currenttarget)
5. [캡처링](#5-캡처링)
6. [버블링 활용 예제](#6-버블링-활용-예제)
7. [실습: 클릭 이벤트](#7-실습-클릭-이벤트)
8. [실습: Input 이벤트](#8-실습-input-이벤트)
9. [실습: Click & Input 종합](#9-실습-click--input-종합)
10. [실습: Todo 리스트](#10-실습-todo-리스트)
11. [실습: 로또 번호 추첨](#11-실습-로또-번호-추첨)
12. [이벤트 기본 동작 취소](#12-이벤트-기본-동작-취소)
13. [참고: addEventListener와 this](#13-참고-addeventlistener와-this)
14. [참고: Lodash 라이브러리](#14-참고-lodash-라이브러리)

---

## 1. addEventListener

**파일명**: `01-addEventListener.html`

addEventListener를 사용하여 이벤트 핸들러를 등록하는 기본 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button>버튼</button>

  <script>
    // === 1. 버튼 요소 선택 ===
    const button = document.querySelector('button')

    // === 2. 이벤트 핸들러 (콜백 함수) 정의 ===
    const handleClick = function () {
      window.alert('버튼이 클릭 되었습니다!')
    }

    // === 3. addEventListener로 이벤트 핸들러 등록 ===
    // 구조: element.addEventListener(이벤트타입, 핸들러함수)
    button.addEventListener('click', handleClick)
    // 'click' 이벤트가 발생하면 handleClick 함수가 실행됨
  </script>
</body>
</html>
```

**핵심 개념:**
- **addEventListener**: DOM 요소에 이벤트 핸들러를 등록하는 메서드
- **이벤트 타입**: 감지할 이벤트 종류 (예: 'click', 'input', 'submit')
- **이벤트 핸들러**: 이벤트 발생 시 실행될 콜백 함수

**참고 교안**: `JavaScript_Controlling_Event.md` - event handler 섹션

---

## 2. Event 객체

**파일명**: `02-event.html`

이벤트 발생 시 자동으로 전달되는 event 객체를 활용하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button id="btn">버튼</button>

  <script>
    // === 1. 버튼 선택 ===
    const btn = document.querySelector('#btn')

    // === 2. 이벤트 핸들러 (event 객체를 매개변수로 받음) ===
    const detectClick = function (event) {
      // event 객체에는 이벤트에 대한 모든 정보가 담겨 있음
      console.log(event) // PointerEvent 객체
      
      // 이벤트 타입 확인
      console.log(event.type) // 'click'
      
      // 이벤트가 발생한 요소 (이벤트 핸들러가 등록된 요소)
      console.log(event.currentTarget) // <button id="btn">버튼</button>
      
      // this는 event.currentTarget과 동일 (일반 함수인 경우)
      console.log(this) // <button id="btn">버튼</button>
    }

    // === 3. 버튼에 이벤트 핸들러 등록 ===
    btn.addEventListener('click', detectClick)
  </script>
</body>
</html>
```

**핵심 개념:**
- **event 객체**: 이벤트 발생 시 브라우저가 자동으로 생성하여 핸들러에 전달
- **event.type**: 발생한 이벤트의 타입
- **event.currentTarget**: 이벤트 핸들러가 등록된 요소
- **this**: 일반 함수에서는 event.currentTarget과 동일

**참고 교안**: `JavaScript_Controlling_Event.md` - event object 섹션

---

## 3. 이벤트 버블링

**파일명**: `03-bubbling.html`

이벤트 버블링의 동작 원리를 이해하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body * {
      margin: 10px;
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <form id="form">
    form
    <div id="div">
      div
      <p id="p">p</p>
    </div>
  </form>

  <script>
    // === 각 요소 선택 ===
    const formElement = document.querySelector('#form')
    const divElement = document.querySelector('#div')
    const pElement = document.querySelector('#p')

    // === 각 요소에 이벤트 핸들러 등록 ===
    const clickHandler1 = function (event) {
      console.log('form이 클릭되었습니다.')
    }
    const clickHandler2 = function (event) {
      console.log('div가 클릭되었습니다.')
    }
    const clickHandler3 = function (event) {
      console.log('p가 클릭되었습니다.')
    }

    formElement.addEventListener('click', clickHandler1)
    divElement.addEventListener('click', clickHandler2)
    pElement.addEventListener('click', clickHandler3)

    // === p 요소를 클릭하면? ===
    // 출력 결과:
    // 'p가 클릭되었습니다.'
    // 'div가 클릭되었습니다.'
    // 'form이 클릭되었습니다.'
    
    // 이벤트가 p → div → form 순서로 전파됨 (버블링)
  </script>
</body>
</html>
```

**핵심 개념:**
- **이벤트 버블링**: 이벤트가 발생한 요소에서 시작하여 부모 요소로 전파되는 현상
- 가장 안쪽 요소(p)에서 시작하여 최상위 요소(document)까지 순차적으로 전파
- 각 요소에 등록된 핸들러가 순서대로 실행됨

**참고 교안**: `JavaScript_Controlling_Event.md` - 버블링 섹션

---

## 4. target vs currentTarget

**파일명**: `04-target-currentTarget.html`

event.target과 event.currentTarget의 차이를 이해하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    #outerouter {
      width: 300px;
      height: 300px;
      background-color: yellowgreen;
    }

    #outer {
      width: 200px;
      height: 200px;
      background-color: crimson;
    }

    #inner {
      width: 100px;
      height: 100px;
      background-color: skyblue;
    }
  </style>
</head>
<body>
  <div id="outerouter">
    outerouter 
    <div id="outer">
      outer
      <div id="inner">inner</div>
    </div>
  </div>

  <script>
    // === 가장 바깥쪽 요소에만 이벤트 핸들러 등록 ===
    const outerOuterElement = document.querySelector('#outerouter')

    const clickHandler = function (event) {
      // currentTarget: 이벤트 핸들러가 등록된 요소 (항상 동일)
      console.log('currentTarget:', event.currentTarget.id)
      
      // target: 실제로 이벤트가 발생한 요소 (클릭한 요소)
      console.log('target:', event.target.id)
    }

    outerOuterElement.addEventListener('click', clickHandler)

    // === 실행 결과 예시 ===
    // inner를 클릭하면:
    // currentTarget: outerouter (핸들러가 등록된 요소)
    // target: inner (실제로 클릭한 요소)

    // outer를 클릭하면:
    // currentTarget: outerouter (핸들러가 등록된 요소)
    // target: outer (실제로 클릭한 요소)

    // outerouter를 클릭하면:
    // currentTarget: outerouter (핸들러가 등록된 요소)
    // target: outerouter (실제로 클릭한 요소)
  </script>
</body>
</html>
```

**핵심 개념:**

| 속성 | 설명 | 특징 |
|------|------|------|
| **event.target** | 실제로 이벤트가 발생한 요소 | 버블링 중에도 변하지 않음 |
| **event.currentTarget** | 이벤트 핸들러가 등록된 요소 | 일반 함수에서 `this`와 동일 |

**참고 교안**: `JavaScript_Controlling_Event.md` - 버블링 > target과 currentTarget 섹션

---

## 5. 캡처링

**파일명**: `05-capturing.html`

이벤트 캡처링 단계를 이해하는 실습 (거의 사용하지 않음)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Event Capturing</title>
  <style>
    body * {
      margin: 10px;
      border: 1px solid black;
      padding: 10px;
    }
  </style>
</head>
<body>
  <form id="form">
    form
    <div id="div">
      div
      <p id="p">p</p>
    </div>
  </form>

  <script>
    const formElement = document.querySelector('#form')
    const divElement = document.querySelector('#div')
    const pElement = document.querySelector('#p')

    const clickHandler1 = function (event) {
      console.log('form이 클릭되었습니다.')
    }
    const clickHandler2 = function (event) {
      console.log('div가 클릭되었습니다.')
    }
    const clickHandler3 = function (event) {
      console.log('p가 클릭되었습니다.')
    }

    // === 캡처링: 세 번째 인자로 true를 전달 ===
    formElement.addEventListener('click', clickHandler1, true)
    divElement.addEventListener('click', clickHandler2, true)
    pElement.addEventListener('click', clickHandler3, true)

    // === p 요소를 클릭하면? ===
    // 출력 결과 (버블링과 반대):
    // 'form이 클릭되었습니다.'
    // 'div가 클릭되었습니다.'
    // 'p가 클릭되었습니다.'
    
    // 이벤트가 form → div → p 순서로 전파됨 (캡처링)

    // 사용하는 경우: 
    // 자식 요소들이 이벤트를 처리하기 전에 
    // 부모 선에서 먼저 검사하거나 막아야 할 때
    // 근데 거의 사용 안 함!
  </script>
</body>
</html>
```

**핵심 개념:**
- **캡처링**: 이벤트가 최상위 요소에서 타겟 요소로 하향 전파되는 단계
- **버블링**: 타겟 요소에서 최상위 요소로 상향 전파되는 단계
- `addEventListener`의 세 번째 인자를 `true`로 설정하면 캡처링 단계에서 이벤트 감지

**주의사항:**
- 캡처링은 거의 사용하지 않음
- 기본값은 `false`로 버블링 단계에서 이벤트를 감지

**참고 교안**: `JavaScript_Controlling_Event.md` - 캡처링과 버블링 섹션

---

## 6. 버블링 활용 예제

**파일명**: `06-bubbling-example.html`

이벤트 위임(Event Delegation)을 활용한 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div>
    <button>버튼1</button>
    <button>버튼2</button>
    <button>버튼3</button>
    <button>버튼4</button>
    <button>버튼5</button>
  </div>
  
  <script>
    // === 부모 요소에만 이벤트 핸들러 등록 (이벤트 위임) ===
    const divTag = document.querySelector('div')

    const clickHandler = function (event) {
      // event.target으로 실제 클릭된 버튼 확인
      console.log(event.target)
      // 클릭한 버튼에 따라 다른 요소가 출력됨
    }

    divTag.addEventListener('click', clickHandler)

    // === 장점 ===
    // 1. 버튼마다 개별 핸들러를 등록할 필요 없음
    // 2. 동적으로 추가되는 버튼에도 자동으로 적용
    // 3. 메모리 효율적
  </script>
</body>
</html>
```

**핵심 개념:**
- **이벤트 위임**: 부모 요소에 이벤트 핸들러를 등록하여 여러 자식 요소의 이벤트를 한 번에 처리
- 버블링을 활용하여 효율적인 이벤트 관리
- `event.target`으로 실제 클릭된 요소 구분

**참고 교안**: `JavaScript_Controlling_Event.md` - 버블링의 필요성 섹션

---

## 7. 실습: 클릭 이벤트

**파일명**: `07-practice-click-event.html` / `07-sol-practice-click-event.html`

버튼 클릭 시 카운터를 증가시키는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button id="btn">버튼</button>
  <p>
    클릭횟수 :
    <span id="counter">0</span>
  </p>

  <script>
    // 목표: 버튼을 클릭하면 숫자를 1씩 증가시키기

    // === 1. 버튼 클릭 횟수 초기값 설정 ===
    let initialValue = 0

    // === 2. 버튼 요소 선택 ===
    const btn = document.querySelector("#btn")

    // === 3. 이벤트 핸들러(콜백 함수) 작성 ===
    const clickHandler = function () {
      // 3.1 버튼 클릭 횟수 +1
      initialValue += 1
      
      // 3.2 클릭 횟수를 보여주는 태그 선택
      const pTag = document.querySelector("p")
      
      // 3.3 태그의 콘텐츠를 +1 된 버튼 클릭 횟수로 변경
      pTag.textContent = `클릭횟수 : ${initialValue}`
    }

    // === 4. 버튼에 이벤트 핸들러 등록 ===
    btn.addEventListener("click", clickHandler)
  </script>
</body>
</html>
```

**풀이 포인트:**
1. 클릭 횟수를 저장할 변수 선언 (`let` 사용)
2. 버튼 요소 선택
3. 클릭 시 카운터 증가 및 화면 업데이트
4. `addEventListener`로 이벤트 등록

**참고 교안**: `JavaScript_Controlling_Event.md` - event handler 활용 > click 이벤트 섹션

---

## 8. 실습: Input 이벤트

**파일명**: `08-practice-input-event.html` / `08-sol-practice-input-event.html`

사용자 입력을 실시간으로 출력하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <input type="text" id="text-input" />
  <p></p>

  <script>
    // 목표: 사용자 입력 값을 실시간으로 출력하기

    // === 1. input 요소 선택 ===
    const inputTag = document.querySelector("#text-input")
    
    // === 2. 입력 값을 출력할 p 태그 선택 ===
    const pTag = document.querySelector("p")
    
    // === 3. 이벤트 핸들러 작성 ===
    const inputHandler = function (event) {
      // event.currentTarget.value로 입력 값 가져오기
      console.log(event.currentTarget.value)
      
      // 3.1 작성하는 데이터가 어디에 누적되고 있는지 찾기
      // console.log(event)
      // console.log(event.currentTarget)
      // console.log(event.currentTarget.value)
      
      // 3.2 p 요소의 컨텐츠에 작성하는 데이터를 추가
      pTag.textContent = event.currentTarget.value
    }

    // === 4. input 요소에 핸들러 연결 ===
    inputTag.addEventListener("input", inputHandler)
  </script>
</body>
</html>
```

**풀이 포인트:**
1. `input` 이벤트는 입력 값이 변경될 때마다 실시간으로 발생
2. `event.currentTarget.value`로 현재 입력 값 접근
3. `textContent`로 p 태그에 실시간 표시

**참고 교안**: `JavaScript_Controlling_Event.md` - event handler 활용 > input 이벤트 섹션

---

## 9. 실습: Click & Input 종합

**파일명**: `09-practice-click-input-event.html` / `09-sol-practice-click-input-event.html`

입력 이벤트와 클릭 이벤트를 결합한 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .blue {
      color: blue;
    }
  </style>
</head>
<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text" id="text-input">

  <script>
    // 목표: 
    // 1. 입력 값을 실시간으로 출력
    // 2. 클릭 버튼을 클릭 시 출력 값의 CSS를 변경

    // === input 구현 ===
    const inputTag = document.querySelector('#text-input')
    const h1Tag = document.querySelector('h1')

    const inputHandler = function (event) {
      h1Tag.textContent = event.currentTarget.value
    }

    inputTag.addEventListener('input', inputHandler)

    // === click 구현 ===
    const btn = document.querySelector('#btn')

    const clickHandler = function () {
      // 방법 1: add 메서드 사용
      h1Tag.classList.add('blue')

      // 방법 2: toggle 메서드 사용
      // h1Tag.classList.toggle('blue')

      // 방법 3: if 조건문 사용
      // if (h1Tag.classList.contains('blue')) {
      //   h1Tag.classList.remove('blue')
      // } else {
      //   h1Tag.classList.add('blue')
      // }
    }

    btn.addEventListener('click', clickHandler)
  </script>
</body>
</html>
```

**풀이 포인트:**
1. `input` 이벤트로 실시간 텍스트 출력
2. `click` 이벤트로 클래스 추가/토글
3. `classList` 메서드 활용 (add, toggle, remove, contains)

**참고 교안**: `JavaScript_Controlling_Event.md` - event handler 활용 섹션

---

## 10. 실습: Todo 리스트

**파일명**: `10-practice-todo.html` / `10-sol-practice-todo.html`

할 일 목록을 추가하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <input type="text" class="input-text">
  <button id="btn">+</button>
  <ul></ul>

  <script>
    // 목표: 
    // 1. Input창에 입력 후 '+'버튼 클릭 시, 실시간으로 리스트에 출력
    // 2. 추가기능: 빈 문자열이 입력될 경우, 경고 대화상자를 띄우기

    // === 1. 필요한 요소 선택 ===
    const inputTag = document.querySelector('.input-text')
    const btn = document.querySelector('#btn')
    const ulTag = document.querySelector('ul')

    // === 2. 이벤트 핸들러 작성 ===
    const addTodo = function (event) {
      // 2.1 사용자 입력 데이터 저장
      const inputData = inputTag.value

      // 추가 기능: 빈 문자열 검사
      if (inputData.trim()) {
        // 2.2 데이터를 저장할 li 요소 생성
        const liTag = document.createElement('li')

        // 2.3 li 요소 컨텐츠에 데이터 입력
        liTag.textContent = inputData

        // 2.4 li 요소를 부모 ul 요소의 자식 요소로 추가
        ulTag.appendChild(liTag)

        // 2.5 todo 추가 후 input의 입력 데이터는 초기화
        inputTag.value = ''
      } else {
        alert('할 일을 입력하세요!')
      }
    }

    // === 3. 버튼에 이벤트 핸들러 등록 ===
    btn.addEventListener('click', addTodo)
  </script>
</body>
</html>
```

**풀이 포인트:**
1. `createElement`로 새 li 요소 생성
2. `textContent`로 내용 설정
3. `appendChild`로 ul에 추가
4. `trim()`으로 빈 문자열 검사
5. 입력 후 input 초기화

**참고 교안**: `JavaScript_Controlling_Event.md` - event handler 활용 > click & input 이벤트 종합 섹션

---

## 11. 실습: 로또 번호 추첨

**파일명**: `11-practice--lottery.html` / `11-sol-practice--lottery.html`

Lodash 라이브러리를 활용한 로또 번호 생성 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>로또 추천 번호</h1>
  <button id="btn">행운 번호 받기</button>
  <div></div>

  <!-- Lodash 라이브러리 CDN 로드 -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    // Lodash 메서드 참고:
    // _.range(1, 46): 1부터 45까지의 배열 생성
    // _.sampleSize(numbers, 6): 45개의 리스트에서 6개 번호 추출

    // === 1. 필요한 요소 선택 ===
    const btn = document.querySelector("#btn")
    const divTag = document.querySelector("div")

    // === 2. 로또 번호를 화면에 출력하는 함수 (이벤트 핸들러) ===
    const getLottery = function (event) {
      // 2.1 1부터 45까지의 배열 생성
      const numbers = _.range(1, 46)
      
      // 2.2 45개의 요소가 있는 배열에서 6개 번호 추출
      const sixNumbers = _.sampleSize(numbers, 6)
      
      // 2.3 6개의 li 요소를 담을 ul 요소 생성
      const ulTag = document.createElement("ul")
      
      // 2.4 추출한 번호 배열을 반복하면서 li 요소를 생성
      sixNumbers.forEach((number) => {
        // 2.5 번호를 담을 li 요소 생성
        const liTag = document.createElement("li")
        
        // 2.6 번호를 li 요소에 입력
        liTag.textContent = number
        
        // 2.7 만들어진 li를 ul 요소에 추가
        ulTag.appendChild(liTag)
      })
      
      // 2.8 완성한 ul 요소를 div 요소에 추가
      divTag.appendChild(ulTag)
    }

    // === 3. 버튼 요소에 이벤트 핸들러 등록 ===
    btn.addEventListener("click", getLottery)
  </script>
</body>
</html>
```

**풀이 포인트:**
1. **Lodash 활용**:
   - `_.range(1, 46)`: 1~45 배열 생성
   - `_.sampleSize(array, n)`: 배열에서 n개 랜덤 추출
2. **DOM 조작**:
   - `createElement`로 ul, li 생성
   - `forEach`로 배열 순회
   - `appendChild`로 요소 추가

**참고 교안**: `JavaScript_Controlling_Event.md` - 실습 예제 섹션

---

## 12. 이벤트 기본 동작 취소

**파일명**: `12-prevent-event.html`

preventDefault()를 사용하여 기본 동작을 취소하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>중요한 내용</h1>

  <form id="my-form">
    <input type="text" name="username">
    <button type="submit">Submit</button>
  </form>

  <script>
    // === 1. 복사 이벤트 금지 ===
    const h1Tag = document.querySelector('h1')

    h1Tag.addEventListener('copy', function (event) {
      console.log(event)
      // 복사 기본 동작 취소
      event.preventDefault()
      alert('복사 할 수 없습니다.')
    })

    // === 2. 폼 제출 시 페이지 새로고침 동작 취소 ===
    const formTag = document.querySelector('#my-form')

    const handleSubmit = function (event) {
      // form의 기본 동작(페이지 새로고침) 취소
      event.preventDefault()
      
      // 이제 여기서 직접 데이터 처리 가능
      console.log('form이 제출되었습니다')
    }

    formTag.addEventListener('submit', handleSubmit)
  </script>
</body>
</html>
```

**핵심 개념:**
- **event.preventDefault()**: 이벤트의 기본 동작을 취소
- **주요 사용 사례**:
  - form 제출 시 페이지 새로고침 방지
  - 링크 클릭 시 페이지 이동 방지
  - 복사/붙여넣기 방지
  - 우클릭 메뉴 방지

**주의사항:**
- `preventDefault()`는 이벤트 전파를 막지 않음 (버블링은 계속됨)
- 이벤트 전파를 막으려면 `stopPropagation()` 사용

**참고 교안**: `JavaScript_Controlling_Event.md` - 이벤트 기본 동작 취소하기 섹션

---

## 13. 참고: addEventListener와 this

**파일명**: `99-listener-with-this.html`

addEventListener에서 this의 동작 방식을 이해하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button id="function">function</button>
  <button id="arrow">arrow function</button>

  <script>
    // === 일반적인 this 바인딩 규칙 ===
    // 1. 일반 함수 호출: window
    // 2. 메서드 호출: 메서드를 소유한 객체

    // addEventListener는 위의 일반적인 규칙과 다르게 동작하는데,
    // 이는 JavaScript 엔진이 addEventListener 메서드를 특별하게 처리하기 때문
    // 내부 구현: https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener

    const functionButton = document.querySelector('#function')
    const arrowButton = document.querySelector('#arrow')

    // === 1. 일반 함수 사용 ===
    functionButton.addEventListener('click', function () {
      console.log(this) // <button id="function">function</button>
      // this가 이벤트가 발생한 요소(functionButton)를 가리킴
    })

    // === 2. 화살표 함수 사용 ===
    arrowButton.addEventListener('click', () => {
      console.log(this) // window
      // 화살표 함수는 자신만의 this를 가지지 않으므로
      // 상위 스코프(전역)의 this를 참조
    })

    // === 3. 화살표 함수에서는 event 객체 사용으로 대체 가능 ===
    arrowButton.addEventListener('click', (event) => {
      console.log(event.currentTarget) 
      // <button id="arrow">arrow function</button>
      // event.currentTarget을 사용하면 화살표 함수에서도
      // 이벤트가 발생한 요소에 접근 가능
    })
  </script>
</body>
</html>
```

**핵심 개념:**

| 함수 종류 | this | 대안 |
|-----------|------|------|
| **일반 함수** | 이벤트가 발생한 요소 | - |
| **화살표 함수** | 상위 스코프의 this (window) | `event.currentTarget` |

**권장 사항:**
- 요소 자체에 접근해야 하는 경우: 일반 함수 사용
- this가 필요 없거나 상위 스코프의 this를 참조해야 하는 경우: 화살표 함수 + `event.currentTarget`

**참고 교안**: `JavaScript_Controlling_Event.md` - 참고 > addEventListener와 화살표 함수 관계 섹션

---

## 14. 참고: Lodash 라이브러리

**파일명**: `99-lodash.html`

Lodash 라이브러리의 유용한 메서드들을 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- Lodash CDN -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <input type="text" id="searchInput" placeholder="검색어 난타해보기">
</head>
<body>
  <script>
    // === 1. _.uniqBy: 객체 배열에서 특정 키 기준으로 중복 제거 ===
    const users = [
      { id: 1, name: '철수' },
      { id: 2, name: '영희' },
      { id: 1, name: '철수' },
    ];

    // 먼저 나온 Key 값이 생존
    const uniqueUsersLodash = _.uniqBy(users, 'id');
    console.log(uniqueUsersLodash);  
    // [{ id: 1, name: '철수' }, { id: 2, name: '영희' }]

    // === 2. _.orderBy: 다중 조건 정렬 ===
    const posts = [
      { user: 'A', age: 20 },
      { user: 'B', age: 30 },
      { user: 'C', age: 20 },
    ];

    const sorted = _.orderBy(posts, ['age', 'user'], ['desc', 'asc']);
    console.log(sorted)  
    // [{user: 'B', age: 30}, {user: 'A', age: 20}, {user: 'C', age: 20}]

    // === 3. _.cloneDeep: 깊은 복사 ===
    const original = { 
      profile: { name: 'Kim', skills: ['JS', 'Vue'] } 
    };

    const deep = _.cloneDeep(original);
    deep.profile.skills.push('Lodash'); // 원본은 안전함
    console.log("오리지널", original)
    console.log("깊은 복사", deep)

    // === 4. _.isEqual: 깊은 비교 ===
    const objA = { a: 1, b: { c: 2 } };
    const objB = { a: 1, b: { c: 2 } };

    console.log(objA === objB); // false (참조가 다름)
    console.log(_.isEqual(objA, objB)); // true (값이 같음)

    // === 5. _.debounce: 마지막 호출만 실행 ===
    // 사용자 입력이 끝나고 x초 뒤에 한 번 요청하도록 할 때 유용
    // 사용 사례: 검색 자동완성, API 호출 최적화

    // 사용자가 입력을 멈춘 지 1000ms가 지나면 함수 실행
    const handleSearch = _.debounce((keyword) => {
      console.log(`1초 뒤 호출: `, keyword);
    }, 1000);

    // input 이벤트 핸들러에 연결
    const inputElement = document.querySelector('#searchInput')
    inputElement.addEventListener('input', (e) => handleSearch(e.target.value));

    // === 6. _.throttle: 일정 주기마다 실행 ===
    // 사용 사례: 스크롤 이벤트, 리사이즈 이벤트 최적화

    // 1000ms마다 한 번씩만 실행됨
    let mouseNum = 0
    const handleScroll = _.throttle(() => {
      mouseNum++;
      console.log('마우스 이동 횟수: ', mouseNum);
    }, 1000);

    window.addEventListener('mousemove', handleScroll);

    // === 7. _.isEmpty: 객체가 비었는지 확인 ===
    // 주의: 숫자는 비었다고 판단하니 주의 필요
    console.log(_.isEmpty(null));      // true
    console.log(_.isEmpty(undefined)); // true
    console.log(_.isEmpty(''));        // true
    console.log(_.isEmpty([]));        // true
    console.log(_.isEmpty({}));        // true
    console.log(_.isEmpty(0))          // true (주의!)
    console.log(_.isEmpty(100))        // true (주의!)
  </script>
</body>
</html>
```

**Lodash 주요 메서드 정리:**

| 메서드 | 기능 | 활용 |
|--------|------|------|
| **_.uniqBy()** | 특정 키 기준 중복 제거 | 배열에서 고유 값만 추출 |
| **_.orderBy()** | 다중 조건 정렬 | 복잡한 정렬 조건 적용 |
| **_.cloneDeep()** | 깊은 복사 | 중첩 객체 완전 복사 |
| **_.isEqual()** | 깊은 비교 | 객체 값 비교 |
| **_.debounce()** | 마지막 호출만 실행 | 검색 자동완성, API 최적화 |
| **_.throttle()** | 일정 주기마다 실행 | 스크롤/리사이즈 최적화 |
| **_.isEmpty()** | 빈 값 확인 | 데이터 유효성 검사 |

**참고 자료**: [Lodash 공식 문서](https://lodash.com/docs/)

---

## 실습 순서 추천

1. **01-addEventListener.html**: addEventListener 기본
2. **02-event.html**: event 객체 이해
3. **03-bubbling.html**: 버블링 기본
4. **04-target-currentTarget.html**: target vs currentTarget
5. **05-capturing.html**: 캡처링 (참고용)
6. **06-bubbling-example.html**: 이벤트 위임
7. **07-practice-click-event.html**: 클릭 이벤트 실습
8. **08-practice-input-event.html**: Input 이벤트 실습
9. **09-practice-click-input-event.html**: 종합 실습
10. **10-practice-todo.html**: Todo 리스트
11. **11-practice--lottery.html**: 로또 번호 (Lodash)
12. **12-prevent-event.html**: preventDefault
13. **99-listener-with-this.html**: this 이해
14. **99-lodash.html**: Lodash 활용

---

## 핵심 개념 요약표

| 개념 | 설명 | 예시 |
|------|------|------|
| **addEventListener** | 이벤트 핸들러 등록 | `element.addEventListener('click', handler)` |
| **event 객체** | 이벤트 정보를 담은 객체 | `event.type`, `event.target` |
| **이벤트 버블링** | 자식 → 부모로 이벤트 전파 | p → div → form |
| **이벤트 캡처링** | 부모 → 자식으로 이벤트 전파 | form → div → p |
| **event.target** | 실제 이벤트 발생 요소 | 클릭한 요소 |
| **event.currentTarget** | 핸들러가 등록된 요소 | 일반 함수에서 `this`와 동일 |
| **이벤트 위임** | 부모에 핸들러 등록 | 여러 자식 요소 관리 |
| **preventDefault()** | 기본 동작 취소 | form 제출, 링크 이동 방지 |

---

## 주요 이벤트 타입

| 이벤트 | 발생 시점 | 주요 사용 |
|--------|----------|-----------|
| **click** | 요소 클릭 시 | 버튼 클릭 처리 |
| **input** | 입력 값 변경 시 (실시간) | 실시간 검색, 입력 유효성 |
| **change** | 입력 완료 후 포커스 이탈 시 | 폼 입력 완료 |
| **submit** | 폼 제출 시 | 폼 데이터 처리 |
| **keydown** | 키보드 누를 때 | 특정 키 입력 감지 |
| **keyup** | 키보드 뗄 때 | Enter 키 감지 |
| **mouseover** | 마우스 올릴 때 | 호버 효과 |
| **mouseout** | 마우스 벗어날 때 | 호버 효과 해제 |
| **copy** | 복사 시 | 복사 방지 |
| **scroll** | 스크롤 시 | 무한 스크롤 |

---

## 주의사항 체크리스트

- [ ] 이벤트 핸들러는 함수 자체를 전달 (`handler()` ✗, `handler` ✓)
- [ ] `event.target`과 `event.currentTarget` 구분하기
- [ ] 화살표 함수에서 this 사용 주의 → `event.currentTarget` 사용
- [ ] `preventDefault()`로 기본 동작 취소
- [ ] `stopPropagation()`은 필요한 경우에만 사용
- [ ] 이벤트 위임으로 효율적인 이벤트 관리
- [ ] `input.value`로 입력 값 접근
- [ ] `textContent`로 텍스트 조작 (innerHTML 지양)
- [ ] 빈 문자열 검사 시 `trim()` 사용
- [ ] Lodash 사용 시 CDN 로드 확인

---

## 디버깅 팁

```javascript
// 이벤트 객체 전체 확인
element.addEventListener('click', (event) => {
  console.log(event)
})

// 이벤트 타입 확인
console.log(event.type)

// 클릭한 요소 확인
console.log(event.target)

// 핸들러가 등록된 요소 확인
console.log(event.currentTarget)

// this 확인 (일반 함수)
element.addEventListener('click', function() {
  console.log(this)
})

// 입력 값 확인
inputElement.addEventListener('input', (e) => {
  console.log(e.currentTarget.value)
})
```

---

**작성일**: 2024  
**참고 교안**: SSAFY JavaScript_Controlling_Event.md

