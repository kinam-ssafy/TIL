# JavaScript DOM 완벽 가이드

## 📚 목차

1. [JavaScript의 역사](#javascript의-역사)
2. [변수 선언](#변수-선언)
3. [DOM 기초](#dom-기초)
4. [DOM 선택](#dom-선택)
5. [DOM 조작](#dom-조작)
6. [실습 예제](#실습-예제)
7. [핵심 정리](#핵심-정리)

---

## 🎯 학습 목표

- DOM이 무엇인지 설명하고 HTML과의 관계를 이해한다.
- `let`과 `const`를 사용해 변수와 상수를 선언할 수 있다.
- `querySelector`와 `querySelectorAll`로 DOM 요소를 선택한다.
- `textContent`와 `setAttribute`로 요소 내용과 속성을 바꾼다.
- `classList` 속성으로 요소의 클래스를 동적으로 조작한다.
- `createElement`와 `appendChild`로 새 DOM 요소를 추가한다.
- `style` 프로퍼티를 사용해 요소의 스타일을 직접 변경한다.

---

## 🌟 시작하기

웹사이트에서 다크 모드 버튼을 누르면 화면이 어두워지는 건 어떻게 일어나는 걸까요?

1. 우리가 보는 웹 페이지는 **HTML**이라는 '설계도'입니다. 그리고 이 설계도만으로는 아무런 변화도 일어나지 않는 그저 정적인 문서일 뿐입니다.

2. 이 설계도에 생명을 불어넣는 것이 바로 **자바스크립트(JavaScript)**입니다. 자바스크립트는 웹 페이지의 특정 요소를 찾아내고 내용을 바꾸거나, 색깔을 입히거나, 심지어 새로운 요소를 만들어 붙이는 등 모든 동적인 조작을 할 수 있습니다.

3. 이때 자바스크립트가 HTML 설계도를 이해하고 조작할 수 있도록 브라우저는 설계도를 **'DOM(Document Object Model)'**이라는 객체 트리 구조로 변환하여 제공합니다.

정적인 페이지에 머무르지 않고 사용자의 행동에 따라 실시간으로 변화하는 동적인 웹 페이지를 직접 만들어 봅시다.

---

## JavaScript의 역사

### 웹 브라우저와 JavaScript

#### 웹의 탄생 (1990)

- **Tim Berners-Lee** 경이 WWW 하이퍼텍스트 시스템을 고안하여 개발
- URL, HTTP 최초 설계 및 구현
- 초기의 웹은 정적인 텍스트 페이지만을 지원

**주요 개념:**
- **URL**: 특정 웹페이지나 파일을 찾기 위한 고유한 경로 주소
- **HTTP**: 웹 브라우저와 서버가 데이터를 주고받기 위한 통신 규약
- **WWW**: World Wide Web, 전 세계적인 정보 공유 시스템

#### 웹 브라우저의 대중화 (1993)

- Netscape사의 최초 상용 웹 브라우저인 **Netscape Navigator** 출시
- 당시 약 90% 이상의 시장 점유율을 가짐
- Netscape사는 웹의 동적인 기능을 만들기 위한 프로젝트를 시작

#### JavaScript의 탄생 (1995)

- 당시 Netscape 소속 개발자 **Brendan Eich**는 회사의 요구사항이었던 웹의 동적 기능 개발을 넘어 스크립트 언어 **'Mocha'**를 개발함
- 이후 LiveScript로 이름을 변경했으나 당시 가장 인기있던 'Java'의 명성에 기대보고자 **'JavaScript'**로 이름을 변경
- JavaScript는 Netscape Navigator 2.0에 탑재되어 웹 페이지에 동적 기능을 추가하는 데 사용됨

#### JavaScript 파편화 (1996)

- Microsoft가 자체 웹 브라우저인 **인터넷 익스플로러(IE) 3.0**에 JavaScript와 유사한 언어인 **'JScript'**를 도입
- 이로 인해 여러 회사가 독자적으로 JavaScript 규격을 변경하여 자체 브라우저에 탑재하기 시작
- **JavaScript 파편화의 시작**

### 1차 브라우저 전쟁 (1995-2001)

- Microsoft는 IE를 자사 윈도우 운영체제에 내장하여 무료로 배포
- 빌 게이츠를 필두로 한 Microsoft의 공격적인 마케팅, 자금력 그리고 압도적인 윈도우 운영체제 점유율 앞에 Netscape는 빠르게 몰락하기 시작
- 결국 IE의 시장 점유율은 2002년 약 96%에 달하여 Microsoft가 승리
- 훗날 Brendan Eich와 Netscape의 핵심 개발진은 모질라 재단을 설립하여 **Firefox** 브라우저를 출시함 (2003)

#### 1차 브라우저 전쟁의 영향

**웹 표준의 부재**로 인해 각 기업에서 자체 표준을 확립하려는 상황 발생
- 이는 웹 개발자들에게 큰 혼란을 주었고 결과적으로 **웹 표준의 중요성을 인식하는 계기**가 됨

**💡 표준이 중요한 이유:**
- 브라우저나 기기에 상관없이 웹 사이트가 동일하게 작동하여 일관된 사용자 경험을 제공합니다.
- 브라우저별 코드를 따로 작성할 필요가 없어 개발 시간과 비용이 줄고 유지보수가 쉬워집니다.

### ECMAScript 출시 (1997)

- JavaScript의 파편화를 막기 위해 Netscape사는 **ECMA 재단**에 웹 표준 제작을 요청
- ECMA에서 **ECMAScript**라는 표준 언어를 정의하여 발표 (1997)
- 이때부터 JavaScript는 ECMAScript 표준에 기반을 두고 발전하기 시작

> **ECMA International**: 정보와 통신 시스템을 위한 국제적 표준화 기구

### 2차 브라우저 전쟁 (2004-2017)

- 웹 표준이 정의되었지만 당시 가장 높은 점유율을 가진 IE는 웹 표준을 지키지 않았고 독자적인 규격을 유지하여 웹 시장을 주도
- IE의 독주에 대항하기 시작한 Firefox가 2008년까지 30% 점유율 차지

#### Chrome 브라우저의 등장 (2008)

- Google의 **Chrome** 브라우저 출시
- Chrome은 출시 3년 만에 Firefox의 점유율을 넘어서고 그로부터 반년 뒤 IE의 점유율을 넘어섬

**Chrome이 시장 우위를 점하게 된 이유:**

가장 결정적인 이유는 바로 **"적극적인 웹 표준 준수"**

1. **호환성**
   - 웹 표준을 준수함으로써, 사용자들은 브라우저 간에 일관된 웹 페이지를 볼 수 있게 됨
   - 이는 다양한 플랫폼 및 기기에서 웹 사이트가 일관되게 동작할 수 있음을 의미

2. **강력한 개발자 도구**
   - 웹 개발자를 위한 강력한 도구를 제공하여 웹 애플리케이션을 개발하는 데 도움

#### 2차 브라우저 전쟁의 영향

Chrome이 웹 표준을 준수하고 새로운 웹 기술을 적극적으로 채택함으로써, 다른 브라우저 제조사들도 웹 표준 준수에 대한 중요성을 인식하고 이에 따라 웹 표준을 채택하는 데 더 많은 노력을 기울이게 됨

**V8 자바스크립트 엔진**: 구글이 개발한 고성능 엔진으로 웹을 문서에서 애플리케이션 플랫폼으로 바꾸는 데 결정적인 역할을 했습니다.

---

## 변수 선언

### JavaScript 변수 선언 키워드

JavaScript에서 변수를 선언할 때는 세 가지 키워드를 사용할 수 있습니다.

#### 1. let
- **재할당이 가능한 변수**를 선언
- **블록 스코프(Block Scope)**를 가짐
- 재선언 불가능

```javascript
let number = 10  // 선언 및 초기값 할당
number = 20      // 재할당 가능
```

#### 2. const
- **재할당이 불가능한 상수**를 선언
- 선언 시 **반드시 초기화**해야 함
- **블록 스코프(Block Scope)**를 가짐

```javascript
const name = 'Alice'  // 선언 및 초기값 할당
// name = 'Bella'     // 재할당 불가능 (에러 발생)
```

#### 3. var (⚠️ 사용 권장하지 않음)
- 재선언 및 재할당이 가능
- **함수 스코프(Function Scope)**를 가짐
- **호이스팅** 문제로 현재는 사용을 권장하지 않음

```javascript
var x = 1
var x = 2  // 재선언 가능
```

### 변수 작성 규칙

#### 반드시 지켜야 할 규칙
1. 예약어 사용 불가
   ```javascript
   let let = 'error'    // SyntaxError
   const const = 10     // SyntaxError
   ```

2. 숫자로 시작할 수 없음
   ```javascript
   let 1st = 'error'    // SyntaxError
   let first1 = 'ok'    // 정상
   ```

3. 공백 사용 불가
   ```javascript
   let my name = 'error'   // SyntaxError
   let myName = 'ok'       // 정상 (camelCase)
   ```

4. 특수문자는 `$`, `_`만 사용 가능
   ```javascript
   let $price = 100      // 정상
   let _temp = 'ok'      // 정상
   let my-var = 'error'  // SyntaxError
   ```

#### 권장 스타일
- **camelCase** 사용 (JavaScript 표준)
  ```javascript
  let userName = 'Alice'
  let isLoggedIn = true
  let maxCount = 100
  ```

### 블록 스코프와 함수 스코프

#### 블록 스코프 (let, const)
```javascript
if (true) {
  let x = 1
  const y = 2
  console.log(x, y)  // 1 2
}
// console.log(x)  // ReferenceError: x is not defined
// console.log(y)  // ReferenceError: y is not defined
```

#### 함수 스코프 (var)
```javascript
function foo() {
  var x = 1
  console.log(x)  // 1
}
// console.log(x)  // ReferenceError: x is not defined
```

### 호이스팅 (Hoisting)

**호이스팅**이란 변수 선언문이 코드의 최상단으로 끌어올려지는 듯한 현상입니다.

#### var의 호이스팅
```javascript
console.log(name)  // undefined
var name = '홍길동'
```

위 코드는 다음과 같이 동작합니다:
```javascript
var name           // 선언이 최상단으로 호이스팅
console.log(name)  // undefined
name = '홍길동'
```

#### let, const는 호이스팅 문제 방지
```javascript
console.log(age)   // ReferenceError: Cannot access 'age' before initialization
let age = 30

console.log(height)  // ReferenceError: Cannot access 'height' before initialization
const height = 170
```

> **TDZ (Temporal Dead Zone)**: let과 const로 선언된 변수도 기술적으로는 호이스팅 되지만, 변수가 만들어지는 내부 과정이 다르기 때문에 이 문제를 방지할 수 있습니다.

### ✅ 변수 선언 권장 사항
1. 기본적으로 **const**를 사용
2. 재할당이 필요한 경우에만 **let**을 사용
3. **var**는 사용하지 않음

---

## DOM 기초

### DOM이란?

**DOM (Document Object Model)**
- 웹 페이지(Document)를 구조화된 **객체로 표현**한 것
- 이를 통해 JavaScript 같은 프로그래밍 언어가 HTML 문서의 구조, 스타일, 내용 등을 **동적으로 조작**할 수 있음

### 문서 구조

HTML 문서는 계층적인 트리 구조를 가집니다:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>World</p>
  </body>
</html>
```

### Document 객체

**document 객체**
- 웹 페이지를 의미하는 DOM의 진입점
- 페이지를 구성하는 모든 요소에 접근 가능
- HTML 요소, 속성, 텍스트는 모두 document 객체 아래의 하위 객체로 구성

```javascript
console.log(document)
console.log(document.title)     // 페이지 제목
console.log(document.body)      // body 요소
```

### DOM Tree

모든 HTML 요소, 속성, 텍스트는 document 객체 아래의 하위 객체로 구성된 **트리 구조(DOM Tree)**를 형성합니다.

```
document
  └─ html
      ├─ head
      │   └─ title
      │       └─ "My Page"
      └─ body
          ├─ h1
          │   └─ "Hello"
          └─ p
              └─ "World"
```

---

## DOM 선택

DOM 조작을 위해서는 먼저 원하는 요소를 선택해야 합니다.

### 선택 메서드

#### 1. document.querySelector(selector)
- **CSS 선택자와 일치하는 첫 번째 요소**를 하나 반환
- 선택자 문법은 CSS와 동일
- 요소가 없으면 `null` 반환

```javascript
// 태그 선택
const heading = document.querySelector('h1')

// 클래스 선택
const item = document.querySelector('.item')

// ID 선택
const container = document.querySelector('#container')

// 복합 선택자
const link = document.querySelector('div > a.active')
```

#### 2. document.querySelectorAll(selector)
- **CSS 선택자와 일치하는 모든 요소**를 NodeList로 반환
- NodeList는 배열과 유사하지만 배열은 아님
- 요소가 없으면 빈 NodeList 반환

```javascript
// 모든 p 태그 선택
const paragraphs = document.querySelectorAll('p')

// 모든 .item 클래스 선택
const items = document.querySelectorAll('.item')

// NodeList 순회
paragraphs.forEach(p => {
  console.log(p.textContent)
})
```

### CSS 선택자 예시

| 선택자 | 설명 | 예시 |
|--------|------|------|
| `태그` | 태그 이름으로 선택 | `querySelector('p')` |
| `.클래스` | 클래스로 선택 | `querySelector('.item')` |
| `#아이디` | ID로 선택 | `querySelector('#main')` |
| `부모 > 자식` | 직계 자식 선택 | `querySelector('div > p')` |
| `요소.클래스` | 특정 요소의 클래스 | `querySelector('a.active')` |

---

## DOM 조작

선택한 요소의 내용, 속성, 스타일을 변경하거나 새로운 요소를 추가/삭제할 수 있습니다.

### 1. 속성 조작

#### textContent
요소의 **순수한 텍스트 콘텐츠**를 조작 (HTML 태그 제외)

```javascript
const h1 = document.querySelector('h1')

// 읽기
console.log(h1.textContent)

// 쓰기
h1.textContent = '새로운 제목'
```

#### setAttribute(name, value)
요소의 **속성 값을 설정**

```javascript
const link = document.querySelector('a')

// href 속성 설정
link.setAttribute('href', 'https://www.example.com')

// target 속성 설정
link.setAttribute('target', '_blank')
```

#### getAttribute(name)
요소의 **속성 값을 가져오기**

```javascript
const link = document.querySelector('a')

const href = link.getAttribute('href')
console.log(href)  // 'https://www.example.com'
```

#### removeAttribute(name)
요소의 **속성 제거**

```javascript
const link = document.querySelector('a')
link.removeAttribute('target')
```

### 2. HTML 콘텐츠 조작

#### textContent vs innerHTML

```javascript
const div = document.querySelector('div')

// textContent: 순수 텍스트만
div.textContent = '<strong>Bold</strong>'
// 결과: <strong>Bold</strong> (그대로 텍스트로 표시)

// innerHTML: HTML로 해석
div.innerHTML = '<strong>Bold</strong>'
// 결과: Bold (굵은 글씨로 표시)
```

⚠️ **주의**: innerHTML은 XSS(Cross-Site Scripting) 공격에 취약할 수 있으므로 사용자 입력을 그대로 사용하지 않도록 주의!

### 3. DOM 요소 조작

#### createElement(tagName)
새로운 HTML 요소를 **메모리에 생성**

```javascript
const newDiv = document.createElement('div')
const newP = document.createElement('p')
```

#### appendChild(node)
생성한 요소를 **특정 부모 요소의 마지막 자식으로 추가**

```javascript
const ul = document.querySelector('ul')
const newLi = document.createElement('li')
newLi.textContent = '새 항목'

// ul의 마지막에 li 추가
ul.appendChild(newLi)
```

#### removeChild(node)
**자식 요소 제거**

```javascript
const ul = document.querySelector('ul')
const firstLi = ul.querySelector('li')

// 첫 번째 li 제거
ul.removeChild(firstLi)
```

#### 완전한 예제
```javascript
// 1. 새 요소 생성
const newH2 = document.createElement('h2')

// 2. 내용 추가
newH2.textContent = '새로운 제목입니다'

// 3. 클래스 추가
newH2.classList.add('highlight')

// 4. 문서에 추가
const container = document.querySelector('#container')
container.appendChild(newH2)
```

### 4. classList 조작

요소의 **클래스 목록을 동적으로 제어**

#### classList.add(className)
클래스 **추가**

```javascript
const box = document.querySelector('.box')
box.classList.add('active')
box.classList.add('highlight', 'large')  // 여러 개 추가 가능
```

#### classList.remove(className)
클래스 **제거**

```javascript
box.classList.remove('active')
box.classList.remove('highlight', 'large')  // 여러 개 제거 가능
```

#### classList.toggle(className)
클래스 **토글** (있으면 제거, 없으면 추가)

```javascript
box.classList.toggle('active')
// active가 있으면 제거, 없으면 추가
```

#### classList.contains(className)
클래스 **포함 여부 확인**

```javascript
if (box.classList.contains('active')) {
  console.log('active 클래스가 있습니다')
}
```

### 5. Style 조작

#### style 프로퍼티
요소의 **CSS 스타일을 직접 변경**

```javascript
const box = document.querySelector('.box')

// 배경색 변경
box.style.backgroundColor = 'blue'

// 텍스트 색상 변경
box.style.color = 'white'

// 여러 스타일 한번에 변경
box.style.cssText = `
  background-color: blue;
  color: white;
  padding: 20px;
  border-radius: 10px;
`
```

**주의사항:**
- CSS의 kebab-case는 camelCase로 변환
  - `background-color` → `backgroundColor`
  - `font-size` → `fontSize`
  - `border-radius` → `borderRadius`

```javascript
// ❌ 틀린 방법
box.style.background-color = 'blue'

// ✅ 올바른 방법
box.style.backgroundColor = 'blue'
```

---

## 실습 예제

### 예제 1: 텍스트 변경하기

```javascript
// h1 요소의 텍스트 변경
const title = document.querySelector('h1')
title.textContent = '환영합니다!'

// 여러 요소의 텍스트 변경
const items = document.querySelectorAll('.item')
items.forEach((item, index) => {
  item.textContent = `항목 ${index + 1}`
})
```

### 예제 2: 클래스 토글하기 (다크 모드)

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background-color: white;
      color: black;
    }
    body.dark-mode {
      background-color: #1a1a1a;
      color: white;
    }
  </style>
</head>
<body>
  <button id="toggleBtn">다크 모드 전환</button>
  <h1>안녕하세요!</h1>
  
  <script>
    const toggleBtn = document.querySelector('#toggleBtn')
    
    toggleBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode')
    })
  </script>
</body>
</html>
```

### 예제 3: 새 요소 추가하기 (할 일 목록)

```html
<!DOCTYPE html>
<html>
<body>
  <input type="text" id="todoInput" placeholder="할 일을 입력하세요">
  <button id="addBtn">추가</button>
  <ul id="todoList"></ul>
  
  <script>
    const todoInput = document.querySelector('#todoInput')
    const addBtn = document.querySelector('#addBtn')
    const todoList = document.querySelector('#todoList')
    
    addBtn.addEventListener('click', () => {
      // 1. 입력값 가져오기
      const todoText = todoInput.value
      
      if (todoText.trim() === '') {
        alert('할 일을 입력해주세요!')
        return
      }
      
      // 2. 새 li 요소 생성
      const newLi = document.createElement('li')
      newLi.textContent = todoText
      
      // 3. 목록에 추가
      todoList.appendChild(newLi)
      
      // 4. 입력창 비우기
      todoInput.value = ''
    })
  </script>
</body>
</html>
```

### 예제 4: 속성 변경하기

```javascript
// 이미지 src 변경
const img = document.querySelector('img')
img.setAttribute('src', 'new-image.jpg')
img.setAttribute('alt', '새로운 이미지')

// 링크 href 변경
const link = document.querySelector('a')
link.setAttribute('href', 'https://www.google.com')
link.setAttribute('target', '_blank')

// data 속성 사용
const box = document.querySelector('.box')
box.setAttribute('data-id', '123')
box.setAttribute('data-type', 'premium')
```

### 예제 5: 스타일 동적 변경

```javascript
const box = document.querySelector('.box')

// 마우스 호버 효과
box.addEventListener('mouseenter', () => {
  box.style.backgroundColor = 'lightblue'
  box.style.transform = 'scale(1.1)'
  box.style.transition = 'all 0.3s'
})

box.addEventListener('mouseleave', () => {
  box.style.backgroundColor = 'white'
  box.style.transform = 'scale(1)'
})
```

---

## 핵심 정리

### 핵심 키워드

| 개념 | 설명 | 예시 |
|------|------|------|
| **DOM** | HTML 문서를 객체로 표현한 것 | `document.querySelector()` |
| **querySelector** | CSS 선택자로 요소 하나를 선택 | `document.querySelector('.heading')` |
| **querySelectorAll** | CSS 선택자로 요소 여러 개를 선택 | `document.querySelectorAll('p')` |
| **textContent** | 요소의 텍스트 내용을 조작 | `h1.textContent = '수정'` |
| **classList** | 요소의 클래스 목록을 제어 | `h2.classList.add('red')` |
| **setAttribute** | 요소의 속성 값을 설정 | `a.setAttribute('href', url)` |
| **createElement** | 새 HTML 요소를 메모리에 생성 | `document.createElement('h1')` |
| **appendChild** | 요소를 부모의 마지막 자식으로 추가 | `parent.appendChild(child)` |
| **style** | 요소의 CSS 스타일을 직접 변경 | `box.style.color = 'red'` |

### 변수 선언 요약

JavaScript에서 변수를 선언할 때는 세 가지 키워드를 사용할 수 있음:

- **let**: 재할당이 가능한 변수를 선언함 (블록 스코프를 가짐)
- **const**: 재할당이 불가능한 상수를 선언함, 선언 시 반드시 초기화해야 함 (블록 스코프를 가짐)
- **var**: 재선언 및 재할당이 가능하고 함수 스코프를 가지며 호이스팅 문제로 현재는 사용을 권장하지 않음

✅ **권장사항**: 기본적으로 `const`를 사용하고 재할당이 필요한 경우에만 `let`을 쓰는 것이 좋음

### DOM 요약

**DOM (Document Object Model)**
- 웹 페이지(Document)를 구조화된 객체로 표현한 것
- 이를 통해 JavaScript 같은 프로그래밍 언어가 HTML 문서의 구조, 스타일, 내용 등을 동적으로 조작할 수 있음
- 모든 HTML 요소, 속성, 텍스트는 document 객체 아래의 하위 객체로 구성된 트리 구조(DOM Tree)를 형성

**DOM 요소 선택**
- DOM 조작을 위해서는 먼저 원하는 요소를 선택해야 함
- `document.querySelector(selector)`: CSS 선택자와 일치하는 첫 번째 요소를 하나 반환함
- `document.querySelectorAll(selector)`: CSS 선택자와 일치하는 모든 요소를 NodeList 형태로 반환함

**DOM 요소 조작**

선택한 요소의 내용, 속성, 스타일을 변경하거나 새로운 요소를 추가/삭제할 수 있음

1. **콘텐츠 조작**: `textContent` 프로퍼티를 사용해 요소 안의 텍스트를 읽거나 변경함

2. **속성 조작**:
   - `classList` 프로퍼티(`add`, `remove`, `toggle` 메서드)로 클래스를 동적으로 제어함
   - `setAttribute(name, value)` 메서드로 href 같은 일반 속성의 값을 설정함

3. **요소 조작**:
   - `document.createElement(tagName)`로 새 요소를 메모리에 생성함
   - `appendChild()` 메서드로 생성한 요소를 특정 부모 요소의 마지막 자식으로 추가함

4. **스타일 조작**: `style` 프로퍼티를 사용해 요소의 CSS 스타일을 직접 변경함

---

## 🎯 다크 모드 구현 예제

웹사이트에서 다크 모드 버튼을 누르면 화면이 어두워지는 건 어떻게 일어나는 걸까요?

버튼 클릭 한 번으로 웹 페이지에 변화를 일으키는 방법, 이제 우리는 그 해답을 알고 있습니다.

**단 3단계면 우리도 다크 모드를 구현할 수 있습니다:**

1. `querySelector`로 웹 페이지 전체(body)를 선택합니다.
2. `classList.toggle()`로 'dark-mode' 클래스를 동적으로 추가/제거합니다.
3. 미리 정의된 CSS 스타일에 따라 배경과 글자색이 즉시 변경됩니다.

이제 자바스크립트로 웹 페이지의 클래스를 제어하여, 사용자와 상호작용하는 동적인 디자인 변경을 손쉽게 구현할 수 있습니다.

```javascript
// 간단한 다크 모드 구현
const toggleButton = document.querySelector('#darkModeToggle')

toggleButton.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode')
})
```

---

## 확인 문제

### 문제

1. JavaScript의 표준 명세 이름은 무엇인가요?
   - a) JScript
   - b) Mocha
   - c) ECMAScript ✅
   - d) TypeScript

2. 다음 중 변수명으로 사용할 수 없는 것은?
   - a) name
   - b) $user
   - c) let ✅
   - d) userName

3. 변수 선언 시 기본적으로 사용을 권장하는 키워드는?
   - a) var
   - b) let
   - c) const ✅
   - d) function

4. 웹 페이지(Document)를 객체로 표현한 모델은?
   - a) HTML
   - b) CSS
   - c) API
   - d) DOM ✅

5. CSS 선택자와 일치하는 첫 번째 요소를 반환하는 메서드는?
   - a) getElementById()
   - b) querySelectorAll()
   - c) getElementsByClassName()
   - d) querySelector() ✅

6. CSS 선택자와 일치하는 모든 요소를 NodeList로 반환하는 메서드는?
   - a) querySelector()
   - b) getElementsByTagName()
   - c) querySelectorAll() ✅
   - d) getElementById()

7. 요소에 클래스를 추가하는 classList의 메서드는?
   - a) toggle()
   - b) remove()
   - c) add() ✅
   - d) contains()

8. 요소의 속성 값을 설정하는 메서드는?
   - a) getAttribute()
   - b) removeAttribute()
   - c) hasAttribute()
   - d) setAttribute() ✅

9. 요소의 순수한 텍스트 콘텐츠를 조작하는 속성은?
   - a) innerHTML
   - b) textContent ✅
   - c) innerText
   - d) value

10. 새로운 HTML 요소를 메모리에 생성하는 메서드는?
    - a) appendChild()
    - b) createElement() ✅
    - c) removeChild()
    - d) createTextNode()

11. 생성한 요소를 특정 부모 요소의 마지막 자식으로 추가하는 메서드는?
    - a) insertBefore()
    - b) append()
    - c) appendChild() ✅
    - d) prepend()

12. var 키워드의 특징이 아닌 것은?
    - a) 재할당 가능
    - b) 재선언 가능
    - c) 블록 스코프 ✅
    - d) 호이스팅

### 정답 해설

1. **ECMAScript**: JavaScript의 파편화를 막기 위해 ECMA 재단에서 만든 표준 언어 명세입니다.

2. **let**: let은 변수 선언 키워드로 프로그래밍 언어가 예약해둔 단어이므로 변수명으로 쓸 수 없습니다.

3. **const**: const를 기본으로 사용하여 의도치 않은 재할당을 막고, 필요시에만 let을 사용합니다.

4. **DOM**: DOM(Document Object Model)은 웹 페이지를 구조화된 객체로 제공하는 API입니다.

5. **querySelector()**: querySelector()는 제공된 선택자를 만족하는 첫 번째 element 객체를 반환합니다.

6. **querySelectorAll()**: querySelectorAll()은 제공된 선택자를 만족하는 모든 요소를 NodeList로 반환합니다.

7. **add()**: add()를 사용하여 지정한 클래스 값을 추가할 수 있습니다.

8. **setAttribute()**: setAttribute()를 사용하여 지정된 요소의 속성 값을 설정하거나 갱신합니다.

9. **textContent**: textContent는 HTML 태그를 제외한 순수한 텍스트 데이터만 가져오거나 설정합니다.

10. **createElement()**: createElement()는 요소를 생성합니다. appendChild로 문서에 삽입해야 보입니다.

11. **appendChild()**: appendChild()는 한 노드를 특정 부모 노드의 자식 목록 중 마지막 자식으로 삽입합니다.

12. **블록 스코프**: var는 함수 스코프를 가지며, let과 const가 블록 스코프를 가집니다.

---

## 마무리

JavaScript DOM을 학습하신 것을 축하합니다! 🎉

이제 여러분은:
- 웹 페이지의 요소를 선택하고
- 내용과 속성을 변경하며
- 새로운 요소를 추가하고
- 스타일을 동적으로 조작할 수 있습니다

계속해서 실습하면서 더 복잡한 인터랙션을 만들어보세요!

---

**작성일**: 2024
**과정**: SSAFY JavaScript DOM
