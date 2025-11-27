# JavaScript DOM 조작 실습 코드 정리

## 📚 목차

1. [변수 선언](#1-변수-선언)
2. [DOM 선택](#2-dom-선택)
3. [요소 속성 조작](#3-요소-속성-조작)
4. [콘텐츠 조작](#4-콘텐츠-조작)
5. [DOM 요소 조작](#5-dom-요소-조작)
6. [스타일 조작](#6-스타일-조작)

---

## 1. 변수 선언

**파일명**: `00-js-variable.html`

JavaScript의 변수 선언 키워드인 `let`과 `const`의 사용법을 익히는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    // 1. let 키워드
    let number = 10  // 1.1 선언 및 초기값 할당
    number = 20      // 1.2 재할당 가능
    // let number = 20 // 1.3 재선언 불가능 (에러 발생)

    // 2. const 키워드 
    // const number = 10 // 2.1 선언 및 초기값 할당
    // number = 10       // 2.2 재할당 불가능 (에러 발생)
    // const number = 20 // 2.3 재선언 불가능 (에러 발생)
    // const number      // 2.4 선언 시 초기화 필수 (에러 발생)

    // 3. block scope (블록 스코프)
    // let과 const는 블록 스코프를 가짐
    // let x = 1
    // if (x === 1) {
    //     let x = 2
    //     console.log(x) // 2 (블록 내부의 x)
    // }
    // console.log(x) // 1 (블록 외부의 x)
  </script>
</body>
</html>
```

**핵심 개념:**
- `let`: 재할당 가능, 재선언 불가능, 블록 스코프
- `const`: 재할당 불가능, 재선언 불가능, 블록 스코프, 선언 시 초기화 필수
- 블록 스코프: `{}` 안에서 선언된 변수는 블록 밖에서 접근 불가

**참고 교안**: `DOM01.md` - 변수 선언 섹션

---

## 2. DOM 선택

**파일명**: `01-select.html`

`querySelector`와 `querySelectorAll`을 사용하여 DOM 요소를 선택하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>
  
  <script>
    // querySelector(): CSS 선택자와 일치하는 첫 번째 요소를 반환
    console.log(document.querySelector('.heading'))
    // 출력: <h1 class="heading">DOM 선택</h1>
    
    console.log(document.querySelector('.content'))
    // 출력: <p class="content">content1</p> (첫 번째 요소만)
    
    // querySelectorAll(): CSS 선택자와 일치하는 모든 요소를 NodeList로 반환
    console.log(document.querySelectorAll('.content'))
    // 출력: NodeList(3) [p.content, p.content, p.content]
    
    console.log(document.querySelectorAll('ul > li'))
    // 출력: NodeList(2) [li, li]
    // 'ul > li'는 ul의 직계 자식인 li 요소를 선택
  </script>
</body>
</html>
```

**핵심 개념:**
- `querySelector(selector)`: 선택자와 일치하는 **첫 번째 요소 하나**를 반환
- `querySelectorAll(selector)`: 선택자와 일치하는 **모든 요소**를 NodeList로 반환
- CSS 선택자 문법 사용 가능 (클래스, ID, 태그, 자식 선택자 등)

**참고 교안**: `DOM01.md` - DOM 선택 섹션

---

## 3. 요소 속성 조작

**파일명**: `02-element-manipulation.html`

클래스 속성과 일반 속성을 조작하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .red {
      color: crimson;
    }
  </style>
</head>
<body>
  <h1 class="heading">DOM 조작</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>

  <script>
    // === 클래스 속성 조작 ===
    const h1Tag = document.querySelector('.heading')
    console.log(h1Tag.classList)
    // 출력: DOMTokenList ['heading']

    // classList.add(): 클래스 추가
    // h1Tag.classList.add('red')
    // console.log(h1Tag.classList)
    // 출력: DOMTokenList ['heading', 'red']

    // classList.remove(): 클래스 제거
    // h1Tag.classList.remove('red')
    // console.log(h1Tag.classList)
    // 출력: DOMTokenList ['heading']

    // classList.toggle(): 클래스 토글 (있으면 제거, 없으면 추가)
    // h1Tag.classList.toggle('red')
    // console.log(h1Tag.classList)
    // 출력: 토글 상태에 따라 DOMTokenList ['heading'] 또는 ['heading', 'red']

    // === 일반 속성 조작 ===
    const aTag = document.querySelector('a')
    
    // getAttribute(): 속성 값 가져오기
    console.log(aTag.getAttribute('href'))
    // 출력: 'https://www.google.com/'

    // setAttribute(): 속성 값 설정
    // aTag.setAttribute('href', 'https://www.naver.com/')
    // console.log(aTag.getAttribute('href'))
    // 출력: 'https://www.naver.com/'

    // removeAttribute(): 속성 제거
    // aTag.removeAttribute('href')
    // console.log(aTag.getAttribute('href'))
    // 출력: null
  </script>
</body>
</html>
```

**핵심 개념:**
- **classList**: 클래스 속성을 제어하는 객체
  - `add(className)`: 클래스 추가
  - `remove(className)`: 클래스 제거
  - `toggle(className)`: 클래스 토글 (있으면 제거, 없으면 추가)
- **일반 속성 메서드**:
  - `getAttribute(name)`: 속성 값 가져오기
  - `setAttribute(name, value)`: 속성 값 설정
  - `removeAttribute(name)`: 속성 제거

**참고 교안**: `DOM01.md` - DOM 조작 섹션 (classList, setAttribute)

---

## 4. 콘텐츠 조작

**파일명**: `03-contents-manipulation.html`

`textContent`를 사용하여 요소의 텍스트 내용을 조작하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 class="heading">DOM 조작</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>

  <script>
    // textContent: 요소의 텍스트 콘텐츠를 조작
    const h1Tag = document.querySelector('.heading')
    
    // textContent 읽기
    console.log(h1Tag.textContent)
    // 출력: 'DOM 조작'

    // textContent 쓰기 (텍스트 변경)
    h1Tag.textContent = '내용 수정'
    console.log(h1Tag.textContent)
    // 출력: '내용 수정'
    // 화면의 h1 텍스트가 '내용 수정'으로 변경됨
  </script>
</body>
</html>
```

**핵심 개념:**
- `textContent`: 요소의 **순수한 텍스트 콘텐츠**를 읽거나 변경
- HTML 태그는 제외하고 텍스트만 다룸
- 읽기와 쓰기 모두 가능

**참고 교안**: `DOM01.md` - DOM 조작 섹션 (textContent)

---

## 5. DOM 요소 조작

**파일명**: `04-dom-manipulation.html`

새로운 요소를 생성하고, 추가하고, 삭제하는 실습

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
    <p>DOM 요소 조작</p>
  </div>

  <script>
    // === 요소 생성 ===
    // createElement(): 새로운 HTML 요소를 메모리에 생성
    const h1Tag = document.createElement('h1')
    h1Tag.textContent = '제목'
    console.log(h1Tag)
    // 출력: <h1>제목</h1> (아직 화면에는 보이지 않음)

    // === 요소 추가 ===
    // appendChild(): 생성한 요소를 특정 부모 요소의 마지막 자식으로 추가
    // const divTag = document.querySelector('div')
    // divTag.appendChild(h1Tag)
    // console.log(divTag)
    // 출력: <div><p>DOM 요소 조작</p><h1>제목</h1></div>
    // 화면에 h1 요소가 나타남

    // === 요소 삭제 ===
    // removeChild(): 자식 요소 제거
    // const pTag = document.querySelector('p')
    // divTag.removeChild(pTag)
    // 화면에서 p 요소가 사라짐
  </script>
</body>
</html>
```

**핵심 개념:**
- `createElement(tagName)`: 새로운 HTML 요소를 **메모리에** 생성
  - 생성만 하고 문서에 추가하지 않으면 화면에 보이지 않음
- `appendChild(node)`: 요소를 부모 요소의 **마지막 자식으로 추가**
  - 이 단계에서 화면에 나타남
- `removeChild(node)`: 부모 요소에서 자식 요소를 제거

**참고 교안**: `DOM01.md` - DOM 조작 섹션 (createElement, appendChild, removeChild)

---

## 6. 스타일 조작

**파일명**: `05-style-property.html`

`style` 프로퍼티를 사용하여 요소의 CSS 스타일을 직접 변경하는 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>Lorem, ipsum dolor.</p>

  <script>
    const pTag = document.querySelector('p')

    // style 프로퍼티로 CSS 스타일 직접 변경
    // CSS의 kebab-case는 camelCase로 변환하여 사용
    pTag.style.color = 'crimson'          // color: crimson
    pTag.style.fontSize = '2rem'          // font-size: 2rem
    pTag.style.border = '1px solid black' // border: 1px solid black

    console.log(pTag.style)
    // 출력: CSSStyleDeclaration 객체 (설정된 모든 스타일 속성)
    // 화면의 p 요소 스타일이 즉시 변경됨
  </script>
</body>
</html>
```

**핵심 개념:**
- `element.style.property`: 요소의 CSS 스타일을 **인라인 스타일로** 직접 변경
- CSS 속성명의 변환 규칙:
  - CSS: `font-size` (kebab-case) → JavaScript: `fontSize` (camelCase)
  - CSS: `background-color` → JavaScript: `backgroundColor`
  - CSS: `border-radius` → JavaScript: `borderRadius`
- 값은 문자열로 지정 (단위 포함)

**참고 교안**: `DOM01.md` - DOM 조작 섹션 (Style 조작)

---

## 보너스: hello.js

**파일명**: `hello.js`

JavaScript 파일을 외부에서 불러오는 예시

```javascript
console.log('hello')
```

**사용 방법:**
```html
<!-- HTML 파일에서 외부 JS 파일 불러오기 -->
<script src="hello.js"></script>
```

**핵심 개념:**
- JavaScript 코드를 별도의 `.js` 파일로 분리하여 관리 가능
- HTML에서 `<script src="파일경로"></script>`로 불러옴
- 코드의 재사용성과 유지보수성 향상

---

## 실습 순서 추천

1. **00-js-variable.html**: 변수 선언 기초 이해
2. **01-select.html**: DOM 요소 선택 방법 익히기
3. **03-contents-manipulation.html**: 텍스트 콘텐츠 변경
4. **02-element-manipulation.html**: 클래스와 속성 조작
5. **04-dom-manipulation.html**: 요소 생성, 추가, 삭제
6. **05-style-property.html**: 스타일 직접 변경

---

## 핵심 메서드 요약표

| 메서드/프로퍼티 | 기능 | 예시 |
|----------------|------|------|
| `querySelector()` | 첫 번째 요소 선택 | `document.querySelector('.class')` |
| `querySelectorAll()` | 모든 요소 선택 | `document.querySelectorAll('div')` |
| `textContent` | 텍스트 내용 읽기/쓰기 | `element.textContent = '텍스트'` |
| `classList.add()` | 클래스 추가 | `element.classList.add('active')` |
| `classList.remove()` | 클래스 제거 | `element.classList.remove('active')` |
| `classList.toggle()` | 클래스 토글 | `element.classList.toggle('active')` |
| `getAttribute()` | 속성 값 가져오기 | `element.getAttribute('href')` |
| `setAttribute()` | 속성 값 설정 | `element.setAttribute('href', 'url')` |
| `removeAttribute()` | 속성 제거 | `element.removeAttribute('href')` |
| `createElement()` | 요소 생성 | `document.createElement('div')` |
| `appendChild()` | 자식 요소 추가 | `parent.appendChild(child)` |
| `removeChild()` | 자식 요소 제거 | `parent.removeChild(child)` |
| `style` | 스타일 직접 변경 | `element.style.color = 'red'` |

---

## 주의사항

1. **변수 선언**: `var`는 사용하지 말고, 기본적으로 `const`를 사용하고 재할당이 필요한 경우에만 `let` 사용
2. **CSS 속성명**: JavaScript에서 스타일 변경 시 camelCase로 변환 필요 (`font-size` → `fontSize`)
3. **요소 생성**: `createElement()`로 생성한 요소는 반드시 `appendChild()` 등으로 추가해야 화면에 보임
4. **선택자**: CSS 선택자 문법을 정확히 사용 (클래스는 `.class`, ID는 `#id`)

---

**작성일**: 2024  
**참고 교안**: SSAFY JavaScript DOM01.md
